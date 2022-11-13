from api_wrappers.okx import OkxClient


if __name__ == '__main__':
    # test initialization
    assert OkxClient.test_preview(), 'Wrong initialize BaseClient instance'

    # init instance of OKX client
    client = OkxClient()

    resp = client.get_account_balance()
    resp
