# -*- coding: utf-8 -*-
import cv2
import numpy as np
from PIL import Image
# 提取水印区域ROI
img = cv2.imread("/Users/lespark/PycharmProjects/day01/picture_spider/picture/2480211486108922.jpg")
im = Image.open("/Users/lespark/PycharmProjects/day01/picture_spider/picture/2480211486108922.jpg")
# 图片的宽度和高度
img_size = im.size
width = img_size[0]
height = img_size[1]
b = int(height-height/3)
# print(b)
# 数组第一个元素是水印的左上角的y值和右下角的y比，第二个元素是，水印左上角的x值和右下角的x值比
# roi = img[711:748, 248:351]
roi = img[52:89, 248:351]
roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
# 处理白色水印
# 设定白色HSV范围
lower_white = np.array([0, 0, 0])
upper_white = np.array([180, 255, 46])
# 创建白色水印蒙层
kernel = np.ones((3, 3), np.uint8)
mask_white = cv2.inRange(roi_hsv, lower_white, upper_white)
# 对白色水印蒙层进行膨胀操作
dilate_white = cv2.dilate(mask_white, kernel, iterations=1)
# 修补白色水印
res_1 = cv2.inpaint(roi, dilate_white, 5, flags=cv2.INPAINT_TELEA)
# 修补之后的水印区域回填到原图中
img[b:height, 0:width] = res_1
cv2.imwrite("./p5.jpg", img)
# 如果水印有其他颜色
# 例如红色
# lower_red = np.array([0, 43, 46])
# upper_red = np.array([10, 255, 255])
# res_1_hsv = cv2.cvtColor(res_1, cv2.COLOR_BGR2HSV)
# mask_red = cv2.inRange(res_1_hsv, lower_red, upper_red)
# dilate_red = cv2.dilate(mask_red, kernel,iterations=1)
# res_2 = cv2.inpaint(res_1, dilate_red, 5, flags=cv2.INPAINT_TELEA)
# img[b:height, 0:width] = res_2
# cv2.iimwrite("./p55.jpg", img)

















