import asyncio
import websockets

connected_clients = set()

async def chat_handler(websocket):  
    connected_clients.add(websocket)
    print("New client connected!")  
    try:
        async for message in websocket:
            print(f"Received: {message}")
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    finally:
        connected_clients.remove(websocket)

async def main():
    print("Starting WebSocket server...")  
    server = await websockets.serve(chat_handler, "0.0.0.0", 8765)  
    print("WebSocket server running on ws://0.0.0.0:8765")  
    await server.wait_closed()  

if __name__ == "__main__":
    asyncio.run(main())
