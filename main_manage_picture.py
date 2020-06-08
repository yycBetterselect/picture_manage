# -*- coding: utf-8 -*-
import cv2
import numpy as np

path = "/Users/lespark/PycharmProjects/day01/picture_spider/1245461471530076.jpg"

img = cv2.imread(path)
height, width, depth = img.shape[0:3]

# 图片二值化处理，把[240, 240, 240]~[255, 255, 255]以外的颜色变成0
thresh = cv2.inRange(img, np.array([0, 0, 0]), np.array([180, 255, 46]))
# 创建形状和尺寸的结构元素
kernel = np.ones((3, 3), np.uint8)
# 扩张待修复区域
for i in range(2, 6):
    hi_mask = cv2.dilate(thresh, kernel, iterations=i+1)

    # hi_mask[int(height*0.15):int(height*0.85), 0:width] = 0
    hi_mask[int(height*0.20):int(height*0.85), 0:width] = 0
    # hi_mask[711:748, 248:351] = 0
    # hi_mask[52:89, 248:351] = 0
    cv2.imwrite("mask2_%s.jpg" % (i + 1), hi_mask)
    # cv2.imwrite("/Users/lespark/PycharmProjects/day01/picture_spider/c.jpg", hi_mask)
    specular = cv2.inpaint(img, hi_mask, 3, flags=cv2.INPAINT_TELEA)
    cv2.imwrite("result2_%s.jpg" % (i+1), specular)


