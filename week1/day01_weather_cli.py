"""Day 01 - Weather CLI

Goal: Build a simple command-line weather checker.
"""

from __future__ import annotations

from datetime import datetime
import json
import urllib.error
import urllib.parse
import urllib.request


WEEKDAY_KR = ["월", "화", "수", "목", "금", "토", "일"]


def get_korean_datetime_string() -> str:
	"""Return current date and weekday in Korean."""
	now_local = datetime.now()
	weekday = WEEKDAY_KR[now_local.weekday()]
	return f"{now_local.year}년 {now_local.month}월 {now_local.day}일 ({weekday})"


def fetch_weather(city: str) -> dict[str, str]:
	"""Fetch current weather data for the given city from wttr.in."""
	encoded_city = urllib.parse.quote(city)
	url = f"https://wttr.in/{encoded_city}?format=j1"

	req = urllib.request.Request(url, headers={"User-Agent": "weather-cli"})
	with urllib.request.urlopen(req, timeout=10) as response:
		payload = response.read().decode("utf-8")

	data = json.loads(payload)
	current = data["current_condition"][0]

	return {
		"city": city,
		"description": current["weatherDesc"][0]["value"],
		"temp_c": current["temp_C"],
		"feels_like_c": current["FeelsLikeC"],
		"humidity": current["humidity"],
		"wind_kmph": current["windspeedKmph"],
	}


def main() -> None:
	"""Entry point for Day 01."""
	print(f"오늘 날짜: {get_korean_datetime_string()}")

	city = "서울"
	try:
		weather = fetch_weather(city)
	except urllib.error.URLError:
		print("날씨 정보를 가져오지 못했습니다. 네트워크 연결을 확인해 주세요.")
		return
	except (KeyError, IndexError, json.JSONDecodeError):
		print("날씨 데이터 형식이 예상과 달라 파싱에 실패했습니다.")
		return

	print(f"현재 {weather['city']}시 날씨")
	print(f"- 상태: {weather['description']}")
	print(f"- 기온: {weather['temp_c']}°C")
	print(f"- 체감: {weather['feels_like_c']}°C")
	print(f"- 습도: {weather['humidity']}%")
	print(f"- 풍속: {weather['wind_kmph']} km/h")


if __name__ == "__main__":
	main()

