import time
import asyncio

async def function1():
    await asyncio.sleep(1)
    print("func 1")
    
async def function2():
    await asyncio.sleep(1)
    print("func 2")

async def function3():
    await asyncio.sleep(4)
    print("func 3")
    
    
async def main():
#  task = asyncio.create_task(function1)
#  #await function1()
#  await function2()
#  await function3()
 

 L = await asyncio.gather(
    function1();
    function2();
    function3();
)
 print(L)
    
asyncio.run(main())
 
 # await ka mtlab ky pehly ye function execute ho lay, phir next execute ho.
 # async hum multiple functions ko execute krny ky liye use krty han.
