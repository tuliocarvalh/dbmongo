import pymongo
from pymongo import MongoClient
from pass_ import *
import random
password = password()
url = f""
cluster = MongoClient(url)

db = cluster["test"]

dblist = cluster.list_database_names()
print(cluster.list_database_names())