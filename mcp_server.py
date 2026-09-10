import sys
import json
from client import VWAPExecution

vwap = VWAPExecution()

def handle_call(name, arguments):
    if name == "add_trade":
        px = arguments["price"]
        vol = arguments["volume"]
        res = vwap.add_trade(px, vol)
        return {"vwap": res, "total_volume": vwap.cum_vol}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
