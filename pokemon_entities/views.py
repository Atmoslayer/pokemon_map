import datetime
import folium
import json

from django.utils.timezone import localtime
from django.http import HttpResponseNotFound
from django.shortcuts import render

from pokemon_entities.models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):

    pokemon_objects = Pokemon.objects.all()
    pokemon_entities_objects = PokemonEntity.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity_object in pokemon_entities_objects:
        time_now = datetime.datetime.now().timestamp()
        pokemon_appeared_time = localtime(pokemon_entity_object.appeared_at).timestamp()
        pokemon_disappeared_time = localtime(pokemon_entity_object.disappeared_at).timestamp()
        if pokemon_appeared_time <= time_now <= pokemon_disappeared_time:
            add_pokemon(
                folium_map, pokemon_entity_object.lat,
                pokemon_entity_object.lon,
                request.build_absolute_uri(f'media/{pokemon_entity_object.pokemon.image}')
            )


    pokemons_on_page = []
    for pokemon_object in pokemon_objects:
        pokemons_on_page.append({
            'pokemon_id':  pokemon_object.id,
            'img_url': request.build_absolute_uri(f'media/{pokemon_object.image}'),
            'title_ru': pokemon_object.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):

    time_now = datetime.datetime.now().timestamp()
    pokemon_objects = Pokemon.objects.filter(id=int(pokemon_id))
    pokemon_entities_objects = PokemonEntity.objects.filter(
        pokemon_id=int(pokemon_id),
        appeared_at__it=time_now,
        disappeared_at__gt=time_now)

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity_object in pokemon_entities_objects:

        # pokemon_appeared_time = localtime(pokemon_entity_object.appeared_at).timestamp()
        # pokemon_disappeared_time = localtime(pokemon_entity_object.disappeared_at).timestamp()
        # if pokemon_appeared_time <= time_now <= pokemon_disappeared_time:
        add_pokemon(
            folium_map, pokemon_entity_object.lat,
            pokemon_entity_object.lon,
            request.build_absolute_uri(f'http://127.0.0.1:8000/media/{pokemon_entity_object.pokemon.image}')
        )

    pokemons_on_page = {}
    for pokemon_object in pokemon_objects:
        previous_evolution = {}
        next_evolution = {}
        if pokemon_object.previous_evolution:
            previous_evolution = {
                'title_ru': pokemon_object.previous_evolution.title,
                'pokemon_id': pokemon_object.previous_evolution.id,
                'img_url': request.build_absolute_uri(f'http://127.0.0.1:8000/media/{pokemon_object.previous_evolution.image}')
            }
        if pokemon_object.next_evolution:
            next_evolution = {
                'title_ru': pokemon_object.next_evolution.title,
                'pokemon_id': pokemon_object.next_evolution.id,
                'img_url': request.build_absolute_uri(f'http://127.0.0.1:8000/media/{pokemon_object.next_evolution.image}')
            }
        pokemons_on_page = {
            'pokemon_id': pokemon_object.id,
            'img_url': request.build_absolute_uri(f'http://127.0.0.1:8000/media/{pokemon_entity_object.pokemon.image}'),
            'title_ru': pokemon_object.title,
            'description': pokemon_object.description,
            'title_en': pokemon_object.title_en,
            'title_jp': pokemon_object.title_jp,
            'previous_evolution': previous_evolution,
            'next_evolution': next_evolution
        }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon':  pokemons_on_page
    })
