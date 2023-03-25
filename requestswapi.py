# Importando as bibliotecas
import requests
import json

# Usando requests para definir a URL base da API Star Wars
base_url = 'https://swapi.dev/api/'

# Consulta os personagens que aparecem em 4 filmes ou mais
# URL + o caminho de onde quero encontrar as informações
people_url = base_url + 'people/'

# Definindo uma lista vazia que será preenchida pelos dados requisitados
people_data = []
while people_url:
    response = requests.get(people_url)
    data = json.loads(response.text)
    people_data.extend(data['results'])
    people_url = data['next']

#   Após fazer a primeira consulta irá realizar um "filtro" para apresentar somente os personagens que aparecem
# em quatro filmes ou mais
four_films_or_more = []
for person in people_data:
    if len(person['films']) >= 4:
        four_films_or_more.append(person)

# Importando os dados encontrados para um arquivo JSON
with open('list_people.json', 'w') as f:
    json.dump(four_films_or_more, f, indent=2)

# Consulta os planetas que possuem 5 moradores ou mais
# URL + o caminho de onde quero encontrar as informações
planets_url = base_url + 'planets/'

# Definindo uma lista vazia que será preenchida pelos dados requisitados
planets_data = []
while planets_url:
    response = requests.get(planets_url)
    data = json.loads(response.text)
    planets_data.extend(data['results'])
    planets_url = data['next']

#   Após fazer a primeira consulta irá realizar um "filtro" para apresentar somente os planetas que possuem
# 5 moradores ou mais
five_residents_or_more = []
for planet in planets_data:
    if len(planet['residents']) >= 5:
        five_residents_or_more.append(planet)

# Importando os dados encontrados para um arquivo JSON
with open('list_planets.json', 'w') as f:
    json.dump(five_residents_or_more, f, indent=2)