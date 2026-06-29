import os
import re
import csv
from collections import Counter

def extract_ips_from_log(file_path):
    "로그 파일에서 IP 주소를 추출하는 함수"
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ip_list = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            ips = re.findall(ip_pattern, line)
            ip_list.extend(ips)

    return ip_list

def count_ip_frequency(ip_list):
    "IP 주소별 접속 빈도를 계산하는 함수"
    return Counter(ip_list)

def save_result_to_csv(ip_counter, output_file):
    "분석 결과를 CSV 파일로 저장하는 함수"
    with open(output_file, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['순위', 'IP 주소', '접속 횟수'])

        for rank, (ip, count) in enumerate(ip_counter.most_common(), start=1):
            writer.writerow([rank, ip, count])

def print_top_3_ips(ip_counter):
    "접속 빈도가 높은 상위 3개 IP 주소를 출력하는 함수"
    print("\n[상위 3개 접속 IP 주소]")
    print("-" * 35)

    top_3 = ip_counter.most_common(3)
    for rank, (ip, count) in enumerate(top_3, start=1):
        print(f"{rank}위: {ip} - {count}회")

def main():
    print("로그 파일 IP 분석 프로그램")
    print("=" * 35)

    # file_path = "C:\\Users\\EZ\\Desktop\\rookies\\PBL\\python\\01\\sample_log_file.log"
    file_path = input("분석할 로그 파일 경로를 입력하세요: ")

    if not os.path.exists(file_path):
        print("오류: 입력한 로그 파일이 존재하지 않습니다.")
        return

    ip_list = extract_ips_from_log(file_path)

    if not ip_list:
        print("로그 파일에서 IP 주소를 찾을 수 없습니다.")
        return

    ip_counter = count_ip_frequency(ip_list)
    print_top_3_ips(ip_counter)

    output_file = "C:\\Users\\EZ\\Desktop\\rookies\\PBL\\python\\01\\ip.analysis.csv"
    save_result_to_csv(ip_counter, output_file)

    print(f"\n전체 분석 결과가 '{output_file}' 파일로 저장되었습니다.")

if __name__ == "__main__":
    main()