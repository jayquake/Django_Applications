from django.db.models import *
from PIL import Image
from account_app.models import Profile
from django.core.validators import MinValueValidator


class Card(Model):
    name = CharField(max_length=1000)
    attribute = CharField(max_length=1000)
    weight = IntegerField(default=0)
    attack = IntegerField(default=0)
    move = CharField(max_length=60, default="head kick")
    image = ImageField(default='default.jpg', upload_to='pokemon_pics')

    def __str__(self):
        return f'{self.name}'

    def __int__(self):
        return f'{self.weight}'


class CardSale(Model):
    profile = ForeignKey(Profile, on_delete=CASCADE)
    card = ForeignKey(Card, on_delete=CASCADE)
    price = IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.card.name


class CardBuy(Model):
    profile = ForeignKey(Profile, on_delete=CASCADE)
    card = ForeignKey(CardSale, on_delete=CASCADE)
    price = IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.card.name


class Deck(Model):
    profile = OneToOneField(Profile, on_delete=CASCADE)
    cards = ManyToManyField(Card)

    def __str__(self):
        return self.profile.name

    def get_points(self):
        return sum([card.attack for card in self.cards.all()])