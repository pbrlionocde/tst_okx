from api_wrappers.okx import OkxClient

if __name__ == '__main__':
    # init instance of OKX client
    client = OkxClient()

    resp = client.get_account_balance(demo=True)
    resp
