# telegram-bot-notify

## build docker image

```
docker build -t telegram_bot_notify ./
```

## docker deploy

```
docker run -d --name notify \
-p 80:80 \
-e TOKEN="password" \
-e PORT=80 \
-e BOT_CHAT_ID="123456789" \
-e BOT_TOKEN="/bot1****0******8:AAf3H**********I-Widk" \
telegram_bot_notify
```

## access web page

http://0.0.0.0/form

## api

`curl -d 'token={token}&msg={message text}' 'http://0.0.0.0/notify'`
