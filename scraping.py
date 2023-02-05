from bs4 import BeautifulSoup
import requests

url = "https://www.bseindia.com/corporates/ann.html"
# url="https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&param=7564&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_1_3.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_Q1PDG4YW86MF_wp2&fm=neo%2Fmerchandising&iid=M_dcc51dcc-e504-4193-b013-9916444bce93_3.Q1PDG4YW86MF&ppt=hp&ppn=homepage&ssid=5adgr1f6lc0000001674409409702"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup)
#name = soup.find_all('table',{'id':"lblann"})
# mobile_name = soup.find_all("div",{"class":"_4rR01T"})
# description = soup.find_all('td', {'class': 'TTRow_right'})
# time = soup.find_all('td', {'class': 'TTRow_right'})
# print(name,description,time)
# print(mobile_name)
# for mobile in mobile_name:
#     print(mobile.text)

detail = soup.find_all('a',{"data-bs-target":"#mySingleNewsModal"})
print(detail)
# print(name)