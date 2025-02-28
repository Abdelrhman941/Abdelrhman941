import requests
import os

# بيانات المستودع الخاص بك
OWNER = "Abdelrhman941"  # استبدل باسم المستخدم الخاص بك
REPO = "Abdelrhman941"   # استبدل باسم المستودع الخاص بك
TOKEN = os.getenv("GH_TOKEN")  # التوكن من GitHub Secrets

# رابط API لجلب إحصائيات الزوار
URL = f"https://api.github.com/repos/{OWNER}/{REPO}/traffic/views"

# تنفيذ الطلب
headers = {"Authorization": f"token {TOKEN}"}
response = requests.get(URL, headers=headers)

# التحقق من نجاح الطلب
if response.status_code == 200:
    data = response.json()
    unique_visitors = data["uniques"]  # عدد الزوار الفريدين

    # تحديث ملف README.md
    with open("README.md", "r", encoding="utf-8") as file:
        content = file.read()

    new_content = content.replace("![Visitor Count](https://komarev.com/ghpvc/?username=Abdelrhman941&color=blue&style=flat)",  
                                  f"**👀 Real Visitors:** {unique_visitors}")

    with open("README.md", "w", encoding="utf-8") as file:
        file.write(new_content)
else:
    print("❌ فشل في جلب البيانات:", response.json())
