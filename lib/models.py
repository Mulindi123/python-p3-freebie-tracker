from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

company_dev_association = Table(
    "company_devs",
    Base.metadata,
    Column("company_id", Integer, ForeignKey("companies.id"), primary_key=True),
    Column("dev_id", Integer, ForeignKey("devs.id"), primary_key=True),
    extend_existing=True
)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    #relationships
    freebies = relationship("Freebie", backref=backref("company"))
    devs = relationship("Dev", secondary=company_dev_association, back_populates="devs")

    def __repr__(self):
        return f'<Company {self.name}>'



class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    #relationships
    freebies = relationship("Freebie", backref=backref("dev"))
    companies = relationship("Company", secondary=company_dev_association, back_populates="devs")

    def __repr__(self):
        return f'<Dev {self.name}>'
    
class Freebie(Base):
    __tablename__ = "freebies"
    id = Column(Integer, primary_key=True)
    item_name = Column(String())
    value = Column(Integer)
    company_id = Column(Integer, ForeignKey("companies.id"))
    dev_id = Column(Integer, ForeignKey("devs.id"))

    def __repr__(self):
        return f"<Freebie {self.item_name}>"