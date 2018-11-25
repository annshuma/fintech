# coding: utf8
import json


def test_success_get_subscription(http_client):
    """
    1. Send request to get subscriptions
    2. Check response status code is 200
    3. Check response content-length > 0
     """

    get_response = http_client.get_subscriptions(siebel_id ='shumeyko' , request_id='1',
                                                 system_code='2')  # GET subscription method

    assert get_response.status_code == 200
    assert get_response.headers['content-length'] > '0'