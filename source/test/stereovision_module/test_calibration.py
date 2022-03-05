import os
from os import path

import pytest

import source.stereovision_module.params as params
from source.stereovision_module.calibration import Calibrator

os.chdir('/home/runner/work/RoboticArm/RoboticArm/source/stereovision_module')

def test_show_rectified_pair():
    calib = Calibrator()
    try:
        calib.show_rectified_pair(100)
        assert False
    except IOError:
        assert True

def test_first_photo_less_than_last():
    assert(params.TOTAL_PHOTOS - params.FIRST_PHOTO > 0)

def test_show_rectified_pair_saving():
    calib = Calibrator()
    calib.show_rectified_pair(1)
    file_path = os.getcwd() + "/rectifyed_left.jpg"
    assert(os.path.isfile(file_path) is True)