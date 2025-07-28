from aiogram import Router , types
from aiogram.filters import Command

from keyboards.keyboard import get_channels_keyboard

START_TEXT ="""
Що б отримати контент підпишіться на ці канали⬇️⬇️⬇️
"""

router = Router()

@router.message(Command("start"))
async def start_command(message : types.Message):
    bot = message.bot
    await bot.send_message(chat_id=message.chat.id,text=START_TEXT,reply_markup=get_channels_keyboard())


