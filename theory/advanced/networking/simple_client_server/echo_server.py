import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# AF_INET => IPV4 // SOCK_STREAM => TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen()
print(f'Server started and listening on port: {PORT}')

while True:
    # wait for incoming connections
    remote_socket, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # read all received data and sent them back
    while True:
        data = remote_socket.recv(1024)
        if not data:
            break
        remote_socket.sendall(data)

    # close the connection with remote host
    remote_socket.close()
