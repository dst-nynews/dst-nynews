from sqlmodel import SQLModel, create_engine

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
