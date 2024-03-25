from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    character_name = Column(String)

    def __repr__(self):
        return f"<Role(id={self.id}, character_name='{self.character_name}')>"

    @property
    def auditions(self):
        return [audition for audition in self.auditions]

    @property
    def actors(self):
        return [audition.actor for audition in self.auditions]

    @property
    def locations(self):
        return [audition.location for audition in self.auditions]

    def lead(self):
        hired_audition = next((audition for audition in self.auditions if audition.hired), None)
        return hired_audition if hired_audition else "no actor has been hired for this role"

    def understudy(self):
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        return hired_auditions[1] if len(hired_auditions) > 1 else "no actor has been hired for understudy for this role"


class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer, primary_key=True)
    actor = Column(String)
    location = Column(String)
    phone = Column(Integer)
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship("Role", backref=backref("auditions", cascade="all, delete-orphan"))

    def __repr__(self):
        return f"<Audition(id={self.id}, actor='{self.actor}', location='{self.location}', hired={self.hired})>"

    def call_back(self):
        self.hired = True

engine = create_engine('sqlite:///theater_database.db', echo=True)

# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

