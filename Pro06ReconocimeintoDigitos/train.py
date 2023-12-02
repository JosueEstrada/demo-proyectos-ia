# Usage
# python train.py --dataset data/digits.csv --model models/svm.cpickle

# Import the necessary packages
import joblib
from sklearn.svm import LinearSVC
from utils.hog import HOG
from utils import dataset
import argparse

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="Path to the dataset file")
ap.add_argument("-m", "--model", required=True,
                help="Path to where the model will be stored")
args = vars(ap.parse_args())

# Load the dataset and initialize the data matrix
(digits, target) = dataset.load_digits(args["dataset"])
data = []

# Initialize the HOG descriptor
hog = HOG(orientations=18, pixelsPerCell=(10, 10),
          cellsPerBlock=(1, 1), transform=True)

# Loop over the images
for image in digits:
    # Deskew the image, center it
    image = dataset.deskew(image, 20)
    image = dataset.center_extent(image, (20, 20))

    # Describe the image and update the data matrix
    hist = hog.describe(image)
    data.append(hist)

# Train the model
model = LinearSVC(random_state=42)
model.fit(data, target)

# Dump the model to file
joblib.dump(model, args["model"])

# Show the accuracy on the training data
# acc = model.score(data, target)
# print("[INFO] training accuracy: {:.2f}%".format(acc * 100))
