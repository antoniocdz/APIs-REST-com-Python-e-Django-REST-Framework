import requests

headers = {'Authorization': 'Token ae43728eab9e68cbf9b156f888cfaee7f89d4925'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

print(resultado.json())

# Testando se o endpoint está correto
assert resultado.status_code == 200

# Testando a quantidade de registros
assert resultado.json()['count'] == 7

# # Testando se o título do primeiro curso está correto
assert resultado.json()['results'][1]['titulo'] == 'Asp.Net Core com React.js'

