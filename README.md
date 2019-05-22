# Set up

## Use support for the core Bluetooth layers and protocols to dump BLE traffic
  - I used [aur/bluez-utils-compat 5.50-3](http://www.bluez.org/) with otput as follows:
    ```
    > 04 3E 2B 02 01 03 01 86 FB 74 A3 00 CD 1F 02 01 06 1B FF 4C 
    00 02 15 A8 A5 C6 92 CA 0A 4F A7 82 CC 16 5A 1D 43 43 E6 00 
    01 00 02 C8 5E D0
    ```
  - If using other BLE traffic scanner with different output edit function:
    ```
    def get_bytes_from_line(line):
    bytes = line.split()
    bytes.pop(0)
    return(bytes)
    ```
   - you should end up with `bytes` list as follows:
    `['04', '3E', '2B', '02', '01', '03', '01', '86', 'FB', '74', 'A3', '00', 'CD', '1F', '02', '01', '06', '1B', 'FF', '4C',         '00', '02', '15', 'A8', 'A5', 'C6', '92', 'CA', '0A', '4F', 'A7', '82', 'CC', '16', '5A', '1D', '43', '43', 'E6', '00',         '01', '00', '02', 'C8', '5E', 'D0']`
    
# How to use with bluez-utils-compat
1. run: `sudo hcitool lescan --duplicates`
2. open new twrminal window
3. run to learn how to use filter: `sudo hcidump --raw | python ble_filtering.py filter --help`
4. run example filter by MAC address: `sudo hcidump --raw | python ble_filtering.py filter -m "86 FB 74 A3 00 CD"`
