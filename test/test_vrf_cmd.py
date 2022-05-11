'''
Author: your name
Date: 2022-04-09 10:04:10
LastEditTime: 2022-05-11 22:56:23
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
    data1 = '40 00 11 06 08 4C 09 75 6E 09 09'
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


def test_decode_cmd06_request_to_main():
    data1 = '40 F1 15 03 00 06 00 A1'
    datas = [data1] #, data3, data4, data5
    print_t(datas)

def test_decode_cmd0a_req_res_to_main():
    data1 = '40 00 15 02 08 0A 55'
    data2 = '00 40 18 0E 80 0A 22 2F 0F 82 6A 82 66 82 6A 7C 68 32 1C'
    datas = [data1, data2] #, data3, data4, data5
    print_t(datas)


def test_decode_cm81_req_res_to_main():
    data1 = '40 01 15 04 08 81 00 00 D9'
    data2 = '01 FE 58 10 80 81 35 6C 02 00 6E 09 E9 FF 00 00 00 00 00 00 9C'
    datas = [data1, data2] #, data3, data4, data5
    print_t(datas)



def test_decode_cm0f_0c_10_req_res_to_main():
    data1 = '40 00 15 02 08 0F 50'
    data2 = '00 40 18 0A 80 0F 76 72 7A 82 23 55 03 00 54'
    data3 = '40 00 15 02 08 10 4F'
    data4 = '00 40 18 08 80 10 02 33 33 01 00 03 C0'
    data5 = '40 00 15 07 08 0C 81 00 00 48 00 9F'
    data6 = '00 40 18 08 80 0C 00 00 00 00 48 00 94'
    data7 = '40 00 15 02 08 08 57'
    data8 = '00 40 18 14 80 08 43 53 2D 4D 45 37 44 30 41 58 37 42 20 20 20 20 00 66 B8'
    data9 = '40 00 15 02 08 13 4C'
    data10 = '00 40 18 06 80 13 00 52 95 0B 01'
    data11 = '40 00 15 03 08 5F 00 01'
    data12 = '00 40 18 0B 80 5F 00 00 00 00 00 00 75 77 75 FB'
    data13 = '40 F0 10 03 00 51 00 F2'
    
    datas = [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13] #, data3, data4, data5
    print_t(datas)

    