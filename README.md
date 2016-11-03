# Neuron Detection in Calcium Imaging Data
### Overview
Calcium Imaging is a techinque wherein neurons in living organisms become flurocent in response to Calcium ions. The dataset used for this project consists of images in TIFF format which represents a timeseries. The goal is to identify neurons in these images that are responding to the calcium ion administration. Such neurons are known as Region of Interest (ROI).
The following Python script files and configuration files are used to retrieve the ROIs in the dataset provided.
- config.json : This file is used to configure the main neuron finding program.
- neuronfinder.py : This python script reads the parameters in config.json and implements the main neuron finding logic.
- merge_json_files.py : Merges the output of neuronfinder.py into a single output file in json format.
