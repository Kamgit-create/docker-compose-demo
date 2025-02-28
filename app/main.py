import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, MessageReactionUpdated

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


@dp.message(CommandStart())
async def start_command_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


@dp.message_reaction()
async def thumbs_up_handler(message_reaction: MessageReactionUpdated) -> None:
    """
    Handler to detect when a user adds or removes a 👍 reaction
    """
    user_name = html.bold(message_reaction.user.full_name)
    thumbs_up = "👍"

    old_reactions = []
    new_reactions = []

    for reaction in message_reaction.old_reaction:
        if reaction.emoji == thumbs_up:
            old_reactions.append(reaction)
    for reaction in message_reaction.new_reaction:
        if reaction.emoji == thumbs_up:
            new_reactions.append(reaction)

    old_count = len(old_reactions)
    new_count = len(new_reactions)

    if new_count > old_count:
        # reaction was added
        await bot.send_message(
            message_reaction.chat.id,
            f"I'm glad you liked it, {user_name} 😊",
            reply_to_message_id=message_reaction.message_id,
        )
    elif new_count < old_count:
        # reaction was removed
        await bot.send_message(
            message_reaction.chat.id,
            f"I'm sad now, {user_name} 😢\n"
            f"You removed their like!",
            reply_to_message_id=message_reaction.message_id,
        )


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
