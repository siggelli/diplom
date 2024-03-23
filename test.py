import request
import data


def get_track():
    response = request.post_new_order(data.order_body)
    track = response.json()['track']
    return str(track)


def test_positive_assert():
    track = get_track()
    order_response = request.get_order(track)
    assert order_response.status_code == 200




