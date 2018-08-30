from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import bs4
S=str(input("Enter source:"))
D=str(input("Enter dstn:"))
din=str(input("Enter day:"))
mahina=str(input("Enter month:"))
browser = webdriver.Chrome("E:\\chromedriver.exe")
browser.get("http://www.indianrail.gov.in/between_Imp_Stations.html")

fromStation = Select(browser.find_element_by_name("lccp_src_stncode"))
fromStation.select_by_value(S)
toStation = Select(browser.find_element_by_name("lccp_dstn_stncode"))
toStation.select_by_value(D)
dday = browser.find_element_by_name("lccp_day").clear()
dday = browser.find_element_by_name("lccp_day").send_keys(din)
mm = browser.find_element_by_name("lccp_month").clear()
mm = browser.find_element_by_name("lccp_month").send_keys(mahina)
sub = browser.find_element_by_name("submit2").click()

#usingbs4

#create a file
file = open("train.txt", 'w')
file.write("train availability from "+S+" to "+D+"\n\n")
file.close()
f = open("train.txt",'a')


radioButtons = browser.find_elements_by_name("lccp_trndtl")
for rd in range(len(radioButtons)):
	radioButtons = browser.find_elements_by_name("lccp_trndtl")
	radioButtons[rd].click()
	subb = browser.find_element_by_name("lccp_submitacc").click()
	browser.switch_to_alert().accept();
	html_str=browser.page_source
	soup=bs4.BeautifulSoup(html_str)
	data = []
	tableSet = soup.findAll('table', attrs={'class':'table_border'})
	#train number and code
	tt = tableSet[0].find('tbody')
	rws = tt.find_all('tr')
	dtl=[]
	for ro in rws:
		columns = ro.find_all('td')
		columns = [ele.text.strip() for ele in columns]
		dtl.append([ele for ele in columns if ele])
	print("TABLE 1 IS")
	f.writelines('\t  '.join(dtl[0])+"\n")
	f.writelines('\t      '.join(dtl[1])+"\n")
	f.write("\n")
	
	table_body = tableSet[1].find('tbody')
	rows = table_body.find_all('tr')
	count = 1
	tablehead = rows[0].find_all('th')
	tablehead = [ele.text.strip() for ele in tablehead]
	data.append([ele for ele in tablehead if ele])
	for row in rows:
		cols = row.find_all('td')
		cols = [ele.text.strip() for ele in cols]
		if count%2 == 0:
			data.append([ele for ele in cols if ele])
		count = count + 1
	print(data)
	f.writelines('\t'.join(i) + '\n' for i in data)
	browser.execute_script("window.history.go(-1)")