import sys
import hashkey.ccxt as ccxt_module
sys.modules['ccxt'] = ccxt_module

from hashkey.ccxt import hashkey as HashkeySync
from hashkey.ccxt.async_support.hashkey import hashkey as HashkeyAsync
from hashkey.ccxt.pro.hashkey import hashkey as HashkeyWs
