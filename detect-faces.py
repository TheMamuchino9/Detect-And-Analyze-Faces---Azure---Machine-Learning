# Import the libraries need to call the Face service and execute the remaining cells in this notebook
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
import faces # Custom Python code
import matplotlib.pyplot as plt
from PIL import Image
import os

key = 'c25488f3e6a04fbab1be1bbb8302d2fd'
endpoint = 'https://udacity-cog-services-mamuchino9.cognitiveservices.azure.com/'

print('Ready to analyze faces using the Azure Face service at {}.'.format(endpoint))

# Instantiate a Face client
credentials = CognitiveServicesCredentials(key)
client = FaceClient(endpoint, credentials)




#Detect faces and facial attributes

imagePath = os.path.join('images', 'family.jpg')
attributes = ['age', 'gender', 'emotion']
# Detect faces
with open(imagePath, mode="rb") as imageData:
    faceResults = client.face.detect_with_stream(imageData, return_face_attributes=attributes)# TODO: Complete this line to call the a face detect method that accepts an image data stream as an argument.

# Display the faces and output the Face Id for each detected face.
faces.show_faces(imagePath, faceResults, show_id=False, show_attributes=True)






###Find similar faces###

imageOnePath = os.path.join('images', 'me-02.jpg')
imageTwoPath = os.path.join('images', 'not-me.jpg')

# Detect faces in the first image
with open(imageOnePath, mode="rb") as imageOneData:
    faceOneResults = client.face.detect_with_stream(imageOneData)

# Retrieve the first face identified in the image
faceOne = faceOneResults[0]

# Detect faces in the second image
with open(imageTwoPath, mode="rb") as imageTwoData:
    faceTwoResults = client.face.detect_with_stream(imageTwoData)

# Retrieve the face Ids found in the second image.
imageTwoFaceIds = list(map(lambda face: face.face_id, faceTwoResults))

# Find faces in image two that are similar to the face in image one
similarFaces = client.face.find_similar(face_id=faceOne.face_id, face_ids=imageTwoFaceIds)# TODO: Complete this line to look for similar faces in the two images.

# Show the face in image 1, and similar faces in image 2
faces.show_similar_faces(imageOnePath, faceOne, imageTwoPath, faceTwoResults, similarFaces)