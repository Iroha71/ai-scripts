import glob
import os
import shutil
from typing import List

dir_path: str = './data/百鬼あやめ'
images: List[str] = glob.glob(f"{dir_path}/*.jpg481605")
for img in images:
  os.remove(img)