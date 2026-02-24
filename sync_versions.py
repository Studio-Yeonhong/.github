import json
import re
import os

# 버전 정의 파일 경로
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VERSIONS_FILE = os.path.join(BASE_DIR, "versions.json")
README_FILES = [
    os.path.join(BASE_DIR, "README.md"),
    os.path.join(BASE_DIR, "README.en.md"),
    os.path.join(BASE_DIR, "README.ja.md"),
]

def update_readme(file_path, versions):
    if not os.path.exists(file_path):
        return

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 배지 업데이트 로직
    # 형식: ![Bot](https://img.shields.io/badge/bot-VERSION-hotpink)
    content = re.sub(
        r"(!\[Bot\]\(https://img\.shields\.io/badge/bot-)(.*?)(-hotpink\))",
        rf"\g<1>{versions['bot'].replace('-', '--')}\g<3>",
        content
    )
    content = re.sub(
        r"(!\[API\]\(https://img\.shields\.io/badge/api-)(.*?)(-blue\))",
        rf"\g<1>{versions['api'].replace('-', '--')}\g<3>",
        content
    )
    content = re.sub(
        r"(!\[Cache\]\(https://img\.shields\.io/badge/cache-)(.*?)(-green\))",
        rf"\g<1>{versions['cache'].replace('-', '--')}\g<3>",
        content
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    with open(VERSIONS_FILE, "r", encoding="utf-8") as f:
        versions = json.load(f)

    for readme in README_FILES:
        print(f"Updating {os.path.basename(readme)}...")
        update_readme(readme, versions)
    print("All README files updated successfully.")

if __name__ == "__main__":
    main()
