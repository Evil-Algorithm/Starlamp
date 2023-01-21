"""Tasker module, handles the asynchronous execution of all coroutines
    TODO: 
    queue to handle multiple coroutines
    scheduler to handle timed coroutines
    manager to handle all coroutines
    DJANGO_SETTINGS_MODULE as environment variable
"""
from django.conf import settings
import logging
import asyncio
import sglib


async def tasker():
    "Run a coroutine"
    try:
        path = await sglib.folder_path("test")
        logging.info(f"tasker: {path}")
    except:
        logging.fatal("tasker: logging not configured")


if __name__ == "__main__":
    settings.configure()
    m_path = settings.MEDIA_ROOT

    logging.basicConfig(
        filename="logs/tasker.log",
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    logging.info("tasker: started")
    asyncio.run(tasker())
