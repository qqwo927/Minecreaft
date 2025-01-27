import cv2
from face_recognition import face_locations, load_image_file
import face_recognition
import numpy as np
import argparse
import time
import cv2
import os
from PIL import Image
def kt(path,argss):
# 加载图片
    img = cv2.imread(path)

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_recognition.face_locations(gray)
    print(faces)


# import the necessary packages


# 构造参数解析器并解析参数
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", type=str,
      default=os.path.sep.join([r"D:\image", "guangtou.png"]),
      help="path to input image that we'll apply GrabCut to")
    ap.add_argument("-c", "--iter", type=int, default=10,
      help="# of GrabCut iterations (larger value => slower runtime)")
    args = vars(ap.parse_args())

    # load the input image from disk and then allocate memory for the
    # output mask generated by GrabCut -- this mask should hae the same
    # spatial dimensions as the input image
    image = cv2.imread(path)
    mask = np.zeros(image.shape[:2], dtype="uint8")

    # define the bounding box coordinates that approximately define my
    face_locations = face_recognition.face_locations(image)[0]
    top=face_locations[0]
    lft=face_locations[3]
    btm=face_locations[2]
    rgt=face_locations[1]
    hgh=top-btm
    wdt=rgt-lft

    rect =(int(lft-wdt*argss[0]) ,int(top+hgh*argss[2]) ,int(rgt+wdt*argss[1]) ,int(top-hgh*argss[3]))
    fgModel = np.zeros((1, 65), dtype="float")  #两个空数组，便于在从背景分割前景时使用（fgModel和bgModel）
    bgModel = np.zeros((1, 65), dtype="float")
    # apply GrabCut using the the bounding box segmentation method
    start = time.time()
    #GrabCut返回我们填充的掩码以及两个我们可以忽略的数组
    (mask, bgModel, fgModel) = cv2.grabCut(image, mask, rect, bgModel,fgModel, iterCount=args["iter"], mode=cv2.GC_INIT_WITH_RECT)
    end = time.time()
    print("[INFO] applying GrabCut took {:.2f} seconds".format(end - start))

    # the output mask has for possible output values, marking each pixel
    # in the mask as (1) definite background, (2) definite foreground,
    # (3) probable background, and (4) probable foreground
    values = (
      ("Definite Background", cv2.GC_BGD),
      ("Probable Background", cv2.GC_PR_BGD),
      ("Definite Foreground", cv2.GC_FGD),
      ("Probable Foreground", cv2.GC_PR_FGD),
    )
    # loop over the possible GrabCut mask values
    for (name, value) in values:
      # construct a mask that for the current value
      print("[INFO] showing mask for '{}'".format(name))
      valueMask = (mask == value).astype("uint8") * 255
      # display the mask so we can visualize it
      
      # 找到所有确定的背景或可能的背景像素，并将它们设置为0 ，所有其他像素应该标记为1(前景)
    outputMask = np.where((mask == cv2.GC_BGD) | (mask == cv2.GC_PR_BGD), 0, 1)
    # scale the mask from the range [0, 1] to [0, 255]
    outputMask = (outputMask * 255).astype("uint8")
    # apply a bitwise AND to the image using our mask generated by
    # GrabCut to generate our final output image
    output = cv2.bitwise_and(image, image, mask=outputMask)

    # show the input image followed by the mask and output generated by
    return outputMask #原图
        #GrabCUt生成的掩膜mask
def kc(path,argss):
# 加载图片
    img = cv2.imread(path)

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_recognition.face_locations(gray)
    print(faces)


# import the necessary packages


# 构造参数解析器并解析参数
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", type=str,
      default=os.path.sep.join([r"D:\image", "guangtou.png"]),
      help="path to input image that we'll apply GrabCut to")
    ap.add_argument("-c", "--iter", type=int, default=10,
      help="# of GrabCut iterations (larger value => slower runtime)")
    args = vars(ap.parse_args())

    # load the input image from disk and then allocate memory for the
    # output mask generated by GrabCut -- this mask should hae the same
    # spatial dimensions as the input image
    image = cv2.imread(path)
    mask = np.zeros(image.shape[:2], dtype="uint8")
    
    # define the bounding box coordinates that approximately define my
    face_locations = face_recognition.face_locations(image)[0]
    top=face_locations[0]
    lft=face_locations[3]
    btm=face_locations[2]
    rgt=face_locations[1]
    hgh=top-btm
    wdt=rgt-lft
    print(img.size)
    rect =(0+int(Image.open(path).width*argss[0]) ,int(btm+hgh*argss[2]) ,int((Image.open(path).width)-int(Image.open(path).width*argss[1])) ,int(btm-hgh*argss[3]))
    fgModel = np.zeros((1, 65), dtype="float")  #两个空数组，便于在从背景分割前景时使用（fgModel和bgModel）
    bgModel = np.zeros((1, 65), dtype="float")
    # apply GrabCut using the the bounding box segmentation method
    start = time.time()
    #GrabCut返回我们填充的掩码以及两个我们可以忽略的数组
    (mask, bgModel, fgModel) = cv2.grabCut(image, mask, rect, bgModel,fgModel, iterCount=args["iter"], mode=cv2.GC_INIT_WITH_RECT)
    end = time.time()
    print("[INFO] applying GrabCut took {:.2f} seconds".format(end - start))

    # the output mask has for possible output values, marking each pixel
    # in the mask as (1) definite background, (2) definite foreground,
    # (3) probable background, and (4) probable foreground
    values = (
      ("Definite Background", cv2.GC_BGD),
      ("Probable Background", cv2.GC_PR_BGD),
      ("Definite Foreground", cv2.GC_FGD),
      ("Probable Foreground", cv2.GC_PR_FGD),
    )
    # loop over the possible GrabCut mask values
    for (name, value) in values:
      # construct a mask that for the current value
      print("[INFO] showing mask for '{}'".format(name))
      valueMask = (mask == value).astype("uint8") * 255
      # display the mask so we can visualize it
      
      # 找到所有确定的背景或可能的背景像素，并将它们设置为0 ，所有其他像素应该标记为1(前景)
    outputMask = np.where((mask == cv2.GC_BGD) | (mask == cv2.GC_PR_BGD), 0, 1)
    # scale the mask from the range [0, 1] to [0, 255]
    outputMask = (outputMask * 255).astype("uint8")
    # apply a bitwise AND to the image using our mask generated by
    # GrabCut to generate our final output image
    output = cv2.bitwise_and(image, image, mask=outputMask)

    # show the input image followed by the mask and output generated by
    return outputMask #原图
def kf(path,argss):
# 加载图片
    img = cv2.imread(path)

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_recognition.face_locations(gray)
    print(faces)


# import the necessary packages


# 构造参数解析器并解析参数
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", type=str,
      default=os.path.sep.join([r"D:\image", "guangtou.png"]),
      help="path to input image that we'll apply GrabCut to")
    ap.add_argument("-c", "--iter", type=int, default=10,
      help="# of GrabCut iterations (larger value => slower runtime)")
    args = vars(ap.parse_args())

    # load the input image from disk and then allocate memory for the
    # output mask generated by GrabCut -- this mask should hae the same
    # spatial dimensions as the input image
    image = cv2.imread(path)
    mask = np.zeros(image.shape[:2], dtype="uint8")

    # define the bounding box coordinates that approximately define my
    face_locations = face_recognition.face_locations(image)[0]
    top=face_locations[0]
    lft=face_locations[3]
    btm=face_locations[2]
    rgt=face_locations[1]
    hgh=top-btm
    wdt=rgt-lft
    rect =(int(lft-wdt*argss[0]) ,int(top+hgh*argss[2]) ,int(rgt+wdt*argss[1]) ,int(top-hgh*argss[3]))
    fgModel = np.zeros((1, 65), dtype="float")  
    bgModel = np.zeros((1, 65), dtype="float")

    start = time.time()

    (mask, bgModel, fgModel) = cv2.grabCut(image, mask, rect, bgModel,fgModel, iterCount=args["iter"], mode=cv2.GC_INIT_WITH_RECT)
    end = time.time()
    print("[INFO] applying GrabCut took {:.2f} seconds".format(end - start))

    values = (
      ("Definite Background", cv2.GC_BGD),
      ("Probable Background", cv2.GC_PR_BGD),
      ("Definite Foreground", cv2.GC_FGD),
      ("Probable Foreground", cv2.GC_PR_FGD),
    )

    for (name, value) in values:

      print("[INFO] showing mask for '{}'".format(name))
      valueMask = (mask == value).astype("uint8") * 255

    outputMask = np.where((mask == cv2.GC_BGD) | (mask == cv2.GC_PR_BGD), 0, 1)

    outputMask = (outputMask * 255).astype("uint8")

    return outputMask


class UnsupportedFormat(Exception):
    def __init__(self, input_type):
        self.t = input_type

    def __str__(self):
        return "不支持'{}'模式的转换，请使用为图片地址(path)、PIL.Image(pil)或OpenCV(cv2)模式".format(self.t)


class MatteMatting():
    def __init__(self, original_graph, mask_graph, input_type='path'):
        """
        将输入的图片经过蒙版转化为透明图构造函数
        :param original_graph:输入的图片地址、PIL格式、CV2格式
        :param mask_graph:蒙版的图片地址、PIL格式、CV2格式
        :param input_type:输入的类型，有path：图片地址、pil：pil类型、cv2类型
        """
        if input_type == 'path':
            self.img1 = cv2.imread(original_graph)
            self.img2 = mask_graph
        elif input_type == 'pil':
            self.img1 = self.__image_to_opencv(original_graph)
            self.img2 = self.__image_to_opencv(mask_graph)
        elif input_type == 'cv2':
            self.img1 = original_graph
            self.img2 = mask_graph
        else:
            raise UnsupportedFormat(input_type)

    @staticmethod
    def __transparent_back(img):
        """
        :param img: 传入图片地址
        :return: 返回替换白色后的透明图
        """
        img = img.convert('RGBA')
        L, H = img.size
        color_0 = (255, 255, 255, 255)  # 要替换的颜色
        for h in range(H):
            for l in range(L):
                dot = (l, h)
                color_1 = img.getpixel(dot)
                if color_1 == color_0:
                    color_1 = color_1[:-1] + (0,)
                    img.putpixel(dot, color_1)
        return img

    def save_image(self, path, mask_flip=False):
        """
        用于保存透明图
        :param path: 保存位置
        :param mask_flip: 蒙版翻转，将蒙版的黑白颜色翻转;True翻转;False不使用翻转
        """
        if mask_flip:
            img2 = cv2.bitwise_not(self.img2)  # 黑白翻转
        image = cv2.add(self.img1, img2)
        image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # OpenCV转换成PIL.Image格式
        img = self.__transparent_back(image)
        img.save(path)

    @staticmethod
    def __image_to_opencv(image):
        """
        PIL.Image转换成OpenCV格式
        """
        img = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
        return img
def scale_resize(img,scale):
    # 要缩小图像，建议选择：cv2.INTER_AREA；如果要放大图像，cv2.INTER_CUBIC效果更好但是速度慢
    if scale <= 1:
        method = cv2.INTER_AREA
    else:
        method = cv2.INTER_CUBIC
    newh = int(img.shape[1] * scale)
    neww = int(img.shape[0] * scale)
    new_dim = [neww, newh]
    resizedimg = cv2.resize(img, new_dim, method)
    return resizedimg

def aaa(cc):
    img = cv2.imread('a.jpg', cv2.IMREAD_GRAYSCALE)
    mask = img.copy()
     
    # 二值化，100为阈值，小于100的变为255，大于100的变为0
    # 也可以根据自己的要求，改变参数：
    # cv2.THRESH_BINARY
    # cv2.THRESH_BINARY_INV
    # cv2.THRESH_TRUNC
    # cv2.THRESH_TOZERO_INV
    # cv2.THRESH_TOZERO
    _, binaryzation = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY_INV)
     
    # 找到所有的轮廓
    contours, _ = cv2.findContours(cc, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
     
    area = []
    # 找到最大的轮廓
    for k in range(len(contours)):
        print(k)
        area.append(cv2.contourArea(contours[k]))
    max_idx = np.argmax(np.array(area))
     
    # 填充最大的轮廓
    mask = cv2.drawContours(mask, contours, max_idx, 0, cv2.FILLED)
    mask = cv2.bitwise_not(mask)
    return mask

    
    
    
arga=(0.4,0.1,0.5,0.5)#face
argb=(0.4,0.1,0.6,0.1)#hair
argc=(0.01,0.02,1,1)#cloth

a =kf('a.jpg',arga)
b = kt('a.jpg',argb)
c = kc('a.jpg',argc)

cc = cv2.add(cv2.add(a,b),c)
cv2.imshow("GrabasdaCut s",cc)
cv2.waitKey(0)
person = cv2.imread("a.jpg")
back = cv2.imread("cc.jpg")
mask = cc
#将背景图resize到和原图一样的尺寸
back = cv2.resize(back,(person.shape[1],person.shape[0]))
#这一步是将背景图中的人像部分抠出来，也就是人像部分的像素值为0
scenic_mask =~mask
scenic_mask = scenic_mask  / 255.0
back[:,:,0] = back[:,:,0] * scenic_mask
back[:,:,1] = back[:,:,1] * scenic_mask
back[:,:,2] = back[:,:,2] * scenic_mask
#这部分是将我们的人像抠出来，也就是背景部分的像素值为0
mask = mask / 255.0
person[:,:,0] = person[:,:,0] * mask
person[:,:,1] = person[:,:,1] * mask
person[:,:,2] = person[:,:,2] * mask
#这里做个相加就可以实现合并
result = cv2.add(back,person)
#cv2.imshow("GrabCut Mas", a)
#cv2.imshow("GrabCut Mask", result)
#cv2.waitKey(0)

cv2.imshow("GrabasdaCut Mas",result)
cv2.waitKey(0)
####扣脸 扣头发 扣衣服分开再合并！！！！