# ホロライブの画像を集める
import os
import argparse
from icrawler.builtin import BingImageCrawler

def parse_keyword() -> str:
  """入力された引数を取得する

  Returns:
      str: vtuber名
  """
  parser: argparse.ArgumentParser = argparse.ArgumentParser()
  parser.add_argument("-name", required=True)
  args: argparse.Namespace = parser.parse_args()

  return args.name

def crawl(keyword: str):
  """Vtuberの画像を集め、ディレクトリに保存する

  Args:
      keyword (str): 検索ワード
  """
  base_dir: str = "./data"
  if not os.path.exists(base_dir):
    os.mkdir(base_dir)

  if not os.path.exists(os.path.join(base_dir, keyword)):
    os.mkdir(os.path.join(base_dir, keyword))

  crawler: BingImageCrawler = BingImageCrawler(storage={'root_dir': os.path.join(base_dir, keyword)})
  crawler.crawl(keyword=keyword, max_num=1000)

if __name__ == "__main__":
  vtuber_name: str = parse_keyword()
  crawl(vtuber_name)