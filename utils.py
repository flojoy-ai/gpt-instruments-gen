import os
import re
import logging

logger = logging.getLogger()
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
