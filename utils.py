import os
import re
from pyairtable.api.types import Fields
from airtable_table import AllInstrumentTableCols as Cols
import requests
from log import logger

CACHE_DIR = os.path.join(os.curdir, ".cache")


def striped_str(s: str):
    return " ".join(s.strip().splitlines()).replace(":", ",")


def construct_slugs_by_cat(
    cats: list[str],
    slug: str,
):
    base = "instruments-database"
    _, device = os.path.split(slug)
    _, manufacturer = os.path.split(_)

    return [
        (
            f"{base}/{capitalize_name(cat)}/{capitalize_name(manufacturer)}/{device}",
            capitalize_name(cat),
        )
        for cat in cats
    ]


def capitalize_name(name: str):
    name = " ".join(name.split("-"))
    split_by_space = name.split(" ")
    return " ".join([x.capitalize() for x in split_by_space])


def ensure_dirs(
    base_path: str,
    dir_path: str,
):
    # joined_path = os.path.join(base_path, dir_path)

    folders = dir_path.split(os.path.sep)
    current_path = base_path

    for folder in folders:
        folder_path = os.path.join(current_path, folder)
        current_path = folder_path
        if folder_path.endswith(".mdx"):
            continue
        if not os.path.exists(current_path):
            os.makedirs(current_path)


def get_keywords(category: str, vendor: str, lib: str):
    return f"{category}, {vendor}, {lib}"


def get_device_file_name(given_name: str):
    device_name = given_name.replace("/", "-")
    device_name = device_name.replace("/", "").replace("_", "-").replace(",", "")
    device_name = re.sub(r"\s+", "-", device_name).strip("-")
    device_name = device_name.replace("&", "")
    return device_name


def add_space_after_angle(input_string: str):
    # Define a regular expression pattern to find numbers followed by "<" or ">"
    pattern = re.compile(r"([<>])\s*(\d+(\.\d+)?)")

    # Use re.sub to replace matches with the modified string
    result_string = pattern.sub(r"\1 \2", input_string)

    return result_string


image_mapping: dict[str, bool] = {}


def is_valid_url(id: str, device_name: str, url: str):
    if id in image_mapping:
        return image_mapping[id]
    res = requests.head(url)
    if res.status_code == 200:
        image_mapping[id] = True
        return True
    image_mapping[id] = False
    logger.warn(f"Invalid image url found for device: {device_name}, id: {id}")
    return False


def validate_image_url(fields: Fields):
    device_image = fields.get(Cols.device_image_url, None)
    if device_image and is_valid_url(
        id=fields.get(Cols.id, "no id found"),
        device_name=fields.get(Cols.correct_device_name, fields.get(Cols.device_name)),
        url=device_image,
    ):
        return device_image
    return ""


def get_cache_path(file_name: str):
    return f"{CACHE_DIR}/{file_name}"
