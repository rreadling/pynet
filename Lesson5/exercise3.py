"""
3. Similar to lesson3, exercise4 write a function that normalizes a MAC address to the following format:

01:23:45:67:89:AB

This function should handle the lower-case to upper-case conversion.

It should also handle converting from '0000.aaaa.bbbb' and from '00-00-aa-aa-bb-bb' formats.

The function should have one parameter, the mac_address. It should return the normalized MAC address

Single digit bytes should be zero-padded to two digits. In other words, this:

a:b:c:d:e:f

should be converted to:

0A:0B:0C:0D:0E:0F

Write several test cases for your function and verify it is working properly.
"""
import re

def mac_norm(mac_addr):
    mac_addr = mac_addr.upper()
    
    if ':' in mac_addr or '-' in mac_addr:
        new_mac = []
        octets = re.split(r"[-:]",mac_addr)

        for octet in octets:
            if len(octet) < 2:
                octet = octet.zfill(2)
            new_mac.append(octet)

    elif '.' in mac_addr:
        new_mac = []
        sections = mac_addr.split('.')
        if len(sections) != 3:
            raise ValueError("Something went wrong")

        for word in sections:
            if len(word) < 4:
                word = word.zfill(4)
            new_mac.append(word[:2])
            new_mac.append(word[2:])
    
    return ":".join(new_mac)

old_mac = '0062.ec29.70fe'

print(mac_norm(old_mac))

short_mac = 'a:b:c:d:e:f'

print(mac_norm(short_mac))
