# Github Raven

Filter out github bot slack messages.
Inspired by [Christian Sepulveda](https://medium.com/justideas-io/slack-notifications-filter-4760ed642457v)
since [this](https://github.com/integrations/slack/issues/1408) is still an issue.

## Local dev

First set up your `.env`
```
export SLACK_BOT_TOKEN=<>
export SLACK_SIGNING_SECRET=<>
export FORWARD_CHANNEL_ID=<>
```

Install [ngrok](https://ngrok.com/download) and run it
```
ngrok http 300
```

In another terminal set up python and run the local server:
```
source .env
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip3 install -r requirements.txt
 ./.venv/bin/uvicorn app:api --reload --port 3000 --log-level warning
```


## Deploying

Install fly.io, log in and run:
```
fly deploy
```
