import pymysql
import os
import json

file = os.path.abspath('..\..\instagram hashcrowler\Crawler') + "\output.json"
json_data = open(file, encoding="utf-8").read()
json_obj = json.loads(json_data)


def validate_string(val):
    if val != None:
        if type(val) is int:
            return str(val).encode('utf-8')
        else:
            return val


con = pymysql.connect(host='localhost', user='root',
                      passwd='', db='br24_crawler')
cursor = con.cursor()


# parse json data to SQL insert
for i, item in enumerate(json_obj):
    Post_URL = validate_string(item.get("key", None))
    Image_Url = validate_string(item.get("img_url", None))
    Caption = validate_string(item.get("caption", None))
    location = validate_string(item.get("location", None))
    Hashtags = "hashtag"
    Description = "desc"
    cursor.execute("INSERT INTO crawler (Post_URL,	Image_Url,	Caption, Location,Hashtags,Description) VALUES (%s,	%s,	%s, %s, %s, %s)",(Post_URL, Image_Url,Caption, location, Hashtags, Description))
con.commit()
con.close()
