""" 2. Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list. Use the .extend() method to add two more IP addresses to the end of the list.

Use list concatenation to add two more IP addresses to the end of the list.

Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in the list.

Using the .pop() method to remove the first IP address in the list and the last IP address in the list.

Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.
"""

from __future__ import print_function, unicode_literals

ip_list = ['192.168.1.1', '8.8.8.8', '8.8.4.4', '152.33.1.1', '10.4.0.1']

ip_list.append('10.4.0.16')
ip_list.extend(['152.33.1.5', '172.16.30.1'])
ip_list = ip_list + ['1.1.1.1', '10.4.254.254']
print(ip_list)

print(ip_list[0])
print(ip_list[-1])

first_ip = ip_list.pop(0) # pop off 192.168.1.1, new first is 8.8.8.8
last_ip = ip_list.pop() # pop off 10.4.254.254

ip_list[0] = '2.2.2.2' # replace 8.8.8.8 with 2.2.2.2

print(ip_list[0])
