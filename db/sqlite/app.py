from datetime import date
from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine


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


# Write the name of the database file.
sqlite_file_name = "covid.db"
# Use the name of the database file to create the database URL.
sqlite_url = f"sqlite:///{sqlite_file_name}"

# Create the engine using the URL. This doesn't create the database yet.
engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    """Put the code that creates side effects in a function.

    In this case, only one line that creates the database file with the table.
    """
    # Create all the tables
    # (The tables were automatically registered in SQLModel.metadata.)
    SQLModel.metadata.create_all(engine)


def create_counts():
    count_1 = Count(
        date=date(2020, 1, 24),
        state="Illinois",
        county="Cook",
        fips=17031,
        cases=1,
        deaths=0,
    )
    count_2 = Count(
        date=date(2020, 1, 24),
        state="Washington",
        county="Snohomish",
        fips=53061,
        cases=1,
        deaths=0,
    )
    count_3 = Count(
        date=date(2022, 5, 13),
        state="Wyoming",
        county="Sweetwater",
        fips=56037,
        cases=11088,
        deaths=126,
    )
    count_4 = Count(
        date=date(2022, 5, 13),
        state="Wyoming",
        county="Teton",
        fips=56039,
        cases=10074,
        deaths=16,
    )

    with Session(engine) as session:
        session.add(count_1)
        session.add(count_2)
        session.add(count_3)
        session.add(count_4)

        session.commit()


if __name__ == "__main__":
    """Add a main block, or "Top-level script environment".

    And put some logic to be executed when this is called directly with Python,
    but that is not executed when importing something from this module.
    """

    # In this main block, call the functions to run the script.
    create_db_and_tables()
    create_counts()
