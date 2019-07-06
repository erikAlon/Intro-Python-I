import asyncio


async def cr1():
    x = input("input: ")
    await asyncio.sleep(1)
    print('... World!' + x)


async def cr2():
    print('fadfd ...')
    await asyncio.sleep(3)
    print('... ffasdf!')


async def cr3():
    print('Hi ...')
    await asyncio.sleep(.5)
    print('... HOOO!')


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(cr1(), cr2(), cr1()))


# Python 3.7+
# asyncio.run(main())
main()

# async ==> await
# .sleep(int, float)
# .get_event_loop() ==> .run_until_complete( ==> .gather(async_functions...))
