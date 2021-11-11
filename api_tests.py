from http import HTTPStatus
from unittest import TestCase

import requests


class TestPetStoreApi(TestCase):
    base_url = 'https://petstore.swagger.io'

    def test_post_new_pet(self):
        """
        Test post request to add new pet
        """
        url = self.base_url + '/v2/pet'
        data = {
            "id": 0,
            "category": {
                "id": 5,
                "name": "my_pet"
            },
            "name": "dog_name",
            "photoUrls": [
                "test_photo_url"
            ],
            "tags": [
                {
                    "id": 5,
                    "name": "test_dog_tag"
                }
            ],
            "status": "available"
        }

        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        response_body = response.json()
        self.assertEqual(response_body["name"], 'dog_name', 'New pet dog_name not found')

    def test_put_pet(self):
        """
        Test put request to update existing pet
        """
        # Add new pet
        url = self.base_url + '/v2/pet'
        data = {
            "id": 555,
            "category": {
                "id": 1,
                "name": "my_test_pet"
            },
            "name": "pet_name",
            "photoUrls": [
                "test_photo_url"
            ],
            "tags": [
                {
                    "id": 2,
                    "name": "test_pet_tag"
                }
            ],
            "status": "available"
        }

        response_add = requests.post(url, json=data)
        self.assertEqual(response_add.status_code, HTTPStatus.OK)
        json_response_add = response_add.json()
        self.assertEqual(json_response_add["name"], 'pet_name', 'Incorrect pet name in add response')

        # Update existing pet
        url2 = self.base_url + '/v2/pet'
        data2 = {
            "id": 555,
            "category": {
                "id": 1,
                "name": "my_test_pet"
            },
            "name": "pet_test_name",
            "photoUrls": [
                "test_photo_url"
            ],
            "tags": [
                {
                    "id": 2,
                    "name": "test_pet_tag"
                }
            ],
            "status": "na"
        }
        response_update = requests.put(url2, json=data2)
        self.assertEqual(response_update.status_code, HTTPStatus.OK)
        json_response_update = response_update.json()
        self.assertEqual(json_response_update["name"], 'pet_test_name', 'Incorrect pet name in update response')

        # Get pet by ID
        url3 = self.base_url + '/v2/pet/555'
        response_get = requests.get(url3)
        self.assertEqual(response_get.status_code, HTTPStatus.OK)
        json_response_get = response_get.json()
        self.assertEqual(json_response_get["name"], 'pet_test_name', 'Incorrect pet name in get response')
        self.assertEqual(json_response_get["status"], 'na', 'Incorrect status in update response')

    def test_get_store_inventory(self):
        """
        Test get request to check inventory is not empty
        """
        url = self.base_url + '/v2/store/inventory'
        response = requests.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        response_body = response.json()
        self.assertTrue(response_body["available"] > 0, 'Items not found in inventory')

    def test_post_new_user(self):
        """
        Test post request to create new user
        """
        url = self.base_url + '/v2/user'
        data = {
                "id": 1,
                "username": "aroosha.arif",
                "firstName": "Aroosha",
                "lastName": "Arif",
                "email": "arooshaa17@gmail.com",
                "password": "newuser1",
                "phone": "+4912637878787",
                "userStatus": 1
            }

        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        response_body = response.json()
        self.assertEqual(response_body["message"], '1', 'Response body value is not 1')

    def test_get_user_by_username(self):
        """
        Test get request to get user by username
        """
        url = self.base_url + '/v2/user/aroosha.arif'
        response = requests.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        response_body = response.json()
        self.assertEqual(response_body["username"], 'aroosha.arif', 'User not found')
