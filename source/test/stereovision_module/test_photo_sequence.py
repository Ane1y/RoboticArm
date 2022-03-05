import os

import pytest
from source.stereovision_module.photo_sequence import PhotoSequence

os.chdir('/home/runner/work/RoboticArm/RoboticArm/source/stereovision_module')

def test_negative_total_photos():
    try:
        seq = PhotoSequence(-6)
        assert False
    except IOError:
        assert True

def test_take_photos():
    try:
        seq = PhotoSequence(15)
        seq.take_photos(1.5)
        assert False
    except IOError:
        assert True

def test_saving_of_pair_images():
    try:
        total_photo = 3        #more than we have in src folder
        seq = PhotoSequence(total_photo)
        seq.pair_images()
        assert False
    except OSError:
        assert True