import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
SLACK_APP_TOKEN = os.environ['SLACK_APP_TOKEN']

# CHANNEL = os.environ['CHANNEL']


app = App(token=SLACK_BOT_TOKEN)

if __name__ == '__main__':
    SocketModeHandler(app=app, app_token=SLACK_APP_TOKEN)


# rtm = RTMClient(token=APP_TOKEN)
# @rtm.on('emoji_changed')
# def handle(client, event):
#    if event['subtype'] == 'add':
#         name = event['name']
#         message = {
#             'channel': CHANNEL,
#             'text': f':{name}: ({name})',
#         }
#         client.web_client.chat_postMessage(**message)

# rtm.start()
