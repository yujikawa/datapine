import os
import shutil
import fire
from tqdm import tqdm
from .operators.sqlite_operator import SqliteOperator
from .operators.db_connection import DBConnection

def etl(path: str):
    d = DBConnection(path)
    s = SqliteOperator(d)
    for f in tqdm([s.sorce_file_to_db, s.query, s.export_data]):
        r = f()
        print(r)

def init(path: str):
    os.makedirs(os.path.join(path, 'db'), exist_ok=True)
    os.makedirs(os.path.join(path, 'export'), exist_ok=True)
    os.makedirs(os.path.join(path, 'sqls'), exist_ok=True)
    os.makedirs(os.path.join(path, 'result'), exist_ok=True)

def main():
    fire.Fire({"etl": etl, "init": init})
