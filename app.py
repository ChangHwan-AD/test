from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    now = datetime.now()
    return render_template("index.html", now=now)


@app.route("/stock")
def stock():
    indices = [
        {"name": "KOSPI", "price": "2,612.34", "change": "15.23", "change_pct": "+0.59%", "direction": "up"},
        {"name": "KOSDAQ", "price": "843.17", "change": "6.82", "change_pct": "+0.82%", "direction": "up"},
        {"name": "S&P 500", "price": "6,025.99", "change": "32.45", "change_pct": "+0.54%", "direction": "up"},
    ]

    stocks = [
        {"symbol": "005930", "name": "삼성전자", "price": "71,200", "change": "800", "change_pct": "+1.14%", "direction": "up"},
        {"symbol": "000660", "name": "SK하이닉스", "price": "178,500", "change": "3,500", "change_pct": "+2.00%", "direction": "up"},
        {"symbol": "AAPL", "name": "Apple Inc.", "price": "$232.15", "change": "1.82", "change_pct": "+0.79%", "direction": "up"},
        {"symbol": "MSFT", "name": "Microsoft Corp.", "price": "$415.60", "change": "3.20", "change_pct": "-0.76%", "direction": "down"},
        {"symbol": "NVDA", "name": "NVIDIA Corp.", "price": "$138.25", "change": "5.10", "change_pct": "+3.83%", "direction": "up"},
        {"symbol": "TSLA", "name": "Tesla Inc.", "price": "$352.80", "change": "8.40", "change_pct": "-2.32%", "direction": "down"},
        {"symbol": "035420", "name": "NAVER", "price": "214,500", "change": "1,500", "change_pct": "+0.70%", "direction": "up"},
        {"symbol": "035720", "name": "카카오", "price": "42,350", "change": "650", "change_pct": "-1.51%", "direction": "down"},
    ]

    return render_template("stock.html", indices=indices, stocks=stocks)


@app.route("/even")
def even():
    return render_template("even.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
