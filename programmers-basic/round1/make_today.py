import os

def create_today():
    # 1. 현재 경로 확인
    current_dir = os.getcwd()
    
    # 2. 날짜 입력 받기
    day_input = input("📅 오늘 몇 일차(Day)인가요? (숫자만 입력): ").strip()
    if not day_input:
        print("❌ 날짜를 입력해야 합니다.")
        return
        
    day_folder = f"day{int(day_input):02d}"
    target_path = os.path.join(current_dir, day_folder)
    
    # 3. 폴더 생성
    if not os.path.exists(target_path):
        os.makedirs(target_path)
        print(f"✅ {day_folder} 폴더 생성 완료.")

    problems = []
    print("\n📝 오늘 풀 문제 정보를 입력하세요 (종료하려면 문제명에서 엔터)")
    
    while True:
        title = input("- 문제명: ").strip()
        if not title: break
        eng_name = input("  파일명(영어): ").strip()
        url = input("  문제URL: ").strip()
        problems.append({"title": title, "file": eng_name, "url": url})

    if not problems:
        return

    # 4. 빈 C 파일 생성 (내용 없음)
    for p in problems:
        c_file_path = os.path.join(target_path, f"{p['file']}.c")
        if not os.path.exists(c_file_path):
            with open(c_file_path, "w", encoding="utf-8") as f:
                pass  # 아무 내용도 쓰지 않고 파일만 생성
            print(f"📄 빈 파일 생성: {p['file']}.c")

    # 5. README.md 생성 (민철님 전용 템플릿)
    readme_path = os.path.join(target_path, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(f"# 📅 Day {int(day_input):02d} (Round 1)\n\n")
        f.write("## 📊 오늘 해결한 문제 목록\n")
        f.write("| 순번 | 문제명 | 상태 | 난이도 |\n| :--- | :--- | :---: | :--- |\n")
        for i, p in enumerate(problems, 1):
            f.write(f"| {i} | [{p['title']}]({p['url']}) | ✅ | Lv. 0 |\n")
        
        f.write("\n---\n\n## 🔍 문제별 상세 기록\n")
        for i, p in enumerate(problems, 1):
            f.write(f"\n### {i}. {p['title']}\n")
            f.write("- **핵심 로직:** \n- **사용한 개념:** \n- **회고:** \n")
        
        f.write("\n---\n\n## 💬 오늘의 전체 회고\n- **총평:** \n- **내일의 목표:** \n")

    print(f"\n🚀 세팅 완료! {day_folder} 폴더로 이동해서 작업을 시작하세요.")

if __name__ == "__main__":
    create_today()
