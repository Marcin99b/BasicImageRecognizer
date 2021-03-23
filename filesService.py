import os
from PIL import Image
from numpy import asarray, save, load


generatedLabelsPath = os.getcwd() + '\\numbers\\labels.npy'
generatedImagesPath = os.getcwd() + '\\numbers\\images.npy'


def getNumbers():
    labels = load(generatedLabelsPath)
    images = load(generatedImagesPath)
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
            data = asarray(image)
            images.append(data)
            labels.append(folderNameNumber)
    save(generatedLabelsPath, labels)
    save(generatedImagesPath, images)


print(os.getcwd())

generate()
# run -> python filesService.py
