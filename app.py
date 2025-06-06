from flask import Flask
from views.routes import main
from views.auth import auth


app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(auth)

if __name__ == '__main__':
    app.run(debug=True)
