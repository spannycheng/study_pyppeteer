#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author : spanny 
# time:2020/2/25

import asyncio
from pyppeteer import launch

async def main():
    driver = await launch()
    page = await driver.newPage()

    await page.goto('http://www.porters.vip/verify/sign')
    await page.click('#fetch_button')

    resp = await page.xpath('//*[@id="content"]')
    text = await(await resp[0].getProperty('textContent')).jsonValue()

    print(text)

asyncio.get_event_loop().run_until_complete(main())
