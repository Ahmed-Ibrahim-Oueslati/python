import socket
import ssl

# Create a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket for TLS/SSL
mysock = ssl.wrap_socket(mysock)

# Connect to GitHub's server (HTTPS, port 443)
mysock.connect(('github.com', 443))

# Construct HTTP GET request for the specific URL
cmd = 'GET /Ahmed-Ibrahim-Oueslati/alx-low_level_programming/tree/master/sebn_work HTTP/1.1\r\nHost: github.com\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\r\nConnection: close\r\n\r\n'
mysock.send(cmd.encode())

# Receive data
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()
