class StudentScores:
    # 생성자 : 파일 읽어서 딕셔너리 저장
    def __init__(self, filename):
        self.filename = filename
        self.scores = {}

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()

                    # 빈 줄 건너뛰기
                    if line == "":
                        continue
                    try: 
                        name, score = line.split(",")
                        name = name.strip()
                        score = int(score.strip())
                        self.scores[name] = score
                    except ValueError as e: 
                        print(e)
        except FileNotFoundError as e:
            print(self.filename, e)
    
    # 학생들 평균 점수 계산 메서드
    def calculate_avg(self):
        if len(self.scores) == 0:
            return 0
        
        total = sum(self.scores.values())
        avg = total / len(self.scores)
        return avg
    
    # 평균 이상인 학생 이름 리스트 반환 메서드
    def get_above_avg(self):
        above_avg_students = []
        for name, score in self.scores.items():
            if score >= self.calculate_avg():
                above_avg_students.append(name)
        return above_avg_students
    
    # 평균 미만 학생 데이터 별도 파일로 저장 메서드
    def save_below_avg(self, output_filename = "below_average_korean.txt"):
        try:
            with open(output_filename, "w", encoding="utf-8") as file:
                for name, score in self.scores.items():
                    if score < self.calculate_avg():
                        file.write(f"{name}, {score}\n")
            print(f"평균 미만 학생 데이터가 {output_filename} 파일에 저장되었습니다.")
        except Exception as e:
            print(f"파일 저장 중 오류 발생 : {e}") 
    
    # 평균 점수와 평균 이상 학생 리스트 출력 메서드
    def print_summary(self):
        print("=" * 10 + "학생 성적 분석 결과" + "=" * 10)
        print(f"전체 학생 수 : {len(self.scores)}명")
        print(f"평균 점수 : {self.calculate_avg()}점")
        
        print(f"\n[평균 이상 학생 리스트]")
        if len(self.get_above_avg()) == 0:
            print("평균 이상 학생이 없습니다.")
        else:
            for name in self.get_above_avg():
                print(name)

if __name__ == "__main__":
    student_scores = StudentScores("scores_korean.txt")

    student_scores.print_summary()
    student_scores.save_below_avg()
