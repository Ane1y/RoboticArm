import os

from stereovision_module.dm_tune import *

os.chdir('/home/runner/work/RoboticArm/RoboticArm/source/stereovision_module')

def test_is_pair_calibrated():
    calibration_files = os.listdir('ress')
    assert(x for x in calibration_files if x == "cam_mats_left.npy")

def test_is_there_setting_file():
    fName = '3dmap_set.txt'
    f=open(fName, 'r')
    data = json.load(f)
    assert(list(map(type, (data[key] for key in data)))[0] is int)

def test_save_map_settings():
    save_map_settings(1)
    fName = '3dmap_set.txt'
    f = open(fName, 'r')
    data = json.load(f)
    assert(data['minDisparity']==MDS)
