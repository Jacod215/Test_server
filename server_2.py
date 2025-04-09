from time import struct_time

import uvicorn
from fastapi import FastAPI
import uuid
import random
app = FastAPI()

rooms = []


# прописати код для сервера виконування
@app.get("/get_sicret_namber")
def get_sicret_namber():
    while True:
        byky = [0, 0, 0, 0]
        byky = random.sample(range(10), 4)
        if byky[0] != 0:
            break
    return byky

@app.post("/creat_room/{user_id}")
def creat_room(user_id:str):
    if not rooms:
        room_id = random.sample(range(1000, 9999), 1)[0]
        rooms.append({"room_id": room_id, "GUESTS": [{"id": user_id}], "namber": get_sicret_namber()})
        return rooms
    else:
        while True:
            room_id = random.sample(range(1000, 9999), 1)
            for i in range(len(rooms)):
                if rooms[i]["room_id"] != room_id:
                    rooms.append({"room_id": room_id, "GUESTS": [{"id": user_id}], "namber": get_sicret_namber()})
                    return rooms

@app.get("/join_room/{room_id}/{user_id}")
def join_room(room_id:int , user_id:str):
    print(rooms)
    for i in range(len(rooms)):
        if rooms[i]["room_id"] == room_id:
            guests = rooms[i]["GUESTS"]
            guests.append({"id": user_id})
    return rooms

@app.get("/disconnect/{room_id}/{user_id}")
def disconnect(room_id:int,user_id:str):
    for i in range(len(rooms)):
        if rooms[i]["room_id"] == room_id:
            guests = rooms[i]["GUESTS"]
            guests.remove({"id": user_id})
    return rooms

if __name__ == '__main__':
    uvicorn.run(app=app)