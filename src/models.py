from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    climate = db.Column(db.String(120), nullable=False)
    created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    diameter = db.Column(db.String(120), nullable=False)
    edited = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    gravity = db.Column(db.String(120), nullable=False)
    image = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    orbital_period = db.Column(db.String(120), nullable=False)
    population = db.Column(db.String(120), nullable=False)
    rotation_period = db.Column(db.String(120), nullable=False)
    surface_water = db.Column(db.String(120), nullable=False)
    terrain = db.Column(db.String(120), nullable=False)
    uid = db.Column(db.Integer, unique=True, nullable=False)
    url = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "climate": self.climate,
            "created": self.created.isoformat(),
            "diameter": self.diameter,
            "edited": self.edited.isoformat(),
            "gravity": self.gravity,
            "image": self.image,
            "name": self.name,
            "orbital_period": self.orbital_period,
            "population": self.population,
            "rotation_period": self.rotation_period,
            "surface_water": self.surface_water,
            "terrain": self.terrain,
            "uid": self.uid,
            "url": self.url
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    birth_year = db.Column(db.String(120), nullable=False)
    created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    edited = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    eye_color = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(120), nullable=False)
    hair_color = db.Column(db.String(120), nullable=False)
    height = db.Column(db.String(120), nullable=False)
    homeworld = db.Column(db.String(120), nullable=False)
    image = db.Column(db.String(120), nullable=False)
    mass = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    skin_color = db.Column(db.String(120), nullable=False)
    uid = db.Column(db.Integer, unique=True, nullable=False)
    url = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "birth_year": self.birth_year,
            "created": self.created.isoformat(),
            "edited": self.edited.isoformat(),
            "eye_color": self.eye_color,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "height": self.height,
            "homeworld": self.homeworld,
            "image": self.image,
            "mass": self.mass,
            "name": self.name,
            "skin_color": self.skin_color,
            "uid": self.uid,
            "url": self.url
        }

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cargo_capacity = db.Column(db.String(120), nullable=False)
    consumables = db.Column(db.String(120), nullable=False)
    cost_in_credits = db.Column(db.String(120), nullable=False)
    created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    crew = db.Column(db.String(120), nullable=False)
    edited = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    films = db.Column(db.ARRAY(db.String), nullable=False)
    image = db.Column(db.String(120), nullable=False)
    length = db.Column(db.String(120), nullable=False)
    manufacturer = db.Column(db.String(120), nullable=False)
    max_atmosphering_speed = db.Column(db.String(120), nullable=False)
    model = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    passengers = db.Column(db.String(120), nullable=False)
    pilots = db.Column(db.ARRAY(db.String), nullable=False)
    uid = db.Column(db.Integer, unique=True, nullable=False)
    url = db.Column(db.String(120), nullable=False)
    vehicle_class = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Vehicle %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "cost_in_credits": self.cost_in_credits,
            "created": self.created.isoformat(),
            "crew": self.crew,
            "edited": self.edited.isoformat(),
            "films": self.films,
            "image": self.image,
            "length": self.length,
            "manufacturer": self.manufacturer,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "model": self.model,
            "name": self.name,
            "passengers": self.passengers,
            "pilots": self.pilots,
            "uid": self.uid,
            "url": self.url,
            "vehicle_class": self.vehicle_class
        }