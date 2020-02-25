#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author : spanny 
# time:2020/2/25

import os
os.environ['PYPPETEER_HOME'] = 'D:\Program Files'
import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False, args=['--disable-infobars'])
    page = await browser.newPage()
    await page.goto('https://h5.ele.me/login/')
    await page.type('form section input', '12345678999') # 模拟键盘输入手机号
    await page.click('form section button') # 模拟鼠标点击获取验证码
    await asyncio.sleep(200)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())