from __future__ import print_function, unicode_literals
# 2. Prompt a user to enter in an IP address from standard input. Read the IP address in and break it up into its octets. Print out the octets in decimal, binary, and hex.

# Four columns, fifteen characters wide, a header column, data centered in the column.

my_ip = input("Enter an IP address:  ")

ip_list = list(my_ip.split("."))

first_binary = bin(int(ip_list[0]))
sec_binary = bin(int(ip_list[1]))
third_binary = bin(int(ip_list[2]))
fourth_binary = bin(int(ip_list[3]))

first_hex = hex(int(ip_list[0]))
sec_hex = hex(int(ip_list[1]))
third_hex = hex(int(ip_list[2]))
fourth_hex = hex(int(ip_list[3]))


print("Octet1"," " * 9,"Octet2"," " * 9,"Octet3"," " * 9,"Octet4",)
print("-" * 80)
print("-" * 80)

print("{:^15}{:^15}{:^15}{:^15}".format(*ip_list))
print("{:^15}{:^15}{:^15}{:^15}".format(first_binary,sec_binary,third_binary,fourth_binary))
print("{:^15}{:^15}{:^15}{:^15}".format(first_hex,sec_hex,third_hex,fourth_hex))

print("-" * 80)
print("-" * 80)