# 解决登录/请求时图片验证
'''
# 1.0
from PIL import Image
import pytesseract

# 二值化
def convert_img(img, threshold):
    img = img.convert('L') # 灰度化处理（把彩图变成黑白图）
    pixels = img.load() # 获取图片对应二维数值值
    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] > threshold:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    return img

# 二值化 + 降噪
def convert_img1(img, threshold):
    img = img.convert('L') # 灰度化处理（把彩图变成黑白图）
    pixels = img.load() # 获取图片对应二维数值值
    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] > threshold:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    data = img.getdata()
    w, h = img.size
    count = 0
    for x in range(1, h-1):
        for y in range(1, h-1):
            mid_pixel = data[w * y + x]
            if mid_pixel == 0:
                top_pixel = data[w * (y - 1) + x]
                left_pixel = data[w * y + (x - 1)]
                down_pixel = data[w * (y + 1) + x]
                right_pixel = data[w * y + (x + 1)]
                if top_pixel == 0:
                    count += 1
                if left_pixel == 0:
                    count += 1
                if down_pixel == 0:
                    count += 1
                if right_pixel == 0:
                    count += 1
                if count > 4:
                    img.putpixel((x, y), 0)
    return img

# 图片1
captcha = Image.open('./source/imgs/0.webp')
result = pytesseract.image_to_string(captcha)
print('result:'+result)
# 图片2
captcha1 = Image.open('./source/imgs/1.webp')
result1 = pytesseract.image_to_string(captcha1)
print('result1:'+result1)
# 图片3
captcha2 = Image.open('./source/imgs/2.png')
result2 = pytesseract.image_to_string(convert_img(captcha2, 150))
print('result2:'+result2)
# 图片4
captcha3 = Image.open('./source/imgs/3.webp')
result3 = pytesseract.image_to_string(convert_img1(captcha3, 150))
print('result3:'+result3)
'''

# 2.0 使用opencv提升验证准确率
# from PIL import Image
import pytesseract
import cv2

img = cv2.imread('./source/imgs/2.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 灰值化处理
th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1) # 二值化处理
cv2.imshow('test', th1)
cv2.waitKey(0)
cv2.destroyAllWindows()
