from trading_view_wrapper.analyze import Analyzer

analyze_handler = Analyzer()
for res in analyze_handler():
    print(res)
