import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from typing import Optional
import numpy as np
import math
from utils import logger


def scrape_docs(link: str) -> str:
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    main_content = soup.find("div", class_="document")
    content = []
    if main_content:
        paragraphs = main_content.find_all("p")
        content.extend([p.text for p in paragraphs])
        return "\n\n".join(content)
    else:
        logger.info(f"No documentation found on the page {link}.")
        return ""


def get_source_url_from_docs(url: str) -> Optional[str]:
    """Find class source from a readthedocs url

    Given a readthedocs url, find the sourcecode url
    (class deinition) and return that url
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    sources = soup.find_all("a", attrs={"href": True})
    for source_link in sources:
        span_tag = source_link.find("span", string="[source]")
        if span_tag:
            source_url = source_link["href"]
            if not source_url.startswith("http"):
                source_url = urljoin(url, source_url)
            return source_url
    raise Exception(f"Could not find class source from {url}")


def get_class_definition(docs_url: str) -> str:
    class_url = get_source_url_from_docs(docs_url)
    response = requests.get(class_url)
    soup = BeautifulSoup(response.content, "html.parser")
    main_content = soup.find("div", class_="document")
    return main_content.get_text().replace("[docs]", "")


def get_docs_from_link(docs_url: str) -> str:
    docs = ""
    if docs_url in (np.nan, math.nan):
        return docs
    try:
        return get_class_definition(docs_url)
    except:
        return docs
