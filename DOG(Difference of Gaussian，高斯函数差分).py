#coding:utf-8

import cv2
import numpy as np
from scipy import signal

# 二维高斯卷积核拆分为水平核垂直一维卷积核，分别进行卷积
def gaussConv(image, size, sigma):
    H, W = size
    # 先水平一维高斯核卷积
    xr, xc = np.mgrid[0:1, 0:W]
    xc = xc.astype(np.float32)
    xc -= (W-1.0)/2.0
    xk = np.exp(-np.power(xc, 2.0)/(2*sigma*sigma))
    image_xk = signal.convolve2d(image, xk, 'same', 'symm')

    # 垂直一维高斯核卷积
    yr, yc = np.mgrid[0:H, 0:1]
    yr = yr.astype(np.float32)
    yr -= (H-1.0)/2.0
    yk = np.exp(-np.power(yr, 2.0)/(2*sigma*sigma))
    image_yk = signal.convolve2d(image_xk, yk, 'same','symm')
    image_conv = image_yk/(2*np.pi*np.power(sigma, 2.0))

    return image_conv

#直接采用二维高斯卷积核，进行卷积
def gaussConv2(image, size, sigma):
    H, W = size
    r, c = np.mgrid[0:H:1.0, 0:W:1.0]
    c -= (W - 1.0) / 2.0
    r -= (H - 1.0) / 2.0
    sigma2 = np.power(sigma, 2.0)
    norm2 = np.power(r, 2.0) + np.power(c, 2.0)
    LoGKernel = (1 / (2*np.pi*sigma2)) * np.exp(-norm2 / (2 * sigma2))
    image_conv = signal.convolve2d(image, LoGKernel, 'same','symm')

    return image_conv

def DoG(image, size, sigma, k=1.1):
    Is = gaussConv(image, size, sigma)
    Isk = gaussConv(image, size, sigma*k)

    # Is = gaussConv2(image, size, sigma)
    # Isk = gaussConv2(image, size, sigma * k)

    doG = Isk - Is
    doG /= (np.power(sigma, 2.0)*(k-1))
    return doG

if __name__ == "__main__":
    img = cv2.imread("./Pics/test.jpg", 0)
    sigma = 1
    k = 1.1
    size = (7, 7)
    DoG_edge = DoG(img, size, sigma, k)
    DoG_edge[DoG_edge>255] = 255
    DoG_edge[DoG_edge<0] = 0
    DoG_edge = DoG_edge / np.max(DoG_edge)
    DoG_edge = DoG_edge * 255
    DoG_edge = DoG_edge.astype(np.uint8)

    cv2.namedWindow("Original", 0)
    cv2.resizeWindow("Original", 360, 480)

    cv2.namedWindow("DoG_edge", 0)
    cv2.resizeWindow("DoG_edge", 360, 480)

    cv2.imshow("Original", img)
    cv2.imshow("DoG_edge", DoG_edge)

    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()



