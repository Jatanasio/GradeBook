import socket
import threading

# Server setup
HOST = '127.0.0.1'  # localhost
PORT = 12345

clients = {}  # Dictionary to map client sockets to usernames

def handle_client(client_socket, client_address):
    """Handles communication with a client."""
    try:
        # Ask for a username
        username = client_socket.recv(1024).decode('utf-8')
        clients[client_socket] = username
        
        print(f"{username} ({client_address}) has joined the chat.")
        broadcast(f"{username} has joined the chat!", client_socket)
        
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if message == "QUIT":
                break
            if message:
                print(f"{username}: {message}")
                broadcast(f"{username}: {message}", client_socket)
            else:
                break
    except:
        pass
    finally:
        # Cleanup on client disconnect
        print(f"{clients[client_socket]} ({client_address}) has left the chat.")
        broadcast(f"{clients[client_socket]} has left the chat.", client_socket)
        client_socket.close()
        del clients[client_socket]

def broadcast(message, sender_socket=None):
    """Sends a message to all connected clients except the sender."""
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                del clients[client]

def start_server():
    """Starts the server."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server running on {HOST}:{PORT}")
    
    while True:
        client_socket, client_address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()

if __name__ == "__main__":
    start_server()
