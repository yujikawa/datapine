from operators.sqlite_operator import SqliteOperator
from operators.db_connection import DBConnection

if __name__ == '__main__':
    d = DBConnection("sample_pj")
    s = SqliteOperator(d)
    s.sorce_file_to_db()
    s.query()
    s.export_data()
