import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 맥 폰트 설정
plt.rcParams["font.family"] = "AppleGothic"
plt.rcParams["axes.unicode_minus"] = False

class CustomerSalesAnalysis:
    # 고객 구매 데이터 생성
    def __init__(self):
        np.random.seed(42)  # 랜덤값 시드 고정
        count = 20          # 데이터 개수
        customers = [f"고객{i}" for i in range(1, 21)] # 고객명 : 고객1 ~ 고객20
        products = [f"상품{i}" for i in range(1, 6)] # 상품명 : 상품1 ~ 상품5
        dates = pd.date_range(start="2024-01-01", end="2024-12-31") # 랜덤 구매일자 생성
        prices = np.arange(10000, 200001, 5000) # 랜덤 단가 : 1만원 ~ 20만원, 단가별 5천원씩 차이

        data = {
            "고객명" : customers,
            "구매일자" : np.random.choice(dates, size=count),
            "상품명" : np.random.choice(products, size=count),
            "수량" : np.random.randint(1, 6, size=count),
            "단가" : np.random.choice(prices, size=count) 
        }
        self.df = pd.DataFrame(data)

        # 구매일자를 날짜형 데이터로 변환
        self.df["구매일자"] = pd.to_datetime(self.df["구매일자"])
        # 매출 컬럼 생성
        self.df["매출"] = self.df["수량"] * self.df["단가"]
        # 월 컬럼 생성
        self.df["월"] = self.df["구매일자"].dt.month

    # 전체 데이터 출력
    def show_data(self):
        print("===== 고객 구매 데이터 ======")
        print(self.df)

    # 월별 매출 총합 계산
    def monthly_sales(self):
        monthly = self.df.groupby("월")["매출"].sum()

        print("\n ===== 월별 매출 총합 =====")
        print(monthly)
        
        return monthly
    
    # 고객별 누적 매출 계산 
    def customer_total_sales(self):
        customer_total = self.df.groupby("고객명")["매출"].sum()

        print("\n ===== 고객별 누적 매출 =====")
        print(customer_total)
        
        return customer_total

    # 월별 매출 총합 막대 그래프
    def barplot_month(self):
        plt.figure(figsize=(8, 5))
        self.monthly_sales().plot(kind="bar")

        plt.title("월별 매출 총합")
        plt.xlabel("월")
        plt.ylabel("매출")
        plt.tight_layout()
        plt.show()

    # 고객별 누적 매출 파이 차트
    def pieplot_customer(self):
        plt.figure(figsize=(7, 7))
        self.customer_total_sales().plot(
            kind="pie",
            autopct="%.1f%%", # 퍼센트 표시
        )
        plt.title("고객별 누적 매출 비율")
        plt.ylabel("") # y축 라벨 지우기
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    analysis = CustomerSalesAnalysis()
    
    analysis.show_data()
    analysis.barplot_month()
    analysis.pieplot_customer()
