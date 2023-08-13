import pytest
from fastapi.testclient import TestClient

from fastapi_tutorial.l40_testing.main import app
from fastapi_tutorial.l40_testing.main import (
    ERROR_MSG_INVALID_TOKEN, ERROR_MSG_EXISTENT_ITEM)


@pytest.fixture()
def test_client() -> TestClient:
    return TestClient(app)


def test_read_main(test_client: TestClient) -> None:
    response = test_client.get('/')

    assert response.status_code == 200
    assert response.json() == {"msg": "Hello world!"}


@pytest.mark.parametrize(
    'item_id,x_token,expected_http_status_code,expected_json',
    [
        pytest.param(
            'foo',
            'coneofsilence',
            200,
            {'id': 'foo', 'title': 'Foo', 'description': 'There goes my hero'},
            id='success'),
        pytest.param(
            'foo',
            'blablabla',
            400,
            {'detail': ERROR_MSG_INVALID_TOKEN},
            id='invalid token'),
        pytest.param(
            'furfles',
            'coneofsilence',
            404,
            {'detail': 'No item with id: furfles'},
            id='Nonexistent Item')
    ])
def test_read_item(
        test_client: TestClient,
        item_id: str,
        x_token: str,
        expected_http_status_code: int,
        expected_json: dict) -> None:
    response = test_client.get(
        f'/items/{item_id}', headers={'X-Token': f'{x_token}'})

    assert response.status_code == expected_http_status_code
    assert response.json() == expected_json


@pytest.mark.parametrize(
    'item,x_token,expected_http_status_code,expected_json',
    [
        pytest.param(
            {
                'id': 'pamonha',
                'title': 'Pamanha',
                'description': 'Pamonha quentinha'
            },
            'coneofsilence',
            200,
            {
                'id': 'pamonha',
                'title': 'Pamanha',
                'description': 'Pamonha quentinha'
            },
            id='success'),
        pytest.param(
            {
                'id': 'pamonha',
                'title': 'Pamanha',
                'description': 'Pamonha quentinha'
            },
            'coneofsilence',
            400,
            {'detail': ERROR_MSG_EXISTENT_ITEM},
            id='replay - already existent item'),
        pytest.param(
            {
                'id': 'soap',
                'title': 'Soap',
                'description': 'Soap Bubbles'
            },
            'malicioustoken',
            400,
            {'detail': ERROR_MSG_INVALID_TOKEN},
            id='invalid token')
    ])
def test_create_item(
        test_client: TestClient,
        item: dict,
        x_token: str,
        expected_http_status_code: int,
        expected_json) -> None:
    response = test_client.post(
        '/items/',
        headers={'X-Token': x_token},
        json=item)

    assert response.status_code == expected_http_status_code
    assert response.json() == expected_json
