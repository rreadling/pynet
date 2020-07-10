"""
1a. Create an ssh_conn function. This function should have three parameters: ip_addr, username, and password. The function should print out each of these three variables and clearly indicate which variable it is printing out.

Call this ssh_conn function using entirely positional arguments.

Call this ssh_conn function using entirely named arguments.

Call this ssh_conn function using a mix of positional and named arguments.
"""

def ssh_conn(ip_addr, username, password):
    print("IP address is {}".format(ip_addr))
    print("Username:  {}".format(username))
    print("Password:  {}".format(password))


ssh_conn('192.168.1.1', 'admin', 'letmein') #call with positional arguments

my_ip = "8.8.8.8"
my_username = "rob"
my_pass = "rob1234"

ssh_conn(my_ip, my_username, my_pass) #call with named arguments

ssh_conn("10.1.1.1", my_username, "mypassword") #call with a mix of each

