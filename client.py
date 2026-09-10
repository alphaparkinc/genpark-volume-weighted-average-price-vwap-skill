class VWAPExecution:
    """
    Volume-Weighted Average Price (VWAP) Benchmark Calculator.
    VWAP = sum(price * volume) / sum(volume).
    """
    def __init__(self):
        self.cum_pv = 0.0
        self.cum_vol = 0.0

    def add_trade(self, price, volume):
        self.cum_pv += price * volume
        self.cum_vol += volume
        return self.cum_pv / self.cum_vol if self.cum_vol > 0 else 0.0
