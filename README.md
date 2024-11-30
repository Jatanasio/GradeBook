# Overview

This is a messaging app. I created this program because I wanted to learn how to develop an interactive program that can connect multiple people.This as a clinet/server based system, so in order to properly run it if you are using one computer, you will first need to run the server.py program in a separate terminal. After that, you can add client users in a separate terminal for each one. 

[Software Demo Video](https://www.youtube.com/watch?v=SA84IEIXUqU)

# Network Communication

The architecture used for this application is the Client-Server model. In this model, the server listens for incoming connections from clients, handles their requests, and sends back responses. The server manages multiple clients simultaneously by creating a new thread for each connection, allowing independent communication with each client. Clients send messages to the server, and the server broadcasts these messages to all connected clients, creating a simple chat room environment.

The application uses the TCP (Transmission Control Protocol) to establish reliable, connection-oriented communication between the client and the server. TCP ensures that messages are delivered in the correct order and without loss, which is ideal for a chat application where the integrity of messages is important. Port #: 12345

The server formats incoming messages as strings (e.g., "username: message") and broadcasts them to all connected clients. The format of the message is kept simple, as each client simply displays the incoming message with the sender's username.

# Development Environment

* VS Code
* Python
* Libraries: Socket, Threading

# Useful Websites

* [Python Server Libraries](https://docs.python.org/3/library/socketserver.html)
* [Python Socket Libraries](https://docs.python.org/3/library/socket.html)

# Future Work

* Enhance UI
* Create the option to send emojis
* Add the ability to send images