
import pyrogram
import asyncio

from asyncio import sleep as slp
from pyrogram import Client, filters
from pyrogram.types import User, Message

from config import API_ID
from config import API_HASH
from config import SESSION
from config import ADMINS
from config import TIME
from config import GROUPS


@bot.on_message(filters.group & filters.chat(GROUPS) & filters.all)
async def deleter(bot: Client, cmd: Message):
         if cmd.from_user.id not in ADMINS:
                  await slp(int(TIME))
                  await cmd.delete()

