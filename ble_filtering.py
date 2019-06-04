#!/usr/bin/env python

import click
import sys
import requests

# index
# ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46',]
# ibeacon
#?['04', '3E', '2B', '02', '01', '00', '01', '25', '42', '82', '9A', 'DE', 'D5', '1F', '02', '01', '06', '1A', 'FF', '4C', '00', '02', '15', '0E', '62', '1B', 'A3', '22', 'D7', '43', 'D0', '8E', 'E6', '36', 'F6', '66', '99', '64', '00', 'DE', 'CA', 'FB', 'AD', 'BF', 'BF', 'BA']
# ['04', '3E', '2A', '02', '01', '00', '01', '4E', '6A', 'E2', 'F3', '84', 'E7', '1E', '02', '01', '06', '1A', '16', '4C', '00', '02', '15', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'C3', 'C9']
# custom
# ['04', '3E', '2B', '02', '01', '00', '01', 'D4', 'DC', 'B6', '6E', '6E', 'D9', '1F', '02', '01', '06', '1B', '16', 'BA', '11', '74', 'D4', 'DC', 'B6', '6E', '6E', 'D9', '00', 'FF', 'FF', '00', '00', 'FF', 'FF', 'FF', '00', '02', '08', '02', '00', 'FF', 'FF', '01', 'BF', 'B9']
# custom sr
# ['04', '3E', '2B', '02', '01', '04', '01', '4E', '6A', 'E2', 'F3', '84', 'E7', '1F', '03', '03', 'DE', 'DA', '1A', 'FF', 'DE', 'DA', '6E', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '01', '00', '05', '00', '00', '00', '4E', '6A', 'E2', 'F3', '84', 'E7', 'C9']
class bcolors:
    ENDC = '\033[0m'
    CBOLD = '\33[1m'
    CITALIC = '\33[3m'
    CURL = '\33[4m'
    CBLINK = '\33[5m'
    CBLINK2 = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'

    CBLACKBG = '\33[40m'
    CREDBG = '\33[41m'
    CGREENBG = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG = '\33[46m'
    CWHITEBG = '\33[47m'

    CGREY = '\33[90m'
    CRED2 = '\33[91m'
    CGREEN2 = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2 = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2 = '\33[96m'
    CWHITE2 = '\33[97m'

class ibeacon:
    #-------------------iBeacon-------------------------
    POS_MAC_ADDR_START = 7
    POS_MAC_ADDR_END = POS_MAC_ADDR_START + 6

    POS_VENDOR_START = 19
    POS_VENDOR_END = POS_VENDOR_START + 4

    POS_UUID_ADDR_START = POS_VENDOR_END
    POS_UUID_ADDR_END = POS_UUID_ADDR_START + 16

    POS_MAJOR_ADDR_START = POS_UUID_ADDR_END
    POS_MAJOR_ADDR_END = POS_MAJOR_ADDR_START + 2

    POS_MINOR_ADDR_START = POS_MAJOR_ADDR_END
    POS_MINOR_ADDR_END = POS_MINOR_ADDR_START + 2

    POS_TX_POWER_START = POS_MINOR_ADDR_END
    POS_TX_POWER_END = POS_TX_POWER_START + 1

    POS_RSSI_START = POS_TX_POWER_END
    POS_RSSI_END = POS_RSSI_START + 1

    VENDOR_ID = ['4C', '00', '02', '15']

    LEN = 45
    #---------------------------------------------------
    mac = []
    vendor = []
    uuid = []
    major = []
    minor = []
    tx_power = []
    rssi = []

class custom:
    #---------------------custom--------------------------
    POS_MAC_ADDR_START = 7
    POS_MAC_ADDR_END = POS_MAC_ADDR_START + 6

    POS_CUSTOM_ID_START = 19
    POS_CUSTOM_ID_END = POS_CUSTOM_ID_START + 2

    POS_PACKET_TYPE_START = POS_CUSTOM_ID_END
    POS_PACKET_TYPE_END = POS_PACKET_TYPE_START + 1

    POS_DATA_MAC_ADDR_START = POS_PACKET_TYPE_END
    POS_DATA_MAC_ADDR_END = POS_DATA_MAC_ADDR_START + 6

    POS_DATA_ADDR_START = POS_DATA_MAC_ADDR_END
    POS_DATA_ADDR_END = POS_DATA_ADDR_START + 15

    POS_DEVICE_TYPE_START = POS_DATA_ADDR_END
    POS_DEVICE_TYPE_END = POS_DEVICE_TYPE_START + 1

    POS_TX_POWER_START = POS_DEVICE_TYPE_END
    POS_TX_POWER_END = POS_TX_POWER_START + 1

    POS_RSSI_START = POS_TX_POWER_END
    POS_RSSI_END = POS_RSSI_START + 1

    CUSTOM_ID = ['BA', '11']

    LEN = 46

    #---------------------------------------------------
    custom_id = []
    packet_type = []
    mac = []
    data = []
    device_type = []
    tx_adv = []
    rssi = []

class other:
    #-------------------other-------------------------
    POS_MAC_ADDR_START = 7
    POS_MAC_ADDR_END = POS_MAC_ADDR_START + 6
    POS_ADV_DATA_START = 13
    #---------------------------------------------------
    mac = []
    adv_data = []

MAC_ADDR = 1
UUID = 2
MAJOR = 3
MINOR = 4
PACKET_TYPE = 5
DATA = 6
DEVICE_TYPE = 7

def is_ibeacon(bytes):
    if (bytes[ibeacon.POS_VENDOR_START:ibeacon.POS_VENDOR_END] == ibeacon.VENDOR_ID and len(bytes) == ibeacon.LEN):
        return True
    else:
        return False

def is_custom_device(bytes):
    if (bytes[custom.POS_CUSTOM_ID_START:custom.POS_CUSTOM_ID_END] == custom.CUSTOM_ID and len(bytes) == custom.LEN):
        return True
    else:
        return False

def generate_ibeacon_packet(bytes):
    ibeacon.mac = bytes[ibeacon.POS_MAC_ADDR_START:ibeacon.POS_MAC_ADDR_END]
    ibeacon.vendor = bytes[ibeacon.POS_VENDOR_START:ibeacon.POS_VENDOR_END]
    ibeacon.uuid = bytes[ibeacon.POS_UUID_ADDR_START:ibeacon.POS_UUID_ADDR_END]
    ibeacon.major = bytes[ibeacon.POS_MAJOR_ADDR_START:ibeacon.POS_MAJOR_ADDR_END]
    ibeacon.minor = bytes[ibeacon.POS_MINOR_ADDR_START:ibeacon.POS_MINOR_ADDR_END]
    ibeacon.tx_power = bytes[ibeacon.POS_TX_POWER_START:ibeacon.POS_TX_POWER_END]
    ibeacon.rssi = bytes[ibeacon.POS_RSSI_START:ibeacon.POS_RSSI_END]
    return ibeacon

def generate_custom_packet(bytes):
    custom.mac = bytes[custom.POS_MAC_ADDR_START:custom.POS_MAC_ADDR_END]
    custom.custom_id = bytes[custom.POS_CUSTOM_ID_START:custom.POS_CUSTOM_ID_END]
    custom.packet_type = bytes[custom.POS_PACKET_TYPE_START:custom.POS_PACKET_TYPE_END]
    custom.data = bytes[custom.POS_DATA_ADDR_START:custom.POS_DATA_ADDR_END]
    custom.device_type = bytes[custom.POS_DEVICE_TYPE_START:custom.POS_DEVICE_TYPE_END]
    custom.tx_power = bytes[custom.POS_TX_POWER_START:custom.POS_TX_POWER_END]
    custom.rssi = bytes[custom.POS_RSSI_START:custom.POS_RSSI_END]
    return custom

def generate_other_packet(bytes):
    other.mac = bytes[other.POS_MAC_ADDR_START:other.POS_MAC_ADDR_END]
    other.adv_data = bytes[other.POS_ADV_DATA_START:]
    return other

def get_bytes_from_line(line):
    if (line):
        bytes = line.split()
        bytes.pop(0)
        return(bytes)
    else:
        return 0

def get_bytes_from_filter_str(filter_str):
    bytes = filter_str.split()
    return(bytes)

def filtering(class_name, filter, filter_str_bytes):
    if (filter == MAC_ADDR):
        if (class_name.mac == filter_str_bytes): return True
        else: return False
    if (filter == UUID):
        if (class_name.uuid == filter_str_bytes): return True
        else: return False
    if (filter == MAJOR):
        if (class_name.major == filter_str_bytes): return True
        else: return False
    if (filter == MINOR):
        if (class_name.minor == filter_str_bytes): return True
        else: return False
    if (filter == PACKET_TYPE):
        if (class_name.packet_type == filter_str_bytes): return True
        else: return False
    if (filter == DATA):
        if (class_name.data == filter_str_bytes): return True
        else: return False
    if (filter == DEVICE_TYPE):
        if (class_name.device_type == filter_str_bytes): return True
        else: return False

def print_ibeacon(ibeacon_class):
    print(bcolors.CRED + bcolors.CBOLD + " ".join(ibeacon_class.mac) + " " +
          bcolors.CGREEN + bcolors.CBOLD + "I" + " " +
          bcolors.CWHITE + bcolors.CBOLD + " ".join(ibeacon_class.uuid) + " " +
          bcolors.CBLUE + bcolors.CBOLD + " ".join(ibeacon_class.major) + " " +
          bcolors.CBLUE + bcolors.CBOLD + " ".join(ibeacon_class.minor) + " " +
          bcolors.CVIOLET + bcolors.CBOLD + " ".join(ibeacon_class.tx_power) + " " +
          bcolors.CBEIGE + bcolors.CBOLD + " ".join(ibeacon_class.rssi) + " " +
          bcolors.ENDC)

def print_custom(custom_calss):
    print(bcolors.CRED + bcolors.CBOLD + " ".join(custom_calss.mac) + " " +
        bcolors.CGREEN + bcolors.CBOLD + "C" + " " +
          bcolors.CYELLOW + bcolors.CBOLD + " ".join(custom_calss.packet_type) + " " +
          bcolors.CWHITE + bcolors.CBOLD + " ".join(custom_calss.data) + " " +
          bcolors.CYELLOW + bcolors.CBOLD + " ".join(custom_calss.device_type) + " " +
          bcolors.CVIOLET + bcolors.CBOLD + " ".join(custom_calss.tx_power) + " " +
          bcolors.CBEIGE + bcolors.CBOLD + " ".join(custom_calss.rssi) + " " +
          bcolors.ENDC)

def print_other(other_class):
    print(bcolors.CRED + bcolors.CBOLD + " ".join(other_class.mac) + " " +
        bcolors.CGREEN + bcolors.CBOLD + "O" + " " +
          bcolors.CYELLOW + bcolors.CBOLD + " ".join(other_class.adv_data) + " " +
          bcolors.ENDC)

@click.command()
@click.option("-n", "--none", help='No filtering!', is_flag=True)
@click.option("-m", "--mac", help='Enter MAC separated by whitespace inside " "', is_flag=False)
@click.option("-u", "--uuid", help='Enter UUID separated by whitespace inside " "', is_flag=False)
@click.option("-ma", "--major", help='Enter MAJOR separated by whitespace inside " "', is_flag=False)
@click.option("-mi", "--minor", help='Enter MINOR separated by whitespace inside " "', is_flag=False)
@click.option("-d", "--data", help='Enter DATA separated by whitespace inside " "', is_flag=False)
@click.option("-pt", "--packet_type", help='Enter PACKET TYPE separated by whitespace inside " "', is_flag=False)
@click.option("-dt", "--device_type", help='Enter DEVICE TYPE separated by whitespace inside " "', is_flag=False)

def filter(none, mac, uuid, major, minor, data, packet_type, device_type):
    line = ""
    for line_part in sys.stdin:
        if (line_part[0] == ">"):
            bytes = get_bytes_from_line(line)
            # print(bytes)
            parse_data(none, mac, uuid, major, minor, data, packet_type, device_type, bytes)
            line = ""
            line += line_part.strip()
        else:
            line += " " + line_part.strip()

def parse_data(none, mac, uuid, major, minor, data, packet_type, device_type, bytes):

    ibeacon = None
    custom = None
    other = None

    if not (none or mac or uuid or major or minor or data or packet_type or device_type):
        print("No filter set!")
        sys.exit(0)

    if (is_ibeacon(bytes)):
        ibeacon = generate_ibeacon_packet(bytes)
    elif (is_custom_device(bytes)):
        custom = generate_custom_packet(bytes)
    else:
        other = generate_other_packet(bytes)

    if (ibeacon):
        if mac:
            if (filtering(ibeacon, MAC_ADDR, get_bytes_from_filter_str(mac))):
                print_ibeacon(ibeacon)
        elif uuid:
            if (filtering(ibeacon, UUID, get_bytes_from_filter_str(uuid))):
                print_ibeacon(ibeacon)
        elif major:
            if (filtering(ibeacon, MAJOR, get_bytes_from_filter_str(major))):
                print_ibeacon(ibeacon)
        elif minor:
            if (filtering(ibeacon, MINOR, get_bytes_from_filter_str(minor))):
                print_ibeacon(ibeacon)
        elif none:
            print_ibeacon(ibeacon)

    elif (custom):
        if mac:
            if (filtering(custom, MAC_ADDR, get_bytes_from_filter_str(mac))):
                print_custom(custom)
        elif data:
            if (filtering(custom, DATA, get_bytes_from_filter_str(data))):
                print_custom(custom)
        elif packet_type:
            if (filtering(custom, PACKET_TYPE, get_bytes_from_filter_str(packet_type))):
                print_custom(custom)
        elif device_type:
            if (filtering(custom, DEVICE_TYPE, get_bytes_from_filter_str(device_type))):
                print_custom(custom)
        elif none:
            print_custom(custom)
    else:
        if mac:
            if (filtering(other, MAC_ADDR, get_bytes_from_filter_str(mac))):
                print_other(other)
        elif none:
            print_other(other)

@click.group()
def main():
    pass

main.add_command(filter)

if __name__ == "__main__":
    main()