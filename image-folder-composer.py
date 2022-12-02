# 特定のディレクトリにある画像を別のディレクトリへ移動させる
import os
import argparse
from typing import Tuple
import shutil

def count_images(path: str) -> int:
  """ディレクトリ内の画像数を調べる

  Args:
      path (str): 画像数を調べるフォルダのパス

  Returns:
      int: 画像数
  """
  
  return sum(os.path.isfile(os.path.join(path, name)) for name in os.listdir(path))

def get_copy_dir() -> tuple:
  """コピー元とコピー先ディレクトリ名を取得する

  Returns:
      Tuple[str, str]: [0]コピー元, [1]コピー先ディレクトリ名
  """
  parser: argparse.ArgumentParser = argparse.ArgumentParser()
  parser.add_argument('origin')
  parser.add_argument('copy_goal')
  args: argparse.Namespace = parser.parse_args()

  return (args.origin, args.copy_goal)

def copy_images(image_num: int, origin_dir: str, copy_dir: str):
  """画像を指定のディレクトリに移動する

  Args:
      image_num (int): 画像数（ファイル名の重複を防ぐため）
      origin_dir (str): コピー元ディレクトリパス
      copy_dir (str): コピー先ディレクトリパス
  """
  index: int = 0
  for img in os.listdir(origin_dir):
    filename: str = os.path.splitext(os.path.basename(img))[0]
    new_filepath = os.path.join(copy_dir, f"{filename}-{image_num + index}.jpg")
    shutil.move(os.path.join(origin_dir, img), new_filepath)
    index += 1

if __name__ == "__main__":
  dir: Tuple[str, str] = get_copy_dir()
  img_num: int = count_images(dir[0])
  copy_images(img_num, dir[0], dir[1])
  os.rmdir(dir[0])