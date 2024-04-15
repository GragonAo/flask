import logging
import os
import sys

from dotenv import load_dotenv
from playhouse.pool import PooledMySQLDatabase

load_dotenv()

db_config = {
    'database': os.getenv('MYSQL_DB', 'peewee'),
    'user': os.getenv('MYSQL_USER', 'root'),
    'password': os.getenv('MYSQL_PASSWORD', 'password'),
    'host': os.getenv('MYSQL_HOST', 'localhost'),
    'port': int(os.getenv('MYSQL_PORT', 3306))
}
conn = PooledMySQLDatabase(**db_config)


def init_db():
    try:
        conn.connect()
    except Exception as e:
        logging.error(f"数据库连接失败,请检查.env内数据库配置选项是否正确!: {e}")
        sys.exit(1)


def close_db():
    if conn.is_closed():
        return
    conn.close()
