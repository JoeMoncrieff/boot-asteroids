import pygame
from asteroid import Asteroid
from player import Player
from constants import *
from asteroidfield import AsteroidField
from shot import Shot
from score import Score
from button import Button

class Controller:
    def __init__(self,updatable,drawable,asteroids,shots):
        self.updatable = updatable
        self.drawable = drawable
        self.asteroids = asteroids
        self.shots = shots
        self.player = None
        self.asteroidfield = None
        self.score = None
        self.main_game = None
