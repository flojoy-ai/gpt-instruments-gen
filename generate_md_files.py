import os
from airtable_table import (
    get_table_data_list,
    AllInstrumentTableCols as Cols,
)
from pyairtable.api.types import RecordDict, Fields
from templates import (
    get_device_template,
    get_category_template,
    get_unit_device_template,
    INS_BY_CAT_TEMPLATE,
    INS_BY_LIBS_TEMPLATE,
    INS_BY_VENDOR_TEMPLATE,
)
from utils import (
    construct_slugs_by_cat,
    ensure_dirs,
    get_keywords,
    get_py_code_tabs,
    add_space_after_angle,
    get_lib_desc,
)
from generate_snippets import generate_snippets
from tqdm.auto import tqdm
from load_data import get_libs_cats_map
from typing import Literal


def generate_md_files(base_path: str):
    for cat in ["category", "library", "manufacturer"]:
        generate_instruments_pages(by=cat, base_path=base_path)  # type: ignore
    table_list = get_table_data_list()
    for record in tqdm(table_list, total=len(table_list)):
        process_record(record, base_path)


def process_record(record: RecordDict, base_path: str):
    fields = record["fields"]
    categories = fields.get(Cols.category, [])
    slug = (
        fields[Cols.docs_wiki].replace("/instruments-wiki", "instruments-database")
        if Cols.docs_wiki in fields and fields.get(Cols.docs_wiki, None)
        else f"instruments-database/{categories[0]}/{fields[Cols.vendor]}/{fields.get(Cols.device_name,'').replace(' ', '-')}"
    )
    constructed_slugs = construct_slugs_by_cat(categories, slug)
    title = f"Connecting to {fields[Cols.correct_device_name]} by {fields[Cols.vendor]} in Python"
    vendor = fields[Cols.vendor]
    for file_path, category in constructed_slugs:
        ensure_dirs(base_path, file_path + ".mdx")
        device_name = fields[Cols.device_name]
        corrected = fields[Cols.correct_device_name]
        device_name = corrected if corrected and corrected != "" else device_name
        tabs = get_py_code_tabs(
            device_name=device_name,
            lib=fields[Cols.library],
            category=category,
            manufacturer=vendor,
        )
        keywords = (
            "keywords: ["
            + get_keywords(
                category=category,
                lib=fields.get(Cols.library, ""),
                vendor=fields[Cols.vendor],
            )
            + "]"
        )
        template = get_device_template(
            title=title,
            sidebar_label=fields.get(Cols.correct_device_name, ""),
            description=fields.get(Cols.description, ""),
            category=category,
            device_spec=fields.get(Cols.device_specification, ""),
            meta_image=fields.get(Cols.device_image_url, ""),
            slug=file_path,
            vendor=fields.get(Cols.vendor, ""),
            vendor_description=fields.get(Cols.vendor_desc, ""),
            vendor_headquarter=fields.get(Cols.headquarters, ""),
            vendor_logo_url=fields.get(Cols.vendor_logo_url, ""),
            vendor_revennue=fields.get(Cols.revenue, ""),
            vendor_website=fields.get(Cols.vendor_website, ""),
            keywords=keywords,
            second_tab_item=tabs,
        )
        template = add_space_after_angle(template)
        with open(os.path.join(base_path, file_path.strip() + ".mdx"), "w") as f:
            f.write(template.strip())


templates = {
    "category": INS_BY_CAT_TEMPLATE,
    "library": INS_BY_LIBS_TEMPLATE,
    "manufacturer": INS_BY_VENDOR_TEMPLATE,
}


def process_with_mapping(
    by: Literal["category", "library", "manufacturer"],
    map_obj: dict[str, list[Fields]],
    template: str,
    base_path: str,
):
    ins_db_path = os.path.join(base_path, "instruments-database")
    ensure_dirs(base_path=base_path, dir_path="instruments-database")
    match by:
        case "category":
            for cat, fields in map_obj.items():
                device_templates = ""

                for field in fields:
                    slug = (
                        field[Cols.docs_wiki].replace("/instruments-wiki", "")
                        if Cols.docs_wiki in field and field.get(Cols.docs_wiki, None)
                        else f"{cat}/{field[Cols.vendor]}/{field.get(Cols.device_name,'').replace(' ', '-')}"
                    )
                    constructed_slugs = construct_slugs_by_cat([cat], slug)
                    slug, _ = constructed_slugs[0]
                    unit_device_template = get_unit_device_template(
                        slug=slug.replace("instruments-database/", ""),
                        img=field.get(Cols.device_image_url, ""),
                        device_name=field.get(
                            Cols.correct_device_name, field[Cols.device_name]
                        ),
                    )
                    device_templates += unit_device_template

                cat_template = get_category_template(
                    cat_name="Category",
                    cat_title=cat,
                    cat_desc=fields[0].get(Cols.category_description, ""),
                    device_templates=device_templates,
                )
                template += cat_template
                with open(os.path.join(ins_db_path, "all-instruments.mdx"), "w") as f:
                    f.write(template.strip())
            return
        case "library":
            for lib, fields in map_obj.items():
                device_templates = ""
                for field in fields:
                    categories = field.get(Cols.category, [])
                    slug = (
                        field[Cols.docs_wiki].replace("/instruments-wiki", "")
                        if Cols.docs_wiki in field and field.get(Cols.docs_wiki, None)
                        else f"{categories[0]}/{field[Cols.vendor]}/{field.get(Cols.device_name,'').replace(' ', '-')}"
                    )
                    constructed_slugs = construct_slugs_by_cat(categories, slug)
                    for slug_, _ in constructed_slugs:
                        unit_device_template = get_unit_device_template(
                            slug=slug_.replace("instruments-database/", ""),
                            img=field.get(Cols.device_image_url, ""),
                            device_name=field.get(
                                Cols.correct_device_name, field[Cols.device_name]
                            ),
                        )
                        device_templates += unit_device_template

                cat_template = get_category_template(
                    cat_name="Library",
                    cat_title=lib,
                    cat_desc=get_lib_desc(lib),
                    device_templates=device_templates,
                )
                template += cat_template
                with open(
                    os.path.join(ins_db_path, "python-daq-library.mdx"), "w"
                ) as f:
                    f.write(template.strip())
            return
        case "manufacturer":
            for manufac, fields in map_obj.items():
                device_templates = ""
                for field in fields:
                    categories = field.get(Cols.category, [])

                    slug = (
                        field[Cols.docs_wiki].replace("/instruments-wiki", "")
                        if Cols.docs_wiki in field and field.get(Cols.docs_wiki, None)
                        else f"{categories[0]}/{field[Cols.vendor]}/{field.get(Cols.device_name,'').replace(' ', '-')}"
                    )
                    constructed_slugs = construct_slugs_by_cat(categories, slug)
                    for slug_, _ in constructed_slugs:
                        unit_device_template = get_unit_device_template(
                            slug=slug_.replace("instruments-database/", ""),
                            img=field.get(Cols.device_image_url, ""),
                            device_name=field.get(
                                Cols.correct_device_name, field[Cols.device_name]
                            ),
                        )
                        device_templates += unit_device_template

                cat_template = get_category_template(
                    cat_name="Manufacturer",
                    cat_title=manufac,
                    cat_desc=fields[0].get(Cols.vendor_desc, ""),
                    device_templates=device_templates,
                )
                template += cat_template
                with open(os.path.join(ins_db_path, "vendors.mdx"), "w") as f:
                    f.write(template.strip())
            return


def generate_instruments_pages(
    by: Literal["category", "library", "manufacturer"], base_path: str
):
    mapping = get_libs_cats_map()
    map_obj = mapping[by]
    core_template = templates[by]
    process_with_mapping(
        by=by, map_obj=map_obj, template=core_template, base_path=base_path
    )


if __name__ == "__main__":
    import argparse

    # Create a parser object
    parser = argparse.ArgumentParser(
        description="A simple command-line argument parser"
    )

    # Define command-line arguments
    parser.add_argument(
        "-d", "--dir", type=str, help="Instruments database directory path"
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the parsed arguments
    docs_dir = args.dir if args.dir != "" else os.path.join(os.curdir, "docs")

    generate_snippets()
    generate_md_files(
        base_path=docs_dir.replace("\\", "/").replace("/instruments-database", ""),
    )
