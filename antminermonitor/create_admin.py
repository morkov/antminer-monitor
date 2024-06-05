from antminermonitor.database import db_session, init_db
from antminermonitor.blueprints.user.models import User


def create_admin():
    """
        Create admin user if not exist with default password 'antminermonitor'
    """
    init_db()
    print("[INFO] Checking if admin user exists...")
    admin = User.query.filter_by(username='admin').first()

    if not admin:
        print("[INFO] Creating admin user with password 'antminermonitor'...")
        admin = User(
            username='admin',
            email='foo@bar.org',
            surname='admin',
            firstname='admin',
            active=0)
        admin.set_password('antminermonitor')
        db_session.add(admin)
        db_session.commit()
    elif admin:
        print("[INFO] Admin user already exists.")
    else:
        print("[INFO] Something went wrong.")


def main():
    create_admin()


if __name__ == '__main__':
    main()
