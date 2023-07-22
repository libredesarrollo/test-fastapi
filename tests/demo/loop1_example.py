import asyncio

async def taskAsync(text = "Message"):
    while(True):
        print(text)
        await asyncio.sleep(1)

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
# loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(taskAsync())
    asyncio.ensure_future(taskAsync())
    asyncio.ensure_future(taskAsync("Other Message"))
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    loop.close()