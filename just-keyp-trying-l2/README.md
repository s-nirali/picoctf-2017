Steps
-----

1. Open data.pcap file in wireshark.
2. Add a new column for 'Leftover Capture Data'.
3. Wireshark > File > Export Packet Dissections > As Plain Text - save it to data.txt file.
4. Extract data from the 'Leftover Capture Data' column in data.txt file.
5. Use columns 1 and 3 of the data in data.txt and refer to pg 53 in http://www.usb.org/developers/hidpage/Hut1_12v2.pdf to decode the data.
6. If 1st column is '20', use the 2nd option in 'Usage Name' column of 'Table 12: Keyboard/Keypad page' on pg 53, otherwise use the 1st option for decoding.
7. Flag is: flag{pr355_0nwards_deafcb32}
