import pytest
import requests
import socket

from src.website_checker import is_website_online

class MockResponse:
    def __init__(self, status_code):
        self.status_code = status_code

def test_valid_online_website(monkeypatch):
    # Mock successful request
    def mock_head(*args, **kwargs):
        return MockResponse(200)
    
    # Mock DNS resolution
    def mock_gethostbyname(*args, **kwargs):
        return '8.8.8.8'
    
    monkeypatch.setattr(requests, 'head', mock_head)
    monkeypatch.setattr(socket, 'gethostbyname', mock_gethostbyname)
    
    assert is_website_online('google.com') is True

def test_website_with_redirect(monkeypatch):
    # Mock successful request with redirect
    def mock_head(*args, **kwargs):
        return MockResponse(302)
    
    # Mock DNS resolution
    def mock_gethostbyname(*args, **kwargs):
        return '8.8.8.8'
    
    monkeypatch.setattr(requests, 'head', mock_head)
    monkeypatch.setattr(socket, 'gethostbyname', mock_gethostbyname)
    
    assert is_website_online('example.com') is True

def test_offline_website(monkeypatch):
    # Mock request exception
    def mock_head(*args, **kwargs):
        raise requests.RequestException()
    
    # Mock DNS resolution failure
    def mock_gethostbyname(*args, **kwargs):
        raise socket.gaierror()
    
    monkeypatch.setattr(requests, 'head', mock_head)
    monkeypatch.setattr(socket, 'gethostbyname', mock_gethostbyname)
    
    assert is_website_online('nonexistent.website') is False

def test_invalid_url():
    with pytest.raises(ValueError):
        is_website_online('')
    
    with pytest.raises(ValueError):
        is_website_online(None)

def test_website_with_error_status(monkeypatch):
    # Mock error status code
    def mock_head(*args, **kwargs):
        return MockResponse(404)
    
    # Mock DNS resolution
    def mock_gethostbyname(*args, **kwargs):
        return '8.8.8.8'
    
    monkeypatch.setattr(requests, 'head', mock_head)
    monkeypatch.setattr(socket, 'gethostbyname', mock_gethostbyname)
    
    assert is_website_online('broken-website.com') is False