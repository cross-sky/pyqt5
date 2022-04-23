'''
Author: your name
Date: 2022-04-09 10:03:42
LastEditTime: 2022-04-23 17:15:56
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \video\rd505_cmd.py
'''

import logging
from vrf.vrf_define import *
import sys

logging.basicConfig(level=logging.DEBUG)
sys.path.append("..")


def string_to_bytes(strs):
    '''
    string to bytes
    eg:
    '0123456789ABCDEF0123456789ABCDEF'
    b'0123456789ABCDEF0123456789ABCDEF'
    '''
    return bytes(strs, encoding='utf8')

def string_to_listbytes(strs):
    '''
    string to bytes
    eg:
    '0123456789ABCDEF0123456789ABCDEF'
    b'0123456789ABCDEF0123456789ABCDEF'
    '''
    return bytes.fromhex(strs)
    #return bytes(strs, encoding='utf8')



def checkFcc(str_data):
    hex_data = string_to_listbytes(str_data)
    temp = 0
    cc = hex_data[hex_data[DATA_BC]+4]
    d_len = hex_data[DATA_BC]+4
    if d_len > len(hex_data):
        logging.debug('Len error')
        return ''
        
    for i in range(0, hex_data[DATA_BC]+4):
        temp ^= hex_data[i]

    logging.debug('check fcc: {}, data fcc: {}'.format(hex(temp), hex(cc)))
    if((temp&0xff) != cc ):
        logging.debug('FCC CCHECK ERROR!!!')
        return ''
    
    logging.debug('FCC CHECK OK')
    return hex_data


class RD505CMD():
    def __init__(self, data) -> None:
        # self.data_org = data
        self.data = checkFcc(data) #string_to_listbytes(data)
        self.state_dict = {}
    
    # CHECK FCC ERROR
    def cmd_check(self):
        if (self.data != ''):
            self.decodeCmd4cRCcontrol()
            self.decodeCmd49ResMain()
            self.decodeCmd0DResMain()
            self.decodeCmd0DRCcontrol()

    def cmd_decode_addr(self,  hex_data:list):
        dat_dict = {}
        dat_dict[RCCONTROL_ADDR] = hex_data[DATA_SA] + ((hex_data[DATA_EA] & 0xf0) << 8)
        dat_dict[MAIN_ADDR] = hex_data[DATA_DA] + ((hex_data[DATA_EA] & 0x0F) << 8)
        dat_dict[DATA_LEN] = len(hex_data) - 5
        dat_dict[DATA_CMD] = hex_data[DATA_CMD]
        dat_dict[CMD_REPLAY] = (hex_data[DATA_CC]) & 0x01
        dat_dict[CMD_FORMATE] = (hex_data[DATA_CC]) & (CMD_CC_MASK_CMD_FORMAT)
        return dat_dict

    # check cmd cc formate 00 config,  bit 2 request, bit 3 response
    def check_cmd_cc(self, hex_data, cmd,  cmd_format):
            ex_flag = (hex_data[DATA_CC]&BIT1) >> 1

            if ((not ex_flag) and (hex_data[DATA_CMD]!= cmd)):
                logging.debug('data is not cmd: {} '.format(hex(cmd)))
                return False
                
            if ((hex_data[DATA_CC] & CMD_CC_MASK_CMD_FORMAT) != cmd_format):  # response
                logging.debug('data is not cmd {}, {}'.format(hex(cmd), CMD_CC_TYPE_BIT3_4_DICT.get(cmd_format)))
                return False
            return True

    # decode cmd 4c rc request
    def decodeCmd4cRCcontrol(self):
        hex_data = self.data

        self.data_decode_dict = {}
        # check
        if (not self.check_cmd_cc(hex_data, 0x4c, CMD_CC_CMD_FORMAT_CONFIG)):
            return
        logging.debug('decode cmd 4c response')
        self.data_decode_dict.update(self.cmd_decode_addr(hex_data))

        self.data_decode_dict[SYSTEM_MODE] = hex_data[6] & 0x07
        
        # check 4c type  temp or windspeed or up_wind_dir or lr_wind_dir
        self.data_decode_dict[CMD_TYPE] = hex_data[6] & 0xf8

        self.data_decode_dict[WIND_SPEED] = hex_data[7] & (BIT6 + 0x07)

        self.data_decode_dict[WIN_DIR_UP] = hex_data[7] & 0x38

        self.data_decode_dict[SYS_TEMPT] = (hex_data[8] - 70 ) / 2

        self.data_decode_dict[WIN_DIR_LR] = hex_data[9] & 0x3f


    def decodeCmd0DRCcontrol(self):
        self.data_decode_cmd0d = {}
        hex_data = self.data

        if (not self.check_cmd_cc(hex_data, 0x0d, CMD_CC_CMD_FORMAT_REQUEST)):
            return

        logging.debug('decode cmd0D Rc recontrol request')
        self.data_decode0d_rc_dict = {}
        self.data_decode0d_rc_dict.update(self.cmd_decode_addr(hex_data))


    def decodeCmd81ResMain(self):
        logging.debug('decode cmd 81')


    def decodeCmd49ResMain(self):
        self.data_decode_rescmd49 = {}
        hex_data = self.data

        if (not self.check_cmd_cc(hex_data, 0x49, CMD_CC_CMD_FORMAT_RESPONSE)):
            return
        ex_flag = (hex_data[DATA_CC]&BIT1) >> 1

        if ((ex_flag) and (hex_data[DATA_CMD+3] != 0x49)):
            logging.debug('cmd + 3 data is not cmd49 res')
            return

        logging.debug('decode cmd 49 main response')
        self.data_decode_rescmd49.update(self.cmd_decode_addr(hex_data))
        self.data_decode_rescmd49[ERROR_SYSTEM_NUM] = ((hex_data[DATA_AU0]<<2) + ((hex_data[DATA_AU1]&0xc0)>>6)) - 0x20
        self.data_decode_rescmd49[ERROR_INDOOR_NUM] = hex_data[DATA_AU1]&0x3F
        self.data_decode_rescmd49[ERROR_CODE] = hex_data[DATA_AN] 
        logging.debug(self.data_decode_rescmd49[DATA_LEN])


    def decodeCmd81ResMain(self):
        self.data_decode_rescmd81 = {}
        hex_data = self.data
        
        ex_flag = (hex_data[DATA_CC]&BIT1) >> 1
        # (hex_data[DATA_CC]&BIT1)  == BIT1
        if ((not ex_flag) and (hex_data[DATA_CMD]!= 0x81)):
            logging.debug('data is not cmd81 res')
            return

    

    def decodeCmd0DResMain(self):
        self.data_decode_rescmd0d = {}
        hex_data = self.data
        
        if (not self.check_cmd_cc(hex_data, 0x0d, CMD_CC_CMD_FORMAT_RESPONSE)):
            return

        logging.debug('decode cmd 0x0d  main response')
        format_temp = (hex_data[DATA_CC]&(BIT2+BIT3))
        if (format_temp == CMD_CC_CMD_FORMAT_RESPONSE):
            if (hex_data[DATA_BC] != 0x12):
                logging.debug('data bc is not 0x12')
                return False
            self.data_decode_rescmd0d.update(self.cmd_decode_addr(hex_data))
            self.data_decode_rescmd0d[SYSTEM_NUMBBER] = (hex_data[DATA_CMD+1]<<2)+(hex_data[DATA_CMD+2]>>6) - 0x20
            self.data_decode_rescmd0d[INDOOR_NUMBER] = (hex_data[DATA_CMD+2]&0x3F)

            