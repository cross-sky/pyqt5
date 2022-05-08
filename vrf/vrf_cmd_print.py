'''
Author: your name
Date: 2022-04-23 10:16:57
LastEditTime: 2022-05-08 12:28:33
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

    
def myprint_fcc_error(dat_dict):
    strs = [
        'error: {}'.format(dat_dict['HEX_DATA']),
    ]
    for s in strs:
        logging.debug(s)
    return strs


def myprint_cmd0x49_response(dat_dict):
    addrs = myprint_addr(dat_dict)
    strs = [
        'ERROR_SYSTEM_NUM: {}'.format(dat_dict[ERROR_SYSTEM_NUM] + 1),
        'ERROR_INDOOR_NUM: {}'.format(dat_dict[ERROR_INDOOR_NUM] + 1),
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

def myprint_cmd0x81_response(dat_dict):
    strs = [
        'PRE_HEAT : {}'.format(dat_dict[PRE_HEAT]),
        'NANOE_AB : {}'.format(dat_dict[NANOE_AB]),
        'NANOEG_AB : {}'.format(dat_dict[NANOEG_AB]),
        'SYSTEM_STATUS : {}'.format(dat_dict[SYSTEM_STATUS]),
        'PRE_INDOOR : {}'.format(dat_dict[PRE_INDOOR]),
        'SYSTEM_MODE : {}'.format(SYSTEM_MODE_DICT.get(dat_dict[SYSTEM_MODE])),
        'WIN_DIR_UP : {}'.format(WIN_DIR_UP_DIC.get(dat_dict[WIN_DIR_UP])),
        'FRESH_AIR : {}'.format(dat_dict[FRESH_AIR]),
        'MODE_FIT : {}'.format(dat_dict[MODE_FIT]),
        'TRY_RUN : {}'.format(dat_dict[TRY_RUN]),
        'ALLOW_MODE : {}'.format(dat_dict[ALLOW_MODE]),
        'FILTER_RST_SIGN : {}'.format(dat_dict[FILTER_RST_SIGN]),
        'CENTRAL_CTR_BAN_FLAG : {}'.format(hex(dat_dict[CENTRAL_CTR_BAN_FLAG])),
        'CENTRAL_CTR_ADDR : {}'.format(hex(dat_dict[CENTRAL_CTR_ADDR])),
        'SYS_TEMPT : {}'.format(dat_dict[SYS_TEMPT]),
        'STYLE_A2W_TEMPT : {}'.format(dat_dict[STYLE_A2W_TEMPT]),
        'WIND_SPEED :{},  {}'.format(hex(dat_dict[WIND_SPEED]),WIND_SPEED_DIC.get(dat_dict[WIND_SPEED])),
        'WARNING_MACHINE : {}'.format(dat_dict[WARNING_MACHINE]),
        'SAVE_ENERGY : {}'.format(dat_dict[SAVE_ENERGY]),
        'ECONAVI : {}'.format(dat_dict[ECONAVI]),
        'NANOE_STATUS : {}'.format(dat_dict[NANOE_STATUS]),
        'CLEANING : {}'.format(dat_dict[CLEANING]),
        
        'WIN_DIR_LR :{}, {}'.format(hex(dat_dict[WIN_DIR_LR]),WIN_DIR_LR_DIC.get(dat_dict[WIN_DIR_LR])),
        
        ]
    strs += myprint_addr(dat_dict)
    for s in strs:
        logging.debug(s)
    return strs

def myprint_cmd0x0f_request(dat_dict):
    return myprint_cmd_comm_request(dat_dict)

def myprint_cmd0x0f_response(dat_dict):
    strs = [
        'COLD temperature: {}'.format(dat_dict[SYSTEM_TEMP_GROUP][SYSTEM_MODE_AUTO]),
        'WARM temperature: {}'.format(dat_dict[SYSTEM_TEMP_GROUP][SYSTEM_MODE_WARM]),
        'WET temperature: {}'.format(dat_dict[SYSTEM_TEMP_GROUP][SYSTEM_MODE_WET]),
        'AUTO temperature: {}'.format(dat_dict[SYSTEM_TEMP_GROUP][SYSTEM_MODE_COLD]),

        'COLD SPEED: {}'.format(WIND_SPEED_DIC.get(dat_dict[SYSTEM_SPEED_GROUP][SYSTEM_MODE_COLD])),
        'WARM SPEED: {}'.format(WIND_SPEED_DIC.get(dat_dict[SYSTEM_SPEED_GROUP][SYSTEM_MODE_WARM])),
        'WET SPEED: {}'.format(WIND_SPEED_DIC.get(dat_dict[SYSTEM_SPEED_GROUP][SYSTEM_MODE_WET])),
        'AUTO SPEED: {}'.format(WIND_SPEED_DIC.get(dat_dict[SYSTEM_SPEED_GROUP][SYSTEM_MODE_AUTO])),
        'WIND SPEED: {}'.format(WIND_SPEED_DIC.get(dat_dict[SYSTEM_SPEED_GROUP][SYSTEM_MODE_WIND])),
    ]
    strs += myprint_addr(dat_dict)
    for s in strs:
        logging.debug(s)
    return strs


def myprint_cmd0x0c_request(dat_dict:dict):
    strs = [
        'eep code : {}'.format(dat_dict[EP_ADDR])
        ]
    haskey = dat_dict.get(TIMER_TYPE)
    if(haskey != None):
        strs += [
        'TIMER_TYPE  : {}'.format(dat_dict[TIMER_TYPE]),
        'TIMER_HOUR  : {}'.format(dat_dict[TIMER_HOUR]),
        'TIMER_REMAIN_HOUR  : {}'.format(dat_dict[TIMER_REMAIN_HOUR]),
        ]
    strs += myprint_addr(dat_dict)
    for s in strs:
        logging.debug(s)
    return strs









