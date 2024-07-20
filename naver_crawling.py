from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pymysql
import time
import re
from datetime import datetime

ChromeDriverManager().install()

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


# 크롬 드라이버 실행
browser = webdriver.Chrome()

# 네이버 플레이스에서 각 맛집의 블로그 리뷰를 
restaurants = [
    "명동교자",
    # "옛날민속집 본점",
    # "만족 오항족발",
    # "쟈니덤플링",
    # "미즈컨테이너",
    # "마코토",
    # "을밀대",
    # "혜화돌쇠아저씨",
    # "우래옥",
    # "바토스",
    # "오율",
    # "마리쿡",
    # "청솔나무",
    # "지하손만두",
    # "초마",
    # "삼청동수제비",
    # "토속촌 삼계탕",
    # "대원갈비",
    # "청담돈가",
    # "윤씨밀방",
    # "바바인디아",
    # "육회자매집",
    # "청진옥",
    # "하카다분코",
    # "모모코",
    # "툭툭누들타이",
    # "귀족족발",
    # "테이스팅룸 이태원점",
    # "이문설농탕",
    # "리틀사이공",
    # "활화산 조개구이 칼국수",
    # "홍스쭈꾸미",
    # "어부와백정 영등포 본점",
    # "아이해브어드림",
    # "필동면옥",
    # "대장장이화덕피자",
    # "부자피자",
    # "미진",
    # "단",
    # "서부면옥",
    # "고상",
    # "역전회관",
    # "마론키친앤바",
    # "더함",
    # "새벽집",
    # "떼아떼베네",
    # "소프트리",
    # "스테파니카페 2호점",
    # "알리고떼",
    # "연남 서서갈비",
    # "대게나라 방이점",
    # "올리아 키친 앤 그로서리",
    # "서울서 둘째로 잘하는 집",
    # "노블카페 강남점",
    # "황소고집",
    # "참설농탕 송파본점",
    # "우노",
    # "순희네빈대떡",
    # "을지면옥",
    # "돈코보쌈",
    # "애플하우스",
    # "봉우화로",
    # "메리고라운드 신천점",
    # "패션 5",
    # "버터핑거팬케이크",
    # "우대가",
    # "성수족발",
    # "마도니셰프 명동점",
    # "노블카페 가로수길점",
    # "먹쉬돈나 삼청동점",
    # "부처스컷 청담",
    # "군산오징어",
    # "진주집",
    # "웃사브",
    # "미미네",
    # "뿔레치킨 홍대본점",
    # "남포면옥",
    # "밀탑",
    # "부첼라",
    # "스시효 청담본점",
    # "동빙고",
    # "서린낙지",
    # "오자오동 함흥냉면",
    # "우성갈비",
    # "평래옥",
    # "피자힐",
    # "호수삼계탕",
    # "호우양꼬치",
    # "마포 본점최대포",
    # "비스떼까",
    # "프로간장게장 본점",
    # "피자리움",
    # "마마스",
    # "맛있는 교토 1호점",
    # "영동왕족발",
    # "커피스튜디오",
    # "한일관 압구정본점",
    # "계열사",
    # "더 가든 키친",
    # "더 스테이크 하우스"
]

for i in restaurants:
    url = f'https://map.naver.com/p/search/{i}?c=13.00,0,0,0,dh'
    browser.get(url)
