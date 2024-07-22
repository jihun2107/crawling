from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pymysql
import time


# 네이버 플레이스에서 각 맛집의 블로그 리뷰를 
restaurants = [
    "명동교자",
    "옛날민속집 본점",
    "만족 오항족발",
    "쟈니덤플링",
    "미즈컨테이너",
    "마코토",
    "을밀대",
    "혜화돌쇠아저씨",
    "우래옥",
    "바토스",
    "오율",
    "마리쿡",
    "청솔나무",
    "지하손만두",
    "초마",
    "삼청동수제비",
    "토속촌 삼계탕",
    "대원갈비",
    "청담돈가",
    "윤씨밀방",
    "바바인디아",
    "육회자매집",
    "청진옥",
    "하카다분코",
    "모모코",
    "툭툭누들타이",
    "귀족족발",
    "테이스팅룸 이태원점",
    "이문설농탕",
    "리틀사이공",
    "활화산 조개구이 칼국수",
    "홍스쭈꾸미",
    "어부와백정 영등포 본점",
    "아이해브어드림",
    "필동면옥",
    "대장장이화덕피자",
    "부자피자",
    "미진",
    "단",
    "서부면옥",
    "고상",
    "역전회관",
    "마론키친앤바",
    "더함",
    "새벽집",
    "떼아떼베네",
    "소프트리",
    "스테파니카페 2호점",
    "알리고떼",
    "연남 서서갈비",
    "대게나라 방이점",
    "올리아 키친 앤 그로서리",
    "서울서 둘째로 잘하는 집",
    "노블카페 강남점",
    "황소고집",
    "참설농탕 송파본점",
    "우노",
    "순희네빈대떡",
    "을지면옥",
    "돈코보쌈",
    "애플하우스",
    "봉우화로",
    "메리고라운드 신천점",
    "패션 5",
    "버터핑거팬케이크",
    "우대가",
    "성수족발",
    "마도니셰프 명동점",
    "노블카페 가로수길점",
    "먹쉬돈나 삼청동점",
    "부처스컷 청담",
    "군산오징어",
    "진주집",
    "웃사브",
    "미미네",
    "뿔레치킨 홍대본점",
    "남포면옥",
    "밀탑",
    "부첼라",
    "스시효 청담본점",
    "동빙고",
    "서린낙지",
    "오자오동 함흥냉면",
    "우성갈비",
    "평래옥",
    "피자힐",
    "호수삼계탕",
    "호우양꼬치",
    "마포 본점최대포",
    "비스떼까",
    "프로간장게장 본점",
    "피자리움",
    "마마스",
    "맛있는 교토 1호점",
    "영동왕족발",
    "커피스튜디오",
    "한일관 압구정본점",
    "계열사",
    "더 가든 키친",
    "더 스테이크 하우스"
]

# 크롬 드라이버 실행
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 네이버 플레이스 홈 화면 url
url = "https://map.naver.com/p?c=15.00,0,0,0,dh"

blog_url_list = []

for i in restaurants:
    try:
        # 네이버 플레이스 홈화면을 브라우저로 띄움
        browser.get(url)
        print(f'지금은 다음 가게를 검색 중 입니다.: {i}')

        # 검색창 찾기
        search = browser.find_element(By.CLASS_NAME, "input_search")

        # 검색창에 맛집 리스트 순서대로 맛집 입력
        print('검색어 입력 중')
        search.send_keys(i)
        time.sleep(2)


        # 검색창으로 검색(엔터를 누름)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        # 검색창 비우기
        search.send_keys(Keys.COMMAND + "a")
        search.send_keys(Keys.BACK_SPACE)

        # 맛집을 클릭할 수 있도록 프레임 이동
        print("프레임 이동 중")
        browser.switch_to.frame(browser.find_element(By.ID, 'searchIframe'))
        time.sleep(2)

        # 첫번째로 나온 맛집을 클릭
        print("첫 번째 맛집 클릭")
        good_restaurant = browser.find_element(By.CLASS_NAME, "qbGlu")
        good_restaurant.click()

        # 메인프레임으로 이동
        print("메인 프레임으로 이동 중")
        browser.switch_to.default_content()
        time.sleep(3)

        # 리뷰 페이지로 갈 수 있도록 프레임 이동
        print("프레임 이동 중")
        browser.switch_to.frame(browser.find_element(By.ID, 'entryIframe'))
        time.sleep(2)

        # 리뷰 버튼 클릭
        print("리뷰 버튼 클릭")
        browser.find_elements(By.CLASS_NAME, "veBoZ")[3].click()

        # 블로그 리뷰 버튼 클릭
        print('블로그 리뷰 버튼 클릭')
        browser.find_elements(By.CLASS_NAME, "YsfhA")[1].click()
        time.sleep(2)

        # 블로그 url 크롤링
        print("블로그 url를 크롤링 중 입니다.")
        url_data = browser.find_elements(By.CLASS_NAME, "uUMhQ")
        for i in url_data:
            blog_url = i.get_attribute("href")
            blog_url_list.append(blog_url)
        
        # 메인프레임으로 이동
        print("프레임 이동 중")
        browser.switch_to.default_content()

        print(blog_url_list)
    except:
        pass

print(blog_url_list)

# MySQL과 연결
conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'ans!!941105',
    db = 'naver_crawling',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

# DB 에 데이터를 저장
with conn.cursor() as cur:
    # 만들어 논 list에서 하나씩 블로그에 들어감
    for i in blog_url_list:
        try:
            # 블로그에 들어감
            browser.get(i)

            # 블로그에 타이틀과 리뷰 글을 스크랩
            title = browser.find_element(By.CLASS_NAME, 'pcol1').text
            review = browser.find_element(By.CLASS_NAME, 'se-main-container').text


            # insert를 이용하여 DB에 정보 입력
            sql = """INSERT INTO Books(
                title, review
                )
                VALUES(
                %s, %s
                )
                """

            # 정보를 커밋
            time.sleep(1)
            cur.execute(sql, (title, review))
            conn.commit()

        # 만약 정보가 없거나 예외가 발생시 패스
        except Exception  as e:
            print(e)