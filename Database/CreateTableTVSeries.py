from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from DatabaseConnection import engine

# Define a declarative base
Base = declarative_base()

# Define the TVSeries table class
class TVSeries(Base):
    __tablename__ = 'tvseries'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    period = Column(String(20), nullable=False)
    episodes = Column(Integer)
    rated = Column(String(10))
    

# Create the table in the database
def create_table():
    try:
        Base.metadata.create_all(bind=engine)
        print('Table created successfully')
    except Exception as ex:
        print(f'An error occurred: {ex}')

if __name__ == "__main__":
    create_table()
