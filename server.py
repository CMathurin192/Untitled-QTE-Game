"""Written by Caleb Mathurin
   June 28, 2024 - August 1, 2024,
   Written through PyCharm Community Edition 2024.1.1 with Python 3.12
   This program is the server code for the QTE-focused game being made with the Pygame library.
   The code follows the structure of the PyCharm project by me titled 'Pygame Socket Testing', which is
   taken and modified from the YouTube video by Bek Brace on Python network programming
   (https://youtu.be/nmzzeAvQHp8?si=uD5y3EGkmmOVTv5U)."""
#CM 6/28/24 - imports
import threading
import socket

#CM 6/28/24 - set up server
host = socket.gethostbyname(socket.gethostname())
port = 5050
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(2)

#CM 6/28/24 - list of server clients (IP address)
clients = []


#CM 7/2/24 - handle client scores
def handle_scores(client):
    while True:
        score = client.recv(8)
        for c in clients:
            if client != c:
                c.send(score)


#CM 6/28/24 - main loop
print('Server is running and listening ...')
while True:
    client, address = server.accept()
    print(f'connection is established with {str(address)}')
    clients.append(client)

    if len(clients) == 2:  # if there are 2 players connected to server
        for c in clients:
            c.send("Ready!".encode("utf-8"))

    handle_scores_thread = threading.Thread(target=handle_scores, args=(client,))
    handle_scores_thread.start()
