import thunder as td

from factorization import ICA
from numpy import arange
from scipy.ndimage.interpolation import shift
from scipy.ndimage import shift
from numpy import random
from scipy.ndimage.filters import gaussian_filter
from registration import CrossCorr


def main():

    data = td.images.fromtif(path='/home/yash/PycharmProjects/Thunder/neurofinder.00.00/images/*',npartitions=4)
    
    #print (data)
    reference = data.mean().toarray()
    algorithm = CrossCorr()
    model = algorithm.fit(data, reference)
    shifts = model.transformations
    model = algorithm.fit(shifts, reference=reference)
    registered = model.transform(data)
    print (registered)



if __name__ == "__main__":
    main()
