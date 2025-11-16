import asyncio


async def say_hello():

    await asyncio.sleep(1)
    print("hello")

if __name__ == '__main__':
    asyncio.run(say_hello())