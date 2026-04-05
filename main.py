import time
import requests

from keep_alive import keep_alive
from sources import scan_dexscreener, scan_gecko, scan_pump_fun

WEBHOOK = "https://discord.com/api/webhooks/1490137623577235497/ZzzvUp5fDvWuMwlWB8SVYyNe5KP70S3V7kpi5nefBSXi3eDxSy4CFQOzkvDXPT_F9WsJ"

seen = set()

# ---------------- SEND ----------------
def send(msg):
    try:
        requests.post(WEBHOOK, json={"content": msg}, timeout=10)
    except Exception as e:
        print("SEND ERROR:", e)

# ---------------- DEDUPE ----------------
def dedupe(item):
    key = item["name"]

    if key in seen:
        return False

    seen.add(key)
    return True

# ---------------- FORMAT ----------------
def format_item(item):
    return f"""🔥 {item['source']} ALERT

Name: {item['name']} ({item['symbol']})
Chain: {item['chain']}
Liquidity/MC: ${item['liq']}

{item['url']}
"""

# ---------------- RUN ----------------
def run_all():
    dex = scan_dexscreener()
    gecko = scan_gecko()
    pump = scan_pump_fun()

    print("DEX:", len(dex))
    print("GECKO:", len(gecko))
    print("PUMP:", len(pump))

    results = dex + gecko + pump

    for r in results:
        print("FOUND:", r)

        try:
            if not dedupe(r):
                continue

            send(format_item(r))

        except Exception as e:
            print("PROCESS ERROR:", e)

# ---------------- MAIN ----------------
def main():
    keep_alive()

    send("✅ Meme Radar PRO ONLINE (LIVE)")

    while True:
        try:
            run_all()
            time.sleep(90)
        except Exception as e:
            print("LOOP ERROR:", e)
            time.sleep(10)

main()
