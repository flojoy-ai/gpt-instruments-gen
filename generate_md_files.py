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
    get_category_page_template,
    get_py_code_tabs,
)
from utils import (
    construct_slugs_by_cat,
    ensure_dirs,
    get_keywords,
    add_space_after_angle,
    validate_image_url,
)
from log import logger
from generate_snippets import generate_snippets, get_lib_desc
from load_data import get_libs_cats_map
from typing import Literal


def generate_md_files(base_path: str):
    """
    Entry point of the script

    Args:
        base_path (str): path to instruments-database folder of docs
    """
    # Generate all instruments pages by category, library and manufacturer
    for cat in ["category", "library", "manufacturer"]:
        generate_instruments_pages(by=cat, base_path=base_path)  # type: ignore

    # Get table from Airtable in list format
    table_list = get_table_data_list()
    logger.info(f"Loaded table in list format from Airtable: {len(table_list)} records")
    for record in table_list:
        process_record(record, base_path)
    logger.info("Finished processing all records")


def process_record(record: RecordDict, base_path: str):
    fields = record["fields"]
    fields["id"] = record["id"]
    categories = fields.get(Cols.category, [])
    slug = (
        fields[Cols.docs_wiki].replace("/instruments-wiki", "instruments-database")
        if Cols.docs_wiki in fields and fields.get(Cols.docs_wiki, None)
        else f"instruments-database/{categories[0]}/{fields[Cols.vendor]}/{fields.get(Cols.device_name,'').replace(' ', '-')}"
    )
    constructed_slugs = construct_slugs_by_cat(categories, slug)
    title = f"Connecting to {fields[Cols.correct_device_name]} by {fields[Cols.vendor]} in Python"
    vendor = fields[Cols.vendor]
    image_url = validate_image_url(fields)
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
            meta_image=image_url,
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


def write_category_overview(instrument_path: str, cat_name: str, cat_template: str):
    category_path = os.path.join(instrument_path, cat_name)
    if not os.path.exists(category_path):
        os.mkdir(category_path)
    overview_file_name = f"{cat_name.replace(' ','-')}_overview.mdx"
    overview_file_path = os.path.join(category_path, overview_file_name)
    temp = get_category_page_template(
        cat_name=cat_name,
        slug=f"instruments-database/{cat_name}/{overview_file_name.replace('.mdx','')}",
    )
    mdx_content = temp + cat_template
    with open(overview_file_path, "w") as f:
        f.write(mdx_content.strip())


templates = {
    "category": INS_BY_CAT_TEMPLATE,
    "library": INS_BY_LIBS_TEMPLATE,
    "manufacturer": INS_BY_VENDOR_TEMPLATE,
}


def all_instruments_by_category(
    cat: str, fields: list[Fields], template: str, ins_db_path: str
):
    device_templates = ""
    for field in fields:
        slug = (
            field[Cols.docs_wiki].replace("/instruments-wiki", "")
            if Cols.docs_wiki in field and field.get(Cols.docs_wiki, None)
            else f"{cat}/{field[Cols.vendor]}/{field.get(Cols.device_name,'').replace(' ', '-')}"
        )
        constructed_slugs = construct_slugs_by_cat([cat], slug)
        slug, _ = constructed_slugs[0]
        image_url = validate_image_url(field)
        unit_device_template = get_unit_device_template(
            slug=slug.replace("instruments-database/", ""),
            img=image_url,
            device_name=field.get(Cols.correct_device_name, field[Cols.device_name]),
        )
        device_templates += unit_device_template
    return device_templates


def all_instruments_by_lib(
    lib: str, fields: list[Fields], template: str, ins_db_path: str
):
    device_templates = ""
    for field in fields:
        categories = field.get(Cols.category, [])
        slug = (
            field[Cols.docs_wiki].replace("/instruments-wiki", "")
            if Cols.docs_wiki in field and field.get(Cols.docs_wiki, None)
            else f"{categories[0]}/{field[Cols.vendor]}/{field.get(Cols.device_name,'').replace(' ', '-')}"
        )
        image_url = validate_image_url(field)
        constructed_slugs = construct_slugs_by_cat(categories, slug)
        for slug_, _ in constructed_slugs:
            unit_device_template = get_unit_device_template(
                slug=slug_.replace("instruments-database/", ""),
                img=image_url,
                device_name=field.get(
                    Cols.correct_device_name, field[Cols.device_name]
                ),
            )
            device_templates += unit_device_template
    return device_templates


def all_instruments_by_vendor(
    vendor: str, fields: list[Fields], template: str, ins_db_path: str
):
    device_templates = ""
    for field in fields:
        categories = field.get(Cols.category, [])

        slug = (
            field[Cols.docs_wiki].replace("/instruments-wiki", "")
            if Cols.docs_wiki in field and field.get(Cols.docs_wiki, None)
            else f"{categories[0]}/{field[Cols.vendor]}/{field.get(Cols.device_name,'').replace(' ', '-')}"
        )
        image_url = validate_image_url(field)
        constructed_slugs = construct_slugs_by_cat(categories, slug)
        for slug_, _ in constructed_slugs:
            unit_device_template = get_unit_device_template(
                slug=slug_.replace("instruments-database/", ""),
                img=image_url,
                device_name=field.get(
                    Cols.correct_device_name, field[Cols.device_name]
                ),
            )
            device_templates += unit_device_template
    return device_templates


def process_with_mapping(
    by: Literal["category", "library", "manufacturer"],
    map_obj: dict[str, list[Fields]],
    template: str,
    base_path: str,
):
    ins_db_path = os.path.join(base_path, "instruments-database")
    # Ensure instruments-database folder
    ensure_dirs(base_path=base_path, dir_path="instruments-database")
    match by:
        case "category":
            for cat, fields in map_obj.items():
                device_templates = all_instruments_by_category(
                    cat=cat, fields=fields, template=template, ins_db_path=ins_db_path
                )
                cat_template = get_category_template(
                    cat_name="Category",
                    cat_title=cat,
                    cat_desc=fields[0].get(Cols.category_description, ""),
                    device_templates=device_templates,
                )
                write_category_overview(
                    instrument_path=ins_db_path, cat_name=cat, cat_template=cat_template
                )
                template += cat_template
                with open(os.path.join(ins_db_path, "all-instruments.mdx"), "w") as f:
                    f.write(template.strip())

            return
        case "library":
            for lib, fields in map_obj.items():
                device_templates = all_instruments_by_lib(
                    lib=lib, fields=fields, template=template, ins_db_path=ins_db_path
                )
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
            for vendor, fields in map_obj.items():
                device_templates = all_instruments_by_vendor(
                    vendor=vendor,
                    fields=fields,
                    template=template,
                    ins_db_path=ins_db_path,
                )
                cat_template = get_category_template(
                    cat_name="Manufacturer",
                    cat_title=vendor,
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
    """
    Generate all instruments page for given category, library or manufacturer
    Args:
        by (Literal['category', 'library', 'manufacturer']): category, library or manufacturer
        base_path (str): path to instruments-database folder of docs"
    """
    # Get mapping object for given category
    mapping = get_libs_cats_map()
    map_obj = mapping[by]
    core_template = templates[by]
    try:
        process_with_mapping(
            by=by, map_obj=map_obj, template=core_template, base_path=base_path
        )
        logger.info(f"Generated all instruments page by {by}.")
    except Exception as e:
        logger.error(f"Failed to generate all instruments page by {by}: {e}")


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
