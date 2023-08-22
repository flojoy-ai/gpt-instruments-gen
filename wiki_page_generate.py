import numpy as np
from load_data import Cols, load_data
from generate_snippets import LIBRARY_SNIPPET_MAP
from tqdm.auto import tqdm
import requests
import re
import os
from templates import DOCS_DIR, DOCS_TEMPLATE
from data_utils import generate_url_slug, cloudinary_upload, clean_name


def instruments_wiki(unique_libs, device_file, site_url, desc, device, vendor, device_img_url, vendor_desc, vendor_web, vendor_logo_url, headquarters, revenue, device_doc_dir, category):
    # gather all existing snippet directories for device
    snippet_dict: dict[str:str] = {}
    for lib in unique_libs:
        snippet_dir = LIBRARY_SNIPPET_MAP[lib]
        snippet = f"{snippet_dir}/{device_file}.txt"
        if os.path.exists(snippet):
            snippet_dict[lib] = snippet

    # ===== SEO description =====
    seo_keywords: str = []
    seo_category = site_url.split("/")[2].replace("-", " ")
    seo_python_libs = list(snippet_dict.keys())
    seo_desc = desc.replace("\n", "").replace(":", "->")
    device_name = device.replace("/", "-").replace(",", "").replace("_", "-")
    seo_doc = f"---\ntitle: Connecting to {device_name} by {vendor} in Python"
    seo_doc += f"\nsidebar_label: {device_name}\ndescription: {seo_desc}\nkeywords: "
    seo_doc += f"[{seo_category}, {vendor}"
    for lib in seo_python_libs:
        seo_doc += f", {lib}"
    seo_doc += f"]\nslug: {site_url}\nimage: {device_img_url}\n---\n"

    device_doc = DOCS_TEMPLATE.format(
        device=device_name,
        desc=desc,
        vendor_desc=vendor_desc,
        vendor_web=vendor_web,
        vendor_logo_url=vendor_logo_url,
        device_img_url=device_img_url,
        headquarters=headquarters,
        revenue=revenue,
        site_url=site_url,
        vendor=vendor,
        seo_keywords=seo_keywords,
    )

    if len(snippet_dict) > 0:
        device_doc += f"<Tabs>\n"
        for lib, snippet in snippet_dict.items():
            with open(snippet, "r") as fr:
                codel = fr.readlines()
                codel = [line for line in codel if not line.startswith("Sure")]
                code = "".join(codel)
                device_doc += f'<TabItem value="{lib}" label="{lib}">\n'
                if "```" in code:
                    code_md = code
                else:
                    code_md = f"```python\n{code}\n```"
                device_doc += f"\n{code_md}\n\n"
                device_doc += f"</TabItem>\n"
        device_doc += f"</Tabs>"

    device_doc_file = f"{device_doc_dir}/{device_file}/{device_file}.md"

    if seo_doc not in device_doc:
        device_doc = seo_doc + device_doc

    with open(device_doc_file, "w") as fw:
        fw.write(device_doc)

    print(f"Completed: {device_file} {category}")

def category_instruments_wiki(category, category_included, category_description, current_category_devices, site_url, device_img_url, device, number, WIKI_PAGE_TEMPLATE, CATEGORY_TEMPLATE, NEW_CATEGORY_TEMPLATE):
    if category not in category_included:
        if number == 0:
            WIKI_PAGE_TEMPLATE += f'## {category} \n\n <details> \n <summary>Category Description</summary> \n {category_description} \n </details> \n\n <div className="flex flex-wrap" style={{{{ marginLeft: "-55px" }}}}>\n\n\n<div className="p-4">\n\n<a href="{site_url}">\n<figure style={{{{ width: "200px", height: "200px", objectFit: "scale-down", marginRight: "15px" }}}}>\n<img src="{device_img_url}" style={{{{ width: "200px", height: "200px", objectFit: "scale-down", marginRight: "15px" }}}} />\n<figcaption>{device}</figcaption>\n</figure>\n</a></div>'
            CATEGORY_TEMPLATE += f'## {category} \n\n <details> \n <summary>Category Description</summary> \n {category_description} \n </details> \n\n <div className="flex flex-wrap" style={{{{ marginLeft: "-55px" }}}}>\n\n\n<div className="p-4">\n\n<a href="{site_url}">\n<figure style={{{{ width: "200px", height: "200px", objectFit: "scale-down", marginRight: "15px" }}}}>\n<img src="{device_img_url}" style={{{{ width: "200px", height: "200px", objectFit: "scale-down", marginRight: "15px" }}}} />\n<figcaption>{device}</figcaption>\n</figure>\n</a></div>'

        else:
            current_category_devices.clear()

            cat_url = (
                category_included[-1]
                .replace(" ", "-")
                .replace("/", "-")
                .replace("_", "-")
                .lower()
            )
            page_url = f"/instruments-wiki/{cat_url}/"
            category_docs = CATEGORY_TEMPLATE.format(
                category=category_included[-1], page_url=page_url
            )
            category_docs = category_docs.replace("{", "{{").replace("}", "}}")
            with open(
                f"./docusaurus/{category_included[-1]}/{category_included[-1]}.md", "w"
            ) as file:
                file.write(category_docs + "\n</div>")

            WIKI_PAGE_TEMPLATE += f'\n</div> \n\n ## {category} \n\n <details> \n <summary>Category Description</summary> \n {category_description} \n </details> \n\n <div className="flex flex-wrap" style={{{{ marginLeft: "-55px" }}}}>\n\n\n<div className="p-4">\n\n<a href="{site_url}">\n<figure style={{{{ width: "200px", height: "200px", objectFit: "scale-down", marginRight: "15px" }}}}>\n<img src="{device_img_url}" style={{{{ width: "200px", height: "200px", objectFit: "scale-down", marginRight: "15px" }}}} />\n<figcaption>{device}</figcaption>\n</figure>\n</a></div>'

            CATEGORY_TEMPLATE = NEW_CATEGORY_TEMPLATE
            CATEGORY_TEMPLATE += f'## {category} \n\n <details> \n <summary>Category Description</summary> \n {category_description} \n </details> \n\n <div className="flex flex-wrap" style={{{{ marginLeft: "-55px" }}}}>\n\n\n<div className="p-4">\n\n<a href="{site_url}">\n<figure style={{{{ width: "200px", height: "200px", objectFit: "scale-down", marginRight: "15px" }}}}>\n<img src="{device_img_url}" style={{{{ width: "200px", height: "200px", objectFit: "scale-down", marginRight: "15px" }}}} />\n<figcaption>{device}</figcaption>\n</figure>\n</a></div>'

        category_included.append(category)
    else:
        if device not in current_category_devices:
            WIKI_PAGE_TEMPLATE += f'\n\n\n<div className="p-4">\n\n<a href="{site_url}">\n<figure style={{{{ width: "200px", height: "200px", objectFit: "scale-down", marginRight: "15px" }}}}>\n<img src="{device_img_url}" style={{{{ width: "200px", height: "200px", objectFit: "scale-down", marginRight: "15px" }}}} />\n<figcaption>{device}</figcaption>\n</figure>\n</a></div>'
            CATEGORY_TEMPLATE += f'\n\n\n<div className="p-4">\n\n<a href="{site_url}">\n<figure style={{{{ width: "200px", height: "200px", objectFit: "scale-down", marginRight: "15px" }}}}>\n<img src="{device_img_url}" style={{{{ width: "200px", height: "200px", objectFit: "scale-down", marginRight: "15px" }}}} />\n<figcaption>{device}</figcaption>\n</figure>\n</a></div>'

    current_category_devices.append(device)

    print(category + " " + str(number))
    number += 1

# def python_lib_wiki(lib: str, python_lib_dict: dict[str:str]):

#         if previous_lib is None:
#             previous_lib = lib

#         if previous_lib != lib:
#             PYTHON_LIB_TEMPLATE += "\n</div>"
#             previous_lib = lib

#         if lib not in python_lib_dict:
#             file_path = os.path.join(LIBRARY_SNIPPET_MAP[lib], f"{lib}_description.txt")

#         if not os.path.exists(file_path):
#             continue
        
#         with open(file_path, "r") as f:
#             python_lib_dict[lib] = f.read()

#         PYTHON_LIB_TEMPLATE += f"\n\n## {lib} \n\n <details> \n <summary>Python Library Description</summary> \n {python_lib_dict[lib]} \n </details> \n\n"
#         PYTHON_LIB_TEMPLATE += (
#             f'<div className="flex flex-wrap" style={{{{ marginLeft: "-40px" }}}}>\n'
#         )

#     PYTHON_LIB_TEMPLATE += f'\n\n<div className="p-4">\n\n<a href="{docs_url}">\n\n<figure style={{{{ width: "185px", height: "200px", objectFit: "scale-down", marginRight: "15px" }}}}>\n<img src="{device_img_url}" style={{{{ width: "185px", height: "200px", objectFit: "scale-down", marginRight: "15px" }}}} />\n<figcaption>{device_name}</figcaption>\n</figure>\n</a>\n\n</div>'