# Neuron Detection in Calcium Imaging Data
### Overview
Calcium Imaging is a techinque wherein neurons in living organisms become flurocent in response to Calcium ions. The dataset used for this project consists of images in TIFF format which represents a timeseries. The goal is to identify neurons in these images that are responding to the calcium ion administration. Such neurons are known as Region of Interest (ROI).
The following Python script files and configuration files are used to retrieve the ROIs in the dataset provided.
- config.json : This file is used to configure the main neuron finding program.
- neuronfinder.py : This python script reads the parameters in config.json and implements the main neuron finding logic.
- merge_json_files.py : Merges the output of neuronfinder.py into a single output file in json format.

### Problem Description
The data are a set of different timeseries images. The goal is to identify neurons in each of the dataset outputing the location as a tuple of pixel location. All images are 512 * 512 in TIFF format. The data also provides groung truth pixel locations of neurons responding to the imaging. The images have black background color and neurons appear in grayish white. The challenge here is to identify active neurons from an image with many passive neurons or other noise which might be introduced due to the imaging device. Thus, the identification is not as easy as locating white patches on dark.

The approch followed by us to solve this problem is given in greater detail in the project report file. To give a brief overview, we first reduced the noise using gaussian filter. Then we used image registraion to apply motion correction to the images. The reason to apply motion correction is that the subject of calcium moves around during iamging and thus, it is applied to bring all images to the same overall reference point. Finally, we used local Non-negative Matrix Factorization to identify the ROIs. We used k-nn algorithm to merge pixels of a single neuron into one region of interest.

### Scores on http://neurofinder.codeneuro.org/, The home of this project.

![Scores](scores.jpg "scores on http://neurofinder.codeneuro.org/")

##### Output format
The output is a json file with regions and its corresponding coordinates. The coordinates represent the pixel pair that are found in the image for an identified neuron. The output is compared to the ground truth on the following,
- Precision : How many of the neurons found are active neurons. The ratio of correctly found neurons to the number of neurons found.
- Recall : How many of the overall neurons in the dataset that were found. Ratio of neurons found to the total possible neurons in the image.
- Inclusion and Exclusion : Determines how many neurons in the regions of a set radius are correctly included and excluded.

### How to Run
- Configure the parameters in config.json file.
- Run neuronfinder.py, this file takes configuration parameters from congig.json. Both need to be in the same directory.
- Run merge_json_files.py, this file outputs one single file with all the regions and coordinates.

### Project Report
Please refer to neuron_finder_report.pdf for detailed information of the project implementation.
