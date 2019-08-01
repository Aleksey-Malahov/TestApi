'''Поиск населенных пунктов доставки по наименованию'''

'''Описание ответа
id – id населенного пункта
title – Наименование населенного пункта
cached_path – Принадлежность к региону
meta: total – количество найденных записей'''

import requests
import pytest
import json

# '''URL запроса'''
# baseURL = https://api.exline.systems/public/v1/regions/destination
#
#
# '''Запрос GET'''
# https://api.exline.systems/public/v1/regions/origin?title=АстGET

@pytest.fixture()
def api_region():
    """URI для создания операции."""
    api_method = 'https://api.exline.systems/public/v1/regions/origin?title=Аст'
    return api_method


@pytest.fixture
def response(api_region):
    """Производим GET запрос к API"""
    print(api_region)
    return requests.get(api_region)


def test_region(api_region):
    """HTTP-код ответа 200. Запрос успешен."""
    response = requests.get(api_region)
    parsed = json.loads(response.text, encoding='utf8')
    print(json.dumps(parsed, indent=4, ensure_ascii=False))
    assert response.status_code == 200


def test_cache_path(response):
    """В ответ получено запрошенное название cached_path"""
    print(response.json()["regions"][0]['cached_path'])
    assert response.json()["regions"][0]['cached_path'] == "Азербайджан, Азербайджан"


def test_title(response):
    """В ответ получено запрошенное название title"""
    print(response.json()["regions"][0]["title"])
    assert response.json()["regions"][0]["title"] == "Астара"


def test_zone(response):
    """В ответ получено запрошенное название Зоны"""
    print(response.json()["regions"][0]["zone"])
    assert response.json()["regions"][0]["zone"] == "ww_1"

