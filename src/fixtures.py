import pytest
from config_functions import get_config_value

def get_config_value(config, key):
    return config.get(key, "Chave não encontrada")

@pytest.fixture
def config_dict():
    return {
        "host": "localhost",
        "port": 8080,
        "debug": True
    }

# Usando a fixture no teste
def test_get_config_value(config_dict):
    assert get_config_value(config_dict, "host") == "localhost"
    assert get_config_value(config_dict, "port") == 8080
    assert get_config_value(config_dict, "debug") is True
    assert get_config_value(config_dict, "missing_key") == "Chave não encontrada"

