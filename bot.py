import requests
from urllib.parse import unquote
from pyrogram import filters, Client, enums
from pyrogram.types.messages_and_media import message
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    SessionPasswordNeeded, FloodWait,
    PhoneNumberInvalid, ApiIdInvalid,
    PhoneCodeInvalid, PhoneCodeExpired
)

data_url = "https://diskuploader.entertainvideo.com/v1/file/cdnurl?param={}"

def verify(url):
    try:
        if "https://mdisk.me/" in url:
            _id = url.split('/')[-1]
            req = requests.get(data_url.format(_id))
            if req.status_code == 200:
                return True
            else:
                return False
        else:
            return False
    except:
        return False


bot = Client('bot',
             api_id=1530272,
             api_hash="67da35e571d0cc9322f1520aa12c7a5b",
             bot_token="5576237716:AAHxnN700jnijovvFtw4AwgdA6YhAowG3m8",
             workers=50,
             sleep_threshold=10
             )


@bot.on_message(filters.command("start"))
async def start(client, message):
    await bot.delete_messages(message.chat.id, message.id)
    await message.reply(
            f"**Hi {message.chat.first_name}!**\n\n"
            "I'm Mdisk Extractor Bot. Just send me link and I'll extract the orginal link from it\n"
            "You can use by coping the stream link and play on mxplayer",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            'Any Issue Contact 🙍', url='https://t.me/seshu2004'),
                        InlineKeyboardButton(
                            '✪ Support ✪', url='https://t.me/yssprojects')
                    ]
                ]
            ))

@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(client, message):
    link = message.matches[0].group(0)
    await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    status = verify(link)
    if status == True:
        _id = link.split('/')[-1]
        url = data_url.format(_id)
        req = requests.get(url).json()
        file_name = unquote(req['filename'])
        await message.reply(
            f"FileName : `{file_name}`\nSource : `{req['source']}`",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            'Any Issue Contact 🙍', url='https://t.me/seshu2004'),
                        InlineKeyboardButton(
                            '✪ Support ✪', url='https://t.me/yssprojects')
                    ]
                ]
            ))


if __name__ == "__main__":
    bot.run()