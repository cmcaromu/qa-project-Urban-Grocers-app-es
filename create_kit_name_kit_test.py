import data
import requests
import sender_stand_request


def positive_assert(name):
    response = sender_stand_request.create_kit(name)

    assert response.status_code == 201
    assert response.json()['name'] == name

def negative_assert(name):
    response = sender_stand_request.create_kit(name)

    assert response.status_code == 400


def test_create_name_1_character():
    positive_assert("a")

def test_create_name_511_characters():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_create_name_with_0_smallest_amount_allowed ():
    negative_assert("")

def test_create_name_with_512_largest_amount_allowed ():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_create_name_with_special_characters():
    positive_assert("№%@,")

def test_create_name_with_space_allowed ():
    positive_assert("A Aaa ")

def test_create_name_with_numbers_allowed ():
    positive_assert("123")

def test_create_kit_without_name():
    response = sender_stand_request.create_kit_with_empty_body()
    assert response.status_code == 400

def test_create_name_with_diferent_parameter():
    negative_assert( 123 )