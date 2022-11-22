from api_wrappers.clients.account import OkxAccountClient
from api_wrappers.clients.public_data import OkxPublicDataClient

if __name__ == '__main__':
    # init instance of OKX client
    # account = OkxAccountClient()

    # resp = account.get_account_balance()
    # resp
    # details = resp.data[0].details[0]
    # details

    # Public data client test
    public_client = OkxPublicDataClient()

    resp = public_client.get_instruments()
    resp
    for instrument in resp:
        if 'ETH' in instrument.inst_id:
            print(instrument.inst_id)
