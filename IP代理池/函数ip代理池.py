import requests
import parsel
import pprint
import time


def check_ip(proxies_list):
    '''检测代理ip质量的方法'''
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }

    can_use = []
    for proxy in proxies_list:
        try:
            response = requests.get('https://www.baidu.com', headers=headers, proxies=proxy, timeout=0.1)
            if response.status_code == 200:
                can_use.append(proxy)
        except Exception as e:
            print(e)

    return can_use


proxies_list = []
for page in range(1, 5):
    print(f'=====================正在抓取第{page}页数据=====================')
    url = f'https://www.kuaidaili.com/free/inha/{page}/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }

    response = requests.get(url=url, headers=headers)
    data = response.text
    # print(data)
    # 解析数据--parse1   转化成Selector对象，Selector对象具有xpath的方法
    # 转换数据类型
    html_data = parsel.Selector(data)
    # print(html_data)
    # parse_list = html_data.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr').extract()
    parse_list = html_data.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')
    # pprint.pprint(parse_list)
    # 代理ip的形式：{‘协议类型’：“ip：端口”}

    for tr in parse_list:
        proxies_dict = {}
        http_type = tr.xpath('./td[4]/text()').extract_first()  # 协议类型
        ip_num = tr.xpath('./td[1]/text()').extract_first()  # ip
        port_num = tr.xpath('./td[2]/text()').extract_first()  # 端口
        #     print(http_type,ip_num,port_num)
        proxies_dict[http_type] = ip_num + ":" + port_num
        #     print(proxies_dict)
        proxies_list.append(proxies_dict)
        time.sleep(0.5)

print(proxies_list)
print('获取到的代理ip数量:', len(proxies_list), '个')

can_use = check_ip(proxies_list)
print('能用的代理ip：', can_use)
print('能用的代理ip数量：', len(can_use))
