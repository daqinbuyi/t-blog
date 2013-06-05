from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import config

class DataBase:

    def __init__(self):
        self.engine = create_engine(config.DATABASE_URI, echo=config.DATABASE_ECHO)
        self.Model = declarative_base()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    
    def create_tables(self):
        self.Model.metadata.create_all(self.engine)

db = DataBase()
