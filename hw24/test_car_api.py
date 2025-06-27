import pytest
import requests
import logging

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(
    filename='test_search.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'
)

logger = logging.getLogger(__name__)

BASE_URL = 'http://127.0.0.1:8080'

@pytest.mark.usefixtures("get_auth_cars_api_token")
class TestCarApi:


    @pytest.mark.parametrize("sort_by, limit", [
        ("price", 5),
        ("year", 3),
        ("engine", 10),
        ("brand", 7),
        ("price", None),
        (None, 4),
        (None, None)
    ])
    def test_car_search(self, get_auth_cars_api_token, sort_by, limit):
        url = f"{BASE_URL}/cars"
        headers = {
                "Authorization": f"Bearer {get_auth_cars_api_token}"
            }
        params = {
            "sort_by": sort_by,
            "limit": limit
        }
        response = requests.get(url=url, headers=headers, params=params)
        logger.info(f"GET /cars | sort_by={sort_by} | limit={limit} | status={response.status_code}")
        assert response.status_code == 200



