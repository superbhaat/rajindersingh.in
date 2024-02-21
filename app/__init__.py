from flask import Flask

app = Flask(__name__,template_folder='templates')
#print(app.config)

# if app.config["ENV"] == "production":
#     app.config.from_object("config.Production")
# elif app.config["ENV"] == "testing":
#     app.config.from_object("config.Testing")
# else:
    #app.config.from_object("config.Develoment")

app.config.from_object("config.Production")
#app.config.from_object("config.Develoment")

from app import frontViews
from app import adminViews
from app import errorHandlers