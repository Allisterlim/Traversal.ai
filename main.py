import asyncio
import pyautogui
import websockets
import json
import time

async def receive_data(websocket):
    # create json
    first = True
    counter = 0
    try:
        while True:
            save_data = {}
            save_filename = "screenshot_" + f"{counter}" + ".json"
            data = await websocket.recv()
            if first:
                first = False
            else:
                # print(data)
                json_data = json.loads(data)
                gaze_x = json_data["GazeX"]
                gaze_y = json_data["GazeY"]
                screenshot = pyautogui.screenshot(
                    region=(gaze_x, gaze_y, 800, 200)
                )

                save_path = "screenshot_" + f"{counter}" + ".jpg"
                counter += 1
                screenshot.save(save_path)

                save_data['gaze_x'] = gaze_x
                save_data['gaze_y'] = gaze_y
                save_data['save_path'] = save_path

                json.dump(save_data, open(save_filename, 'w'))

                #screenshot_x, screenshot_y = json_data["GazeX"], json_data["GazeY"]
                # use these x,y's to determine next screenshot

                # exit()
                time.sleep(3)

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
