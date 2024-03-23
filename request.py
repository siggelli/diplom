import requests
import configuration


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)


def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS + track)