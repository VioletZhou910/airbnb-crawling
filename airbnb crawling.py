import requests
from bs4 import BeautifulSoup
import re
import time
import json

def getHTMLText(url):
    kv={'user-agent':'Mozilla/5.0'}
    try:
        r=requests.get(url,headers=kv,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print("getHTML wrong")
        return ""

def getRoomIDList(html_form):
    soup=BeautifulSoup(html_form,'html.parser')
    room_url_first=soup.find_all('meta',attrs={'itemprop':'url'})
    room_id_list=[]
    for url_more in room_url_first:
        url=url_more.attrs['content']
        room_id_more=re.search(r'\d{6,9}\?',url).group(0)
        room_id=re.search(r'\d{6,9}',room_id_more).group(0)
        room_id_list.append(room_id)
    print(room_id_list)
    return room_id_list

def getRoomInfo(room_id_list,html):
    for room_id in room_id_list:
        try:
            format_url="https://www.airbnb.cn/api/v2/pdp_listing_details/"+room_id+"?_format=for_rooms_show&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&"
            JSON=getHTMLText(format_url)
            print(JSON)
            dic_JSON=json.loads(JSON)
            reviews=dic_JSON["pdp_listing_detail"]["sorted_reviews"]
            for i in reviews:
                print(i.get("comments"))
            time.sleep(5)
        except:
            continue
    
    





def main():
    url="https://www.airbnb.cn/s/%E4%B8%8A%E6%B5%B7%E9%95%BF%E5%AF%BF%E8%B7%AF/homes?refinement_paths%5B%5D=%2Fhomes&toddlers=0&hotSpots=hotSpots&scenic=scenic&subwayLine=subwayLine&businessArea=businessArea&college=college&district=district&station=station&map_toggle=false&hospital=hospital&place_id=ChIJ9YF3tuZvsjUREy8Og6A-abI&poi_tab=businessArea&poi_group=0&s_tag=Qn2rKnGt"
    html=getHTMLText(url)
    room_id_list=getRoomIDList(html)
    getRoomInfo(room_id_list,html)



main()



