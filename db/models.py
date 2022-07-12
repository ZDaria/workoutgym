from sqlalchemy import Column, Integer, Date, Float, String
from .db_connection import Base, engine


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    firstname = Column(String())
    lastname = Column(String())
    age = Column(Integer())
    weight = Column(Float())
    height = Column(Float())
    birthday = Column(Date())

    def __repr__(self):
        return f"{self.id}, {self.firstname}, {self.lastname}"


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
