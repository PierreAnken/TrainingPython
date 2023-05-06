import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

# AF_INET => IPV4 // SOCK_STREAM => TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # connect to remote server
    s.connect((HOST, PORT))

    # send data to the server
    s.sendall(b"Hello, world")

    # listen for 1024 bits (at most) of data
    data = s.recv(1024)

print(f"Received {data}")
