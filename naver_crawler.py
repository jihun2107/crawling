from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')  
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)

def get_blog_content(url): #블로그url 입력받기
    driver.get(url) #url로 이동
    time.sleep(5)  # 페이지 로딩 ㄷ대기

    # 네이버 블로그 본문 내용 추출
    try:
        iframe = driver.find_element(By.ID, 'mainFrame')
        driver.switch_to.frame(iframe)
        time.sleep(2)  #로딩대기

        # 최신 네이버 블로그 본문 구조
        blog_content = driver.find_element(By.CSS_SELECTOR, 'div.se-main-container')
    except Exception as e:
        print("최신 네이버 블로그 구조에서 본문 내용을 찾을 수 없습니다:", e)
        try:
            # 구 네이버 블로그 본문 구조
            blog_content = driver.find_element(By.CSS_SELECTOR, 'div.post-view p')
        except Exception as e:
            print("구 네이버 블로그 구조에서 본문 내용을 찾을 수 없습니다:", e)
            return None
    
    return blog_content.text.strip()

#블로그 URL 리스트
blog_urls = [
    "https://blog.naver.com/msunh/223513992374",
    "https://blog.naver.com/enzio/223510895519",
      "https://blog.naver.com/yisohee/223513235315",
        "https://blog.naver.com/thehman/223485156109",
          "https://blog.naver.com/harmony_mj/223489143172",
            "https://blog.naver.com/gin8772/223510492848",
              "https://blog.naver.com/hwy320/223475206615",
                "https://blog.naver.com/jkleecnu/223512444711",
                  "https://blog.naver.com/nezytable/223513984493",
                    "https://blog.naver.com/aeri0115/223487061763",  
]

# 진행 상황 기록 파일 경로
progress_file = 'progress.txt'

def read_progress():
    if os.path.exists(progress_file):
        with open(progress_file, 'r') as file:
            return int(file.read().strip())
    return 0

def write_progress(index):
    with open(progress_file, 'w') as file:
        file.write(str(index))

# 마지막으로 성공한 인덱스 읽기
start_index = read_progress()

# 각 블로그 URL에 대해 본문 내용 수집 및 파일 저장
for index, blog_url in enumerate(blog_urls):
    content = get_blog_content(blog_url)

    # 결과를 파일에 저장
    if content:
        file_name = f'naver_blog_content_{index + 1}.txt'
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"크롤링 완료! '{file_name}' 파일을 확인하세요.")
    else:
        print(f"블로그 {index + 1}의 본문 내용을 찾을 수 없습니다.")
driver.quit()

