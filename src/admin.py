import os
from flask_admin import Admin
from models import db, User, People, Planet, Vehicle, UserPeopleFavorites, UserPlanetFavorites, UserVehicleFavorites
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    # Add your models here, for example this is how we add the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(People, db.session))
    admin.add_view(ModelView(Planet, db.session))
    admin.add_view(ModelView(Vehicle, db.session))

    # Add the favorites association tables to the admin
    admin.add_view(ModelView(UserPeopleFavorites, db.session, name='User People Favorites'))
    admin.add_view(ModelView(UserPlanetFavorites, db.session, name='User Planet Favorites'))
    admin.add_view(ModelView(UserVehicleFavorites, db.session, name='User Vehicle Favorites'))

    # You can duplicate that line to add new models
    # admin.add_view(ModelView(YourModelName, db.session))