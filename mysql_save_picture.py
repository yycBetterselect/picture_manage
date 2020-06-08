import pymysql
import time

conn = pymysql.connect(host="localhost",
                       port=3306,
                       user="root",
                       password="genesis.mysql.123",
                       charset="utf8",
                       db="genesis")
cursor = conn.cursor()
f = open("/home/iberry/PycharmProjects/game_download/picture_spider/p5.jpg", 'rb')
img = f.read()
f.close()


def inset_imgs():
    try:
        cursor.execute("insert into img(imgs) values(%s)", (pymysql.Binary(img)))
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def select_img(img):
    start_time = time.time()
    try:
        cursor.execute("select imgs from img where imgs=%s", img)
        # 返回元组
        result = cursor.fetchone()[0]
        with open("./save.jpg", "wb") as fs:
            fs.write(result)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    end_time = time.time()
    print(end_time-start_time)


if __name__ == '__main__':
    # inset_imgs()
    select_img(img)


































