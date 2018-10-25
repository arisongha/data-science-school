from selenium import webdriver
import pandas as pd
import time

# NAVER IT/SC ARTICLE CRAWLING

# 기사 크롤링
def type6(articlelist):
    results = driver.find_elements_by_css_selector("#section_body")
    time.sleep(0.05) # StaleElementReferenceException 때문에 넣어줌

    # section_body for loop
    for result in results :
        time.sleep(0.08) # StaleElementReferenceException 때문에 넣어줌
        results2 = result.find_elements_by_css_selector("li")

        # 기사 li for loop
        for result2 in results2 :
            try :
                ### comment : dt의 기사제목을 크롤링 할 때 원래 code와 같이 if 구분을 지어도 되지만 css not selector를 이용해서 .photo 가 아닌것을 crawling해도 된다. 
                ### find_element_by_css_selector('dt:not(.photo) > a')
                
                name = result2.find_element_by_css_selector("dl > dt:nth-child(1) > a").text

                # 기사에 사진이 없거나 동영상 기사일 경우 dt:nth-child(2) > a 를 선택
                if (name == '' or name == '동영상기사') :
                    name = result2.find_element_by_css_selector("dl > dt:nth-child(2) > a").text

            except Exception as ex:
                name = "크롤링 실패한 기사 , 에러이유:{}".format(ex) # StaleElementReferenceException 때문에 넣어줌
            finally :
                articlelist.append(name)

    return articlelist


# 네이버 사이트 오픈
articlelist = []
driver = webdriver.Chrome()
driver.set_window_size(1400, 800)

driver.get("https://www.naver.com/")

driver.find_element_by_css_selector(".section_navbar .area_navigation #PM_ID_serviceNavi .an_item:nth-child(2)").click() # 뉴스 기사로 이동
driver.find_element_by_css_selector("#lnb > ul > li:nth-child(8)").click() # IT/과학 기사로 이동

# main
for i in range(1,11):
    if (i > 1) :
        driver.find_element_by_link_text(str(i)).click() # i 페이지로 이동
    type6(articlelist)
    print("{} page crawling done!".format(i))

# 판다스 데이터 프레임으로 변경
df = pd.DataFrame(articlelist)
