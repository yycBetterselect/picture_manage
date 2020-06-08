import cv2


def get_water():
    # 黑底白字
    src = cv2.imread('/home/iberry/PycharmProjects/game_download/picture_spider/002.jpg')  # 默认的彩色图(IMREAD_COLOR)方式读入原始图像
    # black.jpg
    mask = cv2.imread('/home/iberry/PycharmProjects/game_download/picture_spider/mask2_3.jpg', cv2.IMREAD_GRAYSCALE)  # 灰度图(IMREAD_GRAYSCALE)方式读入水印蒙版图像
    # 参数：目标修复图像; 蒙版图（定位修复区域）; 选取邻域半径; 修复算法(包括INPAINT_TELEA/INPAINT_NS， 前者算法效果较好)
    dst = cv2.inpaint(src, mask, 3, cv2.INPAINT_NS)

    cv2.imwrite('result1.jpg', dst)


get_water()