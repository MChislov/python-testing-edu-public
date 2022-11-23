test_url = "https://api.punkapi.com/v2/beers/8"

def test_get_success():
    get_request = requests.get(test_url)
    assert get_request.status_code == 200
    assert get_request.json()[0]['name'] == 'Fake Lager'
    assert get_request.json()[0]['abv'] == 4.7

def test_delete_failure():
    delete_request = requests.delete(test_url)
    assert delete_request.status_code == 404
    assert delete_request.json()['message'] == "No endpoint found that matches '/v2/beers/8'"
