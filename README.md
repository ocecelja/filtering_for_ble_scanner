# How to use
1. Use support for the core Bluetooth layers and protocols to dump BLE traffic
  - I used custom made bluez-utils-compat-5.50-3-x86_64 with otput as follows:
    `> 04 3E 2B 02 01 00 01 84 93 45 02 6C FD 1F 02 01 06 1B 16 DE DA 74 84 93 45 02 6C FD BF 63 00 04 02 00 01 FF FF FF FF FF FF FF FF 5E C3 AB`
  - If using other BLE traffic scanner with different output edit function:
    ```
    def get_bytes_from_line(line):
    bytes = line.split()
    bytes.pop(0)
    return(bytes)
    ```
    to end up with `bytes` list as follows:
    `['04', '3E', '2B', '02', '01', '04', '01', '5A', 'FA', 'EE', '1E', '82', 'C1', '1F', '03', '03', 'DE', 'DA', '1A', 'FF', 'DE', 'DA', '4E', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '01', '02', '03', '00', '01', '00', '5A', 'FA', 'EE', '1E', '82', 'C1', 'C3']`
