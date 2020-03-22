# aiohandler  
aiohandler = aiohttp handler

loggingモジュールをノンブロッキングでwebhookに送信する拡張ライブラリ  

# 使い方  

`pip install -i https://test.pypi.org/simple/ aiohandler`  

## extensionとして使用する場合

load_extensionで読み込んでください

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
