import requests, ddddocr, time

# 初始化ocr对象，只初始化一次！不要循环里面反复new，会很慢
ocr = ddddocr.DdddOcr(show_ad=False)
bj = 1
while bj:
    count = 0
    headers1 = {
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "accept-encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Host": "47.83.149.21:10099",
        "Pragma": "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    }
    url1 = 'http://47.83.149.21:10099/auth/checkcode?t=' + str(int(time.time()*1000))
    response = requests.get(url=url1, headers=headers1)
    cookies = response.cookies
    content = response.content

    # 识别普通字符验证码
    yzm = ocr.classification(content)
    print("验证码结果：", yzm)
    print(cookies)

    headers2 = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "accept-encoding": "gzip, deflate",
        "content-type": "application/x-www-form-urlencoded",
        "Connection": "keep-alive",
        "Host": "47.83.149.21:10099",
        "origin": "http://47.83.149.21:10099",
        "Pragma": "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    }
    url2 = 'http://47.83.149.21:10099/auth/checklogin'
    data = {
    'ProxyIp': '47.83.149.21',
    'GameID': 'sfeis123',
    # 'GameID': '白开水123',
    # 'Password': 'csp1989123',
    'Password': 'csf1989',
    'GameCode': yzm,
    }
    response = requests.post(url=url2, headers=headers2, data=data, cookies=cookies, allow_redirects=False)
    if response.status_code == 302:
        print(response)
        print(response.cookies)
        url3 = "http://47.83.149.21:10099/api/sign/info"
        response = requests.get(url=url3, headers=headers1, cookies=response.cookies)
        signs = response.json().get("sign",[])
        for i in signs:
            if i.get("status") == 1:
                day = i.get("id")
                url4 = "http://47.83.149.21:10099/api/sign/dosign?day=" + str(day)
                response = requests.get(url=url4, headers=headers1, cookies=response.cookies)
                print(response.text)
                print(day)
                break
        # break
    count += 1
    if count >= 20:
        break
