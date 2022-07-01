import asyncio
import telegram


async def main():
    bot = telegram.Bot("5517966699:AAHgqcf3-oxrnYCEBYRsR6wl9SDUehjCFsU")
    async with bot:
        await bot.send_message(text='Hi John!', chat_id=-641379699)


if __name__ == '__main__':
    asyncio.run(main())
