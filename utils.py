import os
import re
from generate_snippets import LIBRARY_SNIPPET_MAP


def striped_str(s: str):
    return " ".join(s.strip().splitlines()).replace(":", ",")


def construct_slugs_by_cat(
    cats: list[str],
    slug: str,
):
    base = "instruments-database"
    _, device = os.path.split(slug)
    _, manufacturer = os.path.split(_)

    return [(f"{base}/{cat}/{manufacturer}/{device}", cat) for cat in cats]


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


def get_py_code_tabs(device_name: str, lib: str, category: str, manufacturer: str):
    device_file_name = get_device_file_name(device_name)
    tabs_str = f"""
<Tabs>
<TabItem value="Flojoy" label="Flojoy" className="flojoy-instrument-tabs">

<NodeCardCollection category="{category.upper().replace(' ', '_')}" manufacturer="{manufacturer}"></NodeCardCollection>

</TabItem>
"""
    if lib != "":
        snippet_path = f"{LIBRARY_SNIPPET_MAP[lib]}/{device_file_name}.txt"
        try:
            with open(snippet_path, "r") as fr:
                code_lines = fr.readlines()
                code_lines = [
                    line for line in code_lines if not line.startswith("Sure")
                ]
                code = "".join(code_lines)
                tabs_str += f'<TabItem value="{lib}" label="{lib}">\n'
                if "```" in code:
                    code_md = code
                else:
                    code_md = f"```python\n{code}\n```"
                tabs_str += f"\n{code_md}\n\n"
                tabs_str += f"</TabItem>\n"
        except Exception:
            pass
    tabs_str += f"</Tabs>"
    return tabs_str


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


def get_lib_desc(lib: str):
    lib_desc_file_path = f"{LIBRARY_SNIPPET_MAP[lib]}/{lib}_description.txt"
    if not os.path.exists(lib_desc_file_path):
        return ""
    with open(lib_desc_file_path, "r") as lf:
        return lf.read()
