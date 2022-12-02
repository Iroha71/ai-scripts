import cv2
import numpy
import argparse
import glob
from typing import List

def padding(image: numpy.ndarray) -> numpy.array:
  """画像にパディング行い、サイズを合わせる

  Args:
      image (numpy.ndarray): 画像の配列
  """
  height, width, color = image.shape
  if height > width:
    padding_half: int = calc_padding_size(height, width)
    image = cv2.copyMakeBorder(image, 0, 0, padding_half, padding_half, cv2.BORDER_CONSTANT, (0, 0, 0))
  
  if width > height:
    padding_half: int = calc_padding_size(width, height)
    image = cv2.copyMakeBorder(image, padding_half, padding_half, 0, 0, cv2.BORDER_CONSTANT, (0, 0, 0))

  return image


def calc_padding_size(big: float, small: float) -> int:
  """パディングサイズを計算する

  Args:
      big (float): 縦横のうち長い辺の長さ
      small (float): 短い辺の長さ

  Returns:
      int: パディングサイズの半分
  """
  diff: float = big - small

  return int(diff / 2)

if __name__ == "__main__":
  arg: argparse.ArgumentParser = argparse.ArgumentParser()
  arg.add_argument('-path', required=True)
  parsed_arg: argparse.Namespace = arg.parse_args()

  images: List[str] = glob.glob(f"{parsed_arg.path}/*.jpg")

  for image in images:
    pad_image: numpy.ndarray = padding(cv2.imread(image))
    cv2.imwrite(image, pad_image)
    print(f"{image} writed.")