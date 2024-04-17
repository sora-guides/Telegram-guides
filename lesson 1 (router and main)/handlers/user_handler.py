from aiogram import Router, types
from aiogram.filters import CommandStart


router = Router()

@router.message(CommandStart())
async def command_start(message: types.Message) -> None:
    await message.delete()
    await message.answer(
        text=f"Hey {message.from_user.username}, how ya doin?",
    )