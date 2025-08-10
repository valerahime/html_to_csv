import csv
import re
import sys
from urllib.request import urlopen

from bs4 import BeautifulSoup

# First, let's input a URL.
url = input("Enter a URL: ")
try:
    raw_doc = urlopen(url).read()  # This grabs the raw HTML...
except ValueError:  # ...unless it can't be parsed as a URL.
    sys.exit("Please input an actual URL!")

# This parses the HTML document, allowing finder methods.
parsed_doc = BeautifulSoup(raw_doc, "html.parser")

# This finds an element matching <p class="widget-episodeTitle js-vertical-composition-item">
# Kakuyomu apparently uses this for the chapter title.
# .string() outputs the actual text, minus element tags.
chapter_title = parsed_doc.find(
    "p", class_="widget-episodeTitle js-vertical-composition-item"
).string

# This grabs *all* <p> elements with id='p[any number]' and no class.
# Kakuyomu uses this id type for regualr text...
# but ALSO uses `class="blank"` for extra newlines, which we don't want.
paragraphs = parsed_doc.find_all("p", id=re.compile(r"p\d"), class_=None)

# Now let's use the chapter title as our filename.
# Don't forget the humble f-string!
output = f"{chapter_title}.csv"

with open(output, "w", encoding="utf-8-sig") as f:
    writer = csv.writer(f)

    # Paragraphs is an iterable, a.k.a. something that can be looped over.
    # csv.writer has a fancy function to automatically write out every line in an iterable.
    writer.writerows(paragraphs)
