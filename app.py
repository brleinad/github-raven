import json
import os
import logging # TODO: do proper logging
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler
from fastapi import FastAPI, Request

app = App(
    token=os.getenv('SLACK_BOT_TOKEN'),
    signing_secret=os.getenv('SLACK_SIGNING_SECRET')
)
app_handler = SlackRequestHandler(app)

forward_channel_id = os.getenv('FORWARD_CHANNEL_ID')
noisy_github_bots = ['https://github.com/apps/sonarcloud']



@app.event("message")
def handle_message_event(body, logger, client):
    is_github_bot = body.get('event', {}).get('bot_profile', {}).get('name', '') == 'GitHub'
    print('Received slack message')

    if is_github_bot:
        attachments = body.get('event', {}).get('attachments')
        forward_attachments = []
        for attachment in attachments:
            print('FROM: ', attachment.get('pretext'))
            github_user: str = attachment.get('pretext', '')
            is_noisy_bot = next((True for bot in noisy_github_bots if github_user.find(bot) > -1), False)
            if not is_noisy_bot:
                forward_attachments.append(attachment)
        print('Forwarding github: ', json.dumps(forward_attachments, sort_keys=True, indent=4))
        client.chat_postMessage(channel=forward_channel_id, attachments=forward_attachments)


api = FastAPI()


@api.post("/slack/events")
async def endpoint(req: Request):
    return await app_handler.handle(req)


@api.get("/")
def hello():
    return 'Hello'