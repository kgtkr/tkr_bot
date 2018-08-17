import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

cs = os.environ.get("CS")
ck = os.environ.get("CK")
token = os.environ.get("TOKEN")
