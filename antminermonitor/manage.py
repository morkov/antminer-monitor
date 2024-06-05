import subprocess
import sys

from flask.cli import FlaskGroup

from antminermonitor.app import create_app
from antminermonitor.database import db_session, init_db

cli = FlaskGroup(create_app=create_app)


@cli.command()
def format():
    """Runs the yapf and isort formatters over the project."""
    isort = 'isort -rc *.py antminermonitor/'
    yapf = 'yapf -r -i *.py antminermonitor/'

    print('Running {}'.format(isort))
    subprocess.call(isort, shell=True)

    print('Running {}'.format(yapf))
    subprocess.call(yapf, shell=True)


def main():
    cli(sys.argv[1:])


if __name__ == "__main__":
    main()
