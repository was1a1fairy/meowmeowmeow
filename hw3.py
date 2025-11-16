import asyncio


async def say_hello():

    await asyncio.sleep(1)
    print("hello")

if __name__ == '__main__':
    asyncio.run(say_hello())


async def delayed_print(text, delay):

    await asyncio.sleep(delay)
    print(text)

if __name__ == '__main__':
    asyncio.run(delayed_print('bbb',3))