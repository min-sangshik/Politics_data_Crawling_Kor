#-*- coding:utf-8 -*-
'''
Created on 2016. 3. 24.

@author: SangShik
'''

from bs4 import BeautifulSoup
import urllib
import csv

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

if __name__ == '__main__':
    
    #[ STEP 1 ]
    #개표현황(결과자료) 데이터 HTML 파일로 다운로드
    #cr_election_open_status()
    
    #개표현황(결과자료) 데이터 HTML 파일 => 데이터만 추출
    #cr_election_open_status_analysis()
    
    
    #######
    #TEST AREA
    electionName = "20120411"
    cityCode = "1100"
    
    print "try file open  electionName="+electionName+" cityCode="+cityCode
    html_data = fileopen1("Election_Open_Result_"+electionName+"_" +cityCode+".html" )
    #print "[DATA] "+html_data   
    
    #http://www.dreamy.pe.kr/zbxe/CodeClip/163266
    soup = BeautifulSoup(html_data, "html.parser")
    divregion_top = soup.find_all("div", "cont_table") #<div class="cont_table">
    for trdata in divregion_top:
        
        trs =  trdata('tr')
       
        for tr in trs:
            print "START TR"
            tds = tr('td')
            for td in tds:
                print "[TD]"
                print td
            print "END TR\n"
    print "Done"
    

