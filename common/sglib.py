import os
import asyncio
import itertools
import logging
from django.conf import settings


def folder_path(fp: str) -> str:
    """Return the path to a folder in the media directory."""
    try:
        log.debug(f"folder_path: {fp}")
    except:
        print("wuhf")


if __name__ == "__main__":
    settings.configure()
    m_path = settings.MEDIA_ROOT
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    folder_path(fp="wtf")
