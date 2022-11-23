from api_wrappers.clients.account import OkxAccountClient
from api_wrappers.clients.market import OkxMarketClient
from api_wrappers.clients.public_data import OkxPublicDataClient


# init instance of OKX client
def okx_balance():
    account = OkxAccountClient()
    balance = account.get_account_balance()
    details = balance.data[0].details[0]
    print('Balance', details.ccy, ':', details.avail_eq)

    # market = OkxMarketClient()
    # resp = market.get_market_price(load=True)
    # print(resp.mark_px)

    # # Public data client test
    # public_client = OkxPublicDataClient()

    # resp = public_client.get_instruments()
    # for instrument in resp:
    #     if 'ETH' in instrument.inst_id:
    #         print('Instrument id:', instrument.inst_id)


if __name__ == '__main__':
    okx_balance()
