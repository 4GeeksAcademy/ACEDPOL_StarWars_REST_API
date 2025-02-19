import os
from flask_admin import Admin
from models import db, User, People, Planet, Vehicle, UserPeopleFavorites, UserPlanetFavorites, UserVehicleFavorites
from flask_admin.contrib.sqla import ModelView

class UserPeopleFavoritesView(ModelView):
    column_list = ('user_id', 'user_name', 'people_id', 'people_name')
    column_labels = {
        'user_id': 'User ID',
        'user_name': 'User Name',
        'people_id': 'People ID',
        'people_name': 'People Name'
    }
    column_display_pk = True

class UserPlanetFavoritesView(ModelView):
    column_list = ('user_id', 'user_name', 'planet_id', 'planet_name')
    column_labels = {
        'user_id': 'User ID',
        'user_name': 'User Name',
        'planet_id': 'Planet ID',
        'planet_name': 'Planet Name'
    }
    column_display_pk = True

class UserVehicleFavoritesView(ModelView):
    column_list = ('user_id', 'user_name', 'vehicle_id', 'vehicle_name')
    column_labels = {
        'user_id': 'User ID',
        'user_name': 'User Name',
        'vehicle_id': 'Vehicle ID',
        'vehicle_name': 'Vehicle Name'
    }
    column_display_pk = True

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    # Add your models here, for example this is how we add the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(People, db.session))
    admin.add_view(ModelView(Planet, db.session))
    admin.add_view(ModelView(Vehicle, db.session))

    # Add the favorites association tables to the admin with custom views
    admin.add_view(UserPeopleFavoritesView(UserPeopleFavorites, db.session, name='User People Favorites'))
    admin.add_view(UserPlanetFavoritesView(UserPlanetFavorites, db.session, name='User Planet Favorites'))
    admin.add_view(UserVehicleFavoritesView(UserVehicleFavorites, db.session, name='User Vehicle Favorites'))

    # You can duplicate that line to add new models
    # admin.add_view(ModelView(YourModelName, db.session))