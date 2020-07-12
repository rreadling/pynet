"""
2.  Create a function that randomly generates an IP address for a network. The default base network should be '10.10.10.'. For simplicity the network will always be a /24.

You should be able to pass a different base network into your function as an argument.

Randomly pick a number between 1 and 254 for the last octet and return the full IP address.

You can use the following to randomly generate the last octet:

import random
random.randint(1, 254)


Call your function using no arguments.
Call your function using a positional argument.
Call your function using a named argument.

For each function call print the returned IP address to the screen.
"""
import random

def ip_gen (base = '10.10.10.'):
    last_octet = random.randint(1,254)
    print(base+str(last_octet))

ip_gen() #no arguments
print()

ip_gen('192.168.1.') #positional argument
print()

new_base = '172.16.130.'

ip_gen(new_base) #named argument
print()
