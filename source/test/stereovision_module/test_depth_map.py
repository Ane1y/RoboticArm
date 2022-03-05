import os

import pytest
from stereovision.calibration import StereoCalibration
from source.stereovision_module.depth_map import DepthMap

os.chdir('/home/runner/work/RoboticArm/RoboticArm/source/stereovision_module')

def test_build_depth_map_wrong_path():
    depthMap = DepthMap()
    try:
        depthMap.build_depth_map("wrong.png")
        assert False
    except OSError:
        assert True


def test_build_depth_map_wrong_calib_dir():
    try:
        calibration = StereoCalibration(input_folder='mess')
        assert False
    except IOError:
        assert True

def test_build_depth_map_rectified_pair():
    depthMap = DepthMap()
    rectified_pair, disparity = depthMap.build_depth_map("scenes/photo.png")
    assert(len(rectified_pair) == 2)

def test_pair_img_size():
    depthMap = DepthMap()
    rectified_pair, disparity = depthMap.build_depth_map("scenes/photo.png")
    assert(rectified_pair[0].shape == 720L, 527L)
