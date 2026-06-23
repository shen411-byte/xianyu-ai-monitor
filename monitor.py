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


# ===== 真实闲鱼抓取 =====
def fetch_items(keyword):
    url = f"https://www.goofish.com/search?q={keyword}"

    items = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url)
        page.wait_for_timeout(5000)

        # ⚠️ 闲鱼页面结构可能变，这里是“通用抓法”
        cards = page.query_selector_all("a")

        for c in cards:
            try:
                text = c.inner_text()

                if "¥" not in text:
                    continue

                price_part = text.split("¥")[-1].split("\n")[0]
                price = float(price_part.replace(",", "").strip())

                if price <= 0:
                    continue

                items.append({
                    "title": text[:80],
                    "price": price,
                    "url": c.get_attribute("href")
                })
            except:
                continue

        browser.close()

    return items


# ===== 主逻辑：多商品独立最低价 =====
def run():
    result_map = {}

    for kw in KEYWORDS:
        items = fetch_items(kw)

        if not items:
            continue

        min_item = min(items, key=lambda x: x["price"])
        result_map[kw] = min_item

    # ===== 拼微信内容 =====
    content = "🔥 闲鱼多商品最低价监控\n\n"

    for kw, item in result_map.items():
        content += f"""
🎮 {kw}
💰 最低价：¥{item['price']}
📌 {item['title']}
🔗 {item.get('url','')}

------------------
"""

    send_wechat("🎯 闲鱼实时最低价", content)


if __name__ == "__main__":
    run()
