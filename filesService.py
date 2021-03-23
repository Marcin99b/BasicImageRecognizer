import os
from PIL import Image
import numpy as np


generatedLabelsPath = os.getcwd() + '\\numbers\\labels.npy'
generatedImagesPath = os.getcwd() + '\\numbers\\images.npy'


def getNumbers():
    labels = list(np.load(generatedLabelsPath, allow_pickle=True))
    images = list(np.load(generatedImagesPath, allow_pickle=True))
    return labels, images


def generate():
    images = []
    labels = []
    for folderNameNumber in os.listdir('numbers'):
        if '.' in folderNameNumber:
            continue
        for imageName in os.listdir('numbers\\' + folderNameNumber):
            image = Image.open(
                'numbers\\' + folderNameNumber + '\\' + imageName)
            data = np.asarray(image)
            images.append(data)
            labels.append(folderNameNumber)
    np.save(generatedLabelsPath, labels)
    np.save(generatedImagesPath, images)


# print(os.getcwd())
# generate()
# run -> python filesService.py
