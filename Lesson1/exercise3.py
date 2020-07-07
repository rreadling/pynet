from __future__ import print_function, unicode_literals

# 3.   Create three different variables the first variable should use all lower case characters with underscore ( _ ) as the word separator. The second variable should use all upper case characters with underscore as the word separator. The third variable should use numbers, letters, and underscore, but still be a valid variable Python variable name.

# Make all three variables be strings that refer to IPv6 addresses.

# Use the from future technique so that any string literals in Python2 are unicode.

compare if variable1 equals variable2
compare if variable1 is not equal to variable3

ip_address = "2606:a000:100f:cdd0:4563:b256:261:f80"
IP_ADDRESS = "2001:1608:10:25::1c04:b12f"
ip6_address = "2606:a000:100f:cdd0:4563:b256:261:f80"

print (ip_address == IP_ADDRESS)
print (ip_address != ip6_address)