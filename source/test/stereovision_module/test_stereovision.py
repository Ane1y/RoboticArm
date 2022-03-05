import pytest

import stereovision_module.Stereovision


def test_parser_calib():
    parser, _ = Stereovision.parse_args(['-c'])
    assert(parser.calib == True)

def test_parser_shoot():
    parser, _  = Stereovision.parse_args(['-s'])
    assert (parser.shoot == True)

def test_parser_depthmap():
    parser, _  = Stereovision.parse_args(['-d'])
    assert (parser.depthmap == True)

def test_parser_parameters():
    parser, _  = Stereovision.parse_args(['-p'])
    assert (parser.parameters == True)