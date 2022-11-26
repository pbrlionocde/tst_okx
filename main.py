from src.api_wrappers.clients.account import OkxAccountClient
from src.api_wrappers.clients.market import OkxMarketClient
from src.api_wrappers.clients.public_data import OkxPublicDataClient


if __name__ == '__main__':
    # Public data client test
    public_client = OkxPublicDataClient()

    resp = public_client.get_instruments()
    for instrument in resp:
        if 'ETH' in instrument.inst_id:
            print('Instrument id:', instrument.inst_id)
            inst_id = instrument.inst_id
            break
    # init instance of OKX client
    account = OkxAccountClient()
    market = OkxMarketClient()
    balance = account.get_account_balance()
    balance
    details = balance.data[0].details[0]
    print('Balance', details.ccy, ':', details.avail_eq)

    resp = market.get_market_price(inst_id=inst_id, load=True)
    print(resp.dump())
    print(resp.mark_px)


