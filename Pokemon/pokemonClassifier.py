from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Imports
import numpy as np
import tensorflow as tf

# Create a function to load the data
def load_data(data_directory):
    directories = [d for d in os.listdir(data_directory) 
                   if os.path.isdir(os.path.join(data_directory, d))]
    labels = []
    images = []
    for d in directories:
        label_directory = os.path.join(data_directory, d)
        file_names = [os.path.join(label_directory, f) 
                      for f in os.listdir(label_directory) 
                      if (f.endswith(".png") or f.endswith(".jpg"))]
        for f in file_names:
            images.append(skimage.data.imread(f))
            labels.append(int(d))
    return images, labels
tf.logging.set_verbosity(tf.logging.INFO)



ROOT_PATH = "/Users/nimishasharath/Documents/UW/AI/image-processing-shenanigans/Pokemon/data"
train_data_directory = os.path.join(ROOT_PATH, "/Training")
test_data_directory = os.path.join(ROOT_PATH, "/Testing")

# load the data into training and testing directories
images, labels = load_data(train_data_directory)

# Our application logic will be added here

if __name__ == "__main__":
  tf.app.run()