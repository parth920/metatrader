
import MetaTrader5 as mt5
import pandas as pd
import time
from django.shortcuts import render



def initialize_mt5():
    if not mt5.initialize():
        return False, mt5.last_error()
    return True, None

def login_mt5(login, password, server):
    authorized = mt5.login(login, password=password, server=server)
    if authorized:
        account_info = mt5.account_info()
        if account_info is not None:
            account_info_dict = account_info._asdict()
            account_id = account_info_dict.get('login')
            df = pd.DataFrame(list(account_info_dict.items()), columns=['property', 'value'])
            print(df)
            return True, df,account_id
    return False, None,None





def shutdown_mt5():
    mt5.shutdown()


def get_initial_price(symbol, order_type):
    return mt5.symbol_info_tick(symbol).ask if order_type == mt5.ORDER_TYPE_BUY else mt5.symbol_info_tick(symbol).bid


def place_order(symbol, lot_size, order_type, trading_params):
    price = mt5.symbol_info_tick(symbol).ask if order_type == mt5.ORDER_TYPE_BUY else mt5.symbol_info_tick(symbol).bid

    sl = 0.0 #price + float(trading_params['sl_point']) if order_type == mt5.ORDER_TYPE_SELL else 0.0
    tp = price + float(trading_params['tp_point']) if order_type == mt5.ORDER_TYPE_BUY else price - float(trading_params['tp_point'])

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot_size,
        "type": order_type,
        "price": price,
        "sl": sl,  # Optional: Stop Loss
        "tp": tp,  # Optional: Take Profit
        "deviation": 20,  # Optional: Deviation from current price
        "magic": 234000,  # Optional: Magic number for the order
        "comment": "Python API Order",
        "type_time": mt5.ORDER_TIME_GTC,  # Good Till Cancel
        "type_filling": mt5.ORDER_FILLING_IOC,  # Immediate or Cancel
    }

    print(f"Placing order: {'SELL' if order_type == mt5.ORDER_TYPE_SELL else 'BUY'} at price {price}")

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Order failed at price {price}, retcode={result.retcode}")
        print(f"Reason:  {result.comment}")
        return False, result
    else:
        execution_price = round(result.price, 3)  # Get the actual execution price from the order result
        order_type_str = "buy" if order_type == mt5.ORDER_TYPE_BUY else "sell"
        print(f"{order_type_str.capitalize()} order placed at execution price {execution_price}: ticket={result.order}: Total Orders={len(mt5.positions_get(symbol=symbol))}\n")
        return True, result
    
