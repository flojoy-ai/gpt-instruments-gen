from utils import striped_str


def get_device_template(
    title: str,
    sidebar_label: str,
    description: str,
    keywords: str,
    slug: str,
    meta_image: str,
    device_spec: str,
    vendor: str,
    vendor_logo_url: str,
    vendor_description: str,
    vendor_website: str,
    vendor_headquarter: str,
    vendor_revennue: str,
    category: str,
    second_tab_item: str,
):
    TEMPLATE = f"""
---
title: {striped_str(title)}
{f'description: {striped_str(description)}' if description != '' else ''}
{keywords.strip()} 
slug: {slug} 
{f'image: {meta_image}' if meta_image != '' else ''}
sidebar:
    label: {striped_str(sidebar_label)} 
---

import {{ Tabs, TabItem }} from "@astrojs/starlight/components";

## Instrument Card

{description}

{f'![{striped_str(sidebar_label)}]({meta_image})' if meta_image != '' else ''}

Device Specification: {f"[here]({device_spec})" if device_spec.startswith('http') else "[here](/instruments-database/all-instruments)" }

<details style={{{{ marginTop: "15px"}}}}>
<summary><h2 style={{{{display:'inline'}}}}>Manufacturer card: {vendor.upper()}</h2></summary>

![{vendor.upper()}]({vendor_logo_url})

{vendor_description.strip()}

- Headquarters: {vendor_headquarter}
- Yearly Revenue (millions, USD): {vendor_revennue}
- Vendor Website: [here]({vendor_website})

</details>

import FeaturedInstrumentVideo from "@root/src/components/FeaturedInstrumentVideo";

<FeaturedInstrumentVideo
  category="{'_'.join(category.upper().split(' '))}"
  manufacturer="{vendor.upper()}"
></FeaturedInstrumentVideo>

## Connect to the {striped_str(sidebar_label)} in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/contribution/blocks/custom-flojoy-block/)

import NodeCardCollection from "@root/src/components/NodeCardCollection";

{second_tab_item}
"""
    return TEMPLATE


INS_BY_CAT_TEMPLATE = f"""
---
title: Scientific Instruments Database for Python
description: Copy/paste Python examples for connecting to over 400 scientific instruments, sensors, motors, and actuators.
image: https://res.cloudinary.com/dhopxs1y3/image/upload/v1694137012/flojoy-docs/Marketing%20Images/flojoy_and_friends_c6x62c.jpg
keywords: [Python Driver, Agilent, Tektronix, Keysight, DAQ]
sidebar:
    label: 📻 All Instruments
    order: 0
---

Welcome to Flojoy's Instruments Database of Python drivers!

Here you can find copy/paste Python examples for connecting to over 400 scientific instruments, sensors, motors, and actuators.

import InstrumentThumbnail from '@root/src/components/InstrumentThumbnail';

"""

INS_BY_LIBS_TEMPLATE = f"""
--- 
title: Scientific Instruments Database by Python Library
description: Copy/paste Python examples using PyMeasure, QCodes, PyVISA, PySerial, and more.
image: https://res.cloudinary.com/dhopxs1y3/image/upload/v1694137515/flojoy-docs/Marketing%20Images/instrument_menagerie_delnwb.jpg
keywords: [PyMeasure, PyVISA, PySerial, QCodes, Python Driver, Agilent, Tektronix, Keysight, DAQ]
hide_table_of_contents: true
sidebar:
    label: 🐍 By Python library
    order: 1
---

## Welcome!

Welcome to Flojoy's Scientific Instrument Database! 

Here you can find information about some of the most popular Python libraries for scientific Instrument control - including InstrumentKit, QCodes, PyMeasure, PyVISA, and PySerial. 

Flojoy uses these libraries (plus many others) to connect to Instruments with no-code, drag-and-drop blocks called "nodes" in Flojoy Studio. 

Please use this Instruments Database as a resource to [download Studio](/) and [create your own nodes](/custom-nodes/creating-custom-node/) for connecting to scientific hardware in your lab, manufacturing facility, and test stations.

import InstrumentThumbnail from '@root/src/components/InstrumentThumbnail';

"""

INS_BY_VENDOR_TEMPLATE = f"""
--- 
title: Scientific Instruments Database by Manufacturer
description: Copy/paste Python examples for hundreds of instruments from Agilent, Tektronix, Keithley, Keysigh, and more.
image: https://res.cloudinary.com/dhopxs1y3/image/upload/v1694137515/flojoy-docs/Marketing%20Images/instrument_menagerie_delnwb.jpg
keywords: [Python, Agilent, Tektronix, Keysight, DAQ]
hide_table_of_contents: true
sidebar:
   order: 2
   label: 🏭 By Manufacturer
---

## Welcome!

Welcome to Flojoy's Scientific Instrument Database! 

This page is organized by Instrument manufacturer. Here you can find information about vendors collaborating with Flojoy and copy/paste Python examples for connecting to their products in your lab, manufacturing facility, and test stations.

import InstrumentThumbnail from '@root/src/components/InstrumentThumbnail';

"""


def get_category_template(
    cat_name: str, cat_title: str, cat_desc: str, device_templates: str
):
    CAT_TEMPLATE = f"""
## {cat_title.strip()}

<details> 
<summary>{cat_name} Description</summary> 
{cat_desc.strip()}
</details> 

<div className="flex flex-wrap">
{device_templates}
</div>
"""
    return CAT_TEMPLATE


def get_unit_device_template(slug: str, img: str, device_name: str):
    DEVICE_TEMPLATE = f"""
<InstrumentThumbnail 
    path='{slug.strip()}'
    img='{img}'
    label='{striped_str(device_name)}'    
/>
"""
    return DEVICE_TEMPLATE
