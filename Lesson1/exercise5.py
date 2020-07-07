from __future__ import print_function, unicode_literals

# 5. You have the following three variables from the arp table of a router:

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

# Process these ARP entries and print out a table of "IP ADDR" to "MAC ADDRESS" mappings.

split_1 = mac1.split()
split_2 = mac2.split()
split_3 = mac3.split()

ip1 = split_1[1]
ip2 = split_2[1]
ip3 = split_3[1]

mac_addr1 = split_1[3]
mac_addr2 = split_2[3]
mac_addr3 = split_3[3]

print()
print()
print(mac1)
print(mac2)
print(mac3)
print()
print()


print(" " * 10,"IP ADDR"," " * 10,"MAC ADDRESS"," " * 20)
print("-" * 40)
print("-" * 40)

print("{:>20}{:>20}".format(ip1, mac_addr1))
print("{:>20}{:>20}".format(ip2, mac_addr2))
print("{:>20}{:>20}".format(ip3, mac_addr3))