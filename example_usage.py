from client import VWAPExecution

def main():
    print("=== Testing VWAP Benchmark Calculator ===")
    vwap = VWAPExecution()

    vwap.add_trade(150.0, 100)
    current_vwap = vwap.add_trade(152.0, 300)

    print("Calculated VWAP:", current_vwap)
    # (150*100 + 152*300) / 400 = (15000 + 45600) / 400 = 151.5
    assert current_vwap == 151.5
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
