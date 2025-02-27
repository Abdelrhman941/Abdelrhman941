import requests
import os

def fetch_github_data():
    token = os.getenv("GITHUB_TOKEN")
    username = "Abdelrhman941"  # استبدل باسم المستخدم الخاص بك
    headers = {"Authorization": f"token {token}"}
    
    # احضر بيانات المستخدم
    user_url = f"https://api.github.com/users/{username}"
    repos_url = f"https://api.github.com/users/{username}/repos"
    
    user_data = requests.get(user_url, headers=headers).json()
    repos_data = requests.get(repos_url, headers=headers).json()
    
    repo_count = user_data.get("public_repos", 0)
    followers = user_data.get("followers", 0)
    following = user_data.get("following", 0)
    
    repo_names = [repo["name"] for repo in repos_data[:5]]  # أول 5 مستودعات
    top_repos = ", ".join(repo_names)
    
    return repo_count, followers, following, top_repos

def update_readme():
    repo_count, followers, following, top_repos = fetch_github_data()
    
    with open("README.md", "r", encoding="utf-8") as file:
        content = file.readlines()
    
    new_content = []
    in_section = False
    
    for line in content:
        if "<!-- STATS_START -->" in line:
            in_section = True
            new_content.append(line)
            new_content.append(f"- 🔹 عدد المستودعات: {repo_count}\n")
            new_content.append(f"- 👥 المتابعون: {followers}\n")
            new_content.append(f"- 🏆 يتابع: {following}\n")
            new_content.append(f"- 📌 أهم المستودعات: {top_repos}\n")
        elif "<!-- STATS_END -->" in line:
            in_section = False
        
        if not in_section:
            new_content.append(line)
    
    with open("README.md", "w", encoding="utf-8") as file:
        file.writelines(new_content)

if __name__ == "__main__":
    update_readme()
