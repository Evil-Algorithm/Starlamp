import os
import asyncio
import itertools
import logging
import logging.config
from django.conf import settings


async def folder_path(fp: str, included=True) -> str:
    """Return the path to a folder in the media directory."""
    try:
        gal_fp = os.path.join(m_path, fp)
        base_fp = [
            x for x in os.listdir(m_path) if os.path.isdir(os.path.join(gal_fp, x))
        ]
        logging.info(f"sglib: folder_path: {base_fp}")

    except Exception as err:
        logging.fatal(f"sglib: folder_path: {err}")


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
