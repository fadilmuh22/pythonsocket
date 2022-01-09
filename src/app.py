import socket
import os
import json

socket_path = os.environ['SOCKET_FILE']

if os.path.exists(socket_path):
    os.remove(socket_path)

server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server.bind(socket_path)

print("Socket bind on {}".format(socket_path))
while True:
    server.listen(1)
    conn, addr = server.accept()
    datas = conn.recv(1024).decode('utf-8')
    if datas:
        print("Datas received : {}".format(datas.strip()))
        for data in datas.strip().split("\n"):
            try:
                response_data = {}
                parsed_data = json.loads(data)

                response_data[parsed_data['id']] = []

                for i in range(parsed_data['from'], parsed_data['to']+1):
                    if i % 3 == 0 and i % 5 == 0:
                        response_data[parsed_data['id']].append(
                            parsed_data['fizz'] + parsed_data['buzz'])
                    elif i % 3 == 0:
                        response_data[parsed_data['id']].append(
                            parsed_data['fizz'])
                    elif i % 5 == 0:
                        response_data[parsed_data['id']].append(
                            parsed_data['buzz'])
                    else:
                        response_data[parsed_data['id']].append(i)

                res_str = json.dumps(response_data)+"\n"
                conn.send(res_str.encode())
                print("Datas sended : {}".format(res_str))
            except:
                print("String could not be converted to JSON.")
