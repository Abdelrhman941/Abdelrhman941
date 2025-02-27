import requests
import json
import os

# ✅ GitHub Username
USERNAME = "Abdelrhman941"  # غير ده لاسم المستخدم بتاعك
TOKEN = os.getenv("GITHUB_TOKEN")  # لازم تضيف التوكن في الـ Secrets

# ✅ روابط API
API_URL = f"https://api.github.com/users/{USERNAME}"
REPO_URL = f"https://api.github.com/users/{USERNAME}/repos"

# ✅ جلب البيانات من GitHub API
headers = {"Authorization": f"token {TOKEN}"}

def fetch_github_data():
    user_data = requests.get(API_URL, headers=headers).json()
    repos_data = requests.get(REPO_URL, headers=headers).json()

    repo_count = user_data.get("public_repos", 0)
    followers = user_data.get("followers", 0)
    following = user_data.get("following", 0)

    repo_names = [repo["name"] for repo in repos_data[:5]]  # آخر 5 مشاريع
    top_repos = "\n".join([f"- [{repo}](https://github.com/{USERNAME}/{repo})" for repo in repo_names])

    return repo_count, followers, following, top_repos

# ✅ تحديث ملف README.md
def update_readme():
    repo_count, followers, following, top_repos = fetch_github_data()

    with open("README.md", "r", encoding="utf-8") as file:
        readme_content = file.read()

    new_content = f"""
# 💡 About Me  

### **🚀 Welcome to My GitHub!**  
Hey there! I'm **Abdelrhman Ahmad**, a passionate **AI & Data Science** student at **Menoufia University**.  
💡 Always eager to learn, experiment, and contribute to open-source AI projects.  

### **🔍 GitHub Stats**  
📌 **Repositories:** {repo_count}  
📌 **Followers:** {followers}  
📌 **Following:** {following}  

### **🚀 Latest Projects**  
{top_repos}

---
📢 *This README auto-updates every hour using GitHub Actions!*  
    """

    with open("README.md", "w", encoding="utf-8") as file:
        file.write(new_content)

if __name__ == "__main__":
    update_readme()
