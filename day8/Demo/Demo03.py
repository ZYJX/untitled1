# import shutil
# a = '1701B 副本.jpg'
# b = '1701B.jpg'
# shutil.copyfile(a,b)

# 读取和显示图像

def showimg(imagePath):
    img = cv2.imread(imagePath)  # 读取本地图片，目前OpevCV支持bmp、jpg、png、tiff

    cv2.namedWindow("Image")  # 创建一个窗口用来显示图片

    cv2.imshow("Image", img)  # 显示图片

    cv2.waitKey(0)  # 等待输入,这里主要让图片持续显示。

    cv2.destroyAllWindows()  # 释放窗口


if __name__ == '__main__':
    imagePath = 'mini.jpg'

    showimg(imagePath)
