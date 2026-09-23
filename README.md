# hashkey-python
Python SDK (sync and async) for Hashkey cryptocurrency exchange with Rest and WS capabilities.

- You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/hashkey)
- You can check Hashkey's docs here: [Docs](https://www.google.com/search?q=google+hashkey+cryptocurrency+exchange+api+docs)
- Github repo: https://github.com/ccxt/hashkey-python
- Pypi package: https://pypi.org/project/hashkey


## Installation

```
pip install hashkey
```

## Usage

### Sync

```Python
from hashkey import HashkeySync

def main():
    instance = HashkeySync({})
    ob =  instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = instance.fetch_balance()
    # order = instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

main()
```

### Async

```Python
import sys
import asyncio
from hashkey import HashkeyAsync

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = HashkeyAsync({})
    ob =  await instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = await instance.fetch_balance()
    # order = await instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```



### Websockets

```Python
import sys
from hashkey import HashkeyWs

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = HashkeyWs({})
    while True:
        ob = await instance.watch_order_book("BTC/USDC")
        print(ob)
        # orders = await instance.watch_orders("BTC/USDC")

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```





#### Raw call

You can also construct custom requests to available "implicit" endpoints

```Python
        request = {
            'type': 'candleSnapshot',
            'req': {
                'coin': coin,
                'interval': tf,
                'startTime': since,
                'endTime': until,
            },
        }
        response = await instance.public_post_info(request)
```


## Available methods

### REST Unified

- `create_market_buy_order_with_cost(self, symbol: str, cost: float, params: dict = {})`
- `create_order_request(self, symbol: Str, type: Str, side: Str, amount: Num, price: Num = None, params: dict = {})`
- `create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params: dict = {})`
- `create_orders(self, orders: list[OrderRequest], params: dict = {})`
- `create_spot_order_request(self, symbol: Str, type: Str, side: Str, amount: Num, price: Num = None, params: dict = {})`
- `create_spot_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params: dict = {})`
- `create_swap_order_request(self, symbol: Str, type: Str, side: Str, amount: Num, price: Num = None, params: dict = {})`
- `create_swap_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params: dict = {})`
- `fetch_accounts(self, params: dict = {})`
- `fetch_balance(self, params: dict = {})`
- `fetch_canceled_and_closed_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params: dict = {})`
- `fetch_currencies(self, params: dict = {})`
- `fetch_deposit_address(self, code: str, params: dict = {})`
- `fetch_deposits(self, code: Str = None, since: Int = None, limit: Int = None, params: dict = {})`
- `fetch_funding_rate_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params: dict = {})`
- `fetch_funding_rate(self, symbol: str, params={})`
- `fetch_funding_rates(self, symbols: Strings = None, params: dict = {})`
- `fetch_last_prices(self, symbols: Strings = None, params: dict = {})`
- `fetch_ledger(self, code: Str = None, since: Int = None, limit: Int = None, params: dict = {})`
- `fetch_leverage_tiers(self, symbols: Strings = None, params: dict = {})`
- `fetch_leverage(self, symbol: str, params: dict = {})`
- `fetch_markets(self, params: dict = {})`
- `fetch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params: dict = {})`
- `fetch_ohlcv(self, symbol: str, timeframe: str = '1m', since: Int = None, limit: Int = None, params: dict = {})`
- `fetch_open_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params: dict = {})`
- `fetch_open_spot_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params: dict = {})`
- `fetch_open_swap_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params: dict = {})`
- `fetch_order_book(self, symbol: str, limit: Int = None, params: dict = {})`
- `fetch_order(self, id: str, symbol: Str = None, params: dict = {})`
- `fetch_positions_for_symbol(self, symbol: str, params: dict = {})`
- `fetch_positions(self, symbols: Strings = None, params: dict = {})`
- `fetch_status(self, params: dict = {})`
- `fetch_ticker(self, symbol: str, params: dict = {})`
- `fetch_tickers(self, symbols: Strings = None, params: dict = {})`
- `fetch_time(self, params: dict = {})`
- `fetch_trades(self, symbol: str, since: Int = None, limit: Int = None, params: dict = {})`
- `fetch_trading_fee(self, symbol: str, params: dict = {})`
- `fetch_trading_fees(self, params: dict = {})`
- `fetch_withdrawals(self, code: Str = None, since: Int = None, limit: Int = None, params: dict = {})`
- `add_margin(self, symbol: str, amount: float, params: dict = {})`
- `cancel_all_orders(self, symbol: Str = None, params: dict = {})`
- `cancel_order(self, id: str, symbol: Str = None, params: dict = {})`
- `cancel_orders(self, ids: list[str], symbol: Str = None, params: dict = {})`
- `check_type_param(self, methodName: str, params: dict)`
- `custom_urlencode(self, params: dict = {})`
- `describe(self)`
- `encode_account_type(self, type: object)`
- `encode_flow_type(self, type: object)`
- `modify_margin_helper(self, symbol: str, amount: Num, type: str, params: dict = {})`
- `reduce_margin(self, symbol: str, amount: float, params: dict = {})`
- `set_leverage(self, leverage: int, symbol: Str = None, params: dict = {})`
- `set_margin_mode(self, marginMode: str, symbol: Str = None, params: dict = {})`
- `transfer(self, code: str, amount: float, fromAccount: str, toAccount: str, params: dict = {})`
- `withdraw(self, code: str, amount: float, address: str, tag: Str = None, params: dict = {})`

### REST Raw

- `public_get_api_v1_exchangeinfo(request)`
- `public_get_quote_v1_depth(request)`
- `public_get_quote_v1_trades(request)`
- `public_get_quote_v1_klines(request)`
- `public_get_quote_v1_ticker_24hr(request)`
- `public_get_quote_v1_ticker_price(request)`
- `public_get_quote_v1_ticker_bookticker(request)`
- `public_get_quote_v1_depth_merged(request)`
- `public_get_quote_v1_markprice(request)`
- `public_get_quote_v1_index(request)`
- `public_get_api_v1_futures_fundingrate(request)`
- `public_get_api_v1_futures_historyfundingrate(request)`
- `public_get_api_v1_ping(request)`
- `public_get_api_v1_time(request)`
- `private_get_api_v1_spot_order(request)`
- `private_get_api_v1_spot_openorders(request)`
- `private_get_api_v1_spot_tradeorders(request)`
- `private_get_api_v1_futures_leverage(request)`
- `private_get_api_v1_futures_order(request)`
- `private_get_api_v1_futures_openorders(request)`
- `private_get_api_v1_futures_usertrades(request)`
- `private_get_api_v1_futures_positions(request)`
- `private_get_api_v1_futures_historyorders(request)`
- `private_get_api_v1_futures_balance(request)`
- `private_get_api_v1_futures_liquidationassignstatus(request)`
- `private_get_api_v1_futures_risklimit(request)`
- `private_get_api_v1_futures_commissionrate(request)`
- `private_get_api_v1_futures_getbestorder(request)`
- `private_get_api_v1_coininfo(request)`
- `private_get_api_v1_account_vipinfo(request)`
- `private_get_api_v1_account(request)`
- `private_get_api_v1_account_trades(request)`
- `private_get_api_v1_account_type(request)`
- `private_get_api_v1_account_chaintype(request)`
- `private_get_api_v1_account_checkapikey(request)`
- `private_get_api_v1_account_balanceflow(request)`
- `private_get_api_v1_spot_subaccount_openorders(request)`
- `private_get_api_v1_spot_subaccount_tradeorders(request)`
- `private_get_api_v1_subaccount_trades(request)`
- `private_get_api_v1_futures_subaccount_openorders(request)`
- `private_get_api_v1_futures_subaccount_historyorders(request)`
- `private_get_api_v1_futures_subaccount_usertrades(request)`
- `private_get_api_v1_account_deposit_address(request)`
- `private_get_api_v1_account_depositorders(request)`
- `private_get_api_v1_account_withdraworders(request)`
- `private_get_api_v1_affiliate_inviteeinfo(request)`
- `private_post_api_v1_userdatastream(request)`
- `private_post_api_v1_spot_ordertest(request)`
- `private_post_api_v1_spot_order(request)`
- `private_post_api_v1_1_spot_order(request)`
- `private_post_api_v1_spot_batchorders(request)`
- `private_post_api_v1_futures_leverage(request)`
- `private_post_api_v1_futures_order(request)`
- `private_post_api_v1_futures_margintype(request)`
- `private_post_api_v1_futures_positionmargin(request)`
- `private_post_api_v1_futures_position_trading_stop(request)`
- `private_post_api_v1_futures_batchorders(request)`
- `private_post_api_v1_account_assettransfer(request)`
- `private_post_api_v1_account_authaddress(request)`
- `private_post_api_v1_account_withdraw(request)`
- `private_put_api_v1_userdatastream(request)`
- `private_delete_api_v1_spot_order(request)`
- `private_delete_api_v1_spot_openorders(request)`
- `private_delete_api_v1_spot_cancelorderbyids(request)`
- `private_delete_api_v1_spot_cancelallopenorders(request)`
- `private_delete_api_v1_futures_order(request)`
- `private_delete_api_v1_futures_batchorders(request)`
- `private_delete_api_v1_futures_cancelorderbyids(request)`
- `private_delete_api_v1_futures_cancelallopenorders(request)`
- `private_delete_api_v1_userdatastream(request)`

### WS Unified

- `describe(self)`
- `wath_public(self, market: Market, topic: str, messageHash: str, params: dict = {})`
- `watch_private(self, messageHash: object)`
- `get_private_url(self, listenKey: object)`
- `watch_ohlcv(self, symbol: str, timeframe: str = '1m', since: Int = None, limit: Int = None, params: dict = {})`
- `watch_ticker(self, symbol: str, params={})`
- `watch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `watch_order_book(self, symbol: str, limit: Int = None, params: dict = {})`
- `watch_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params: dict = {})`
- `watch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params: dict = {})`
- `watch_positions(self, symbols: Strings = None, since: Int = None, limit: Int = None, params: dict = {})`
- `watch_balance(self, params: dict = {})`
- `set_balance_cache(self, client: Client, type: str, subscribeHash: str)`
- `load_balance_snapshot(self, client: Client, messageHash: str, type: str)`
- `authenticate(self, params: dict = {})`
- `keep_alive_listen_key(self, listenKey: Str, params: dict = {})`

## Contribution
- Give us a star :star:
- Fork and Clone! Awesome
- Select existing issues or create a new issue.