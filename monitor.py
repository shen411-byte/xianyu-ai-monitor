import requests

SCKEY = "SCT366877TkcjPwBYTLfxaz5oD3jF8Xru6"
KEYWORD = "王国之泪"
MAX_SCORE = 75

def send_wechat(title, content):
    url = f"https://sctapi.ftqq.com/{SCKEY}.send"
    requests.post(url, data={"title": title, "desp": content})


# ===== 模拟抓取（云端简化版，避免复杂浏览器）=====
def fetch_items():
    # 这里是“简化版数据源模拟”
    # 实际生产可升级为Playwright版本
    return [
        {"title": "Switch 王国之泪 完整盒装", "price": 240},
        {"title": "塞尔达 仅卡盒 无卡", "price": 180},
        {"title": "王国之泪 实拍 盒说全 急出", "price": 260},
    ]


def score(item):
    text = item["title"]
    price = item["price"]

    score = 50

    # 价格评分（假设合理价300）
    score += (300 - price) / 300 * 40

    # 风险扣分
    if "无卡" in text:
        score -= 40
    if "仅卡盒" in text:
        score -= 40
    if "数字版" in text:
        score -= 30

    # 加分
    if "实拍" in text:
        score += 10
    if "盒说全" in text:
        score += 10

    return min(100, max(0, score))


def run():
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
