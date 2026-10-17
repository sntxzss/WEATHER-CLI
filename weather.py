import httpx

geo_url = "https://geocoding-api.open-meteo.com/v1/search"
def find_city(name):
    responce = httpx.get(geo_url, params={"name": name, "count": 1}, timeout=10)
    responce.raise_for_status()
    results = responce.json().get("results")
    if not results:
        return None
    return results[0]