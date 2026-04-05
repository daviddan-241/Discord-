import requests

# ---------------- DEXSCREENER ----------------
def scan_dexscreener():
    urls = [
        "https://api.dexscreener.com/latest/dex/pairs/solana",
        "https://api.dexscreener.com/latest/dex/pairs/ethereum",
        "https://api.dexscreener.com/latest/dex/pairs/base"
    ]

    results = []

    for url in urls:
        try:
            r = requests.get(url, timeout=10)

            if r.status_code != 200:
                print("DEX BAD STATUS:", r.status_code)
                continue

            data = r.json()
            pairs = data.get("pairs", [])

            for p in pairs[:25]:
                try:
                    liquidity = p.get("liquidity", {}).get("usd", 0)

                    if liquidity and liquidity > 3000:
                        results.append({
                            "source": "DexScreener",
                            "name": p["baseToken"]["name"],
                            "symbol": p["baseToken"]["symbol"],
                            "liq": liquidity,
                            "chain": p.get("chainId"),
                            "url": p["url"]
                        })
                except:
                    continue

        except Exception as e:
            print("DEX ERROR:", e)

    return results


# ---------------- GECKO TERMINAL ----------------
def scan_gecko():
    url = "https://api.geckoterminal.com/api/v2/networks/trending_pools"

    try:
        r = requests.get(url, timeout=10)

        if r.status_code != 200:
            print("GECKO BAD STATUS:", r.status_code)
            return []

        data = r.json()
        pools = data.get("data", [])

        results = []

        for p in pools[:20]:
            try:
                attr = p["attributes"]

                results.append({
                    "source": "GeckoTerminal",
                    "name": attr.get("name", "unknown"),
                    "symbol": "",
                    "liq": attr.get("reserve_in_usd", 0),
                    "chain": p.get("id"),
                    "url": attr.get("pool_address")
                })
            except:
                continue

        return results

    except Exception as e:
        print("GECKO ERROR:", e)
        return []


# ---------------- PUMP.FUN ----------------
def scan_pump_fun():
    url = "https://frontend-api.pump.fun/coins"

    try:
        r = requests.get(url, timeout=10)

        if r.status_code != 200:
            print("PUMP BAD STATUS:", r.status_code)
            return []

        data = r.json()

        results = []

        for c in data[:20]:
            try:
                results.append({
                    "source": "Pump.fun",
                    "name": c.get("name"),
                    "symbol": c.get("symbol"),
                    "liq": c.get("usd_market_cap", 0),
                    "chain": "solana",
                    "url": f"https://pump.fun/{c.get('mint')}"
                })
            except:
                continue

        return results

    except Exception as e:
        print("PUMP ERROR:", e)
        return []
