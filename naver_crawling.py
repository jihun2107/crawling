from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time

# 100개의 맛집 이름을 가져옴
from restaurant_list import restaurants

ChromeDriverManager().install()

# 크롬 드라이버 실행
browser = webdriver.Chrome()

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

        # 검색창으로 검색(엔터를 누름)
        search.send_keys(Keys.ENTER)
        time.sleep(1)

        # 맛집을 클릭할 수 있도록 프레임 이동
        print("프레임 이동 중")
        try:
            browser.switch_to.frame(browser.find_element(By.ID, 'searchIframe'))
        except NoSuchElementException:
            print(f"{i} 검색 결과가 없습니다.")
            continue  # 프레임이 없으면 다음 맛집으로 넘어감
        time.sleep(3)

        # 첫번째로 나온 맛집을 클릭
        print("첫 번째 맛집 클릭")
        try:
            first_rst = browser.find_element(By.CLASS_NAME, "YwYLL")
            first_rst.click()
        except NoSuchElementException:
            print(f"{i} 검색 결과가 없습니다.")
            continue  # 검색 결과가 없으면 다음 맛집으로 넘어감

        print("메인 프레임으로 이동 중")
        browser.switch_to.default_content()
        time.sleep(3)

        # 리뷰 페이지로 갈 수 있도록 프레임 이동
        print("검색한 프레임으로 이동 중")
        try:
            browser.switch_to.frame(browser.find_element(By.ID, 'entryIframe'))
        except NoSuchElementException:
            print(f"{i} entryIframe을 찾을 수 없습니다.")
            continue  # 프레임이 없으면 다음 맛집으로 넘어감
        time.sleep(2)

        # 리뷰 버튼 클릭
        print("리뷰 버튼 클릭")
        try:
            btns = browser.find_elements(By.CLASS_NAME, "veBoZ")
            review_clicked = False
            for btn in btns:
                if btn.text == "리뷰":
                    btn.click()
                    review_clicked = True
                    break
            if not review_clicked:
                print(f"{i} 리뷰 버튼을 찾을 수 없습니다.")
                continue
        except NoSuchElementException:
            print(f"{i} 리뷰 버튼을 찾을 수 없습니다.")
            continue  # 리뷰 버튼이 없으면 다음 맛집으로 넘어감

        # 블로그 리뷰 버튼 클릭
        print('블로그 리뷰 버튼 클릭')
        time.sleep(2)
        try:
            browser.find_elements(By.CLASS_NAME, "YsfhA")[1].click()
        except IndexError:
            print(f"{i} 블로그 리뷰 버튼을 찾을 수 없습니다.")
            continue  # 블로그 리뷰 버튼이 없으면 다음 맛집으로 넘어감

        # 블로그 url 크롤링
        print("블로그 url를 크롤링 중 입니다.")
        time.sleep(5)
        try:
            url_data = browser.find_elements(By.CLASS_NAME, "uUMhQ")
            for data in url_data:
                blog_url = data.get_attribute("href")
                print(blog_url)
                blog_url_list.append(blog_url)
        except NoSuchElementException:
            print(f"{i} 블로그 URL을 찾을 수 없습니다.")
            continue  # 블로그 URL이 없으면 다음 맛집으로 넘어감

        # 메인프레임으로 이동
        print("메인프레임으로 이동 중")
        browser.switch_to.default_content()

    except Exception as e:
        print(f"오류 발생: {e}")
        continue  # 예외 발생 시 다음 맛집으로 넘어감

browser.quit()

# MySQL과 연결 (주석 해제 및 설정 필요)
# conn = pymysql.connect(
#     host = 'localhost',
#     user = 'root',
#     password = 'ans!!941105',
#     db = 'naver_crawling',
#     charset = 'utf8mb4',
#     cursorclass = pymysql.cursors.DictCursor
# )

# # DB에 데이터를 저장 (주석 해제 및 설정 필요)
# with conn.cursor() as cur:
#     # 만들어진 list에서 하나씩 블로그에 들어감
#     for url in blog_url_list:
#         try:
#             # 블로그에 들어감
#             browser.get(url)

#             # 스크랩을 할 수 있도록 프레임 전환
#             browser.switch_to.frame(browser.find_element(By.ID, 'mainFrame'))

#             # 블로그의 타이틀과 리뷰 글을 스크랩
#             title = browser.find_element(By.CLASS_NAME, 'pcol1').text
#             review = browser.find_element(By.CLASS_NAME, 'se-main-container').text

#             # insert를 이용하여 DB에 정보 입력
#             sql = """INSERT INTO Books(
#                 title, review
#                 )
#                 VALUES(
#                 %s, %s
#                 )
#                 """

#             # 정보를 커밋
#             time.sleep(1)
#             cur.execute(sql, (title, review))
#             conn.commit()

#         # 만약 정보가 없거나 예외가 발생시 패스
#         except Exception as e:
#             print(e)