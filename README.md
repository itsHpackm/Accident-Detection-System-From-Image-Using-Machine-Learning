# Accident-Detection-system-From-Image-Using-Machine-Learning
This involves creating an image classification system (web application) for accident detection from an image using the Learning machine. 


## Dataset

Our models were built based on balanced dataset that is a set of images with extension [.jpg].Our dataset is a folder with two sub-folders with “No Accident” and “Accident” labels:
- Folder 1 includes 800 images with the No Accident label.
- Folder 2 includes 801 images with the Accident label.
The purpose of this dataset is to detect accidents, by image processing

### Split Data

- For the traditional models of the Learning machine we used the train_test_split function to divide our data with 80% of the data is dedicated to training and 20% for validation.
- For Deep learning models we subdivided our dataset into training data and data using the OS library which allows us to access our operating system and manipulate the files in a flexible way using a simple python code, and OpenCV that plays a big role in Image Preprocessing namely resizing and displaying images
