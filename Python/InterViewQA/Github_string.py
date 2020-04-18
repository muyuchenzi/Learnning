import re


def string_demo():
    string_var = "djfajfweuriuer0938435987197@#%^$^&%%)(*(&(&%^^%$%^$^*&)&(&fdajfuadojfdurq"
    # string 自身的方法
    # string find
    string_var.find('0938435')
    string_var.index("0938435")
    string_var.rfind("0938435")

    string_var.replace(r"\d", "[number]")
    numb = re.findall(r'\d{2}', string_var)
    sss = re.sub(r'\d', "[number]", string=string_var)
    #
    # 
    # re.match() 从头开始查找一个pattern，然后返回类似于与StartWith，好像没有什么特别的用处 返回一个Match Object
    ss = re.match('123', '123djaffd123')
    # re.search() 从头开始 返回一个Match Object
    tt = re.search('123', "djaffd123")
    # re.findall
    ff = re.findall('1.3', '143djaffd123')
    # string
    sting_examp = "_aai0efe00"
    string_examp='___dfjalfjioeurdjfjdajf23098490839s'
    pattern = r'^[a-zA-Z_]?.*?\d+$'
    res = re.findall(pattern, string=string_examp)
