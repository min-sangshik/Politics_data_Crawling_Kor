'''
Created on 2016. 3. 24.

@author: SangShik
'''

from bs4 import BeautifulSoup
import urllib

# TEST 
thisurl = "http://info.nec.go.kr/electioninfo/electionInfo_report.xhtml"
param = "?electionId=0000000000&requestURI=/WEB-INF/jsp/electioninfo/0000000000/vc/vccp09.jsp&topMenuId=VC&secondMenuId=VCCP09&menuId=VCCP09&statementId=VCCP09_%232&oldElectionType=1&electionType=2&electionName=20120411&electionCode=2&cityCode=1100&townCode=-1&sggCityCode=-1&x=35&y=12"
handle = urllib.urlopen(thisurl+param)


html_gunk =  handle.read()
print html_gunk

soup = BeautifulSoup(handle.read(), "html.parser")


