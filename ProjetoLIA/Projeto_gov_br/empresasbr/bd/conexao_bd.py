import sqlalchemy as sa

from sqlalchemy.future.engine import Engine

from dotenv import load_dotenv

from os import getenv


load_dotenv()


def create_engine(host: str = None, user: str = None, password: str = None, database: str = None) -> Engine:

    host= getenv('HOST')
    user= getenv('USER')
    password= getenv('PASSWORD')
    database= getenv('DATABASE')

    conn_str = f"mysql+pymysql://{user}:{password}@{host}:3306/{database}"
    
    __engine = sa.create_engine(url=conn_str, echo=False)

    return __engine