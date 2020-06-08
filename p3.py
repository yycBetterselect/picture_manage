from nowatermark import WatermarkRemover

path = '/home/iberry/PycharmProjects/game_download/picture_spider/picture/mask2_3.jpg'

watermark_template_filename = path
remover = WatermarkRemover()
remover.load_watermark_template(watermark_template_filename)

remover.remove_watermark('/home/iberry/PycharmProjects/game_download/picture_spider/picture/002.jpg', './20180516144932.jpg')
print(remover.watermark_start_x)
print(remover.watermark_start_y)