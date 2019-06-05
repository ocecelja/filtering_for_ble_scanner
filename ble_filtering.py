#!/usr/bin/env python

import click
import sys
import requests

# index
# ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46',]
# ibeacon
# ['04', '3E', '2A', '02', '01', '00', '01', '4E', '6A', 'E2', 'F3', '84', 'E7', '1E', '02', '01', '06', '1A', '16', '4C', '00', '02', '15', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'FF', 'C3', 'C9']
# custom
# ['04', '3E', '2B', '02', '01', '00', '01', 'D4', 'DC', 'B6', '6E', '6E', 'D9', '1F', '02', '01', '06', '1B', '16', 'BA', '11', '74', 'D4', 'DC', 'B6', '6E', '6E', 'D9', '00', 'FF', 'FF', '00', '00', 'FF', 'FF', 'FF', '00', '02', '08', '02', '00', 'FF', 'FF', '01', 'BF', 'B9']
# custom_sr
# ['04', '3E', '2B', '02', '01', '04', '01', '25', '42', '82', '9A', 'DE', 'D5', '1F', '03', '03', 'BA', '11', '1A', 'FF', 'BA', '11', '04', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '01', '05', '00', '00', '00', '00', '00', '00', '00', '00', '00', 'BD']

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

class custom_sr:
    #-------------------other-------------------------
    POS_MAC_ADDR_START = 7
    POS_MAC_ADDR_END = POS_MAC_ADDR_START + 6

    POS_CUSTOM_ID_START = 20
    POS_CUSTOM_ID_END = POS_CUSTOM_ID_START + 2

    POS_DEVICE_TYPE_START = POS_CUSTOM_ID_END
    POS_DEVICE_TYPE_END = POS_DEVICE_TYPE_START + 1

    POS_DEVICE_ID_START = POS_DEVICE_TYPE_END
    POS_DEVICE_ID_END = POS_DEVICE_ID_START + 4

    POS_DEFINITION_ID_START = POS_DEVICE_ID_END
    POS_DEFINITION_ID_END = POS_DEFINITION_ID_START + 4

    POS_OWNER_ID_START = POS_DEFINITION_ID_END
    POS_OWNER_ID_END = POS_OWNER_ID_START + 2

    POS_FIRMWARE_VERSION_START = POS_OWNER_ID_END
    POS_FIRMWARE_VERSION_END = POS_FIRMWARE_VERSION_START + 4

    POS_OTHER_START = POS_FIRMWARE_VERSION_END
    POS_OTHER_END = POS_OTHER_START + 8

    POS_RSSI_START = POS_OTHER_END
    POS_RSSI_END = POS_RSSI_START + 1
    #---------------------------------------------------
    mac = []
    custom_id = []
    device_type = []
    device_id = []
    definition_id = []
    owner_id = []
    fw_version = []
    other = []
    rssi = []

    CUSTOM_ID = ['BA', '11']

    LEN = 46

class other:
    #-------------------other-------------------------
    POS_MAC_ADDR_START = 7
    POS_MAC_ADDR_END = POS_MAC_ADDR_START + 6
    POS_ADV_DATA_START = 13
    #---------------------------------------------------
    mac = []
    adv_data = []
    rssi = []

MAC_ADDR = 1
UUID = 2
MAJOR = 3
MINOR = 4
PACKET_TYPE = 5
DATA = 6
DEVICE_TYPE = 7

def is_ibeacon(bytes):
    return (bytes[ibeacon.POS_VENDOR_START:ibeacon.POS_VENDOR_END] == ibeacon.VENDOR_ID and len(bytes) == ibeacon.LEN)

def is_custom_device(bytes):
    return (bytes[custom.POS_CUSTOM_ID_START:custom.POS_CUSTOM_ID_END] == custom.CUSTOM_ID and len(bytes) == custom.LEN)

def is_custom_sr_device(bytes):
    return (bytes[custom_sr.POS_CUSTOM_ID_START:custom_sr.POS_CUSTOM_ID_END] == custom_sr.CUSTOM_ID and len(bytes) == custom_sr.LEN)

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

def generate_custom_sr_packet(bytes):
    custom_sr.mac = bytes[custom_sr.POS_MAC_ADDR_START:custom_sr.POS_MAC_ADDR_END]
    custom_sr.custom_id = bytes[custom_sr.POS_CUSTOM_ID_START:custom_sr.POS_CUSTOM_ID_END]
    custom_sr.device_type = bytes[custom_sr.POS_DEVICE_TYPE_START:custom_sr.POS_DEVICE_TYPE_END]
    custom_sr.device_id = bytes[custom_sr.POS_DEVICE_ID_START:custom_sr.POS_DEVICE_ID_END]
    custom_sr.definition_id = bytes[custom_sr.POS_DEFINITION_ID_START:custom_sr.POS_DEFINITION_ID_END]
    custom_sr.owner_id = bytes[custom_sr.POS_OWNER_ID_START:custom_sr.POS_OWNER_ID_END]
    custom_sr.fw_version = bytes[custom_sr.POS_FIRMWARE_VERSION_START:custom_sr.POS_FIRMWARE_VERSION_END]
    custom_sr.other = bytes[custom_sr.POS_OTHER_START:custom_sr.POS_OTHER_END]
    custom_sr.rssi = bytes[custom_sr.POS_RSSI_START:custom_sr.POS_RSSI_END]
    return custom_sr

def generate_other_packet(bytes):
    other.mac = bytes[other.POS_MAC_ADDR_START:other.POS_MAC_ADDR_END]
    other.adv_data = bytes[other.POS_ADV_DATA_START:-1]
    other.rssi = bytes[-1:]
    return other

def get_bytes_from_line(line):
    if (line):
        bytes = line.split()
        return(bytes)
    else:
        return 0

def get_bytes_from_filter_str(filter_str):
    bytes = filter_str.split()
    return(bytes)

def filtering(class_name, filter, filter_str_bytes):
    if (filter == MAC_ADDR):
        return (class_name.mac == filter_str_bytes)
    if (filter == UUID):
        return (class_name.uuid == filter_str_bytes)
    if (filter == MAJOR):
        return (class_name.major == filter_str_bytes)
    if (filter == MINOR):
        return (class_name.minor == filter_str_bytes)
    if (filter == PACKET_TYPE):
        return (class_name.packet_type == filter_str_bytes)
    if (filter == DATA):
        return (class_name.data == filter_str_bytes)
    if (filter == DEVICE_TYPE):
        return (class_name.device_type == filter_str_bytes)

def print_ibeacon(ibeacon_class):
    string = ""
    string += bcolors.CRED + bcolors.CBOLD + " ".join(ibeacon_class.mac) + " "
    string += bcolors.CGREEN + bcolors.CBOLD + "I" + " "
    string += bcolors.CWHITE + bcolors.CBOLD + " ".join(ibeacon_class.uuid) + " "
    string += bcolors.CBLUE + bcolors.CBOLD + " ".join(ibeacon_class.major) + " "
    string += bcolors.CBLUE + bcolors.CBOLD + " ".join(ibeacon_class.minor) + " "
    string += bcolors.CVIOLET + bcolors.CBOLD + " ".join(ibeacon_class.tx_power) + " "
    string += bcolors.CBEIGE + bcolors.CBOLD + " ".join(ibeacon_class.rssi) + " "
    string += bcolors.ENDC
    print(string)

def print_custom(custom_calss):
    string = ""
    string += bcolors.CRED + bcolors.CBOLD + " ".join(custom_calss.mac) + " "
    string += bcolors.CGREEN + bcolors.CBOLD + "C" + " "
    string += bcolors.CYELLOW + bcolors.CBOLD + " ".join(custom_calss.packet_type) + " "
    string += bcolors.CWHITE + bcolors.CBOLD + " ".join(custom_calss.data) + " "
    string += bcolors.CYELLOW + bcolors.CBOLD + " ".join(custom_calss.device_type) + " "
    string += bcolors.CVIOLET + bcolors.CBOLD + " ".join(custom_calss.tx_power) + " "
    string += bcolors.CBEIGE + bcolors.CBOLD + " ".join(custom_calss.rssi) + " "
    string += bcolors.ENDC
    print(string)

def print_custom_sr(custom_sr_calss):
    string = ""
    string += bcolors.CRED + bcolors.CBOLD + " ".join(custom_sr_calss.mac) + " "
    string += bcolors.CGREEN + bcolors.CBOLD + "S" + " "
    string += bcolors.CYELLOW + bcolors.CBOLD + " ".join(custom_sr_calss.device_type) + " "
    string += bcolors.CWHITE + bcolors.CBOLD + " ".join(custom_sr_calss.device_id) + " "
    string += bcolors.CWHITE + bcolors.CBOLD + " ".join(custom_sr_calss.definition_id) + " "
    string += bcolors.CWHITE + bcolors.CBOLD + " ".join(custom_sr_calss.owner_id) + " "
    string += bcolors.CBLUE + bcolors.CBOLD + " ".join(custom_sr_calss.fw_version) + " "
    string += bcolors.CWHITE + bcolors.CBOLD + " ".join(custom_sr_calss.other) + " "
    string += bcolors.CBEIGE + bcolors.CBOLD + " ".join(custom_sr_calss.rssi) + " "
    string += bcolors.ENDC
    print(string)

def print_other(other_class):
    string = ""
    string += bcolors.CRED + bcolors.CBOLD + " ".join(other_class.mac) + " "
    string += bcolors.CGREEN + bcolors.CBOLD + "O" + " "
    string += bcolors.CYELLOW + bcolors.CBOLD + " ".join(other_class.adv_data) + " "
    string += bcolors.CBEIGE + bcolors.CBOLD + " ".join(other_class.rssi) + " "
    string += bcolors.ENDC
    print(string)

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
        if (line_part[0] == ">" or line_part[0] == "<"):
            bytes = get_bytes_from_line(line)
            if (bytes[0] == ">"):
                # print(bytes)
                parse_data(none, mac, uuid, major, minor, data, packet_type, device_type, bytes[1:])
            line = ""
            line += line_part.strip()
        else:
            line += " " + line_part.strip()

def parse_data(none, mac, uuid, major, minor, data, packet_type, device_type, bytes):

    ibeacon = None
    custom = None
    custom_sr = None
    other = None

    if not (none or mac or uuid or major or minor or data or packet_type or device_type):
        print("No filter set!")
        sys.exit(0)

    if (is_ibeacon(bytes)):
        ibeacon = generate_ibeacon_packet(bytes)
    elif (is_custom_device(bytes)):
        custom = generate_custom_packet(bytes)
    elif (is_custom_sr_device(bytes)):
        custom_sr = generate_custom_sr_packet(bytes)
    else:
        other = generate_other_packet(bytes)

    if (ibeacon):
        if mac:
            if (filtering(ibeacon, MAC_ADDR, get_bytes_from_filter_str(mac))):
                # print(" ".join(bytes))
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
                # print(" ".join(bytes))
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
    elif (custom_sr):
        if mac:
            if (filtering(custom_sr, MAC_ADDR, get_bytes_from_filter_str(mac))):
                # print(" ".join(bytes))
                print_custom_sr(custom_sr)
        elif data:
            if (filtering(custom_sr, DATA, get_bytes_from_filter_str(data))):
                print_custom_sr(custom_sr)
        elif packet_type:
            if (filtering(custom_sr, PACKET_TYPE, get_bytes_from_filter_str(packet_type))):
                print_custom_sr(custom_sr)
        elif device_type:
            if (filtering(custom_sr, DEVICE_TYPE, get_bytes_from_filter_str(device_type))):
                print_custom_sr(custom_sr)
        elif none:
                print_custom_sr(custom_sr)
    else:
        if mac:
            if (filtering(other, MAC_ADDR, get_bytes_from_filter_str(mac))):
                # print(" ".join(bytes))
                print_other(other)
        elif none:
            print_other(other)

@click.group()
def main():
    pass

main.add_command(filter)

if __name__ == "__main__":
    main()