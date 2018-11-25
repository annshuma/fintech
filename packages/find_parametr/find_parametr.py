"""Module with class to find parametrs in response"""
import json


class FindParametr(object):
    "Class to find parametrs in response"


    def find_id_post(self, response):

        rs_body = response.text

        create_json = json.loads(rs_body)

        find_id_response_post = create_json['id']

        return find_id_response_post


    def find_id_get(self, response):

        rs_body = response.text

        create_json = json.loads(rs_body)

        find_id_response_get = create_json[0]['id']

        return find_id_response_get


    def find_price(self, response):

        rs_body = response.text

        create_json = json.loads(rs_body)

        find_id_response_get = create_json[0]['price_alert']

        return find_id_response_get