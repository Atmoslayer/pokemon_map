import datetime
import folium
import json

from django.utils.timezone import localtime
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

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

    time_now = datetime.datetime.now()
    pokemons = Pokemon.objects.all()
    pokemon_entities = PokemonEntity.objects.filter(
        appeared_at__lte=time_now,
        disappeared_at__gte=time_now)

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(f'media/{pokemon_entity.pokemon.image}')
        )


    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id':  pokemon.id,
            'img_url': request.build_absolute_uri(f'media/{pokemon.image}'),
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):

    time_now = datetime.datetime.now()
    pokemon = get_object_or_404(Pokemon, id=int(pokemon_id))
    pokemon_entities = pokemon.entities.filter(
        pokemon_id=int(pokemon_id),
        appeared_at__lte=time_now,
        disappeared_at__gte=time_now)

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(f'http://127.0.0.1:8000/media/{pokemon.image}')
        )

    previous_evolution = pokemon.previous_evolution
    next_evolutions = pokemon.next_evolutions.filter(previous_evolution=pokemon)
    previous_evolution_data = {}
    next_evolution_data = {}

    if previous_evolution:
        previous_evolution_data = {
            'title_ru': pokemon.previous_evolution.title,
            'pokemon_id': pokemon.previous_evolution.id,
            'img_url': request.build_absolute_uri(f'http://127.0.0.1:8000/media/{pokemon.previous_evolution.image}')
        }
    next_evolution_data = []
    if next_evolutions:
        for next_evolution in next_evolutions:

            next_evolution_data.append(  {
                'title_ru': next_evolution.title,
                'pokemon_id': next_evolution.id,
                'img_url': request.build_absolute_uri(f'http://127.0.0.1:8000/media/{next_evolution.image}')
            })

    pokemons_on_page = {
        'pokemon_id': pokemon.id,
        'img_url': request.build_absolute_uri(f'http://127.0.0.1:8000/media/{pokemon.image}'),
        'title_ru': pokemon.title,
        'description': pokemon.description,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'previous_evolution': previous_evolution_data,
        'next_evolution': next_evolution_data
    }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon':  pokemons_on_page
    })
