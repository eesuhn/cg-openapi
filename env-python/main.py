import test_coingecko_python

from test_coingecko_python.rest import ApiException
from _constant import (
    CG_DEMO_API_KEY,
    CG_PRO_API_KEY
)


def main():
    configuration = test_coingecko_python.Configuration(
        host = "https://api.coingecko.com/api/v3"
    )
    # configuration.api_key['proKeyAuth'] = CG_PRO_API_KEY
    configuration.api_key['demoKeyAuth'] = CG_DEMO_API_KEY
    with test_coingecko_python.ApiClient(configuration) as api_client:
        # get_networks_list(api_client)
        get_simple_supported_currencies(api_client)
        pass


def get_networks_list(api_client):
    api_instance = test_coingecko_python.NetworksApi(api_client)
    try:
        api_response = api_instance.networks_list()
        print(api_response.to_dict())
    except ApiException as e:
        print("Exception when calling NetworksApi->networks_list: %s\n" % e)


def get_simple_supported_currencies(api_client):
    api_instance = test_coingecko_python.SimpleApi(api_client)
    try:
        api_response = api_instance.simple_supported_currencies()
        print(api_response)
    except ApiException as e:
        print("Exception when calling SimpleApi->simple_supported_currencies: %s\n" % e)


if __name__ == "__main__":
    main()
