from datetime import date
from typing import Optional

from sqlmodel import Field, SQLModel


class State(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    fips: int


class County(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    fips: int
    state_id: Optional[int] = Field(default=None, foreign_key="state.id")


class Count(SQLModel, table=True):
    """Create the model class, representing the table in the database.

    And also mark this class as a table model with table=True.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    date: date
    cases: int
    deaths: int
    state: str
    county: str
    # state_id: Optional[int] = Field(default=None, foreign_key="state.id")
    # county_id: Optional[int] = Field(default=None, foreign_key="county.id")


# class Team(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     name: str = Field(index=True)
#     headquarters: str
#     heroes: List["Hero"] = Relationship(back_populates="team")


# class Hero(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     name: str = Field(index=True)
#     secret_name: str
#     age: Optional[int] = Field(default=None, index=True)
#     team_id: Optional[int] = Field(default=None, foreign_key="team.id")
#     team: Optional[Team] = Relationship(back_populates="heroes")
