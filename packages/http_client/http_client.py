"""Module with class to work with HTTP client"""
import requests
import json


class HttpClient(object):
    "Class to work with HTTP requests."

    def __init__(self):
        self.base_url = 'https://fintech-trading-qa.tinkoff.ru/v1/md/'
        self.headers = {'Authorization': 'Basic ZmludGVjaDoxcTJ3M2Uh'}


    def get_subscriptions(self, request_id, system_code, siebel_id):

        url = self.base_url + 'contacts/' + siebel_id + '/subscriptions?request_id=' + request_id + '&system_code=' + system_code

        response = requests.get(url, headers=self.headers)

        return response


    def create_subscriptions(self, request_id, system_code, siebel_id, data_body):

        url = self.base_url + 'contacts/' + siebel_id + '/subscriptions?request_id=' + request_id + '&system_code=' + system_code

        response = requests.post(url, headers=self.headers, data=json.dumps(data_body))

        return response


    def delete_subscriptions(self, request_id, system_code, siebel_id, create_id):

        url =  self.base_url + 'contacts/' + siebel_id + '/subscriptions/' + str(create_id) + '?request_id=' + request_id + '&system_code=' + system_code

        response = requests.delete(url, headers=self.headers)

        return response