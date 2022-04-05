## ER_Diagram
![Quiz_041](https://user-images.githubusercontent.com/89367058/161764453-411a044b-d744-4f9a-be57-3c4d5e4d719f.png)


## Code
``` python
# database_models
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Clients(Base):
    """ This class creates Clients table"""
    __tablename__ = "Clients"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    address = Column(String(255))
    phone_number = Column(Integer)
    company_name = Column(String(255))


class Paper(Base):
    """ This class creates Paper table"""
    __tablename__ = "Paper"
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    price = Column(Float)
    quantity = Column(Integer)
    type = Column(String(255))
    delivery_date = Column(Date)
    # Foreign key connects to Clients
    user_id = Column(Integer, ForeignKey("Clients.id"))


# This creates the tables
db_engine = create_engine("sqlite:///quiz041_database.db")
Base.metadata.create_all(db_engine)

```

## Run
<img width="1317" alt="Screen Shot 2022-04-05 at 22 28 12" src="https://user-images.githubusercontent.com/89367058/161764622-3cf630c2-02d0-49c0-934b-8e44c9953bf4.png">
<img width="1317" alt="Screen Shot 2022-04-05 at 22 28 23" src="https://user-images.githubusercontent.com/89367058/161764638-05adbf03-8162-4aa2-86e6-26e1e188d189.png">
