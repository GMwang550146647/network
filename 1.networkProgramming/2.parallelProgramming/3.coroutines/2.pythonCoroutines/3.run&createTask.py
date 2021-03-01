import asyncio


def run():
    async def main():
        await asyncio.sleep(1)
        print('hello')

    asyncio.run(main())


def create():
    async def main():
        print('begin')
        await asyncio.sleep(1)
        print('success')
        return 'success'

    # tasks = [asyncio.create_task(main()) for i in range(100)]
    tasks = [asyncio.ensure_future(main()) for i in range(100)]
    loop = asyncio.new_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    run()
    create()
