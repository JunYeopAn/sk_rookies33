import os
import re
import time
from datetime import datetime

## settings
monitor_dir = './monitor_directory'  # Directory to monitor
check_interval = 5  # Check interval in seconds

dangerous_extensions = ['.py', '.class', '.js']  # Dangerous file extensions

email_regex = re.compile(
    r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
)  # Regex to find email addresses

sql_regex = re.compile(
    r"\b(SELECT|INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|TRUNCATE)\b.*?(FROM|INTO|TABLE|DATABASE|WHERE|SET|VALUES)", 
    re.IGNORECASE
)  # Regex to find SQL statements

comment_regex = re.compile(
    r" (#.*|//.*|/\*[\s\S]*?\*/)"
)  # Regex to find comments in code

## Utils Functions
def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def ensure_monitor_directory():
    if not os.path.exists(monitor_dir):
        os.makedirs(monitor_dir)
        print(f"[{get_current_time()}] Created monitor directory: {monitor_dir}")

def get_all_files(directory):
    file_set = set()
    
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_set.add(file_path)
    
    return file_set

def is_warning_extension(file_path):
    _, ext = os.path.splitext(file_path)
    return ext.lower() in dangerous_extensions

def read_file_content(file_path):
    encodings = ["utf-8", "cp949", "euc-kr"]

    for encoding in encodings:
        try:
            with open(file_path, "r", encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError as e:
            print(e)
            continue
        except PermissionError as e:
            print(e)
            return None
        except FileNotFoundError as e:
            print(e)
            return None
        except Exception as e:
            print(e)
            return None
    
    print(f"텍스트 파일이 아니거나 읽을 수 없는 파일입니다: {file_path}")
    return None

def detect_sensitive_info(content):
    detected = []

    comments = comment_regex.findall(content)
    emails = email_regex.findall(content)
    sql_queries = sql_regex.findall(content)

    if comments:
        detected.append(("주석", len(comments)))
    if emails:
        detected.append(("이메일", len(emails)))
    if sql_queries:
        detected.append(("SQL문", len(sql_queries)))
    return detected

def analyze_new_file(file_path):
    print("\n" + "=" * 30 + "\n")
    print("새 파일이 생성되었습니다. \n")
    print(f"시간 : {get_current_time()} \n")
    print(f"경로 : {file_path} \n")

    if is_warning_extension(file_path):
        print("[WARNING] 주의 확장자 파일입니다. \n")
        print(f"{dangerous_extensions} 파일은 보안 위험 가능성이 있습니다. \n")
    else:
        print("[OK] 일반 확장자 파일입니다.")
    
    content = read_file_content(file_path)
    if content is None:
        print("[INFO] 내용 분석을 건너뜁니다. \n")
        print("=" * 30 + "\n")
        return
    
    detected_infos = detect_sensitive_info(content)
    if detected_infos:
        print("[WARNING] 민감 정보로 의심되는 내용이 발견되었습니다. \n")
        for info_type, count in detected_infos:
            print(f" - {info_type}: {count}개 탐지 \n")
    else:
        print("[OK] 민감 정보 패턴이 탐지되지 않았습니다. \n")
    print("=" * 30 + "\n")

## Main Monitoring Function
def monitor_directory():
    ensure_monitor_directory()
    
    print("[START] 디렉터리 모니터링 시작 \n")
    print(f"[TARGET] 감시 대상 : {monitor_dir} \n")
    print(f"[INFO] 검사 주기 : {check_interval}초 \n")
    print("[INFO] 프로그램 종료 : Ctrl + C \n")

    known_files = get_all_files(monitor_dir)

    print(f"[INFO] 초기 파일 목록 기록 완료 : {len(known_files)}개 \n")

    while 1:
        try:
            current_files = get_all_files(monitor_dir)
            new_files = current_files - known_files

            if new_files:
                for file_path in new_files:
                    analyze_new_file(file_path)

            known_files = current_files
            time.sleep(check_interval)
        except KeyboardInterrupt as e:
            print(e)
            break
        except Exception as e:
            print(e)
            time.sleep(check_interval)

if __name__ == "__main__":
    monitor_directory()