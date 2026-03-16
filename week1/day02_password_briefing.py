"""Day 02 - Password and Briefing
"""

import argparse
import random
import string
import sys

def generate_password(length=12):
    """영문(대문자는 1번), 숫자, 특정 특수문자(1개)를 조합하여 12자리 비밀번호 생성"""
	
 	# 1. 사용할 문자 집합 정의
    upper = string.ascii_uppercase  # 대문자 (A-Z)
    lower = string.ascii_lowercase  # 소문자 (a-z)
    digits = string.digits          # 숫자 (0-9)
    symbols = "?!-$"                 # 지정된 특수문자
    
    # 대문자를 제외한 나머지 문자들 합치기
    other_chars = lower + digits + symbols
    
    # 2. 필수 문자 선택 (대문자 1개, 특수문자 1개)
    password_list = [random.choice(upper)]
    password_list.append(random.choice(symbols))
    
    # 3. 나머지 10자리 채우기
    password_list += [random.choice(other_chars) for _ in range(length - 2)]
    
    # 4. 순서 섞기 (대문자가 항상 앞에 오지 않도록)
    random.shuffle(password_list)
    return ''.join(password_list)

def generate_brief(text):
    """텍스트를 문장 단위로 나누어 상위 3문장을 요약본으로 제공"""
    # 줄바꿈이나 마침표를 기준으로 문장 분리 (간단한 구현)
    sentences = text.replace('\n', ' ').split('. ')
    # 비어있지 않은 문장만 필터링
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # 최대 3문장까지 추출
    summary = sentences[:3]
    return ".\n".join(summary) + "." if summary else "입력된 내용이 너무 짧습니다."

def main():
    # 1. ArgumentParser 객체 생성
    parser = argparse.ArgumentParser(description="바이브 코딩 도구: 비밀번호 생성 및 텍스트 요약")
    
    # 2. 서브 커맨드 설정을 위한 객체 생성
    subparsers = parser.add_subparsers(dest="command", help="사용할 기능을 선택하세요")

    # [기능 1] 비밀번호 생성기 서브 커맨드 설정
    subparsers.add_parser("pw", help="12자리 랜덤 비밀번호를 생성합니다")

    # [기능 2] 브리핑 생성기 서브 커맨드 설정
    brief_parser = subparsers.add_parser("brief", help="텍스트를 3줄로 요약합니다")
    brief_parser.add_argument("text", nargs='+', help="요약할 긴 텍스트를 입력하세요 (따옴표로 감싸주세요)")

    # 인자 파싱
    args = parser.parse_args()

    # 3. 선택된 기능 실행
    if args.command == "pw":
        result = generate_password()
        print(f"\n[생성된 비밀번호]: {result}\n")
    
    elif args.command == "brief":
        # 리스트로 들어온 단어들을 공백(' ')으로 연결하여 하나의 문자열로 만듦
        full_text = ' '.join(args.text)
        result = generate_brief(full_text)
        print(f"\n[요약 브리핑]:\n{result}\n")
    
    else:
        # 아무 명령어도 입력하지 않았을 때 도움말 출력
        parser.print_help()

if __name__ == "__main__":
    main()