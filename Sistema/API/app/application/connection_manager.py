from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker
from config import DevConfig

engine = create_engine(DevConfig.SQLALCHEMY_DATABASE_URI, echo=True)

# create a Session
Session = sessionmaker(bind=engine)


class SessionManager:
    __instance = None
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if SessionManager.__instance == None:
            SessionManager()
        return SessionManager.__instance
    def __init__(self):
        """ Virtually private constructor. """
        if SessionManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            SessionManager.__instance = Session()