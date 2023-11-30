import asyncio
import pyautogui
import websockets
import json



async def receive_data(websocket):
    first = True
    try:
        while True:
            data = await websocket.recv()
            if first:
                first = False
            else:
                #print(data)
                json_data = json.loads(data)
                screenshot = pyautogui.screenshot(region=(json_data["GazeX"], json_data["GazeY"], 200, 200))
                screenshot.save("allister.jpg")
                #exit()

            print(f"Received data: {data}")
    except websockets.ConnectionClosed as e:
        print(f"Connection closed unexpectedly: {e}")
    finally:
        await websocket.close()



async def connect_to_server():
    uri = "ws://127.0.0.1:43333"
    
    async with websockets.connect(uri) as websocket:
        print(f"Connected to {uri}")
        await websocket.send("AppKeyTrial")
        await receive_data(websocket)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(connect_to_server())
