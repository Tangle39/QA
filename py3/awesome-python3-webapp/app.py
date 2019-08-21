import logging;

logging.basicConfig(level=logging.INFO)
# logging：日志模块，调试手段
import asyncio, os, json, time
# asyncio提供了完善的异步IO支持；
from datetime import datetime

from aiohttp import web


# 基于asyncio实现的HTTP框架

def index(request):
    return web.Response(body=b'<h1>test</h1>', content_type='text/html')


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
