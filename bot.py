import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
SLACK_APP_TOKEN = os.environ['SLACK_APP_TOKEN']
CHANNEL_ID = os.environ['CHANNEL_ID']


app = App(token=SLACK_BOT_TOKEN)


@app.event('emoji_changed')
def notify_emoji_added(event, say):
    '''絵文字が追加されたときのみ通知する.'''
    if event['subtype'] == 'add':
        emoji_name = event['name']

        say(text=f'{emoji_name}: :{emoji_name}:', channel=CHANNEL_ID)
        say(text=f':{emoji_name}:', channel=CHANNEL_ID)


if __name__ == '__main__':
    handler = SocketModeHandler(app=app, app_token=SLACK_APP_TOKEN)
    handler.start()
