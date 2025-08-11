# HTML to CSV

A small Python repo to scrape a webpage and output its text into a CSV file, primarily using the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#) library.

Different sites should be relegated to their separate script files.

Currently implemented:

- [Kakuyomu](./kakuyomu.py)

## Requirements

- Python 3.13+. I use [mise](https://mise.jdx.dev/) for managing the version through [mise.toml](mise.toml).
- BeautifulSoup 4, aforementioned.

Install all required libraries via pip:
  
```sh
# If you're using mise:
mise pip

# Otherwise:
pip install -r requirements.txt
```

## Usage

Using [TsumeImo chapter 26](https://kakuyomu.jp/works/16818093083276084916/episodes/16818093085087163876) as an example:

```sh
$ python main.py
Enter a URL: https://kakuyomu.jp/works/16818093083276084916/episodes/16818093085087163876
Output to: わたしにだけ冷たい妹が、最近妙に甘えてくる/第26話　恋の白旗.csv
```
