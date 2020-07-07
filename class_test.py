class NetworkDevice:
    
    def __init__(self, platform, ip_addr, username="admin"):  # first argument is ALWAYS self, username has a default argument
        
        self.platform = platform #attribute name
        self.ip_addr = ip_addr #attribute name
        

rtr1 = NetworkDevice(platform="cisco_ios", ip_addr="1.1.1.1")  # named arguments
rtr2 = NetworkDevice("cisco_ios", "1.1.1.2")  # positional arguments


print(rtr1.platform)
print(rtr2)