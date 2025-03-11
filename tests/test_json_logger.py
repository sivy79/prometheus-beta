import pytest
import logging
import json
from src.json_logger import log_json

class MockLogger:
    def __init__(self):
        self.logged_messages = []

    def debug(self, msg):
        self.logged_messages.append(('debug', msg))

    def info(self, msg):
        self.logged_messages.append(('info', msg))

    def warning(self, msg):
        self.logged_messages.append(('warning', msg))

    def error(self, msg):
        self.logged_messages.append(('error', msg))

    def critical(self, msg):
        self.logged_messages.append(('critical', msg))

def test_log_json_default():
    test_dict = {"name": "John", "age": 30}
    result = log_json(test_dict)
    assert json.loads(result) == test_dict

def test_log_json_with_custom_logger():
    mock_logger = MockLogger()
    test_dict = {"key": "value"}
    
    result = log_json(test_dict, logger=mock_logger, log_level='info')
    
    assert len(mock_logger.logged_messages) == 1
    assert mock_logger.logged_messages[0][0] == 'info'
    assert json.loads(mock_logger.logged_messages[0][1]) == test_dict

def test_log_json_different_log_levels():
    log_levels = ['debug', 'info', 'warning', 'error', 'critical']
    test_dict = {"test": "data"}

    for level in log_levels:
        mock_logger = MockLogger()
        result = log_json(test_dict, logger=mock_logger, log_level=level)
        
        assert len(mock_logger.logged_messages) == 1
        assert mock_logger.logged_messages[0][0] == level
        assert json.loads(mock_logger.logged_messages[0][1]) == test_dict

def test_log_json_invalid_input():
    with pytest.raises(TypeError):
        log_json("not a dictionary")

    with pytest.raises(TypeError):
        log_json(123)

def test_log_json_invalid_log_level():
    test_dict = {"key": "value"}
    with pytest.raises(ValueError):
        log_json(test_dict, log_level='invalid_level')

def test_log_json_complex_object():
    complex_dict = {
        "name": "Complex Object",
        "nested": {
            "a": 1,
            "b": [1, 2, 3]
        },
        "list": ["item1", "item2"]
    }
    result = log_json(complex_dict)
    assert json.loads(result) == complex_dict