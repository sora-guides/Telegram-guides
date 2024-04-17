from aiogram import Router, types
from aiogram.filters import Command


router = Router()

@router.message(Command("call", ignore_mention=True))
async def reply_handler(message: types.Message) -> None:
    await message.answer(text="Function is workin!")
    # chat.id - работает в лс и чате | from_user.id - работает в лс и чате, но сообщения пишутся уже в лс