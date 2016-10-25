import thunder as td
from pyspark import SparkContext
from registration import CrossCorr
import json
from extraction import NMF
from scipy.ndimage.interpolation import shift
from scipy.ndimage.filters import gaussian_filter
from pyspark import SparkConf
conf = SparkConf().set("spark.driver.maxResultSize", "3g")
sc = SparkContext(conf=conf)

submission=[]
def main():

    data = td.images.fromtif(path='/home/dharamendra/neurofinder.00.00/images/*',engine=sc,npartitions=4)
    data=data.map(lambda x:gaussian_filter(x,1.5,order=0))
    reference = data.mean().toarray()
    algorithmMC = CrossCorr()
    model = algorithmMC.fit(data, reference)
    shifts = model.transformations
    registered = model.transform(data)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            #print (frequencies)
    algorithm = NMF(k=5, percentile=99, max_iter=50, overlap=0.1)
    model = algorithm.fit(registered, chunk_size=(50, 50), padding=(25, 25))
    merged = model.merge(overlap=0.1,max_iter=10,k_nearest=10)
    print('found %g regions' % merged.regions.count)
    regions = [{'coordinates': region.coordinates.tolist()} for region in merged.regions]
    #print (regions)
    result = {'dataset': '00.00', 'regions': regions}
    submission.append(result)
    with open('submission.json', 'w') as f:
        f.write(json.dumps(submission))

if __name__ == "__main__":
    main()
