#coding=utf-8
import sys
import os
import configparser

base_path = os.getcwd()
sys.path.append(base_path)
import _json
from Util.handle_json import get_value

#1. get cookie
#2. write cookie
#3. 是否携带
