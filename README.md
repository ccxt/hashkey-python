# hashkey-python
Python SDK (sync and async) for Hashkey cryptocurrency exchange with Rest and WS capabilities.

You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/hashkey)
You can check Hashkey's docs here: [Docs](https://ccxt.com)


## Installation

```
pip install __PYTHON_PACKAGE_NAME__
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
```

### Async

```Python
import asyncio
from hashkey import HashkeyAsync

async def main():
    instance = HashkeyAsync({})
    ob =  await instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = await instance.fetch_balance()
    # order = await instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

asyncio.run(main())
```



### Websockets

```Python
from hashkey import HashkeyWs

async def main():
    instance = HashkeyWs({})
    while True:
        ob = await instance.watch_order_book("BTC/USDC")
        print(ob)
        # orders = await instance.watch_orders("BTC/USDC")
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

- `create_market_buy_order_with_cost(self, symbol: str, cost: float, params={})`
- `create_order_request(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_orders(self, orders: List[OrderRequest], params={})`
- `create_spot_order_request(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_spot_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_swap_order_request(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_swap_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `fetch_accounts(self, params={})`
- `fetch_balance(self, params={})`
- `fetch_canceled_and_closed_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_currencies(self, params={})`
- `fetch_deposit_address(self, code: str, params={})`
- `fetch_deposits(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_rate_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_rate(self, symbol: str, params={})`
- `fetch_funding_rates(self, symbols: Strings = None, params={})`
- `fetch_last_prices(self, symbols: Strings = None, params={})`
- `fetch_ledger(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_leverage_tiers(self, symbols: Strings = None, params={})`
- `fetch_leverage(self, symbol: str, params={})`
- `fetch_markets(self, params={})`
- `fetch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_ohlcv(self, symbol: str, timeframe='1m', since: Int = None, limit: Int = None, params={})`
- `fetch_open_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_open_spot_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_open_swap_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_order_book(self, symbol: str, limit: Int = None, params={})`
- `fetch_order(self, id: str, symbol: Str = None, params={})`
- `fetch_positions_for_symbol(self, symbol: str, params={})`
- `fetch_positions(self, symbols: Strings = None, params={})`
- `fetch_status(self, params={})`
- `fetch_ticker(self, symbol: str, params={})`
- `fetch_tickers(self, symbols: Strings = None, params={})`
- `fetch_time(self, params={})`
- `fetch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `fetch_trading_fee(self, symbol: str, params={})`
- `fetch_trading_fees(self, params={})`
- `fetch_withdrawals(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `cancel_all_orders(self, symbol: Str = None, params={})`
- `cancel_order(self, id: str, symbol: Str = None, params={})`
- `cancel_orders(self, ids: List[str], symbol: Str = None, params={})`
- `check_type_param(self, methodName, params)`
- `custom_urlencode(self, params: dict = {})`
- `describe(self)`
- `encode_account_type(self, type)`
- `encode_flow_type(self, type)`
- `set_leverage(self, leverage: Int, symbol: Str = None, params={})`
- `transfer(self, code: str, amount: float, fromAccount: str, toAccount: str, params={})`
- `withdraw(self, code: str, amount: float, address: str, tag=None, params={})`

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
- `private_get_api_v1_account_vipinfo(request)`
- `private_get_api_v1_account(request)`
- `private_get_api_v1_account_trades(request)`
- `private_get_api_v1_account_type(request)`
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
- `private_post_api_v1_userdatastream(request)`
- `private_post_api_v1_spot_ordertest(request)`
- `private_post_api_v1_spot_order(request)`
- `private_post_api_v1_1_spot_order(request)`
- `private_post_api_v1_spot_batchorders(request)`
- `private_post_api_v1_futures_leverage(request)`
- `private_post_api_v1_futures_order(request)`
- `private_post_api_v1_futures_position_trading_stop(request)`
- `private_post_api_v1_futures_batchorders(request)`
- `private_post_api_v1_account_assettransfer(request)`
- `private_post_api_v1_account_authaddress(request)`
- `private_post_api_v1_account_withdraw(request)`
- `private_put_api_v1_userdatastream(request)`
- `private_delete_api_v1_spot_order(request)`
- `private_delete_api_v1_spot_openorders(request)`
- `private_delete_api_v1_spot_cancelorderbyids(request)`
- `private_delete_api_v1_futures_order(request)`
- `private_delete_api_v1_futures_batchorders(request)`
- `private_delete_api_v1_futures_cancelorderbyids(request)`
- `private_delete_api_v1_userdatastream(request)`

### WS Unified

- `describe(self)`
- `wath_public(self, market: Market, topic: str, messageHash: str, params={})`
- `watch_private(self, messageHash)`
- `get_private_url(self, listenKey)`
- `watch_ohlcv(self, symbol: str, timeframe='1m', since: Int = None, limit: Int = None, params={})`
- `watch_ticker(self, symbol: str, params={})`
- `watch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `watch_order_book(self, symbol: str, limit: Int = None, params={})`
- `watch_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `watch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `watch_positions(self, symbols: Strings = None, since: Int = None, limit: Int = None, params={})`
- `watch_balance(self, params={})`
- `set_balance_cache(self, client: Client, type, subscribeHash)`
- `load_balance_snapshot(self, client, messageHash, type)`
- `authenticate(self, params={})`
- `keep_alive_listen_key(self, listenKey, params={})`

## Contribution
- Give us a star :star:
- Fork and Clone! Awesome
- Select existing issues or create a new issue.