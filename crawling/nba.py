from selenium import webdriver
import pandas as pd
import time

# NBA RANK BOARD DATA CRAWLING

articlelist = []
driver = webdriver.Chrome()
driver.set_window_size(1500, 800)

driver.get("http://stats.nba.com/teams/traditional/?sort=GP&dir=-1")

rows = driver.find_elements_by_css_selector(".nba-stat-table__overflow tbody tr") # 각 TEAM이 가지고 있는 속성 : rows

heads = driver.find_elements_by_css_selector(".nba-stat-table__overflow thead > tr th") # Column 에 해당

headCnt = 0
cols = []

# column 수집
for head in heads :
    if (headCnt < 28) :
        cols.append(head.text)
        headCnt += 1

df = pd.DataFrame(columns = cols)
cnt = 0

#각 속성값 수집
for row in rows :
    attrs = [] # row에 해당하는 list
    rowAttrs = row.find_elements_by_css_selector("td")
    for rowAttr in rowAttrs :
        attrs.append(rowAttr.text) # df.loc[rowCnt] 에 사용할수 있게끔 list에 담는다.
    df.loc[cnt] = attrs
    print("{} row crawling done!".format(str(cnt)))
    cnt += 1 # df.loc[] 의 값을 늘려준다.

