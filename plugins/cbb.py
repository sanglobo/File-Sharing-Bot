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
            text = f"<b>➢Canal Principal:<\b> @hubdatv\n➢Grupo: <a href='https://t.me/+c9sK7H99Q2MwZmFh'>Entre aqui</a>\n➢<b>Pedidos:<\b> <a href='https://t.me/HUBdaTV_bot'>Faça aqui</a>\n\n <span style="color:#FFFF00"><span style="background-color:#FF0000">LINKS OFFLINE DEVEM SER REPORTADOS NO GRUPO OU NO BOT DE PEDIDOS.</span></span>",
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
