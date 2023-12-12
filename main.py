import asyncio
import pyautogui
import websockets
import json
import time
import numpy as np


async def receive_data(websocket):
    # create json
    first = True
    counter = 0
    try:
        screenshot = pyautogui.screenshot()
        save_path = "screenshot_" + f"{counter}" + ".jpg"
        screenshot.save(save_path)

        screenshot_data = {}
        save_filename = "screenshot_" + f"{counter}" + ".json"
        screenshot_data["save_path"] = save_path
        counter += 1

        screenshot_data["gaze_x"] = []
        screenshot_data["gaze_y"] = []
        screenshot_data["time"] = []

        # initialize time counter
        timeStep = 0

        while True:
            gaze_data = await websocket.recv()

            # because first data point is invalid (some random string data)
            if first:
                first = False

            else:
                # data = gaze
                json_data = json.loads(gaze_data)
                gaze_x = json_data["GazeX"]
                gaze_y = json_data["GazeY"]

                # add x, y data
                screenshot_data["gaze_x"].append(gaze_x)
                screenshot_data["gaze_y"].append(gaze_y)

                # add time data
                screenshot_data["time"].append(timeStep)
                timeStep += 1

                json.dump(screenshot_data, open(save_filename, "w"))

                # exit()
                time.sleep(1)

                print(f"Received data: {json_data}")
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
