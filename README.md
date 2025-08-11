# HTML to CSV

A small Python repo to scrape a webpage and output its text into a CSV file, primarily using the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#) library.

Different sites should be relegated to their separate script files.

Currently implemented:

- [Kakuyomu](./kakuyomu.py)

## Requirements

- Python ~ 3.13. I use [mise](https://mise.jdx.dev/) for managing the version through [mise.toml](mise.toml).
- BeautifulSoup 4, aforementioned.

Install all required libraries via pip:
  
```sh
pip install -r requirements.txt
```

## Usage

```sh
python main.py
```
