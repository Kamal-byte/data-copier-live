import sys
from config import DB_DETAILS
from util import get_tables
def main():
    """Pass one argument"""
    env = sys.argv[1]
    db_details = DB_DETAILS[env]
    tables = get_tables('table_list')
    for table in tables['table_name']:
        print(table)
        # print(idx)
if __name__ == '__main__':
    main()