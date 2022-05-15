import os
import datetime

class DBConnection():
    def __init__(self, pj_path: str):
        # self.timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        self.pj_path = pj_path
        self.pj_name = pj_path.split(os.sep)[-1]
        os.makedirs(os.path.join(pj_path, "db"), exist_ok=True)
        self.db_path = os.path.join(pj_path, "db", f"{self.pj_name}.db")

