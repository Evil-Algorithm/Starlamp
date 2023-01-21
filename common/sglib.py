import os
import asyncio
import itertools
import logging
import logging.config
from django.conf import settings


async def folder_path(m_path: any, fp: str, included=True) -> str:
    """Return the path to a folder in the media directory."""
    try:
        gal_fp = os.path.join(m_path, fp)
        base_fp = [
            sdir
            for sdir in os.listdir(gal_fp)
            if os.path.isdir(os.path.join(gal_fp, sdir))
        ]
        logging.info(f"sglib: folder_path: {base_fp}")

    except FileNotFoundError as err:
        logging.fatal(f"sglib: folder_path: {err}")

    try:
        ufm_fp = [os.path.join(gal_fp, sdir) for sdir in base_fp]
        sep_dir = f"media{os.path.sep}"

        # Strip everything before the /media directory.
        form_sg = [
            os.path.sep + sep_dir.join(os.path.normpath(y).split(sep_dir)[1:])
            for y in ufm_fp
        ]
        if included:
            return form_sg
        else:
            single_dir = [os.path.basename(y) for y in form_sg]
            return single_dir

    except FileNotFoundError as err:
        logging.fatal(f"sglib: folder_path: {err}")


async def list_files(m_path: any, fp: str, included=True) -> str:
    """Returns a list of files inside a target directory.
    if include is set to true, it will include the gallery directory"""

    try:
        # files in directory
        media_fp = os.path.join(m_path, fp)
        files = [
            f for f in os.listdir(media_fp) if os.path.isfile(os.path.join(media_fp, f))
        ]
    except FileNotFoundError as err:
        logging.fatal(f"sglib: list_files: {err}")
    try:
        # format folder path
        unformed = [os.path.join(media_fp, f) for f in files]
        sep_dir = f"media{os.path.sep}"
        exts = [".jpg", ".jpeg", ".png", ".gif", ".webp"]
        ft_fp = [
            os.path.sep + sep_dir.join(os.path.normpath(y).split(sep_dir)[1:])
            for y in unformed
            if y.endswith(tuple(exts))
        ]
    except FileNotFoundError as err:
        logging.fatal(f"sglib: list_files: {err}")
    try:
        # strip out the last two folders
        if included:
            return ft_fp
        else:
            return files
    except FileNotFoundError as err:
        logging.fatal(f"sglib: list_files: {err}")


async def list_thumbs(m_path: any):
    try:
        scan_media = os.scandir(m_path)
        directories = [subdir.name for subdir in scan_media]
    except FileNotFoundError as err:
        logging.fatal(f"sglib: list_thumbs: {err}")
    try:
        # scan the media root folder
        directories = [subdir.name for subdir in scan_media]
        logging.info(f"sglib: list_thumbs: directories: {directories}")
    except FileNotFoundError as err:
        logging.info(f"{err}")
    try:
        # exclude subdirectories from thumbnail search
        uf_exclude = [
            os.path.join(subdir)
            for folders in folder_path
            for root, subdirectories, files in os.walk(
                folders, topdown=True, followlinks=False
            )
            for subdir in subdirectories
        ]
        logging.info(f"sglib: list_thumbs: uf_exclude: {uf_exclude}")
        exclude = list(itertools.chain.from_iterable(uf_exclude))
        # get thumbnails from non-excluded directories
        # TODO list comprehension
        exts = [".jpg", ".jpeg", ".png", ".gif", ".webp"]
        ufthumb_fp = [
            os.path.join(root, file)
            for root, subdirs, files in os.walk(m_path, topdown=True, followlinks=False)
            if file.endswith(tuple(exts))
            for file in sorted(files)
            if item not in subdirs
            for item in exclude
        ]
    except FileNotFoundError as err:
        logging.fatal(f"{err}")

    try:
        thumb_fp = [
            os.sep.join(os.path.normpath(f).split(os.sep)[-3:] for f in ufthumb_fp)
        ]
        return thumb_fp
    except FileNotFoundError as err:
        logging.fatal("Ahh")
