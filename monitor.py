import requests
from playwright.sync_api import sync_playwright

# ======================
SCKEY = "SCT366877TkcjPwBYTLfxaz5oD3jF8Xru6"
KEYWORDS = [
    "王国之泪 switch",
    "勇者斗恶龙I&II switch"
]
MAX_PRICE = 300
# ======================




def send_wechat(title, content):
    url = f"https://sctapi.ftqq.com/{SCKEY}.send"
    requests.post(url, data={"title": title, "desp": content})


# ======================
# 稳定抓取（增强版）
# ======================
def fetch_items(keyword):
    import requests
    import re

    url = f"https://www.goofish.com/search?q={keyword}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        r = requests.get(url, headers=headers, timeout=10)
        text = r.text

        # 抓价格
        prices = re.findall(r"¥\s?(\d+\.?\d*)", text)

        items = []
        for p in prices[:20]:
            try:
                price = float(p)
                items.append({
                    "title": keyword,
                    "price": price,
                    "url": url
                })
            except:
                continue

        return items

    except Exception as e:
        print("fetch error:", e)
        return []


# ======================
# 主逻辑（稳定版）
# ======================
def run():
    result_map = {}
    debug_log = []

    for kw in KEYWORDS:
        items = fetch_items(kw)

        debug_log.append(f"{kw} → {len(items)}条")

        if not items:
            continue

        min_item = min(items, key=lambda x: x["price"])
        result_map[kw] = min_item

    # ======================
    # 🔥 保底机制（防空消息）
    # ======================
    if not result_map:
        send_wechat(
            "⚠️ 闲鱼监控提醒",
            "本次未抓到任何有效数据\n\n可能原因：\n- 页面结构变化\n- 网络延迟\n- 被风控\n\n调试信息：\n" + "\n".join(debug_log)
        )
        return

    # ======================
    # 正常内容拼接
    # ======================
    content = "🔥 闲鱼多商品最低价（稳定版）\n\n"

    for kw, item in result_map.items():
        content += f"""
🎮 {kw}
💰 ¥{item['price']}
📌 {item['title']}
🔗 {item.get('url','')}

------------------
"""

    content += "\n📊 调试信息：\n" + "\n".join(debug_log)

    send_wechat("🎯 闲鱼稳定监控", content)


if __name__ == "__main__":
    run()
