import cv2 as cv
import math
import numpy as np
from SSIM import ssim
from skimage.metrics import structural_similarity as ssim
from PIL import Image

def psnr(img1, img2):
    mse = np.mean((img1 / 255.0 - img2 / 255.0) ** 2)
    if mse < 1e-10:
        return 100
    psnr2 = 20 * math.log10(1 / math.sqrt(mse))
    return psnr2


imag1 = cv.imread("../results/all_tank/desert2grassland/images/0009_0081_fake.png")
imag2 = cv.imread("../results/all_tank/desert2grassland/images/0009_0081_real.png")
img1 = np.array(Image.open("../results/all_tank/desert2grassland/images/0009_0081_fake.png"))
img2 = np.array(Image.open("../results/all_tank/desert2grassland/images/0009_0081_real.png"))


res = psnr(imag1, imag2)
ssi = ssim(img1, img2, multichannel=True)
print("res:", res)
print("ssim:",ssi)

#python -m pytorch_fid D:\pythonProject\pytorch-CycleGAN-and-pix2pix-master\results\all_tank\5.25\images-summer-winter D:\pythonProject\pytorch-CycleGAN-and-pix2pix-master\results\all_tank\5.25\summer
