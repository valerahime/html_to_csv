import csv
import re
import sys
from pathlib import Path
from urllib.request import urlopen

from bs4 import BeautifulSoup

url = input("Enter a URL: ")  # First, let's input a URL.
try:
    raw_doc = urlopen(url).read()  # This grabs the raw HTML...
except ValueError:  # ...unless it can't be parsed as a URL.
    sys.exit("Please input an actual URL!")

# This parses the HTML document, allowing finder methods.
parsed_doc = BeautifulSoup(raw_doc, "html.parser")

# This finds an element matching <span itemprop="name">
# Kakuyomu puts this at the top of the page for the title of the work.
# .string outputs the actual text, minus element tags.
work_title = parsed_doc.find("span", itemprop="name").string

# This finds an element matching <p class="widget-episodeTitle js-vertical-composition-item">
# Kakuyomu apparently uses this for the chapter title.
chapter_title = parsed_doc.find(
    "p", class_="widget-episodeTitle js-vertical-composition-item"
).string

# This grabs ALL <p> elements with id='p[any number]' and no class.
# Kakuyomu uses this id type for regular text...
# but ALSO adds `class="blank"` for extra newlines, which we don't want.
paragraphs = parsed_doc.find_all("p", id=re.compile(r"p\d"), class_=None)

# Now let's use the chapter title as our filename.
output = f"{work_title}/{chapter_title}.csv"

# Let's make a subdirectory for the work to host all the constituent chapters.
# exist_ok means 'don't error if it already exists'
Path(work_title).mkdir(exist_ok=True)

with open(output, "w", encoding="utf-8-sig") as f:
    writer = csv.writer(f)

    # paragraphs is an iterable, a.k.a. something that can be looped over.
    # csv.writer has a function to write out all items in an iterable.
    writer.writerows(paragraphs)

print(f"Output to: {output}")
