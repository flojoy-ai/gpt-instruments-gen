import re
import cloudinary.uploader
import ast


def generate_url_slug(device_name: str, category: str, vendor: str) -> str:
    special_words = [
        "PCIE",
        "SCPI",
        "EO",
        "sCMOS",
        "HP",
        "DMM6500",
        "PPMS",
        "PM100USB",
        "sCMOS",
        "PCO",
    ]
    category = (
        category.replace(" ", "-")
        .replace("/", "-")
        .replace("&", "-")
        .strip("-")
        .lower()
    )
    vendor = (
        vendor.replace(" ", "-")
        .replace(".", "")
        .replace(",", "")
        .replace("&", "-")
        .strip("-")
        .lower()
    )

    to_lower = lambda x: " ".join(
        a if a in special_words else a.lower() for a in x.split()
    )

    device_name = to_lower(device_name)
    device_name = re.sub(r"\s+", "-", device_name).strip("-")
    device_name = (
        device_name.replace(".", "").replace(",", "").replace("_", "-").replace("&", "")
    )

    url_slug = f"/instruments-database/{category}/{vendor}/{device_name}"
    return url_slug


def clean_name(item: str) -> str:
    item = item.replace("/", "-").replace("_", "-").replace(",", "").replace("&", "")
    return item


def cloudinary_upload(file_path: str, img_data: bytes) -> str:
    response = cloudinary.uploader.upload(
        img_data,
        folder=file_path,
        use_filename=True,
        unique_filename=False,
        overwrite=True,
        format="png",
    )
    return response["secure_url"]


def parse_ast(src_code: str, device_name: str) -> None:
    start = src_code.find("```python")
    end = src_code.find("```", src_code.find("```") + 1)
    src_code = src_code[start + len("```python") : end]
    try:
        ast.parse(src_code)
        print(f"SUCCESS: {device_name} successfully passed the parser.\n")

    except SyntaxError:
        print(f"FAIL: {device_name} does not have a valid library code.\n")
