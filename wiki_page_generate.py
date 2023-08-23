from generate_snippets import LIBRARY_SNIPPET_MAP
import os
from templates import DOCS_TEMPLATE

def instruments_wiki(
    unique_libs,
    device_file,
    site_url,
    desc,
    device,
    vendor,
    device_img_url,
    vendor_desc,
    vendor_web,
    vendor_logo_url,
    headquarters,
    revenue,
    device_doc_dir,
    category,
):
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

