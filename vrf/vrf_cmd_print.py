'''
Author: your name
Date: 2022-04-23 10:16:57
LastEditTime: 2022-04-30 23:17:08
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pyqt5\vrf\vrf_cmd_print.py
'''
from vrf.vrf_cmd import *

# request cmd 0x4c
def myprint_cmd0x4c_request(dat_dict):
    addrs = myprint_addr(dat_dict)
    strs = [
        'SYSTEM_MODE: {}'.format(SYSTEM_MODE_DICT.get(dat_dict[SYSTEM_MODE])),
        'CMD_TYPE: {}'.format(CMD4C_TYPE_DIC.get(dat_dict[CMD_TYPE])),
        'WIND_SPEED: {}'.format(WIND_SPEED_DIC.get(dat_dict[WIND_SPEED])),
        'WIN_DIR_UP: {}'.format(WIN_DIR_UP_DIC.get(dat_dict[WIN_DIR_UP])),
        'SYS_TEMPT: {}'.format(dat_dict[SYS_TEMPT]),
        'WIN_DIR_LR: {}'.format(WIN_DIR_LR_DIC.get(dat_dict[WIN_DIR_LR]))
    ]
    strs += addrs
    for s in strs:
        logging.debug(s)
    return strs
    
    # hex(1)[2:].zfill(2)
def myprint_cmd0x49_response(dat_dict):
    addrs = myprint_addr(dat_dict)
    strs = [
        'ERROR_SYSTEM_NUM: {}'.format(hex(dat_dict[ERROR_SYSTEM_NUM])),
        'ERROR_INDOOR_NUM: {}'.format(hex(dat_dict[ERROR_INDOOR_NUM])),
        'ERROR_CODE: {}'.format(hex(dat_dict[ERROR_CODE]))
    ]
    strs += addrs

    for s in strs:
        logging.debug(s)
    return strs

def myprint_cmd0x0d_request(dat_dict):
    strs = myprint_addr(dat_dict)
    for s in strs:
        logging.debug(s)
    return strs

def myprint_cmd0x0d_response(dat_dict):
    addrs = myprint_addr(dat_dict)
    strs = [
        'SYSTEM_NUMBBER: {}'.format(hex(dat_dict[SYSTEM_NUMBBER])),
        'INDOOR_NUMBER: {}'.format(hex(dat_dict[INDOOR_NUMBER])),
    ]
    strs += addrs

    for s in strs:
        logging.debug(s)
    return strs

def myprint_addr(dat_dict):
    strs = [
        'RCCONTROL_ADDR: {}'.format(hex(dat_dict[RCCONTROL_ADDR])),
        'MAIN_ADDR: {}'.format(hex(dat_dict[MAIN_ADDR])),
        'DATA_LEN: {}'.format(hex(dat_dict[DATA_LEN])),
        'DATA_CMD: {}'.format(hex(dat_dict[DATA_CMD])),
        'CMD_REPLAY: {}'.format(hex(dat_dict[CMD_REPLAY])),
        'CMD_FORMAT: {}, {}'.format(hex(dat_dict[CMD_FORMATE]),CMD_CC_TYPE_BIT3_4_DICT.get(dat_dict[CMD_FORMATE])),
    ]

    return strs




def myprint_cmd_comm_request(dat_dict):
    strs = myprint_addr(dat_dict)
    for s in strs:
        logging.debug(s)
    return strs

def myprint_cmd0x06_request(dat_dict):
    return myprint_cmd_comm_request(dat_dict)

def myprint_cmd0x0a_request(dat_dict):
    return myprint_cmd_comm_request(dat_dict)

def myprint_cmd0x0a_response(dat_dict):
    strs = [
        'COLD UD_WIND GROUP: {}'.format(UD_WIND_DIR_GROUP_DICT.get(dat_dict[UD_WINDIR_GROUP][SYSTEM_MODE_COLD])),
        'COLD TEMP PERIOD: {}, {}'.format(dat_dict[COLD_TEMP_PERIOD][0], dat_dict[COLD_TEMP_PERIOD][1]),
        'WARM UD_WIND GROUP: {}'.format(UD_WIND_DIR_GROUP_DICT.get(dat_dict[UD_WINDIR_GROUP][SYSTEM_MODE_WARM])),
        'WARM TEMP PERIOD: {}, {}'.format(dat_dict[WARM_TEMP_PERIOD][0], dat_dict[WARM_TEMP_PERIOD][1]),
        'WET UD_WIND GROUP: {}'.format(UD_WIND_DIR_GROUP_DICT.get(dat_dict[UD_WINDIR_GROUP][SYSTEM_MODE_WET])),
        'WET TEMP PERIOD: {}, {}'.format(dat_dict[WET_TEMP_PERIOD][0], dat_dict[WET_TEMP_PERIOD][1]),
        'AUTO UD_WIND GROUP: {}'.format(UD_WIND_DIR_GROUP_DICT.get(dat_dict[UD_WINDIR_GROUP][SYSTEM_MODE_AUTO])),
        'AUTO TEMP PERIOD: {}, {}'.format(dat_dict[AUTO_TEMP_PERIOD][0], dat_dict[AUTO_TEMP_PERIOD][1]),
        'WIND UD_WIND GROUP: {}'.format(UD_WIND_DIR_GROUP_DICT.get(dat_dict[UD_WINDIR_GROUP][SYSTEM_MODE_WIND])),
        # 'COLD TEMP PERIOD: {}, {}'.format(dat_dict[COLD_TEMP_PERIOD][0], dat_dict[COLD_TEMP_PERIOD][1]),
        'ALLOWMODE : {}'.format(hex(dat_dict[ALLOW_MODE])),
        'SPEED GROUP: {}'.format(WIND_SPEED_GROUP_DICT.get(dat_dict[SPEED_GROUP])),
        'WIND LR_WIND GROUP: {}'.format(LR_WIND_DIR_GROUP_DICT.get(dat_dict[LR_WINDIR_GROUP])),
    ]
    strs += myprint_addr(dat_dict)
    for s in strs:
        logging.debug(s)
    return strs


def myprint_cmd_unknow(dat_dict):
    strs = [
        'UNKNOW CMD: {}'.format(str(dat_dict['HEX_DATA'])),
    ]
    for s in strs:
        logging.debug(s)
    return strs

def myprint_cmd0x81_request(dat_dict):
    addrs = myprint_addr(dat_dict)
    strs = [
        'ERROR CODE: {}'.format(hex(dat_dict[ERROR_CODE])),
    ]
    strs += addrs

    for s in strs:
        logging.debug(s)
    return strs

def myprint_fcc_error(dat_dict):
    strs = [
        'error: {}'.format(dat_dict['HEX_DATA']),
    ]
    for s in strs:
        logging.debug(s)
    return strs