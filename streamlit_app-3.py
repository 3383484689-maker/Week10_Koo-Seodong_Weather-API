# 🌤️ Weather Explorer – Open API Demo
# Data source: OpenWeatherMap API (https://openweathermap.org/api)
# Author: Your Name

import streamlit as st
import requests

# ---------- 页面设置 ----------
st.set_page_config(page_title="Weather Explorer", layout="centered")

# ---------- 标题 ----------
st.title("🌤️ Weather Explorer (Open API)")
st.write("Get real-time weather data for any city using the OpenWeatherMap API.")
st.caption("Try searching for cities like **Seoul**, **Tokyo**, or **New York**.")

# ---------- 用户输入 ----------
city = st.text_input("🏙️ Enter a city name", "Seoul")

# ---------- API 设置 ----------
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"  # 替换成你自己的 key（https://openweathermap.org/api）
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """调用 OpenWeatherMap API 获取天气数据"""
    params = {
        "q": city,
        "appid": API_KEY if API_KEY != "YOUR_OPENWEATHERMAP_API_KEY" else "b6907d289e10d714a6e88b30761fae22",  # demo key
        "units": "metric",  # 摄氏温度
    }
    try:
        r = requests.get(BASE_URL, params=params)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception:
        return None

# ---------- 显示结果 ----------
if st.button("☁️ Get Weather"):
    with st.spinner("Fetching weather data..."):
        data = get_weather(city)
        if not data:
            st.error("⚠️ City not found or API error.")
        else:
            name = data.get("name", "Unknown location")
            main = data.get("main", {})
            weather = data.get("weather", [{}])[0]
            temp = main.get("temp", "N/A")
            humidity = main.get("humidity", "N/A")
            desc = weather.get("description", "").title()

            # 显示结果
            st.success(f"📍 {name}")
            st.metric("🌡️ Temperature (°C)", f"{temp} °C")
            st.metric("💧 Humidity (%)", f"{humidity}%")
            st.write(f"**Condition:** {desc}")
            st.write("---")
            st.caption("Data Source: OpenWeatherMap API")
