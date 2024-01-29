from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import declarative_base
from DatabaseConnection import engine

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, Sequence('movie_id_seq'), primary_key=True)
    title = Column(String(255))  # Adjust the length as needed
    year = Column(Integer)
    runtime = Column(String(50))  # Adjust the length as needed
    rated = Column(String(50))    # Adjust the length as needed


# Create the table in the database
def create_table():
    try:
        Base.metadata.create_all(bind=engine)
        print('Table created successfully')
    except Exception as ex:
        print(f'An error occurred: {ex}')

if __name__ == "__main__":
    create_table()
