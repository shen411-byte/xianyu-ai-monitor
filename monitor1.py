import requests
import datetime
import os

SCKEY = "SCT366877TkcjPwBYTLfxaz5oD3jF8Xru6"


def send_wechat(title, content):
    url = f"https://sctapi.ftqq.com/{SCKEY}.send"
    requests.post(url, data={
        "title": title,
        "desp": content
    })


def main():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    event = os.getenv("GITHUB_EVENT_NAME", "unknown")
    ref = os.getenv("GITHUB_REF", "unknown")

    content = f"""
## 🧪 GitHub Actions 检测报告

- ⏱ 当前时间：{now}
- 🚀 触发方式：{event}
- 🌿 分支信息：{ref}

---

✔ 如果你看到这条消息：
说明 GitHub Actions 已正常运行
"""

    print(content)
    send_wechat("🧪 Actions检测成功", content)


if __name__ == "__main__":
    main()
