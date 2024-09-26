# telegram-bot-notify

## build docker image

```
docker build -t fankangsong/telegram_bot_notify:latest ./
```

## docker deploy

```
docker run -d --name notify \
-p 80:80 \
-e TOKEN="password" \
-e PORT=80 \
-e BOT_CHAT_ID="123456789" \
-e BOT_TOKEN="/bot1****0******8:AAf3H**********I-Widk" \
fankangsong/telegram_bot_notify
```

## access web page

http://0.0.0.0/web

## api

`curl -d 'token={token}&msg={message text}' 'http://0.0.0.0/notify'`
