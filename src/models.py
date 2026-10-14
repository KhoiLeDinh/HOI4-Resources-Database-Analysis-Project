from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Text, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class DimCountry(Base):
    __tablename__ = "dim_country"
    country_tag = Column(String(3), primary_key=True, index=True)
    country_name = Column(String(100), nullable=False)
    states = relationship("FactStateSnapshot", back_populates="country")

class FactStateSnapshot(Base):
    __tablename__ = "fact_state_1_14_5"

    state_id = Column(Integer, primary_key=True, index=True)
    state_name = Column(String(150), nullable=False)
    owner_tag = Column(String(5), ForeignKey("dim_country.country_tag"), nullable=False)
    state_status = Column(String(50))
    state_category = Column(String(50))
    victory_points = Column(Numeric(10, 2), default=0.0)
    provinces_count = Column(Integer, default=0)
    population = Column(BigInteger, default=0)
    infrastructure = Column(Numeric(5, 2), default=0.0)
    building_slots = Column(Numeric(5, 2), default=0.0)

    # Factory capacity
    military_factories = Column(Numeric(5, 2), default=0.0)
    naval_factories = Column(Numeric(5, 2), default=0.0)
    civilian_factories = Column(Numeric(5, 2), default=0.0)
    total_factories = Column(Numeric(5, 2), default=0.0)

    # Base Strategic Resources
    base_oil = Column(Numeric(10, 2), default=0.0)
    base_aluminum = Column(Numeric(10, 2), default=0.0)
    base_rubber = Column(Numeric(10, 2), default=0.0)
    base_tungsten = Column(Numeric(10, 2), default=0.0)
    base_steel = Column(Numeric(10, 2), default=0.0)
    base_chromium = Column(Numeric(10, 2), default=0.0)
    total_base_resources = Column(Numeric(10, 2), default=0.0)

    country = relationship("DimCountry", back_populates="states")