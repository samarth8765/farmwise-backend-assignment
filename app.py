from flask import Flask
from controllers.extension import db, jwt
from controllers.routes import routes_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/postgres'
app.config['JWT_SECRET_KEY'] = "SECRET_PASSWORD"
db.init_app(app)
jwt.init_app(app)

app.register_blueprint(routes_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)