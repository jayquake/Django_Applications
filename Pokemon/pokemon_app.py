import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pokemon.settings')
django.setup()
import requests
import json
from pokemon_app.models import Card
from random import randint



for number in range(1, 152):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{number}/')
    info = response.json()
    sprite = info.get('sprites').get('front_default')
    species = info.get('species').get('name')
    types = info.get('types')[0].get('type').get('name')
    weight = info.get('weight')
    attack = info.get('stats')[0].get('base_stat')
    move = info.get('moves')[2].get('move').get('name')
    a = Card(name=species, attack=attack, attribute=types, weight=weight, image=sprite, move=move)
    # a.save()
print('done')
# deck = []
# for x in range(5):
#     num = randint(1, Card.objects.all().count())
#     card = Card.objects.get(id=num)
# print(card)







# print(card1)
# print(card2)
# print(card3)
# print(card4)




# def random_card(request):
#     deck = []
#     cards = Card.objects.all().name
#     print(cards)





