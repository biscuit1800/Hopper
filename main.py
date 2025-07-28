from aiogram import Bot, Dispatcher
from aiogram.filters import Command
import asyncio
from env import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


from handlers.cmd_start import router as hendlers_router
from handlers.check_subscription import router as check_router
from handlers.admin_cmds import router as admin_router

dp.include_router(router=hendlers_router)
dp.include_router(router=check_router)
dp.include_router(router=admin_router)


@dp.startup()
async def on_startup(dispatcher: Dispatcher, bot: Bot):
    print("Bot started!")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":

    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        print("Bot stoped")