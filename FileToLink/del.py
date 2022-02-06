
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

bot = Client(
    session_name= SESSION,
    api_id= API_ID,
    api_hash= API_HASH
)


@bot.on_message(filters.command('deletemessage') & filters.group & filters.chat(GROUPS) & filters.all)
async def deleter(bot: Client, cmd: Message):
         if cmd.from_user.id not in ADMINS:
                  await slp(int(TIME))
                  await cmd.delete()

