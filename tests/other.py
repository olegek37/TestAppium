import asyncio
import websockets
import json

async def test_ws():
    async with websockets.connect('ws://192.168.1.125:55550') as ws:
        # Получаем токен
        await ws.send(json.dumps({
            "command": "get_token",
            "username": "mimismart", 
            "password": "1234567890123456"
        }))
        token_msg = await ws.recv()
        print("🔑", token_msg)
        
        # Авторизуемся
        token = json.loads(token_msg)['access_token']
        await ws.send(json.dumps({
            "command": "auth", 
            "access_token": token
        }))
        auth_msg = await ws.recv()
        print("✅", auth_msg)
        
        # # Получаем items
        # await ws.send(json.dumps({"command": "get_items"}))
        # items_msg = await ws.recv()
        # print("📦", items_msg)

        await ws.send(json.dumps({"command": "get_area", "area_id": "MhHJ"}))
        print('get_area:', await ws.recv())

asyncio.run(test_ws())