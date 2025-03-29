import matplotlib.pyplot as plt
import pandas as pd
from pytrends.request import TrendReq

def fetch_trends(keywords, timeframe='today 5-y', geo=''):  
    pytrends = TrendReq()
    pytrends.build_payload(keywords, cat=0, timeframe=timeframe, geo=geo, gprop='')
    data = pytrends.interest_over_time()
    return data

def plot_trends(data, keywords):
    plt.figure(figsize=(10, 5))
    for keyword in keywords:
        plt.plot(data.index, data[keyword], label=keyword)
    plt.xlabel("Year")
    plt.ylabel("Trend Popularity")
    plt.title("Internet Job Trends")
    plt.legend()
    plt.show()

def main():
    print("Enter job-related keywords separated by commas (e.g., Data Scientist, Business Analyst, Software Engineer):")
    keywords = input().split(',')
    keywords = [kw.strip() for kw in keywords]
    
    data = fetch_trends(keywords)
    if not data.empty:
        plot_trends(data, keywords)
    else:
        print("No data available for the given keywords.")

if __name__ == "__main__":
    main()
