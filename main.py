import asyncio
import telegram


async def main():
    bot = telegram.Bot("5517966699:AAHgqcf3-oxrnYCEBYRsR6wl9SDUehjCFsU")
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())
