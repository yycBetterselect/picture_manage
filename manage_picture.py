# -*- coding: utf-8 -*-
import cv2
# import numpy as np
import numpy
path = "/home/iberry/PycharmProjects/game_download/picture_spider/002.jpg"

# img = cv2.imread(path)
# hight, width, depth = img.shape[0:3]
#
# # 图片二值化处理，把[240, 240, 240]~[255, 255, 255]以外的颜色变成0
# thresh = cv2.inRange(img, np.array([240, 240, 240]), np.array([255, 255, 255]))
#
# # 创建形状和尺寸的结构元素
# kernel = np.ones((3, 3), np.uint8)
#
# # 扩张待修复区域
# hi_mask = cv2.dilate(thresh, kernel, iterations=1)
# specular = cv2.inpaint(img, hi_mask, 5, flags=cv2.INPAINT_TELEA)
#
# cv2.namedWindow("Image", 0)
# cv2.resizeWindow("Image", int(width / 2), int(hight / 2))
# cv2.imshow("Image", img)
#
# cv2.namedWindow("newImage", 0)
# cv2.resizeWindow("newImage", int(width / 2), int(hight / 2))
# cv2.imshow("newImage", specular)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
test_dir = '/Users/lespark/PycharmProjects/day01/picture_spider/picture/2480211486108922.jpg'
mask_dir = '/Users/lespark/PycharmProjects/day01/picture_spider/result2_3.jpg'
save_dir = 'b.jpg'
src = cv2.imread(test_dir)
mask = cv2.imread(mask_dir)
save = numpy.zeros(src.shape, numpy.uint8)
for row in range(src.shape[0]):
    for col in range(src.shape[1]):
        for channel in range(src.shape[2]):
            if mask[row, col, channel] == 0:
                val = 0
            else:
                reverse_val = 255 - src[row, col, channel]
                val = 255 - reverse_val * 256 / mask[row, col, channel]
                if val < 0:
                    val = 0
            save[row, col, channel] = val
cv2.imwrite(save_dir, save)