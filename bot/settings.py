from pydantic_settings import BaseSettings

from dotenv import load_dotenv

import os

load_dotenv()


class Settings(BaseSettings):
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")

    YANDEX_TOKEN: str = os.getenv("YANDEX_TOKEN")

    stations_id: dict = {
        "Москва(Яр. Вокзал)": "s2000002",
        "Ростокино": "s9601217",
        "Лосиноостровская": "s9601716",
        "Мытищи": "s9600681",
        "Пушкино": "s9600701",
        "Софрино": "s9601315",
        "Хотьково": "s9601286",
        "Сергиев-Посад": "s9601389",
        "Струнино": "s9601358",
        "Александров-1": "s9601547"
    }

    stations_id_reverse: dict = {
        "s2000002": "Москва(Яр. Вокзал)",
        "s9601217": "Ростокино",
        "s9601716": "Лосиноостровская",
        "s9600681": "Мытищи",
        "s9600701": "Пушкино",
        "s9601315": "Софрино",
        "s9601286": "Хотьково",
        "s9601389": "Сергиев-Посад",
        "s9601358": "Струнино",
        "s9601547": "Александров-1"
    }


settings = Settings()
