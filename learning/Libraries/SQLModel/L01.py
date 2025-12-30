# first map sql tables
from typing import Optional, List
# creating a sqlmodel
from sqlmodel import Field, Session, SQLModel, Relationship, create_engine, select  # Session and create_engine
# needed to write to database


# define a  class
class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    headquarters: str

    # link to the team attr in the hero class
    heroes: list['Hero'] = Relationship(back_populates="team")


# 1. define hero class
class Hero(SQLModel, table=True):
    # class hero is a sql model equivalent to a sql table
    # class attributes are equivalent to each column of the table
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)  # unique constraint which prevents duplication
    secret_name: str
    age: int | None = None

    # connect hero to a team id (foreign key link)
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")

    # link to the heroes attr in the team class
    team: Optional['Team'] = Relationship(back_populates="heroes")


# creating rows
hero_data = [
Hero(name='<NAME>', secret_name='<Name>', age=18),
Hero(name='Deadpond', secret_name='James Walrich'),
Hero(name='Fran Pire', secret_name='Francois Andrews', age=70),
Hero(name='The Knight', secret_name='Willy Macantosh', age=18),
Hero(name='Kitty', secret_name='Jane Sliven', age=23)
]
# initialize an engine to connect to sqlite database 
engine = create_engine('sqlite:///hero.db')

SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    # 1. create the team object
    team1 = Team(name='The preventers', headquarters='sharp tower')

    # 2. Check if it exists
    statement = select(Team).where(Team.name == team1.name)
    existing_team = session.exec(statement).first()

    if not existing_team:
        session.add(team1)
        session.commit()
        session.refresh(team1)


# use session to check for existing entries and add new ones without duplicates when rerunning code
heroes_to_add = hero_data

with Session(engine) as session:

    team = session.exec(
        select(Team).where(Team.name == 'The preventers')

    ).first()
    for hero in heroes_to_add:

        # 1. Search for a hero with this name
        statement = select(Hero).where(Hero.name == hero.name)
        existing_hero = session.exec(statement).first()

        # 2. Decision logic
        if not existing_hero:
            hero.team = team
            session.add(hero)
            print(f'Adding {hero.name} to the database')
        else:
            print(f'skipping {hero.name}: Already exists')
        # 3. finalize
        session.commit()

    # Reading the data immediately after
    statement = select(Hero)
    results = session.exec(statement)
    for hero in results:
        print(hero)


                           