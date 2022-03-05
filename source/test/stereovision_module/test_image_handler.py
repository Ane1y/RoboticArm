import pytest
from source.stereovision_module.image_handler import ImageHandler
import os
import cv2
os.chdir('/home/runner/work/RoboticArm/RoboticArm/source/stereovision_module')

def test_pair_img_size():
    imageToDisp = 'scenes/photo.png'
    hand = ImageHandler()
    pair_img = cv2.imread(imageToDisp, 0)
    imgLeft = pair_img[0:hand.photo_height, hand.leftIndent:hand.imageWidth]
    imgRight = pair_img[0:hand.photo_height, hand.rightIndent:hand.rightIndent + hand.imageWidth - 50]
    assert(pair_img.shape[0] == long(hand.photo_height)) and (pair_img.shape[1] == long(hand.photo_width))

def test_width():
    hand = ImageHandler()
    assert(hand.photo_width > 100) and (hand.photo_width <= 3280) #3280 - max resolution of pi camera

def test_height():
    hand = ImageHandler()
    assert(hand.photo_height > 100) and (hand.photo_height <= 2464)

def test_imageSize():
    hand = ImageHandler()
    assert(hand.imageWidth < (hand.photo_width / 2))

def test_imageFrames():
    hand = ImageHandler()
    assert(hand.imageWidth - hand.leftIndent) > 0

def test_empty_file():
    hand = ImageHandler()
    try:
        hand.split_image('lala.jpg')
        assert False
    except OSError:
        assert True
