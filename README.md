# Github Raven

Filter out github bot slack messages.

## Local dev

First set up your `.env`
```
export SLACK_BOT_TOKEN=<>
export SLACK_SIGNING_SECRET=<>
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