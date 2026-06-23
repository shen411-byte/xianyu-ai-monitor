import requests

# ====== 只改这里 ======
SCKEY = "SCT366877TkcjPwBYTLfxaz5oD3jF8Xru6"

MAX_SCORE = 60
# ======================


def run():
    KEYWORDS = [
        "王国之泪 switch",
        "勇者斗恶龙I&II switch"

    ]

    result_map = {}

    for kw in KEYWORDS:
        items = fetch_items(kw)

        if not items:
            continue

        min_item = min(items, key=lambda x: x["price"])
        result_map[kw] = min_item

    content = "🔥 各商品最低价汇总\n\n"

    for kw, item in result_map.items():
        content += f"""
🎮 {kw}
💰 最低价：¥{item['price']}
📌 {item['title']}
🔗 {item.get('url','')}

-------------------
"""

    send_wechat("🎯 多商品最低价监控", content)
