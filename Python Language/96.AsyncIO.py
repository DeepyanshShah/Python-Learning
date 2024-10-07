import time
import asyncio
import requests

async def instagram():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram.ico","wb").write(response._content)

    await asyncio.sleep(1)
    print("Donwloaded instagram icon") 


async def function1():
    await asyncio.sleep(1)
    print("func 1")
    return "Apple"

async def function2():
    await asyncio.sleep(1)
    print("func 2")

async def function3():
    await asyncio.sleep(4)
    print("func 3")

async def main():

# Enables parallel processing
    L = await asyncio.gather(
        function1(),
        function2(),
        function3()
    )
print(L)

# Executes sequentially

    # task = asyncio.create_task(function1())
    # # await function1()
    # await function2()
    # await function3()

asyncio.run(main())
