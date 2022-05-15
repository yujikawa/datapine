import os
from glob import glob
import sqlite3 
import pandas as pd
from .db_connection import DBConnection
import datetime

class SqliteOperator():
    def __init__(self, db_conn: DBConnection):
        self.db_conn = db_conn
        
    def sorce_file_to_db(self):
        file_list = glob(os.path.join(self.db_conn.pj_path, "source", "*"))

        with sqlite3.connect(self.db_conn.db_path) as conn:
            for file_path in sorted(file_list):
                df = self.load_file(file_path)
                file_name = os.path.splitext(os.path.basename(file_path))[0]
                df.to_sql(file_name ,conn ,if_exists='replace')

        return "Loaded Data source!"

    def query(self):
        file_list = glob(os.path.join(self.db_conn.pj_path, "sqls", "*.sql"))
        with sqlite3.connect(self.db_conn.db_path) as conn:
            for file_path in sorted(file_list):
                sql = self._read_sql(file_path)
                cur = conn.cursor()
                cur.execute(sql)

        return "Transformed Data"
    
    def load_file(self, file_path):
        df = pd.DataFrame([])
        basename = os.path.basename(file_path)
        ext = basename.split('.')[-1]
        if ext == "csv":
            df = pd.read_csv(file_path)
        elif ext in ("xlsx", "xls"):
            df = pd.read_excel(file_path)

        return df

    def export_data(self):
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        export_dir = os.path.join(self.db_conn.pj_path, "export")
        file_list = glob(os.path.join(export_dir, "*.sql"))
        result_dir = os.path.join(self.db_conn.pj_path, "result" , timestamp)
        os.makedirs(result_dir, exist_ok=True)

        with sqlite3.connect(self.db_conn.db_path) as conn:
            for file_path in file_list:
                basename = os.path.basename(file_path)
                table_name, _ = basename.split('.')
                sql = self._read_sql(file_path)
                db_df = pd.read_sql_query(sql, conn)
                db_df.to_csv(os.path.join(result_dir, f'{table_name}.csv'), index=False)
        
        return f"Exported Result: {result_dir}"

    def _read_sql(self, file_path):
        with open(file_path, "r") as f:
            sql = f.read()
        
        return sql




