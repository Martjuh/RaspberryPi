import asyncio
import random
import websockets


# create handler for each connection

class GPIOSimulator:
    def __init__(self):
        self.minimal_interval = None
        self.last_message = None

    def create_signal(self):
        return random.randrange(0, 1, 0.01)

    def collect_data(self, time_window=100):
        pass

    def listen(self, time):
        pass

async def handler(websocket, path):
    data = await websocket.recv()

    reply = f"Data recieved as: {data}!"

    await websocket.send(reply)


start_server = websockets.serve(handler, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    pass