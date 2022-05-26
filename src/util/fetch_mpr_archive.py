import aiohttp
import gzip
import json
import cfg

from time import time

last_archive_time = 0

async def fetch_mpr_archive():
    global last_archive_time

    cur_time = round(time())

    if cur_time - last_archive_time > (60 * 5):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://mpr.makedeb.org/packages-meta-ext-v2.json.gz") as response:
                packages_archive = (await response.content.read()).decode()
                cfg.mpr_package_json = json.loads(packages_archive) 
