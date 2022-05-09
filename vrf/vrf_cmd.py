'''
Author: your name
Date: 2022-04-09 10:03:42
LastEditTime: 2022-05-09 23:48:00
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \video\rd505_cmd.py
'''

import logging
from os import truncate
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

def bytes_to_hexstring(strs):
    '''
    bytes to hex string 
    eg:
    b'\x01#Eg\x89\xab\xcd\xef\x01#Eg\x89\xab\xcd\xef'
    '01 23 45 67 89 AB CD EF 01 23 45 67 89 AB CD EF'
    '''
    return ' '.join(['%02X' % b for b in strs])

# fcc check ok return ->bytes, 
# fcc check error return str
def checkFcc(str_data):
    try: 
        hex_data = string_to_listbytes(str_data)
    except Exception as e:
        logging.debug(e)
        return "could not convert str to listbytes {}, {}".format(str_data, e)
    temp = 0
    if len(hex_data) < 7:
        logging.debug('error, lex_len {} < 7(shortest data)'.format(len(hex_data)))
        return 'error, lex_len {} < 7(shortest data)'.format(len(hex_data))

    if len(hex_data) < DATA_BC+1:
        logging.debug('error, lex_len {} < DATA_BC(4)'.format(len(hex_data)))
        return 'error, lex_len {} < DATA_BC(4)'.format(len(hex_data))
        
    d_len = hex_data[DATA_BC]+5
    if d_len != len(hex_data):
        logging.debug('cmd_len: {} , hex_len: {}'.format(d_len, len(hex_data)))
        logging.debug('Len error')
        return 'error, cmd_len: {} , hex_len: {}'.format(d_len, len(hex_data))
        

    cc = hex_data[hex_data[DATA_BC]+4]
    for i in range(0, hex_data[DATA_BC]+4):
        temp ^= hex_data[i]

    logging.debug('check fcc: {}, data fcc: {}'.format(hex(temp), hex(cc)))
    if((temp&0xff) != cc ):
        logging.debug('FCC CCHECK ERROR!!!')
        return 'error, check fcc: {}, data fcc: {}'.format(hex(temp), hex(cc))
    
    logging.debug('FCC CHECK OK')
    return hex_data


class RD505CMD():
    def __init__(self, data) -> None:
        self.data = checkFcc(data) #string_to_listbytes(data)
        self.state_dict = {}
    
    # CHECK FCC ERROR
    def cmd_check(self):
        unknow_cmd = False

        # compare type is bytes or strs
        if (isinstance(self.data, bytes)):
            unknow_cmd |= self.decode_cmd4c_request_from_main()
            unknow_cmd |= self.decode_cmd49_response_from_main()
            unknow_cmd |= self.decode_cmd0d_response_from_main()
            unknow_cmd |= self.decode_cmd0d_request_to_main()
            unknow_cmd |= self.decode_cmd06_request_to_main()
            unknow_cmd |= self.decode_cmd0a_request_to_main()
            unknow_cmd |= self.decode_cmd0a_response_from_main()
            unknow_cmd |= self.decode_cmd81_request_to_main()
            unknow_cmd |= self.decode_cmd81_response_from_main()
            unknow_cmd |= self.decode_cmd0f_request_to_main()
            unknow_cmd |= self.decode_cmd0f_response_from_main()
            unknow_cmd |= self.decode_cmd0c_request_to_main()
            unknow_cmd |= self.decode_cmd0c_response_from_main()

            if (not unknow_cmd):
                self.my_print_unknow_code()
        else:
            self.my_print_len_or_fcc_error()


    def my_print_len_or_fcc_error(self):
        logging.debug("len or fcc error!!!")
        err_data = self.data
        decode_dict = {}
        decode_dict[MYPRINT_FUNCTION] = 'myprint_fcc_error'
        decode_dict['HEX_DATA'] = err_data
        self.data_decode_dict = decode_dict

    def my_print_unknow_code(self):
        logging.debug("cmd unknow!!!")
        hex_data = self.data
        decode_dict = {}
        decode_dict[MYPRINT_FUNCTION] = 'myprint_cmd_unknow'
        decode_dict['HEX_DATA'] = bytes_to_hexstring(hex_data)
        self.data_decode_dict = decode_dict

    def myprint_function(self,cmd,  cmd_format):
        fun_print = PRINT_FUNCTION_DIC.get(cmd_format).format(hex(cmd)[2:].zfill(2))
        return fun_print

    # decode addr information
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

            if (hex_data[DATA_CMD]!= cmd):
                logging.debug('data is not cmd: {} '.format(hex(cmd)))
                return False

            if ((not ex_flag) and (hex_data[DATA_CMD]!= cmd)):
                logging.debug('exflag and data is not cmd: {} '.format(hex(cmd)))
                return False
                
            if ((hex_data[DATA_CC] & CMD_CC_MASK_CMD_FORMAT) != cmd_format):  # response
                logging.debug('data is not cmd {}, {}'.format(hex(cmd), CMD_CC_TYPE_BIT3_4_DICT.get(cmd_format)))
                return False
            return True
    
    def get_cmd_cc(self, hex_data):
        return (hex_data[DATA_CC]&BIT1) >> 1

    # decode cmd 4c rc request
    def decode_cmd4c_request_from_main(self):
        hex_data = self.data
        decode_dict = {}
        cmd_cc = 0x4c

        # check
        if (not self.check_cmd_cc(hex_data, cmd_cc, CMD_CC_CMD_FORMAT_CONFIG)):
            return False

        logging.debug('decode cmd 4c config')
        decode_dict.update(self.cmd_decode_addr(hex_data))

        decode_dict[SYSTEM_MODE] = hex_data[6] & 0x07
        
        # check 4c type  temp or windspeed or up_wind_dir or lr_wind_dir
        decode_dict[CMD_TYPE] = hex_data[6] & 0xf8

        decode_dict[WIND_SPEED] = hex_data[7] & (BIT6 + 0x07)

        decode_dict[WIN_DIR_UP] = hex_data[7] & 0x38

        decode_dict[SYS_TEMPT] = (hex_data[8] - 70 ) / 2

        decode_dict[WIN_DIR_LR] = hex_data[9] & 0x3f

        decode_dict[MYPRINT_FUNCTION] = self.myprint_function(cmd_cc, CMD_CC_CMD_FORMAT_REQUEST)
        self.data_decode_dict = decode_dict
        return True

    def decode_cmdcomm_request_to_main(self, cmd):
        decode_dict = {}
        hex_data = self.data
        # cmd = 0x06
        # check cmd 06 req
        if (self.check_cmd_cc(hex_data, cmd, CMD_CC_CMD_FORMAT_REQUEST)):
            logging.debug('decode cmd06 Rc recontrol request')
            decode_dict.update(self.cmd_decode_addr(hex_data))
            decode_dict[MYPRINT_FUNCTION] = self.myprint_function(cmd, CMD_CC_CMD_FORMAT_REQUEST)
            self.data_decode_dict = decode_dict
            return True
        # elif(not self.check_cmd_cc(hex_data, cmd, CMD_CC_CMD_FORMAT_CONFIG)):
        #     pass
            
        return False

    def decode_cmd06_request_to_main(self):
        decode_dict = {}
        hex_data = self.data
        cmd = 0x06
        # check cmd 06 req
        if (self.check_cmd_cc(hex_data, cmd, CMD_CC_CMD_FORMAT_REQUEST)):
            logging.debug('decode cmd06 Rc recontrol request')
            decode_dict.update(self.cmd_decode_addr(hex_data))
            decode_dict[MYPRINT_FUNCTION] = self.myprint_function(cmd, CMD_CC_CMD_FORMAT_REQUEST)
            self.data_decode_dict = decode_dict
            return True
        elif(not self.check_cmd_cc(hex_data, cmd, CMD_CC_CMD_FORMAT_CONFIG)):
            pass
            
        return False
        
    #  CMD 06 RESPONSE
    # TODO need to test
    def decode_cmd06_response_from_main(self):
        hex_data = self.data
        decode_dict = {}
        cmd = 0x06
        if (not self.check_cmd_cc(hex_data, cmd, CMD_CC_CMD_FORMAT_RESPONSE)):
            return False

        if ((hex_data[DATA_CC]&BIT1) and (hex_data[DATA_CMD + 3] != cmd)):
            return False

        logging.debug('decode cmd 0x06  main response')
        format_temp = (hex_data[DATA_CC]&CMD_CC_MASK_CMD_FORMAT)
        if (format_temp == CMD_CC_CMD_FORMAT_RESPONSE):
            # if (hex_data[DATA_BC] != 0x12):
            #     logging.debug('data bc is not 0x12')
            #     return False
            decode_dict.update(self.cmd_decode_addr(hex_data))
            decode_dict[MYPRINT_FUNCTION] = self.myprint_function(cmd, CMD_CC_CMD_FORMAT_RESPONSE)
            # decode_dict[SYSTEM_NUMBBER] = (hex_data[DATA_CMD+1]<<2)+(hex_data[DATA_CMD+2]>>6) - 0x20
            # decode_dict[INDOOR_NUMBER] = (hex_data[DATA_CMD+2]&0x3F)
            self.data_decode_dict = decode_dict
        
        return True

    #  CMD 0D REQUEST
    def decode_cmd0d_request_to_main(self):
        decode_dict = {}
        hex_data = self.data

        if (not self.check_cmd_cc(hex_data, 0x0d, CMD_CC_CMD_FORMAT_REQUEST)):
            return False

        logging.debug('decode cmd0D Rc recontrol request')
        decode_dict.update(self.cmd_decode_addr(hex_data))
        decode_dict[MYPRINT_FUNCTION] = self.myprint_function(0x0d, CMD_CC_CMD_FORMAT_REQUEST)
        self.data_decode_dict = decode_dict

        return True

    #  CMD 0D RESPONSE
    def decode_cmd0d_response_from_main(self):
        hex_data = self.data
        decode_dict = {}
        
        if (not self.check_cmd_cc(hex_data, 0x0d, CMD_CC_CMD_FORMAT_RESPONSE)):
            return False

        logging.debug('decode cmd 0x0d  main response')
        format_temp = (hex_data[DATA_CC]&(CMD_CC_MASK_CMD_FORMAT))
        if (format_temp == CMD_CC_CMD_FORMAT_RESPONSE):
            if (hex_data[DATA_BC] != 0x12):
                logging.debug('data bc is not 0x12')
                return False
            decode_dict.update(self.cmd_decode_addr(hex_data))
            decode_dict[MYPRINT_FUNCTION] = self.myprint_function(0x0d, CMD_CC_CMD_FORMAT_RESPONSE)
            decode_dict[SYSTEM_NUMBBER] = (hex_data[DATA_CMD+1]<<2)+(hex_data[DATA_CMD+2]>>6) - 0x20
            decode_dict[INDOOR_NUMBER] = (hex_data[DATA_CMD+2]&0x3F)
            self.data_decode_dict = decode_dict
        
        return True

    #  CMD 0A REQUEST
    def decode_cmd0a_request_to_main(self):
        return self.decode_cmdcomm_request_to_main(0x0a)

    def decode_cmd0a_response_from_main(self):
        hex_data = self.data
        decode_dict = {}
        cmd = 0x0a

        if (not self.check_cmd_cc(hex_data, cmd, CMD_CC_CMD_FORMAT_RESPONSE)):
            return False

        logging.debug('decode cmd 0x0a  main response')
        format_temp = (hex_data[DATA_CC]&CMD_CC_MASK_CMD_FORMAT)
        if (format_temp == CMD_CC_CMD_FORMAT_RESPONSE):
            # len is 0x0e or 0x0d
            if (hex_data[DATA_BC] == 0x0d or hex_data[DATA_BC] == 0x0e):
                ud_group  = [0, 0, 0, 0, 0]
                if((hex_data[CMD0A_RES_DATA_FL] & 0X0F) == 0):
                    ud_group[SYSTEM_MODE_AUTO] = UD_WIND_DIR_GROUP_NO
                    ud_group[SYSTEM_MODE_WARM] = UD_WIND_DIR_GROUP_NO
                    ud_group[SYSTEM_MODE_COLD] = UD_WIND_DIR_GROUP_NO
                    ud_group[SYSTEM_MODE_WET] = UD_WIND_DIR_GROUP_NO
                    ud_group[SYSTEM_MODE_WIND] = UD_WIND_DIR_GROUP_NO
                    
                elif((hex_data[CMD0A_RES_DATA_FL] & 0X0F) == 1):
                    ud_group[SYSTEM_MODE_AUTO] = UD_WIND_DIR_GROUP_ONLY_AUTO
                    ud_group[SYSTEM_MODE_WARM] = UD_WIND_DIR_GROUP_ONLY_AUTO
                    ud_group[SYSTEM_MODE_COLD] = UD_WIND_DIR_GROUP_ONLY_AUTO
                    ud_group[SYSTEM_MODE_WET] = UD_WIND_DIR_GROUP_ONLY_AUTO
                    ud_group[SYSTEM_MODE_WIND] = UD_WIND_DIR_GROUP_ONLY_AUTO
                    
                elif((hex_data[CMD0A_RES_DATA_FL] & 0X0F) == 2):
                    ud_group[SYSTEM_MODE_AUTO] = UD_WIND_DIR_GROUP_5
                    ud_group[SYSTEM_MODE_WARM] = UD_WIND_DIR_GROUP_5
                    ud_group[SYSTEM_MODE_COLD] = UD_WIND_DIR_GROUP_3
                    ud_group[SYSTEM_MODE_WET] = UD_WIND_DIR_GROUP_3
                    ud_group[SYSTEM_MODE_WIND] = UD_WIND_DIR_GROUP_5
                    
                else:
                    ud_group[SYSTEM_MODE_AUTO] = UD_WIND_DIR_GROUP_5
                    ud_group[SYSTEM_MODE_WARM] = UD_WIND_DIR_GROUP_5
                    ud_group[SYSTEM_MODE_COLD] = UD_WIND_DIR_GROUP_3
                    ud_group[SYSTEM_MODE_WET] = UD_WIND_DIR_GROUP_3
                    ud_group[SYSTEM_MODE_WIND] = UD_WIND_DIR_GROUP_5
                    
                decode_dict[UD_WINDIR_GROUP] = ud_group

                #  allow mode
                decode_dict[ALLOW_MODE] = hex_data[CMD0A_RES_DATA_RS]

                # LR window
                if(hex_data[CMD0A_RES_DATA_FM] & (BIT3|BIT2|BIT1)):
                    if (hex_data[CMD0A_RES_DATA_FM] & BIT4):
                        decode_dict[SPEED_GROUP] = WIND_SPEED_GROUP_5
                    else:
                        decode_dict[SPEED_GROUP] = WIND_SPEED_GROUP_3
                else:
                    decode_dict[SPEED_GROUP] = WIND_SPEED_GROUP_NO

                decode_dict[COLD_TEMP_PERIOD] = [int((hex_data[CMD0A_RES_DATA_CT] - 70) / 2), int((hex_data[CMD0A_RES_DATA_CB] - 70) / 2)]
                decode_dict[WARM_TEMP_PERIOD] = [int((hex_data[CMD0A_RES_DATA_HT] - 70) / 2), int((hex_data[CMD0A_RES_DATA_HB] - 70) / 2)]
                decode_dict[WET_TEMP_PERIOD] = [int((hex_data[CMD0A_RES_DATA_DT] - 70) / 2), int((hex_data[CMD0A_RES_DATA_DB] - 70) / 2)]
                decode_dict[AUTO_TEMP_PERIOD] = [int((hex_data[CMD0A_RES_DATA_FT] - 70) / 2), int((hex_data[CMD0A_RES_DATA_FB] - 70) / 2)]

                if (hex_data[DATA_BC] == 0x0e):
                    temp = hex_data[CMD0A_RES_DATA_FL2] >> 4
                    if (temp == 0x03):
                        decode_dict[LR_WINDIR_GROUP] = LR_WIND_DIR_GROUP_5
                    elif (temp == 0x02):
                        decode_dict[LR_WINDIR_GROUP] = LR_WIND_DIR_GROUP_3
                    else:
                        decode_dict[LR_WINDIR_GROUP] = LR_WIND_DIR_GROUP_NO
                
                decode_dict.update(self.cmd_decode_addr(hex_data))
                decode_dict[MYPRINT_FUNCTION] = self.myprint_function(cmd, CMD_CC_CMD_FORMAT_RESPONSE)
                self.data_decode_dict = decode_dict
                return True
        return False


    def decode_cmd49_response_from_main(self):
        hex_data = self.data
        decode_dict = {}

        if (not self.check_cmd_cc(hex_data, 0x49, CMD_CC_CMD_FORMAT_RESPONSE)):
            return False
        ex_flag = (hex_data[DATA_CC]&BIT1) >> 1

        if ((ex_flag) and (hex_data[DATA_CMD+3] != 0x49)):
            logging.debug('cmd + 3 data is not cmd49 res')
            return False

        logging.debug('decode cmd 49 main response')
        decode_dict.update(self.cmd_decode_addr(hex_data))
        decode_dict[ERROR_SYSTEM_NUM] = ((hex_data[DATA_AU0]<<2) + ((hex_data[DATA_AU1]&0xc0)>>6)) - 0x20
        decode_dict[ERROR_INDOOR_NUM] = hex_data[DATA_AU1]&0x3F
        decode_dict[ERROR_CODE] = hex_data[DATA_AN] 
        decode_dict[MYPRINT_FUNCTION] = self.myprint_function(0x49, CMD_CC_CMD_FORMAT_RESPONSE)
        self.data_decode_dict = decode_dict
        return True

    # def decodeCmd81ResMain(self):
    #     logging.debug('decode cmd 81')


    def decode_cmd81_request_to_main(self):
        hex_data = self.data
        decode_dict = {}
        cmd = 0x81

        
        if (not self.check_cmd_cc(hex_data, cmd, CMD_CC_CMD_FORMAT_REQUEST)):
            return False

        logging.debug('decode cmd 81 request')

        if (hex_data[DATA_BC] == 10):
            decode_dict[ERROR_CODE] = hex_data[8]
        else:
            decode_dict[ERROR_CODE] = 0
        
        decode_dict.update(self.cmd_decode_addr(hex_data))
        decode_dict[MYPRINT_FUNCTION] = self.myprint_function(cmd, CMD_CC_CMD_FORMAT_REQUEST)
        self.data_decode_dict = decode_dict
        return True

    def decode_cmd81_response_from_main(self):
        hex_data = self.data
        decode_dict = {}
        cmd = 0x81

        check_false = False
        check_false |=  self.check_cmd_cc(hex_data, cmd, CMD_CC_CMD_FORMAT_RESPONSE )
        check_false |=  self.check_cmd_cc(hex_data, cmd, CMD_CC_CMD_FORMAT_CHANGE )
        if ( not check_false ):
            return False

        logging.debug('decode cmd 81 response')

        decode_dict[PRE_HEAT] = (hex_data[CMD81_RES_DATA_D2] & BIT1) >> 1
        decode_dict[NANOE_AB] = (hex_data[CMD81_RES_DATA_D12] & BIT5) >> 5
        decode_dict[NANOEG_AB] = (hex_data[CMD81_RES_DATA_D12] & BIT7) >> 7

        decode_dict[SYSTEM_STATUS] = hex_data[CMD81_RES_DATA_D0] & BIT0
        decode_dict[PRE_INDOOR] = (hex_data[CMD81_RES_DATA_D0] & BIT1) >> 1
        decode_dict[SYSTEM_MODE] = (hex_data[CMD81_RES_DATA_D0] & (BIT5|BIT6|BIT7)) >> 5

        win_up = (hex_data[CMD81_RES_DATA_D0] & (BIT2|BIT3|BIT4)) >> 2
        decode_dict[WIN_DIR_UP] = win_up << 3  # self define bit

        decode_dict[FRESH_AIR] = (hex_data[CMD81_RES_DATA_D1] & BIT2) >> 2
        decode_dict[MODE_FIT] = (hex_data[CMD81_RES_DATA_D0] & (BIT1|BIT0)) 
        decode_dict[ALLOW_MODE] = hex_data[CMD81_RES_DATA_D1] & BIT3
        decode_dict[TRY_RUN] = (hex_data[CMD81_RES_DATA_D2] & BIT3) >> 3
        decode_dict[FILTER_RST_SIGN] = (hex_data[CMD81_RES_DATA_D2] & BIT7) >> 7
        decode_dict[CENTRAL_CTR_BAN_FLAG] = hex_data[CMD81_RES_DATA_D3]
        decode_dict[CENTRAL_CTR_ADDR] = hex_data[CMD81_RES_DATA_D6]
        decode_dict[SYS_TEMPT] = int((hex_data[CMD81_RES_DATA_D4] - 70) /2)
        decode_dict[STYLE_A2W_TEMPT] = hex_data[CMD81_RES_DATA_D5]

        # bind to speed dict
        strong_b5_7 = hex_data[CMD81_RES_DATA_D11] & (BIT5|BIT6)
        speed_5_level = hex_data[CMD81_RES_DATA_D12] & BIT0
        speed = hex_data[CMD81_RES_DATA_D1] >> 5
        if(strong_b5_7):
            decode_dict[WIND_SPEED] = strong_b5_7
        else:
            decode_dict[WIND_SPEED] = (speed_5_level << 6) | speed


        decode_dict[WARNING_MACHINE] = hex_data[CMD81_RES_DATA_D7]
        decode_dict[SAVE_ENERGY] = hex_data[CMD81_RES_DATA_D8] & BIT0
        decode_dict[ECONAVI] = hex_data[CMD81_RES_DATA_D8] & BIT5 >> 5
        decode_dict[NANOE_STATUS] = hex_data[CMD81_RES_DATA_D12] & (BIT3|BIT1)
        decode_dict[CLEANING] = (hex_data[CMD81_RES_DATA_D12] & BIT4) >> 4

        win_lr = (hex_data[CMD81_RES_DATA_D13] & (BIT3|BIT4|BIT5)) >> 3
        decode_dict[WIN_DIR_LR] = win_lr + (win_lr << 3)  # self define
           
        
        decode_dict.update(self.cmd_decode_addr(hex_data))
        decode_dict[MYPRINT_FUNCTION] = self.myprint_function(cmd, CMD_CC_CMD_FORMAT_RESPONSE)
        self.data_decode_dict = decode_dict
        return True
    

    #  CMD 0F REQUEST
    def decode_cmd0f_request_to_main(self):
        return self.decode_cmdcomm_request_to_main(0x0f)   

         
    def decode_cmd0f_response_from_main(self):
        hex_data = self.data
        decode_dict = {}
        cmd = 0x0f

        check_false = False
        check_false |=  self.check_cmd_cc(hex_data, cmd, CMD_CC_CMD_FORMAT_RESPONSE )
        if ( not check_false ):
            return False

        logging.debug('decode cmd 0f response')
        temp_group = [0, 0, 0, 0, 0]
        temp_group[SYSTEM_MODE_AUTO] = (hex_data[CMD0F_RES_DATA_FET_1 ] - 70) / 2
        temp_group[SYSTEM_MODE_WARM] = (hex_data[CMD0F_RES_DATA_FET_2 ] - 70) / 2
        temp_group[SYSTEM_MODE_WET] = (hex_data[CMD0F_RES_DATA_FET_3 ] - 70) / 2
        temp_group[SYSTEM_MODE_COLD] = (hex_data[CMD0F_RES_DATA_FET_4 ] - 70) / 2
        decode_dict[SYSTEM_TEMP_GROUP] = temp_group

        temp_speed = hex_data[CMD0F_RES_DATA_FT_1] >> 4
        strong_temp = hex_data[CMD0F_RES_DATA_FT_EX] & BIT0
        strong_temp <<= 6  # sself define
        temp_group[SYSTEM_MODE_WARM] = strong_temp |temp_speed

        temp_speed = hex_data[CMD0F_RES_DATA_FT_1] & 0x0f
        strong_temp = (hex_data[CMD0F_RES_DATA_FT_EX] & BIT4) >> 4
        strong_temp <<= 6  # sself define
        temp_group[SYSTEM_MODE_AUTO] = strong_temp |temp_speed

        temp_speed = hex_data[CMD0F_RES_DATA_FT_2] >> 4
        strong_temp = (hex_data[CMD0F_RES_DATA_FT_EX] & BIT1) >> 1
        strong_temp <<= 6  # sself define
        temp_group[SYSTEM_MODE_COLD] = strong_temp |temp_speed

        temp_speed = hex_data[CMD0F_RES_DATA_FT_2] & 0x0f
        strong_temp = (hex_data[CMD0F_RES_DATA_FT_EX] & BIT3) >> 3
        strong_temp <<= 6  # sself define
        temp_group[SYSTEM_MODE_WET] = strong_temp |temp_speed

        temp_speed = hex_data[CMD0F_RES_DATA_FT_3] & 0x0f
        strong_temp = (hex_data[CMD0F_RES_DATA_FT_EX] & BIT2) >> 2
        strong_temp <<= 6  # sself define
        temp_group[SYSTEM_MODE_WIND] = strong_temp |temp_speed
        decode_dict[SYSTEM_SPEED_GROUP] = temp_group

        decode_dict.update(self.cmd_decode_addr(hex_data))
        decode_dict[MYPRINT_FUNCTION] = self.myprint_function(cmd, CMD_CC_CMD_FORMAT_RESPONSE)
        self.data_decode_dict = decode_dict
        return True

    # 
    def decode_cmd0c_request_to_main(self):
        hex_data = self.data
        decode_dict = {}
        cmd = 0x0c

        check_false = False
        check_false |=  self.check_cmd_cc(hex_data, cmd, CMD_CC_CMD_FORMAT_CONFIG )
        check_false |=  self.check_cmd_cc(hex_data, cmd, CMD_CC_CMD_FORMAT_REQUEST )
        if ( not check_false ):
            return False

        epcode = hex_data[9]
        if (self.get_cmd_cc(hex_data) == CMD_CC_CMD_FORMAT_CONFIG):
            logging.debug('decode cmd 0c config')
            
            if (epcode == 0x30):
                decode_dict[TIMER_TYPE] = hex_data[10]
                decode_dict[TIMER_HOUR] = hex_data[11] >> 1
                decode_dict[TIMER_REMAIN_HOUR] = hex_data[12] >> 1
                
            decode_dict[MYPRINT_FUNCTION] = self.myprint_function(cmd, CMD_CC_CMD_FORMAT_CONFIG)
        
        else:
            logging.debug('decode cmd 0c request')
            decode_dict[MYPRINT_FUNCTION] = self.myprint_function(cmd, CMD_CC_CMD_FORMAT_REQUEST)
        
        epcode = hex_data[9]
        decode_dict[EP_ADDR] = (hex_data[6] << 8) | epcode
        decode_dict.update(self.cmd_decode_addr(hex_data))
        self.data_decode_dict = decode_dict
        return True


    def decode_cmd0c_response_from_main(self):
        hex_data = self.data
        decode_dict = {}
        cmd = 0x0c

        check_false = False
        check_false |=  self.check_cmd_cc(hex_data, cmd, CMD_CC_CMD_FORMAT_RESPONSE )
        if ( not check_false ):
            return False

        logging.debug('decode cmd 0c response')

        temp = hex_data[DATA_BC]
        if ((hex_data[temp+2] == 0x30) and (temp == 9)):
            decode_dict[TIMER_TYPE] = hex_data[DATA_CMD + 1]
            decode_dict[TIMER_HOUR] = hex_data[DATA_CMD+2] * 5
        elif((hex_data[temp+2] == 0x48) and (temp == 8)):
            decode_dict[FRESH_AIR] = (hex_data[DATA_CMD+1] & BIT1) >> 1
        
        decode_dict[MYPRINT_FUNCTION] = self.myprint_function(cmd, CMD_CC_CMD_FORMAT_RESPONSE)
        decode_dict.update(self.cmd_decode_addr(hex_data))
        self.data_decode_dict = decode_dict
        return True

    
    #  CMD 10 REQUEST
    def decode_cmd10_request_to_main(self):
        return self.decode_cmdcomm_request_to_main(0x10)   

    def decode_cmd10_response_from_main(self):
        hex_data = self.data
        decode_dict = {}
        cmd = 0x10

        check_false = False
        check_false |=  self.check_cmd_cc(hex_data, cmd, CMD_CC_CMD_FORMAT_RESPONSE )
        if ( not check_false ):
            return False

        logging.debug('decode cmd 10 response')

        temp_group = [0, 0, 0, 0, 0]
        temp_group[SYSTEM_MODE_WET] = (hex_data[CMD10_RES_DATA_P1_1 ] >> 4) 
        temp_group[SYSTEM_MODE_WARM] = (hex_data[CMD10_RES_DATA_P1_1 ] & 0X0F) 
        temp_group[SYSTEM_MODE_WIND] = (hex_data[CMD10_RES_DATA_P1_2 ] >> 4) 
        temp_group[SYSTEM_MODE_COLD] = (hex_data[CMD10_RES_DATA_P1_2 ] & 0X0F) 
        decode_dict[SYSTEM_UD_WIND_GROUP] = temp_group
        
        decode_dict[NANOE_FUNC] = hex_data[CMD10_RES_DATA_P2] & BIT0
        decode_dict[ECONAVI_FUNC] = (hex_data[CMD10_RES_DATA_P2] & BIT3) >> 3
        
        decode_dict[MYPRINT_FUNCTION] = self.myprint_function(cmd, CMD_CC_CMD_FORMAT_RESPONSE)
        decode_dict.update(self.cmd_decode_addr(hex_data))
        self.data_decode_dict = decode_dict
        return True


    #  CMD 54 REQUEST
    def decode_cmd54_request_to_main(self):
        hex_data = self.data
        decode_dict = {}
        cmd = 0x54

        check_false = False
        check_false |=  self.check_cmd_cc(hex_data, cmd, CMD_CC_CMD_FORMAT_CONFIG )
        check_false |=  self.check_cmd_cc(hex_data, cmd, CMD_CC_CMD_FORMAT_REQUEST )
        if ( not check_false ):
            return False

        if (self.get_cmd_cc(hex_data) == CMD_CC_CMD_FORMAT_CONFIG):
            decode_dict[SAVE_ENERGY_FUNC] = hex_data[6]&BIT0
            decode_dict[SAVE_ENERGY] = (hex_data[6]&BIT1) >> 1
            logging.debug('decode cmd 54 config')
               
            decode_dict[MYPRINT_FUNCTION] = self.myprint_function(cmd, CMD_CC_CMD_FORMAT_CONFIG)
        
        else:
            logging.debug('decode cmd 54 request')
            decode_dict[MYPRINT_FUNCTION] = self.myprint_function(cmd, CMD_CC_CMD_FORMAT_REQUEST)
        
        decode_dict.update(self.cmd_decode_addr(hex_data))
        self.data_decode_dict = decode_dict
        return True






    


            

            