# wsgi.py
import sys
import os

# 确保项目根目录在 Python 路径中
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app

# 对于某些 WSGI 服务器，可能需要显式导出
application = app
