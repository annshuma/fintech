# coding: utf8
import json


def test_success_delete_subscription(http_client, find_parametr):
    """
    1. Send request to delete subscription.
    2. Check response status code is 200
    3. Check that the content-length = 0
     """

    tinkoff_company = {
        "instrument_id": "TCS_SPBXM",
        "sec_name": "TCS",
        "sec_type": "equity",
        "price_alert": 1000
    }

    create_response = http_client.create_subscriptions(siebel_id='shumeyko', request_id='1', system_code='2',
                                                       data_body=tinkoff_company)  # Create subscription

    create_id = find_parametr.find_id_post(create_response)  # find created subscription ID in POST response

    delete_data = http_client.delete_subscriptions(siebel_id='shumeyko', request_id='1',
                                                   system_code='2', create_id=create_id)  # Delete created subscription

    assert delete_data.status_code == 200
    assert delete_data.headers['content-length'] == '0'


def test_delete_subscription_is_not_found(http_client):
    """
    1. Send request to delete subscription is not found
    2. Check response status code is 404
     """
    create_id = 'ffd6583e-f008-11e8-926a-02a0d1954444'

    delete_data = http_client.delete_subscriptions(siebel_id='shumeyko', request_id='1',
                                                   system_code='2', create_id=create_id)  # Delete created subscription

    assert delete_data.status_code == 404
