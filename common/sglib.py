import os
import asyncio
import itertools
import logging
import logging.config
from django.conf import settings


def folder_path(fp: str) -> str:
    """Return the path to a folder in the media directory."""
    try:
        logging.info(f"folder_path: {fp}")
    except NameError as e:
        logging.critical(f"{e} is not defined")


if __name__ == "__main__":
    settings.configure()
    m_path = settings.MEDIA_ROOT

    logging.basicConfig(
        filename="logs/sglib.log",
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    logging.info("sglib.py: started")
    folder_path("test")
