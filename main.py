from api_wrappers.clients.account import OkxAccountClient
from api_wrappers.clients.market import OkxMarketClient

if __name__ == '__main__':
    # init instance of OKX client
    account = OkxAccountClient()
    market = OkxMarketClient()
    resp = account.get_account_balance()
    resp
    details = resp.data[0].details[0]
    details
    resp = market.get_market_price(load=True)
    resp
