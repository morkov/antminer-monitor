from sqlalchemy.exc import IntegrityError

from antminermonitor.blueprints.asicminer.models.settings import Settings
from antminermonitor.database import db_session, init_db


def create_db():
    """
        Create database. Add miner models and settings.
    """

    init_db()

    settings = []
    settings.append(
        Settings(name="temperature_alert", value="80", description=""))
    settings.append(
        Settings(
            name="email_alert",
            value="True",
            description="Whether to send an email on alert"))

    try:
         for setting in settings:
            db_session.add(setting)
            db_session.commit()
    except IntegrityError:
        print("[INFO] Database already exists.")
    else:
        print("[INFO] Database successfully created.")


def main():
    create_db()


if __name__ == '__main__':
    main()
