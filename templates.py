DOCS_DIR = "docusaurus"

DOCS_TEMPLATE = """
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# {device}

## Instrument Card

<div className="flex">

<div>

{desc}

</div>

<img src="{device_img_url}" style={{{{ width: \"325px\", height: \"200px\", objectFit: \"scale-down\" }}}} />

</div>

<div className="flex text-center">

<p>Device Specification: <a target="\_blank" href="{device_spec}">here</a></p>

</div>

<details style={{{{ marginTop: \"15px\"}}}}>
<summary><h2>Manufacturer Card</h2></summary>

<img src="{vendor_logo_url}" style={{{{ width: \"100%\", height: \"170px\",objectFit: \"scale-down\" }}}} />

{vendor_desc}.

<ul>
  <li>Headquarters: {headquarters}</li>
  <li>Yearly Revenue (millions, USD): {revenue}</li>
  <li>Vendor Website: <a href="{vendor_web}">here</a></li>
</ul>
</details>

## Connect to the {device} in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)
"""

WIKI_PAGE_TEMPLATE = """--- 
hide_table_of_contents: true
sidebar_label: All Instruments
sidebar_position: 0
---

# Instruments Wiki

Welcome to the Instruments Wiki! Here you can find information about the instruments available in Flojoy.

You can find all the available instruments from the sidebar.


"""
CATEGORY_TEMPLATE = """--- 
hide_table_of_contents: true
sidebar_label: {category}
sidebar_position: 1
slug: {page_url}
---

# Controlling {category} in Python

Welcome to the {category} page! Here you can find information about the {category} instruments available in Flojoy.

You can find all the available instruments from the sidebar


"""

NEW_CATEGORY_TEMPLATE = CATEGORY_TEMPLATE

PYTHON_LIB_TEMPLATE = """--- 
hide_table_of_contents: true
sidebar_position: 1
---

# Python Libraries Wiki

Welcome to the Python Libraries Wiki! Here you can find information about instruments supported by libraries.
"""

VENDOR_TEMPLATE = """--- 
hide_table_of_contents: true
sidebar_position: 2
---

# Vendors Wiki

Welcome to the Vendors Wiki! Here you can find information about vendors collaborating with Flojoy and their devices.
"""
