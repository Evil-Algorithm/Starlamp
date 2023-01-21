"""Tasker module, handles the asynchronous execution of all coroutines
    TODO: 
    queue to handle multiple coroutines
    scheduler to handle timed coroutines
    manager to handle all coroutines
    DJANGO_SETTINGS_MODULE as environment variable
    Exceptions need a proper handler
"""
from django.conf import settings
import logging
import asyncio
import sglib


async def tasker(m_path: any) -> None:
    "Run a coroutine"
    try:
        path = await sglib.folder_path(m_path, "../media/")
        logging.info(f"tasker: {path}")

    except Exception as err:
        # TODO proper exception handling
        logging.fatal(f"tasker: your tasks are fucked: {err}")


if __name__ == "__main__":
    settings.configure()
    m_path = settings.MEDIA_ROOT

    logging.basicConfig(
        # filename="logs/tasker.log",
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    logging.info("tasker: started")
    asyncio.run(tasker(m_path=m_path))
