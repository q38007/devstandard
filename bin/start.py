import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根路径
sys.path.append(BASE_DIR)

from core import src

if __name__ == '__main__':
    src.run()
