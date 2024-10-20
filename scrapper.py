import json
import websocket

TOKEN = "YOUR DISCORD TOKEN.GnfEYk.WVx35krvQSHtJhhdobifFHVR4LA2cKgQzl5dxx"

def on_message(ws, message):
    data = json.loads(message)
    
    if data["op"] == 0:
        if data["t"] == "MESSAGE_CREATE":
            author = data["d"]["author"]["username"]
            author_id = data["d"]["author"]["id"]
            content = data["d"]["content"]
            channel_name = ""
            server_name = ""
            
            if "guild_id" in data["d"]:
                server_name = data["d"]["guild_id"]
            
            if "channel_id" in data["d"]:
                channel_name = data["d"]["channel_id"]
            
            print(f"Server: {server_name}")
            print(f"Channel: {channel_name}")
            print(f"Author: {author}")
            print(f"Author ID: {author_id}")
            print(f"Message: {content}")
            print("="*30)

def on_error(ws, error):
    print("Error:", error)

def on_close(ws, close_status_code, close_msg):
    print("Websocket closed")

def on_open(ws):
    payload = {
        "op": 2,
        "d": {
            "token": TOKEN,
            "properties": {
                "$os": "linux",
                "$browser": "mybot",
                "$device": "mybot"
            },
            "compress": False,
            "large_threshold": 250,
            "guild_subscriptions": True
        }
    }
    ws.send(json.dumps(payload))

ws = websocket.WebSocketApp("wss://gateway.discord.gg/?v=9&encoding=json",
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close,
                              on_open=on_open)

ws.run_forever()