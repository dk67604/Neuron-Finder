import thunder as td
from pyspark import SparkContext
from factorization import ICA
sc = SparkContext()

def main():

    data = td.images.fromtif(path='/home/dharamendra/neurofinder.00.00/images/*',engine=sc,npartitions=4)
    print (data.count())
    #t = data.median_filter(3).toseries()
    #frequencies = ts.detrend().fourier(freq=3).toarray()
    #print (frequencies)
if __name__ == "__main__":
    main()
