'''
Author: your name
Date: 2022-04-09 10:04:10
LastEditTime: 2022-04-23 23:36:47
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \video\test\test_rd505_cmd.py
'''

import pytest
import sys
import time
#import logging

sys.path.append(".")

from vrf.vrf_cmd_print import *

#logging.basicConfig(level=logging.DEBUG)

def print_t(datas:list):
    for i in range(len(datas)):
        logging.debug(datas[i])
        dec_cmd0D = RD505CMD(datas[i])
        dec_cmd0D.cmd_check()
        eval(dec_cmd0D.data_decode_dict.get(MYPRINT_FUNCTION))(dec_cmd0D.data_decode_dict)
        logging.debug('----------------------------')
        
def test_decode_cmd4c_temp_response_from_main():
    data1 = '40 00 11 06 08 4C 09 75 6E 09 08 '
    datas = [data1] #
    print_t(datas)

def test_decode_cmd4c_wind_up_response_from_main():
    data1 = '40 00 11 06 08 4C 11 1C 7A 1B 7F'
    datas = [data1] #
    print_t(datas) 

def test_decode_cmd4c_wind_lr_response_from_main():
    data1 = '40 00 11 05 08 4C 0A 55 6C 23  '
    data2 = '40 FE 10 05 00 4C E2 55 6C 3C '
    data3 = '40 FE 10 05 00 4C E2 13 6C 7A '
    data4 = '40 00 11 05 08 4C 12 13 6C 7D  '

    datas = [data1, data2, data3, data4] #
    print_t(datas)

def test_decode_cmd49_response_from_main():
    data1 = '00 FE 58 06 80 49 08 00 00 40 21'
    data2 = '00 FE 58 06 80 49 08 00 00 41 20'
    data3 = '00 FE 58 06 80 49 08 00 49 41 69'
    data4 = ' 00 FE 58 06 80 49 08 00 EC 40 CD'
    data5 = '00 FE 58 06 80 49 08 00 49 40 68'

    datas = [data1, data2, data3, data4, data5] #, data3, data4
    print_t(datas)


def test_decode_cmd0D_response_from_main():
    # 2-1
    data1 = '40 40 18 12 80 0D 08 40 FE FE FE FE FE FE FE FE FE FE FE FE FE FE CF'
    # 1-1
    data2 = '00 40 18 12 80 0D 08 00 FE FE FE FE FE FE FE FE FE FE FE FE FE FE CF'

    datas = [data1, data2] #, data3, data4, data5
    print_t(datas)

def test_decode_cmd0D_request_to_main():
    data1 = '40 F0 15 02 00 0D AA'
    datas = [data1] #, data3, data4, data5
    print_t(datas)


def test_fcc_check():
    # data = '00 FE 58 06 80 49 08 00 00 40 21'
    data = '01 FE 10 02 80 8A E7'
    assert(checkFcc(data) != '')