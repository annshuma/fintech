# coding: utf8
import json


def test_success_create_apple_subscription_integer(http_client, find_parametr):

    """
    1. Send request for creating a subscription to Apple company with an increase in the value of an integer
    2. Check response status code is 200
    3. Check created subscription ID in GET /contacts/{siebel_id}/subscriptions
    4. Delete created subscription
    """

    apple_company = {
        "instrument_id": "AAPL_SPBXM",
        "sec_name": "AAPL",
        "sec_type": "equity",
        "price_alert": 200
    }

    create_response = http_client.create_subscriptions(siebel_id = 'shumeyko', request_id = '1', system_code = '2',
                                                       data_body = apple_company) # Create subscription

    create_id = find_parametr.find_id_post(create_response)   # find created subscription ID in POST response

    get_response = http_client.get_subscriptions(siebel_id = 'shumeyko', request_id = '1',
                                                 system_code = '2')  # GET subscription method

    get_id = find_parametr.find_id_get(get_response) # find created subscription ID in GET response

    assert create_response.status_code == 200
    assert create_id == get_id

    delete_data = http_client.delete_subscriptions(siebel_id = 'shumeyko', request_id = '1', system_code = '2',
                                                   create_id = create_id)  # Delete created subscription



def test_success_create_tinkoff_subscription_float(http_client, find_parametr):

    """
    1. Send request for creating a subscription to Tinkoff.ru company with an increase for the sum with a penny
    2. Check response status code is 200
    3. Check created subscription ID in GET /contacts/{siebel_id}/subscriptions
    4. Delete created subscription
    """

    tinkoff_company = {
        "instrument_id": "TCS_SPBXM",
        "sec_name": "TCS",
        "sec_type": "equity",
        "price_alert": 10.25
    }

    create_response = http_client.create_subscriptions(siebel_id = 'shumeyko', request_id = '1', system_code = '2',
                                                       data_body = tinkoff_company) # Create subscription

    create_id = find_parametr.find_id_post(create_response)   # find created subscription ID in POST response

    get_response = http_client.get_subscriptions(siebel_id = 'shumeyko', request_id = '1', system_code = '2')  # GET subscription method

    get_id = find_parametr.find_id_get(get_response) # find created subscription ID in GET response

    assert create_response.status_code == 200
    assert create_id == get_id

    delete_data = http_client.delete_subscriptions(siebel_id = 'shumeyko', request_id = '1',
                                                   system_code = '2', create_id = create_id)  # Delete created subscription


def test_check_subscription_price(http_client, find_parametr):

    """
    1. Create a subscription to Gazprom company with 100
    2. Check response status code is 200
    3. Create a subscription to Gazprom company with 200
    4. Check subscription price in GET /contacts/{siebel_id}/subscriptions
    5. Delete created subscription
    """

    gazprom_company = {
        "instrument_id": "GAZP_TQBR",
        "sec_name": "GAZP",
        "sec_type": "equity",
        "price_alert": 100
    }

    create_response1 = http_client.create_subscriptions(siebel_id = 'shumeyko', request_id = '1', system_code = '2',
                                                       data_body = gazprom_company) # Create subscription with 100

    gazprom_company = {
        "instrument_id": "GAZP_TQBR",
        "sec_name": "GAZP",
        "sec_type": "equity",
        "price_alert": 200
    }

    create_response2 = http_client.create_subscriptions(siebel_id='shumeyko', request_id='1', system_code='2',
                                                       data_body=gazprom_company)  # Create subscription with 200

    create_id = find_parametr.find_id_post(create_response2)  # find  subscription ID in GET response

    get_response = http_client.get_subscriptions(siebel_id = 'shumeyko', request_id = '1', system_code = '2')  # GET subscription method

    get_price = find_parametr.find_price(get_response) # find  subscription Price in GET response

    assert create_response1.status_code == 200
    assert create_response2.status_code == 200
    assert get_price == 200

    delete_data = http_client.delete_subscriptions(siebel_id = 'shumeyko', request_id = '1',
                                                   system_code = '2', create_id = create_id)  # Delete created subscription



def test_create_subscription_without_instrument_id(http_client):
    """
    1. Create a subscription to Tinkoff company without instrument_id
    2. Check response status code is 404
    """

    gazprom_company = {
        "sec_name": "TCS",
        "sec_type": "equity",
        "price_alert": 100
    }

    create_response = http_client.create_subscriptions(siebel_id='shumeyko', request_id='1', system_code='2',
                                                        data_body=gazprom_company)  # Create subscription without instrument_id

    assert create_response.status_code == 400