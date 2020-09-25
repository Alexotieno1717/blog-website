from app import create_app, db
from app.models import User
from flask_script import Manager, Shell, Server

app = create_app('development')


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User)


if __name__ == '__main__':
    app.run()
