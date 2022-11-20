from api_wrappers.clients.account import OkxAccountClient

if __name__ == '__main__':
    # init instance of OKX client
    account = OkxAccountClient()

    resp = account.get_account_balance()
    resp
    details = resp.data[0].details[0]
    details
