import os
from PIL import Image
import numpy as np


generatedLabelsPath = os.getcwd() + '\\numbers\\labels.npy'
generatedImagesPath = os.getcwd() + '\\numbers\\images.npy'


def getNumbers():
    labels = np.array(np.load(generatedLabelsPath, allow_pickle=True))
    images = np.array(np.load(generatedImagesPath, allow_pickle=True))
    return labels, images


def transformPixel(pixel):
    # 0.0 = white
    # 1.0 = black
    # between 0.0 and 1.0 = gray
    if np.issubdtype(type(pixel), int):
        return 0
    pixel = (pixel - 255) / 255
    result = np.average(pixel) * 100/75
    return result


def transformImage(row):
    return np.array(list(map(transformPixel, row)))


def generate():
    images = []
    labels = []
    for folderNameNumber in os.listdir('numbers'):
        if '.' in folderNameNumber:
            continue
        for imageName in os.listdir('numbers\\' + folderNameNumber):
            image = Image.open(
                'numbers\\' + folderNameNumber + '\\' + imageName)
            image = image.resize((22, 22))  # 88x88 -> 22x22
            data = np.array(image)
            data = np.array(list(map(transformImage, data)))

            images.append(data)
            labels.append(folderNameNumber)
    np.save(generatedLabelsPath, labels)
    np.save(generatedImagesPath, images)


# print(os.getcwd())
generate()
# run -> python filesService.py
