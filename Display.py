import numpy as np
import matplotlib.pyplot as plt
import os



def Show_dataset(path):
    datanames = os.listdir(path)
    imgdir = []
    img = []
    for i in range(len(datanames)):
        imgdir.append(path + '/' + datanames[i])
        img.append(plt.imread(imgdir[i]))

    plt.figure(figsize=(15, 15))
    plt.subplot(4, 1, 1)
    plt.title('dataset')
    plt.axis('off')
    plt.imshow(img[0])

    plt.subplot(4, 1, 2)
    plt.axis('off')
    plt.imshow(img[1])
    plt.subplot(4, 1, 3)
    plt.axis('off')
    plt.imshow(img[2])
    plt.subplot(4, 1, 4)
    plt.axis('off')
    plt.imshow(img[3])
    plt.show()

def Show_dataset2(path):
    datanames = os.listdir(path)
    imgdir = []
    img = []
    for i in range(len(datanames)):
        imgdir.append(path + '/' + datanames[i])
        img.append(plt.imread(imgdir[i]))

    plt.figure(figsize=(15, 15))
    plt.subplot(4, 1, 1)
    plt.title('dataset')
    plt.axis('off')
    plt.imshow(img[4])

    plt.subplot(4, 1, 2)
    plt.axis('off')
    plt.imshow(img[9])
    plt.subplot(4, 1, 3)
    plt.axis('off')
    plt.imshow(img[14])
    plt.subplot(4, 1, 4)
    plt.axis('off')
    plt.imshow(img[19])
    plt.show()


def Show_result(path):
    datanames = os.listdir(path)
    imgdir = []
    img = []
    for i in range(len(datanames)):
        imgdir.append(path + '/' + datanames[i])
        img.append(plt.imread(imgdir[i]))

    plt.figure(figsize=(20, 20))
    plt.subplot(4,5, 1)
    plt.title('Glassland')
    plt.axis('off')
    plt.imshow(img[0])

    plt.subplot(4,5, 2)
    plt.title('Snowfield')
    plt.axis('off')
    plt.imshow(img[1])

    plt.subplot(4,5, 3)
    plt.title('Night')
    plt.axis('off')
    plt.imshow(img[2])

    plt.subplot(4,5, 4)
    plt.title('Fire')
    plt.axis('off')
    plt.imshow(img[3])

    plt.subplot(4,5, 5)
    plt.title('Desert')
    plt.axis('off')
    plt.imshow(img[4])

    for i in range(6,21):
        plt.subplot(4,5, i)
        plt.axis('off')
        plt.imshow(img[i-1])
    plt.show()

path2='./results/tank_cyclegan/test_latest/images'
Show_result(path2)