#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


from pyrogram import Client

from config import Config
from aiohttp import web
from plugins import web_server

PORT = "8000"

if __name__ == "__main__":
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "TroJanz",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=300,
     app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()
   )
    Config.AUTH_USERS.add(680815375)
    app.run()
