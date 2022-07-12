import requests
import re
import parsel

# css选择器提取
lst = []
lst_1 = []
for page in range(1,3):
    headers = {
        "Cookie": "Hm_lvt_f9e56acddd5155c92b9b5499ff966848=1655634222,1656153695; https_waf_cookie=6653a5a2-ec39-448d3126e0c1a8a03162339c045ce57ca58c; Hm_lpvt_f9e56acddd5155c92b9b5499ff966848=1656154659",
        "Host": "www.89ip.cn",
        "Referer": "https://www.89ip.cn/index_3.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br"
    }

    url = f"https://www.89ip.cn/index_{page}.html/"

    response = requests.get(url=url,headers=headers)
    selector = parsel.Selector(response.text)
    # print(response.text)
    ip_list = selector.css('.layui-table tbody tr td:nth-child(1)::text').getall()
    port_list = selector.css('.layui-table tbody tr td:nth-child(2)::text').getall()


    for ip, port in zip(ip_list, port_list):
        http = ip.strip() + ":" + port.strip()
        proxy_dict = {
            "http":"http://" + str(http),
            "https":"https://" + str(http)
        }
        lst.append(proxy_dict)
        try:
            response_1 = requests.get(url="https://www.89ip.cn/index_2.html",headers=headers,proxies=proxy_dict,timeout=2)
            if response_1.status_code == 200:
                print('IP代理可以正常使用',proxy_dict)
                lst_1.append(proxy_dict)
        except Exception as e:
            print(e)
            print(proxy_dict,'IP代理链接超时，无法使用')

print(f"总共获取代理{len(lst)}")
print("---***---"*30)
print(f"获取可以使用的代理{len(lst_1)}")

#快代理 正则抓取数据
'''
lst = []
lst_1 = []
for page in range(1,3):
    headers = {
        "Cookie": "channelid=0; sid=1655567074391981; _gcl_au=1.1.2121027610.1655568021; _ga=GA1.2.56395521.1655568022; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1655568021,1655630171,1656147066; _gid=GA1.2.1151226112.1656147066; _gat=1; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1656147074",
        "Host": "free.kuaidaili.com",
        "Referer": "https://www.kuaidaili.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br"
    }

    url = f"https://free.kuaidaili.com/free/inha/{page}/"

    response = requests.get(url=url,headers=headers)
    # print(response.text)
    ip_list = re.findall('<td data-title="IP">(.*?)</td>',response.text)
    port_list = re.findall('<td data-title="PORT">(\d+)</td>',response.text)
    for ip, port in zip(ip_list, port_list):
        http = ip + ":" + port
        proxy_dict = {
            "http":"http://" + str(http),
            "https":"https://" + str(http)
        }
        lst.append(proxy_dict)
        try:
            response_1 = requests.get(url="https://www.zhihu.com/",headers=headers,proxies=proxy_dict,timeout=2)
            if response_1.status_code == 200:
                print('IP代理可以正常使用',proxy_dict)
                lst_1.append(proxy_dict)
        except Exception as e:
            print(e)
            print(proxy_dict,'IP代理链接超时，无法使用')

    print(f"总共获取代理{len(lst)}")
    print("---***---"*30)
    print(f"获取可以使用的代理{len(lst_1)}")
'''


# url = "http://tiqu.pyhttp.taolop.com/getip?count=1&neek=38626&type=2&yys=0&port=1&sb=&mr=2&sep=0&ts=1&time=2"
# json_data = requests.get(url=url).json()
# ip = json_data["data"][0]["ip"]
# port = str(json_data["data"][0]["port"])
# http = ip + ":" + port
# proxy_dict = {
#     "http":"http://" + str(http),
#     "https":"https://" + str(http),
# }
# response_1 = requests.get(url="https://www.luffycity.com/play/31111",headers=headers,proxies=proxy_dict,timeout=2)
# print(response_1.status_code)


dit = {
'http': 'http://139.9.64.238:443',
'https': 'https://139.9.64.238:443',
}