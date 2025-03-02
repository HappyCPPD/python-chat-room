import asyncio
import websockets
import threading  

async def chat_client():
    uri = "ws://localip:8765"
    username = input("Enter your username: ")

    async with websockets.connect(uri) as websocket:
        print(f"Connected as {username}!")

        async def send_messages():
            loop = asyncio.get_running_loop()
            while True:
                message = await loop.run_in_executor(None, input, "> ")  
                full_message = f"[{username}]: {message}"
                await websocket.send(full_message)

        async def receive_messages():
            async for message in websocket:
                print(f"\n{message}\n> ", end="")

        await asyncio.gather(send_messages(), receive_messages())  

if __name__ == "__main__":
    asyncio.run(chat_client())
