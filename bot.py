import os
from slack_sdk.rtm_v2 import RTMClient

API_TOKEN = os.environ["API_TOKEN"]
CHANNEL = os.environ["CHANNEL"]

rtm = RTMClient(token=API_TOKEN)

@rtm.on("emoji_changed")
def handle(client, event):
   if event["subtype"] == "add":
        name = event["name"]
        message = {
            "channel": CHANNEL,
            "text": f":{name}: ({name})",
        }
        client.web_client.chat_postMessage(**message)

rtm.start()
