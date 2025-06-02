import configuration
import requests
import data
"""
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers_user)  # inserta los encabezados
"""

def post_new_user_token():
    response= requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=data.user_body,  # inserta el cuerpo de solicitud
                         headers=data.headers_user)  # inserta los encabezados
    token = response.json()['authToken'] #obtenemos el valor de la clave authtoken que nos devuelve el servidor
    return token

def post_new_kit(kit_body, auth_token):
    headers = data.headers_kit.copy()
    headers["Authorization"] = f"Bearer {auth_token}"

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)

def body_kit_modificable(name):
    new_body = data.kit_body.copy()
    new_body["name"] = name
    return new_body

def create_kit(name):
    return post_new_kit(body_kit_modificable(name),post_new_user_token())