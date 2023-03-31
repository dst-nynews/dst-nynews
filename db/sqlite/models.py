from datetime import date
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class Count(SQLModel, table=True):
    """Create the model class, representing the table in the database.

    And also mark this class as a table model with table=True.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    date: date
    state: str
    county: str
    fips: int
    cases: int
    deaths: int


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
