#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>➢<a href='https://t.me/HUBdaTV'>Canal Principal</a></b>\n➢<b><a href='https://t.me/+c9sK7H99Q2MwZmFh'>Grupo</a></b>\n➢<b><a href='https://t.me/HUBdaTV_bot'>Pedidos</a></b>\n\n<b>ʟɪɴᴋs ᴏғғʟɪɴᴇ ᴅᴇᴠᴇᴍ sᴇʀ ʀᴇᴘᴏʀᴛᴀᴅᴏs ɴᴏ ɢʀᴜᴘᴏ ᴏᴜ ɴᴏ ʙᴏᴛ ᴅᴇ ᴘᴇᴅɪᴅᴏs.</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
