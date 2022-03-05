import pytest

from stereovision_module.Stereovision import *


def test_parser_calib():
    parser, _ = parse_args(['-c'])
    assert(parser.calib == True)

def test_parser_shoot():
    parser, _  = parse_args(['-s'])
    assert (parser.shoot == True)

def test_parser_depthmap():
    parser, _  = parse_args(['-d'])
    assert (parser.depthmap == True)

def test_parser_parameters():
    parser, _  = parse_args(['-p'])
    assert (parser.parameters == True)