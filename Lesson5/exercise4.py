"""
4. Copy your solution from exercise3 to exercise4. Add an 'import pdb' and pdb.set_trace() statement outside of your function (i.e. where you have your function calls).

Inside of pdb, experiment with:

    Listing your code.
    Using 'next' and 'step' to walk through your code. Make sure you understand the difference between next and step.
    Experiment with 'up' and 'down' to move up and down the code stack.
    Use p <variable> to inspect a variable.
    Set a breakpoint and run your code to the breakpoint.
    Use '!command' to change a variable (for example !new_mac = [])
"""
import re
import pdb

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
