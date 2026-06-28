import MetaTrader5 as mt5

print("=" * 60)
print("MT5 Connection Test")
print("=" * 60)

if mt5.initialize():
    print("MT5 연결 성공")
    print("MT5 Version:", mt5.version())
    print("Terminal:", mt5.terminal_info().name)
    mt5.shutdown()
else:
    print("MT5 연결 실패")
    print(mt5.last_error())