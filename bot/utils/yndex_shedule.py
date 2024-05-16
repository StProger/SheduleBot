from aiohttp import ClientSession

from bot.settings import settings

from datetime import datetime


async def get_shedule(from_, to_):

    url = "https://api.rasp.yandex.net/v3.0/search"

    now_time = datetime.now()

    params = {
        "from": from_,
        "to": to_,
        "format": "json",
        "apikey": settings.YANDEX_TOKEN,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "offset": 10,
        "limit": 300
    }

    async with ClientSession() as session:

        resp = await session.get(url, params=params)

        if resp.status == 200:

            data = await resp.json()
            print(data)
            cur_data = list(filter(lambda shedule: datetime.fromisoformat(shedule["departure"]).timestamp() > now_time.timestamp(), data["segments"]))
            print(cur_data)
            return cur_data

        else:
            return None