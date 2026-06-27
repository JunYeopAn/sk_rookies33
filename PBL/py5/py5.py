import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 맥 한글 폰트 설정
plt.rcParams["font.family"] = "AppleGothic"  
plt.rcParams["axes.unicode_minus"] = False

class StudentScoreAnalysis:
    # 학생 성적 DataFrame 생성 -> 이름 : 학생1 ~ 학생20, 과목 : 수학, 영어, 과학, 점수범위 : 50 ~ 100
    def __init__(self):
        # 시드 고정
        np.random.seed(42)

        # 학생 이름 생성
        students = [f"학생{i}" for i in range(1, 21)]

        # 성적 데이터 생성
        data = {
            "이름" : students,
            "수학" : np.random.randint(50, 101, size= 20),
            "영어" : np.random.randint(50, 101, size= 20), 
            "과학" : np.random.randint(50, 101, size= 20)
        }

        self.df = pd.DataFrame(data)

        # 학생별 평균 점수 추가
        self.df["평균"] = self.df[["수학", "영어", "과학"]].mean(axis=1)

    # 전체 학생 성적 데이터 출력
    def show_data(self):
        print("="*10 + "전체 학생 성적 데이터" + "="*10)
        print(self.df)

    # 과목별 평균 점수 계산
    def sub_avg(self):
        avg_scores = self.df[["수학", "영어", "과학"]].mean()
        return avg_scores
    
    # 과목별 평균 점수 막대 그래프 시각화
    def plot_sub_avg(self):
        plt.figure(figsize=(8, 5))
        self.sub_avg().plot(kind="bar")

        plt.title("과목별 평균 점수")
        plt.xlabel("과목")
        plt.ylabel("평균 점수")
        plt.ylim(0, 100)

        # 막대 위에 평균 점수 표시
        for i, score in enumerate(self.sub_avg()):
            plt.text(i, score+1, f"{score:.1f}", ha="center")

        plt.tight_layout()
        plt.show()

    # 평균 성적 상위 5명
    def top5(self):
        return self.df.sort_values(by="평균", ascending=False).head(5)
    
    # 평균 상위 5명 막대 그래프 시각화
    def plot_top5(self):
        plt.figure(figsize=(8, 5))
        plt.bar(self.top5()["이름"], self.top5()["평균"])

        plt.title("평균 점수 상위 5명")
        plt.xlabel("학생")
        plt.ylabel("평균 점수")
        plt.ylim(0, 100)

        # 막대 위에 평균 점수 표시
        for i, score in enumerate(self.top5()["평균"]):
            plt.text(i, score+1, f"{score:.1f}", ha="center")

        plt.tight_layout()
        plt.show()

    # 전체 분석 실행
    def run_analysis(self):
        self.show_data()
        
        print("\n" + "="*10 + "과목별 평균 점수" + "="*10)
        print(self.sub_avg())

        print("\n" + "="*10 + "평균 점수 상위 5명" + "="*10)
        print(self.top5())

        self.plot_sub_avg()
        self.plot_top5()

if __name__ == "__main__":
    analysis = StudentScoreAnalysis()
    analysis.run_analysis()

