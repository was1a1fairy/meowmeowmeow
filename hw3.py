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


async def cor1():
    await asyncio.sleep(3)
    print(1)

async def cor2():
    await asyncio.sleep(2)
    print(2)

async def cor3():
    await asyncio.sleep(1)
    print(3)

async def main():

    lst_cor = [cor1(),cor2(),cor3()]
    await asyncio.gather(*lst_cor)


if __name__ == '__main__':
    asyncio.run(main())