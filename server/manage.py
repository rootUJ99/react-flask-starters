from flask.cli import FlaskGroup
from service import create_app, db 

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command('recreate_db')
def recreate_db():
  db.drop_all()
  db.create_all()
  db.session.commit()

if __name__ == '__main__':
  print(__name__, 'name in main')
  cli()

