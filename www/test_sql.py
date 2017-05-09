#!/usr/bin/env python
# encoding: utf-8

import orm, asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop,user='www-data', password='www-data', db='awesome')
    u = User(name='Test2', email='test2@example.com', passwd='1234567890', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()