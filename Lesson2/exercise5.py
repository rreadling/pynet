""" 5. Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the first and last lines of the output.

From the first line use the string .split() method to obtain the local AS number.

From the last line use the string .split() method to obtain the BGP peer IP address.

Print both local AS number and the BGP peer IP address to the screen.
"""

from __future__ import print_function, unicode_literals

with open("show_ip_bgp_summ.txt") as f:
	show_bgp = f.readlines()

first = show_bgp[0].strip()
last = show_bgp[-1].strip()

first_line = first.split()
last_line = last.split()

AS_num = first_line[-1]
ip_address = last_line[0]

print(AS_num)
print(ip_address)