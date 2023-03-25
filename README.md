# Projeto de consulta na Star Wars API com Requisições HTTP e JSON

Para rodar este projeto, certifique-se de que as bibliotecas
`requests` e `json` foram importadas, elas resão responsáveis por consumir a Star Wars API e importar os dados das requisições em JSON, respectivamente. Depois `basta clicar em Run`

Este projeto foi codado com `python3.11`

Ele trará de forma automática os dados solicitados em cada consulta, importando-os para um arquivo json.

O código está comentado para saber como foi feito.

Caso seja necessário gerar os arquivos json novamente, pode haver uma lentidão, já que estará realizando todas as requests para obter as informações

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Importando as bibliotecas `requests` e `json` para que o código faça as requisições e possa importar arquivos JSON.

A URL base da API é definida com `base_url` em seguida e será usada posteriormente para construir as URLs de consulta de people e planets.

Foi definida a URL para a consulta dos personagens, concatenando a URL base com o caminho `'people/'`. 
Em seguida, foi definida uma lista vazia `people_data` que será preenchida com os dados people encontrados na API.

Definido o primeiro loop `while` com a variável `people_url` que é inicializada com a URL dos personagens. Dentro do loop, uma requisição é feita para a URL usando a biblioteca `requests`, que retorna os dados. 
A função `json.loads()` é usada para carregar os dados JSON. Os dados dos personagens são adicionados à lista usando o método `extend()`. 
A variável `people_url` é atualizada com o valor `next` dos dados da resposta.

Foi definido o loop `for` para verificar se na lista tem personagens em pelo menos 4 filmes.

Em seguida um arquivo JSON é criado com os dados dos personagens que aparecem em 4 ou mais filmes.

A URL para a consulta dos planetas é definida, concatenando a URL base com o caminho `'planets/'`.
Na linha seguinte, é definida uma lista vazia `planets_data` que será preenchida com os dados dos planetas encontrados na API.

Definido mais um loop `while` semelhante ao loop while anterior para os personagens, para buscar os planetas que possuem 5 ou mais residentes.

O loop `for` percorre a lista `planets_data` e verifica se o planeta tem 5 ou mais residentes.

Em seguida um arquivo JSON é criado com os dados dos planetas que possuem 5 ou mais residentes.