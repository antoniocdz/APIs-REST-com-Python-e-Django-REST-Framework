import requests

headers = {
    'Authorization': 'Token ae43728eab9e68cbf9b156f888cfaee7f89d4925'
}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo": "Novo Curso de Scrum 3",
    "url": "http://www.geekuniversity.com.br/ncs3"
}

# Atualizando o curso de ID 6
resultado = requests.put(
    url=f'{url_base_cursos}8/',
    headers=headers,
    json=curso_atualizado
)

print(f'Status Code: {resultado.status_code}')

try:
    print('Resposta:', resultado.json())
except Exception:
    print('Resposta:', resultado.text)

# Testando o código de status HTTP
assert resultado.status_code == 200, (
    f'Esperado status 200, mas recebeu {resultado.status_code}. '
    f'Resposta: {resultado.text}'
)

# Testando o título
assert resultado.json()['titulo'] == curso_atualizado['titulo']

print('Teste executado com sucesso!')


# import requests
#
# headers = {'Authorization': 'Token ae43728eab9e68cbf9b156f888cfaee7f89d4925'}
# url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
# url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'
#
#
# curso_atualizado = {
#     "titulo": "Novo Curso de Scrum 3",
#     "url": "http://www.geekuniversity.com.br/ncs3"
# }
#
# # Buscando o curso com ID 6
# # curso = requests.get(url=f'{url_base_cursos}6/', headers=headers)
# # print(curso.json())
#
#
# resultado = requests.put(url=f'{url_base_cursos}6/', headers=headers, data=curso_atualizado)
#
#
# # Testando o código de status HTTP
# assert resultado.status_code == 200
#
# # Testando o título
# assert resultado.json()['titulo'] == curso_atualizado['titulo']
#
