import requests
from requests import Response

import requests
from requests import Response

def ensure_200_and_return_content(response: Response) -> dict:
    if response.status_code != requests.codes.ok:
        raise response.raise_for_status()
    return response.json()

def get_from_cache_or_api(cache, name: str, url: str):
    if name in cache:
        return cache[name]
    else:
        response = ensure_200_and_return_content(requests.get(url))
        cache[name] = response.json()
        return cache[name]