# Set up

## Use support for the core Bluetooth layers and protocols to dump BLE traffic
  - I used [aur/bluez-utils-compat 5.50-3](http://www.bluez.org/) with otput as follows:
    ```
    > 04 3E 2B 02 01 00 01 4A 99 73 A5 43 CA 1F 02 01 06 1B 16 BA 
    11 73 4A 99 73 A5 43 CA 00 FF FF FF FF FF FF FF FF FF FF FF 
    FF FF FF 02 BF B8 
    ```
  - If using other BLE traffic scanner with different output edit function:
    ```
    def get_bytes_from_line(line):
    bytes = line.split()
    bytes.pop(0)
    return(bytes)
    ```
   - you should end up with `bytes` list as follows:
    `['04', '3E', '2B', '02', '01', '04', '01', '5A', 'FA', 'EE', '1E', '82', 'C1', '1F', '03', '03', 'DE', 'DA', '1A', 'FF', 'DE', 'DA', '4E', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '01', '02', '03', '00', '01', '00', '5A', 'FA', 'EE', '1E', '82', 'C1', 'C3']`
    
# How to use with bluez-utils-compat
1. run: `sudo hcitool lescan --duplicates`
2. open new twrminal window
3. run to learn how to use filter: `sudo hcidump --raw | python ble_filtering.py filter --help`
