import socket

ip = input("Enter ip address: ")

ports = [80,443,21,8080,22]

for port in ports:
    door = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    door.settimeout(0.5)
    if door.connect_ex((ip,port)) == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSE")
    door.close()