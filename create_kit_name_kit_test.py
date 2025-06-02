import data
import requests
import sender_stand_request


def possitive_assert(name):
    response = sender_stand_request.create_kit(name)

    assert response.status_code == 201
    assert response.json()['name'] == name

def negative_assert(name):
    response = sender_stand_request.create_kit(name)

    assert response.status_code == 400


def test():
    possitive_assert("a")


