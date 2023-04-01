import pymongo
import pandas as pd
import json
from dataclasses import dataclass
import os
@dataclass
# Provide the mongodb localhost url to connect python to mongodb.

class EnvironmentVariable:
    mongo_db_url:str= os.getenv("MONGO_DB_URL")
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")

env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)