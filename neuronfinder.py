import thunder as td
from pyspark import SparkContext
from registration import CrossCorr
import json
from extraction import NMF
from scipy.ndimage.interpolation import shift
from scipy.ndimage.filters import gaussian_filter
from pyspark import SparkConf
###################################################
# Code for creating context for Spark
####################################################
conf = SparkConf().set("spark.driver.maxResultSize", "3g")
sc = SparkContext(conf=conf)

submission=[] #List for storing ROI co-ordinates

def main(config_data):

    data = td.images.fromtif(path=config_data["input_path"],engine=sc,npartitions=int(config_data["npartitions"]))
    ############################################################
    #Code for reduction of noise from image using gaussion filter
    ############################################################
    data=data.map(lambda x:gaussian_filter(x,sigma=float(config_data["sigma"]),order=0))

    ####################################################################################################
    # Code for Motion Correction using Image Registration , this process help in alignment of the images
    ####################################################################################################
    reference = data.mean().toarray()
    algorithmMC = CrossCorr()
    model = algorithmMC.fit(data, reference)
    shifts = model.transformations
    registered = model.transform(data)

    ####################################################################################
    # Code for Local Non-negative Matrix Factorization for Image Extraction
    #####################################################################################                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          #print (frequencies)
    algorithm = NMF(k=int(config_data["k"]), percentile=int(config_data["percentile"]),min_size=int(config_data["min_size"]),
                    max_iter=int(config_data["max_iter_nmf"]), overlap=float(config_data["overlap_nmf"]))

    model = algorithm.fit(registered, chunk_size=(int(config_data["chunk_size_1"]), int(config_data["chunk_size_2"])),
                          padding=(int(config_data["padding_1"]), int(config_data["padding_2"])))

    ####################################################################################
    #Code for finding ROI using spatial region extracted in NMF process
    ####################################################################################
    merged = model.merge(overlap=float(config_data["overlap_merge"]),max_iter=int(config_data["max_iter_merge"]),
                         k_nearest=int(config_data["k_nearest"]))

    print('Total no of regions found %g' % merged.regions.count)

    #####################################################################
    #Code for dumping the identified ROI co-ordinates in JSON file
    #####################################################################
    regions = [{'coordinates': region.coordinates.tolist()} for region in merged.regions]

    result = {'dataset': config_data["dataset"], 'regions': regions}
    submission.append(result)
    with open(config_data["output"]+'.json', 'w') as f:
        f.write(json.dumps(submission))

#############################################
#Boilerplate code for running main method
############################################
if __name__ == "__main__":
    #######################################################################
    #Code for loading configuration file for neuron finding using JSON file
    #######################################################################
    with open('config.json') as config_file:
        config_data=json.load(config_file)
    main(config_data)
