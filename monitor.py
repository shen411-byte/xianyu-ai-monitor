import requests

# ====== 只改这里 ======
SCKEY = "SCT366877TkcjPwBYTLfxaz5oD3jF8Xru6"
KEYWORD = "王国之泪"
MAX_SCORE = 75
# ======================


def send_wechat(title, content):
    url = f"https://sctapi.ftqq.com/{SCKEY}.send"
    requests.post(url, data={"title": title, "desp": content})


def fetch_items():
    # 云端简化模拟数据（后面可升级真实闲鱼抓取）
    return [
        {"title": "Switch 王国之泪 盒说全 急出", "price": 260},
        {"title": "塞尔达 仅卡盒 无卡", "price": 180},
        {"title": "王国之泪 实拍 完整盒装", "price": 240},
    ]


def score(item):
    text = item["title"]
    price = item["price"]

    s = 50

    # 价格评分（假设均价300）
    s += (300 - price) / 300 * 40

    # 风险扣分
    if "无卡" in text:
        s -= 40
    if "仅卡盒" in text:
        s -= 40

    # 加分项
    if "实拍" in text:
        s += 10
    if "盒说全" in text:
        s += 10

    return max(0, min(100, s))


def run():
    print("🚀 running monitor...")

    items = fetch_items()

    best = None
    best_score = 0

    for item in items:
        s = score(item)
        if s > best_score:
            best_score = s
            best = item

    print("最高评分:", best_score)

    if best_score >= MAX_SCORE:
        send_wechat(
            "🔥 AI捡漏推荐",
            f"""
标题：{best['title']}
价格：¥{best['price']}
评分：{best_score}

AI判断：值得买 ✔
"""
        )


run()
