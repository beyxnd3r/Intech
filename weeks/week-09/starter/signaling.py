import asyncio
import websockets



CONNECTIONS = set()

async def handler(websocket):
    print("Client connected")
    CONNECTIONS.add(websocket)
    try:
        async for message in websocket:
            print("Received", message)
                if conn != websocket:
                    await conn.send(message)
    except websockets.exceptions.ConnectionClosed:
    finally:
        CONNECTIONS.remove(websocket)

async def main():
    print("Start signaling")
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()  

if __name__ == "__main__":
    asyncio.run(main())
