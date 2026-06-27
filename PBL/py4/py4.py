import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class SalesAnalysis:
    # 2024/1/1 ~ 12/31 날짜 생성 메서드
    def __init__(self):
        self.dates = pd.date_range(
            start="2024-01-01",
            end="2024-12-31",
            freq="D"
        )
        # 일별 매출 데이터 생성 -> 1000 ~ 10000 사이의 난수 생성 
        self.sales = np.random.randint(1000, 10001, size=len(self.dates))
        # 데이터프레임 생성
        self.df = pd.DataFrame({
            "날짜" : self.dates,
            "매출" : self.sales, 
        })
        # 월 정보 추가
        self.df["월"] = self.df["날짜"].dt.month

    # 월별 매출 총합 계산 메서드
    def calculate_monthly_sales(self):
        monthly_sales = self.df.groupby("월")["매출"].sum()
        return monthly_sales
    
    # 시각화 메서드
    def visualize_sales(self):
        # 맥북 한글 폰트 설정 
        plt.rcParams["font.family"] = "AppleGothic"
        plt.rcParams["axes.unicode_minus"] = False

        # 그래프 크기 설정
        plt.figure(figsize=(10, 6))

        # 꺾은선 그래프
        plt.plot(
            self.calculate_monthly_sales().index,
            self.calculate_monthly_sales().values,
            marker = "o",
            linestyle = "-"
        )
        # 그래프 제목 및 축 라벨
        plt.title("2024년 월별 매출 추이")
        plt.xlabel("월")
        plt.ylabel("매출 총합")

        # x축을 1월 ~ 12월로 표시
        plt.xticks(range(1, 13))
        
        # 격자 표시
        plt.grid(True)

        # 그래프 출력
        plt.show()
    
if __name__ == "__main__":
    sales_analysis = SalesAnalysis()

    sales_analysis.visualize_sales()
