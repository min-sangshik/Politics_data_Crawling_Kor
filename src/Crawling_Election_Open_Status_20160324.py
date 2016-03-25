#-*- coding:utf-8 -*-
'''
Created on 2016. 3. 24.

@author: SangShik
'''

from bs4 import BeautifulSoup
import urllib
import csv
from datetime import datetime, timedelta


#electionName = ["20000413", "20000413", "20040415", "20080409","20120411"]  # 이걸 자동화 해야 하는지는 확인해 보아야 함!! (일단 19대 정보 먼저)
electionName_Arr = ["20120411"]
#temp.append('<option value="20120411">제19대</option>');                    
#temp.append('<option value="20080409">제18대</option>'                    
#temp.append('<option value="20040415">제17대</option>')                    
#temp.append('<option value="20000413">제16대</option>')                    
#temp.append('<option value="19960411">제15대</option>');


#[{"CODE":1100,"NAME":"서울특별시"},
#{"CODE":2600,"NAME":"부산광역시"},{"CODE":2700,"NAME":"대구광역시"},{"CODE":2800,"NAME":"인천광역시"},{"CODE":2900,"NAME":"광주광역시"},
#{"CODE":3000,"NAME":"대전광역시"},{"CODE":3100,"NAME":"울산광역시"},
#{"CODE":4100,"NAME":"경기도"},{"CODE":4200,"NAME":"강원도"},{"CODE":4300,"NAME":"충청북도"},{"CODE":4400,"NAME":"충청남도"},{"CODE":4500,"NAME":"전라북도"},{"CODE":4600,"NAME":"전라남도"},{"CODE":4700,"NAME":"경상북도"},{"CODE":4800,"NAME":"경상남도"},{"CODE":4900,"NAME":"제주특별자치도"}]}}
#{"CODE":5100,"NAME":"세종특별자치시"},
cityCode_Arr = ["1100", 
                        "2600", "2700", "2800", "2900", 
                        "3000", "3100", 
                        "4100", "4200", "4300", "4400", "4500", "4600", "4700", "4800", "4900", 
                        "5100"]

def filesave1(filename, resultdata):
    f = open("../resultdata/"+filename, 'w')
    f.write(resultdata)
    f.close()

def fileopen1(filename):
    try:
        #print filename
        f = open("../resultdata/"+filename, 'r')
        resultdata = f.read()
        #print "[ fileopen1 DATA ] "+resultdata   
        f.close()    
        return resultdata
    except :
        print "Exception - FileOpen : " + filename
        raise

def filesave_csv_1(filename, data):
    with open("../resultdata/"+filename, 'wb') as f:
            writer = csv.writer(f, csv.excel)
            
            for item in data:
                cp949item = [unicode(i).encode('cp949') for i in item]
                writer.writerow(cp949item)
        
######################################################
# 투개표 >> 개표진행상황
# TEST 
# electionType=2                     국회의원 선거  (금번에는 기본으로 설정)  - 고정
# electionName=20120411         제19대 
# electionCode=2                    국회의원 (비례도 있음) - 고정
# cityCode=1100                      서울특별시 내용
######################################################
def cr_election_open_status():
    for electionName in electionName_Arr:
        for cityCode in cityCode_Arr:
            thisurl = "http://info.nec.go.kr/electioninfo/electionInfo_report.xhtml"
            param = "?electionId=0000000000&electionType=2&electionName="+electionName+"&electionCode=2&cityCode="+cityCode+"&requestURI=/WEB-INF/jsp/electioninfo/0000000000/vc/vccp09.jsp&topMenuId=VC&secondMenuId=VCCP09&menuId=VCCP09&statementId=VCCP09_%232&oldElectionType=1&townCode=-1&sggCityCode=-1&x=35&y=12"
            
            print "try electionName="+electionName+" cityCode="+cityCode
            #GET HTML DATA
            handle = urllib.urlopen(thisurl+param)      
            html_gunk =  handle.read()
            
            #FILE SAVE
            filesave1("Election_Open_Result_"+electionName+"_" +cityCode+".html" , html_gunk)
            print "Done"
            
######################################################
# 투개표 >> 개표진행상황
# TEST 다운받은 HTML을 분석하여 XML ?? 등 DB 입력
# electionType=2                     국회의원 선거  (금번에는 기본으로 설정)  - 고정
# electionName=20120411         제19대 
# electionCode=2                    국회의원 (비례도 있음) - 고정
# cityCode=1100                      서울특별시 내용
######################################################
def cr_election_open_status_analysis():
    for electionName in electionName_Arr:
        for cityCode in cityCode_Arr:
            #thisurl = "http://info.nec.go.kr/electioninfo/electionInfo_report.xhtml"
            #param = "?electionId=0000000000&electionType=2&electionName="+electionName+"&electionCode=2&cityCode="+cityCode+"&requestURI=/WEB-INF/jsp/electioninfo/0000000000/vc/vccp09.jsp&topMenuId=VC&secondMenuId=VCCP09&menuId=VCCP09&statementId=VCCP09_%232&oldElectionType=1&townCode=-1&sggCityCode=-1&x=35&y=12"
            
            print "try file open  electionName="+electionName+" cityCode="+cityCode
            #GET HTML DATA from File
            
            #FILE SAVE
            html_data = fileopen1("Election_Open_Result_"+electionName+"_" +cityCode+".html" )
                    
            print "[DATA] "+html_data   
            #soup = BeautifulSoup(handle.read(), "html.parser")
            print "Done"
            
            
######################################################
# 20160325
# SSMIN
# 국회의원선거 electionName(년월일), 와 cityCode 넣으면 엑셀로 기본
# 데이터를 저장하는 함수
# - 기 저장된 HTML파일에서 데이터 파싱후 CSV로 저장
######################################################
def cr_election_open_status_parse_writecsv(electionName, cityCode):
    
    #######################################################
    #TEST AREA
    #######################################################
    #electionName = "20120411"
    
    
    #######################################################
    #cityCode LOOP START
    #######################################################
    #for cityCode in cityCode_Arr:
    #   print cityCode
    
    #cityCode = "1100"
    
    print "try file open  electionName="+electionName+" cityCode="+cityCode
    
    file_name_only = "Election_Open_Result_"+electionName+"_" +cityCode
    file_name_html = file_name_only+".html" 
    file_name_excel = file_name_only+".csv" 
    html_data = fileopen1(file_name_html)
    #print "[DATA] "+html_data   
    
    #######################################################
    #http://www.dreamy.pe.kr/zbxe/CodeClip/163266
    #데이터 형상
    #선거구 총합.... 후보1 후보2......
    #                     득표수1 득표수2.....
    #다시 선거구부터 반복.... (즉 2라인을 셋트로 처리해야 함)
    #######################################################
    soup = BeautifulSoup(html_data, "html.parser")
    divregion_top = soup.find_all("div", "cont_table") #<div class="cont_table">
    
    items_final = []
    items_td_line1 = ["",]
    items_td_line2 = ["",]
    items_final.append(("O 선거 종류","O 선거 횟수", "O 투표일","O 선거구", "O 전체유권자수","O 투표자 수","O 투표율", "O 정당명", "O 후보자명", "O 득표수"))
    
    ################################
    election_name = "국회의원선거"
    election_number = "19"
    election_date = electionName
    election_citycode = cityCode
    ################################
    election_area_name = ""
    election_area_total_people_count = ""
    election_area_votes_people_count = ""
    election_area_votes_people_ratio = ""  #election_area_voted_people_count/election_area_total_people_count
    ################################
    party_name = ""
    candidate_name= ""
    candidate_votes_count = "" # 이 정보가 최종으로 예측되어야 함
    ################################
    for trdata in divregion_top:
        trs =  trdata('tr')
        count_tr = 0
        for tr in trs:
            count_tr = count_tr+1
            #print "START TR" + str(count_tr)
            tds = tr('td')
            
            count_td = 0
            if count_tr > 2:
                td_first_data = ""
                td_first_exception_raise = 0 # 소계와 같이 하나의 선거구 내부에 추가적인 구가 있는 경우!
                
                for td in tds:
                    count_td = count_td+1
                    #print "count _td: " + str(count_td)
                    
                    tddata =  str(td)
                    tddata=tddata.replace("</br>", "")
                    tddata=tddata.replace(",", "")
                    tddata=tddata.replace("<strong>", "")
                    tddata=tddata.replace("</strong>", "")
                    tddata=tddata.replace("<br>", "_")
                    tddata=tddata.replace("<td class=\"alignR\">", "")
                    tddata=tddata.replace("<td class=\"alignC\">", "")
                    tddata=tddata.replace("<td class=\"alignL\">", "")
                    tddata=tddata.replace("</td>", "")
                    #print tddata
                    
                    if count_td == 1: 
                        td_first_data = tddata

                    #file:///E:/workspace/Politics_Data_Crawling/resultdata/Election_Open_Result_20120411_2600.html 중구 동구
                    #print str(tddata)
                
                    if count_tr %2 == 1:
                        #print "firstline"
                        items_td_line1.append(tddata)
                    else:
                        #print "second line"
                        items_td_line2.append(tddata)
                #end for td in tds:
                
                print "check : "  + str(td_first_data)
                
            #Data TR 2 라인을 읽으면 조정해서 배열에 추가하기!!
#             if ((election_date == "20120411" and election_citycode=="2600" and  str(td_first_data) == "중구" ) or
#                (election_date == "20120411" and election_citycode=="2600" and  str(td_first_data) == "동구" ) or
#                (election_date == "20120411" and election_citycode=="2600" and  str(td_first_data) == "해운대구" ) or
#                (election_date == "20120411" and election_citycode=="2600" and  str(td_first_data) == "기장군" )) : 
#                 print "except" + str(td_first_data)
# 
#             else:                    
                
                if count_tr %2 == 0:
                    print str(items_td_line1[1])
                    print str(items_td_line2[2])
                    
                    election_area_name = str(items_td_line1[1])
                    election_area_total_people_count = str(items_td_line2[2]).split("_")[0]
                    #print "election_area_total_people_count:"+election_area_total_people_count
                    election_area_votes_people_count = str(items_td_line2[3]).split("_")[0]
                    #print "election_area_votes_people_count:"+election_area_votes_people_count
                    
                    try:
                        election_area_votes_people_ratio = str(round(float(election_area_votes_people_count)/float(election_area_total_people_count),4))
                    except :
                        #ValueError: could not convert string to float: 
                        print election_area_votes_people_count
                        print election_area_total_people_count
                        election_area_votes_people_ratio = 0
                        
                    #print "election_area_votes_people_ratio:"+election_area_votes_people_ratio
                    ################################
                    #print "len(items_td_line1):"+str(len(items_td_line1))
                    #print "len(items_td_line2):"+str(len(items_td_line2))
                    column_count = len(items_td_line1)
                    #엑셀 헤더 정의
                    
                    
                    for col_candidate in range(4, len(items_td_line1)-3):
                        
                        if items_td_line1[col_candidate] != "" :
                            #print  "col_candidate["+str(col_candidate)+"]"+items_td_line1[col_candidate]
                            party_name = str(items_td_line1[col_candidate]).split("_")[0]
                            candidate_name= str(items_td_line1[col_candidate]).split("_")[1]
                            candidate_votes_count = str(items_td_line2[col_candidate]).split("_")[0]
                            items_final.append(
                                               (election_name,election_number,election_date,
                                                election_area_name, election_area_total_people_count,election_area_votes_people_count,election_area_votes_people_ratio,
                                                party_name, candidate_name, candidate_votes_count))
                       
                    #정리 끝나면 변수리셋
                    items_td_line1 = ["",]
                    items_td_line2 = ["",]
                        

                #END IF count_tr %2 == 0:
                #print "END TR" + str(count_tr) + "\n"
                
    print "Done"
    #File CSV WRITE TEST
    filesave_csv_1(file_name_excel, items_final)
    
    #######################################################
    #cityCode LOOP END
    #######################################################
    
    
    
if __name__ == '__main__':
    
    #[ STEP 1 ]
    #개표현황(결과자료) 데이터 HTML 파일로 다운로드
    #cr_election_open_status()
    
    #개표현황(결과자료) 데이터 HTML 파일 => 저장
    #cr_election_open_status_analysis()
    
    #개표현황(결과자료) 데이터 HTML 파일 파싱 후 CSV 저장
    
    electionName = "20120411"
    #cityCode = "1100"
    for cityCode in cityCode_Arr:
        #print cityCode
        cr_election_open_status_parse_writecsv(electionName, cityCode)
    

    
    
    
    

