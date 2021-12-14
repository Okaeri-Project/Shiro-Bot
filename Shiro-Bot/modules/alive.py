import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from lunaBot.events import register as MEMEK
from lunaBot import telethn as tbot

PHOTO = "https://telegra.ph/file/8c29652140f01b3449895.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  Shiro = "**Holla I'm Shiro!** \n\n"
  Shiro += "🔴 **I'm Working Properly** \n\n"
  Shiro += "🔴 **My Master : [zen](https://t.me/zenfrans) dan [rey](Http://t.me/helzrip)** \n\n"
  Shiro += "🔴 **Telethon Version : {tlhver}** \n\n"
  Shiro += "🔴 **Pyrogram Version : {pyrover}** \n\n"
  Shiro += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/shiro_robot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/Shirosupportgroup")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=Shiro,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  Shiro = "✅ **bot restarted successfully**\n\n• Admin list has been **updated**"
  BUTTON = [[Button.url("📡 ᴜᴘᴅᴀᴛᴇs", "https://t.me/Shirosupportgroup")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=Shiro,  buttons=BUTTON)
