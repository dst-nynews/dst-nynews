from datetime import date

from sqlmodel import Session

from .database import create_db_and_tables, engine
from .models import Count
# from .models import Hero, Team


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


# def create_heroes():
#     with Session(engine) as session:
#         team_z_force = Team(name="Z-Force", headquarters="Sister Margaret’s Bar")

#         hero_deadpond = Hero(
#             name="Deadpond", secret_name="Dive Wilson", team=team_z_force
#         )
#         session.add(hero_deadpond)
#         session.commit()

#         session.refresh(hero_deadpond)

#         print("Created hero:", hero_deadpond)
#         print("Hero's team:", hero_deadpond.team)


def main():
    """Add a main block, or "Top-level script environment".

    And put some logic to be executed when this is called directly with Python,
    but that is not executed when importing something from this module.
    """
    create_db_and_tables()
    create_counts()
    # create_heroes()


if __name__ == "__main__":
    # In this main block, call the functions to run the script.
    main()
