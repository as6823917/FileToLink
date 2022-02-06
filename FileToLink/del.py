
import pyrogram
import asyncio

from asyncio import sleep as slp
from pyrogram import Client, filters
from pyrogram.types import User, Message

from info import API_ID
from info import API_HASH
from info import SESSION
from info import ADMINS
from info import TIME
from  import GROUPS


@app.on_message(filters.group & filters.chat(GROUPS) & filters.all)
async def deleter(bot: Client, cmd: Message):
         if cmd.from_user.id not in ADMINS:
                  await slp(int(TIME))
                  await cmd.delete()

