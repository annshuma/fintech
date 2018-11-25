"""Module with fixture and hooks for Investment API"""
import pytest
from packages.http_client.http_client import HttpClient
from packages.find_parametr.find_parametr import FindParametr


@pytest.fixture(scope="function")
def http_client():
    """Client to work with HTTP requests"""
    return HttpClient()


@pytest.fixture(scope="function")
def find_parametr():
    """Client to find parametrs in response"""
    return FindParametr()