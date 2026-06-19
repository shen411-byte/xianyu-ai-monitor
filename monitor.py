import requests

SCKEY = "SCT366877TkcjPwBYTLfxaz5oD3jF8Xru6"

print("🚀 Python started")

r = requests.post(
    f"https://sctapi.ftqq.com/{SCKEY}.send",
    data={"title": "测试", "desp": "GitHub已运行"}
)

print("状态码:", r.status_code)
print(r.text)
print("cron test wake")
