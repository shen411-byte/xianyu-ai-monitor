import requests

SCKEY = "你的Key"

print("🚀 Python started")

r = requests.post(
    f"https://sctapi.ftqq.com/{SCKEY}.send",
    data={"title": "测试", "desp": "GitHub已运行"}
)

print("状态码:", r.status_code)
print(r.text)
