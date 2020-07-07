"""
2. Create three separate lists of IP addresses. The first list should be the IP addresses of the Houston data center routers, and it should have over ten RFC1918 IP addresses in it (including some duplicate IP addresses).

The second list should be the IP addresses of the Atlanta data center routers, and it should have at least eight RFC1918 IP addresses (including some addresses that overlap with the Houston data center).

The third list should be the IP addresses of the Chicago data center routers, and it should have at least eight RFC1918 IP addresses. The Chicago IP addresses should have some overlap with both the IP addresses in Houston and Atlanta.

Convert each of these three lists to a set.

Using a set operation, find the IP addresses that are duplicated between Houston and Atlanta.

Using set operations, find the IP addresses that are duplicated in all three sites.

Using set operations, find the IP addresses that are entirely unique in Chicago.
"""
from __future__ import unicode_literals, print_function

houston_ips = [
    '10.10.10.1',
    '10.10.20.1',
    '10.10.30.1',
    '10.10.40.1',
    '10.10.50.1',
    '10.10.60.1',
    '10.10.70.1',
    '10.10.80.1',
    '10.10.10.1',
    '10.10.20.1',
    '10.10.70.1',
]

atlanta_ips = [
    '10.10.10.1',
    '10.10.20.1',
    '10.10.30.1',
    '10.10.140.1',
    '10.10.150.1',
    '10.10.160.1',
    '10.10.170.1',
    '10.10.180.1',
]

chicago_ips = [
    '10.10.10.1',
    '10.10.20.1',
    '10.10.140.1',
    '10.10.150.1',
    '10.10.210.1',
    '10.10.220.1',
    '10.10.230.1',
    '10.10.240.1',
]

houston_set = set(houston_ips)
atlanta_set = set(atlanta_ips)
chicago_set = set(chicago_ips)

hst_atl_inter = houston_set.intersection(atlanta_set)

print('Duplicates at Houston and Atlanta sites:')
print(hst_atl_inter)
print('-' * 30)

hst_atl_chic_set = chicago_set.intersection(hst_atl_inter)

print('Duplicates at Houston, Atlanta, and Chicago sites:')
print(hst_atl_chic_set)
print('-' * 30)

print('Addresses unique to Chicago site:')
print(chicago_set.difference(houston_set).difference(atlanta_set))
print('-' * 30)