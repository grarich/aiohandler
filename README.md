# aiohandler  
aiohandler = aiohttp http handler

aiohandler is a logging extension module.  
By using this module, logs can be sent by webhook.  

# installing  
Install and update using pip:

`pip install aiohandler`  

A simple example.
```python
import asyncio
import logging
import aiohandler

WEBHOOK_URL = "Your webhook url"
logger = logging.getLogger()
handler = aiohandler.AioHTTPHandler(WEBHOOK_URL, method="POST", body="content")#bodyはwebhookで送信するパラメータ
logger.addHandler(handler)

loop = asyncio.get_event_loop()

async def main():
    print("hello!")
    logging.info('info')
    logging.debug('debug')
    logging.error('error')
    await asyncio.sleep(1)
    logging.warning('warning')
    logging.critical('critical')
    print("hello world!")

if __name__ == "__main__":
    loop.create_task(main())
    loop.run_forever()
```
# Thank you to everyone who Helped me (#^^#)
