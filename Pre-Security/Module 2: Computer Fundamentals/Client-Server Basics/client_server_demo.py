"""
Client-Server Basics Demo

This script supports my Client-Server Basics notes by demonstrating how a
client connects to a server, sends a request, and receives a response.

It uses Python's built-in socket module, so no external packages are required.
"""

import socket
import threading
import time


HOST = "127.0.0.1"
PORT = 8080


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()

        print(f"Server is listening on {HOST}:{PORT}")

        connection, address = server.accept()

        with connection:
            print(f"Server accepted connection from {address}")

            request = connection.recv(1024).decode("utf-8")
            print(f"Server received request: {request}")

            response = "Hello from the server. Your request was received."
            connection.sendall(response.encode("utf-8"))


def start_client():
    time.sleep(1)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))

        request = "GET /example-page HTTP/1.1"
        print(f"Client sending request: {request}")

        client.sendall(request.encode("utf-8"))

        response = client.recv(1024).decode("utf-8")
        print(f"Client received response: {response}")


if __name__ == "__main__":
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    start_client()

    server_thread.join()
