# -*-coding:utf-8-*-
from PIL import Image

im = Image.open("/home/iberry/PycharmProjects/game_download/picture_spider/0 (1).jpg")
# 图片的宽度和高度
img_size = im.size
width = img_size[0]
height = img_size[1]
print("图片宽度和高度分别是{}".format(img_size))  # (1125, 1500)
'''
裁剪：传入一个元组作为参数
元组里的元素分别是：（距离图片左边界距离x， 距离图片上边界距离y，距离图片左边界距离+裁剪框宽度x+w，距离图片上边界距离+裁剪框高度y+h）
'''
# 截取图片中一块宽和高都是250的
x = 0
y = 0
w = width
h = height-height/37.5
# x,y 为裁剪框左上角的坐标,x+w,y+h,为裁剪框右下角的坐标
# 图片以左上角为坐标原点
region = im.crop((x, y, x + w, y + h))
region.save("./crop_test1.jpeg")
#
# # 截取图片中一块宽是250和高都是300的
# x = 100
# y = 100
# w = 250
# h = 300
# region = im.crop((x, y, x + w, y + h))
# region.save("./crop_test2.jpeg")