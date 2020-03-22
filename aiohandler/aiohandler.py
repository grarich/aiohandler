import aiohttp
import asyncio
import logging
from logging import Handler
import urllib.parse

class AioHTTPHandler(Handler):

    def __init__(self, url, method="GET", body=None):
        logging.Handler.__init__(self)
        method = method.upper()
        if method not in ["GET", "POST"]:
            raise ValueError("method must be GET or POST")
        self.url = url
        self.method = method
        self.body = body

    def mapLogRecord(self, record):
        return record.__dict__

    def emit(self, record):
        asyncio.create_task(self.emitting(record))

    async def emitting(self, record):
        try:
            msg = self.format(record)
            url = self.url
            headers = {}
            data = self.mapLogRecord(record)
            if self.method == "GET":
                if (url.find('?') >= 0):
                    sep = '&'
                else:
                    sep = '?'
                url = url + "%c%s" % (sep, data)
            if self.method == "POST":
                headers["Content-type"] = "application/x-www-form-urlencoded"
            #can't do anything with the result
            if self.body:
                async with aiohttp.request(self.method, url, data={self.body:f"{msg}"}, headers=headers):
                    pass
            else:
                async with aiohttp.request(self.method, url, data=msg, headers=headers):
                    pass
        except Exception:
            self.handleError(record)
