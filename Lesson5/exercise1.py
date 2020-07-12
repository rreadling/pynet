"""
1a. Create an ssh_conn function. This function should have three parameters: ip_addr, username, and password. The function should print out each of these three variables and clearly indicate which variable it is printing out.

Call this ssh_conn function using entirely positional arguments.

Call this ssh_conn function using entirely named arguments.

Call this ssh_conn function using a mix of positional and named arguments.

1b. Expand on the ssh_conn function from exercise1 except add a fourth parameter 'device_type' with a default value of 'cisco_ios'. Print all four of the function variables out as part of the function's execution.

Call the 'ssh_conn2' function both with and without specifying the device_type

Create a dictionary that maps to the function's parameters. Call this ssh_conn2 function using the **kwargs technique.
"""

def ssh_conn(ip_addr, username, password):
    print("IP address is {}".format(ip_addr))
    print("Username:  {}".format(username))
    print("Password:  {}".format(password))

def ssh_conn2(ip_addr, username, password, device_type = "cisco_ios"):
    print("IP address is {}".format(ip_addr))
    print("Username:  {}".format(username))
    print("Password:  {}".format(password))
    print("Device type:  {}".format(device_type))


ssh_conn('192.168.1.1', 'admin', 'letmein') #call with positional arguments
print()

my_ip = "8.8.8.8"
my_username = "rob"
my_pass = "rob1234"

ssh_conn(my_ip, my_username, my_pass) #call with named arguments
print()

ssh_conn("10.1.1.1", my_username, "mypassword") #call with a mix of each
print()

ssh_conn2(my_ip,my_username,my_pass) #call ssh_conn2 w/o device_type - default
print()

ssh_conn2(my_ip,my_username,my_pass,"junos") #specify a device type
print()

my_dict = {'ip_addr': '172.16.130.1', 'username': 'rob', 'password': '12345', 'device_type': 'appleOS'}

ssh_conn2(**my_dict)
print()

