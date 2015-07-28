from datetime import date, datetime, timedelta
import random
import HTMLParser
def ASCII_String_Decode(ascii_str):
    h = HTMLParser.HTMLParser()
    return h.unescape(ascii_str)

def UTF8_String_Decode(str):
    return str.decode('UTF-8')
	
def ConvertScalarToList(str):
    return str.split(',')
	
def Get_Random_Key_From_Dict(dict):
    return ASCII_String_Decode(random.choice(dict.keys()))	
	
def Get_Random_Value_From_Dict(dict):
    return ASCII_String_Decode(random.choice(dict.values()))
	
def Get_Random_Item_From_List(list):
	return random.choice(list)
	
def Is_Leap_Year(year):
    """return True if leap year; else False"""
    if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
	    return True
    else:
        return False
		
def Generate_Travel_Plan_Date(no_of_days):
	no_of_days=int(no_of_days)
	tmpdate = datetime.today() + timedelta(days=no_of_days)
	tmpdate=str(tmpdate)
	newdate=tmpdate[:10]
	newdate=newdate.split("-")
	intended_date=newdate[2]+'-'+newdate[1]+'-'+newdate[0]
	return str(intended_date)
	
def IsOneYearGone(strdate):
    cdate = datetime.strptime(strdate, '%d-%m-%Y')
    tmpdate = cdate + timedelta(days=365)
    return datetime.today() > tmpdate