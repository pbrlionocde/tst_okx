from api_wrappers.okx import OkxClient
from pprint import pprint


if __name__ == '__main__':
    # init instance of OKX client
    client = OkxClient()

    resp = client.get_account_balance()
    t = client.parse_response(resp)
    pprint(t)
