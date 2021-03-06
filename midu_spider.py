# coding: utf-8

import requests

session = requests.session()
session.headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'Content-Length': '1366',
    'Host': 'api.midukanshu.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.11.0',
    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHAiOiJNaWR1IiwiZGV2aWNlIjoiMzJiNGI4ZTg5MTU4NzIwZiIsImdlblRpbWUiOjE1ODE2NzUyMzgsIm5vbmNlIjoiYnAzNzVwamw1MzMzcmFkb3B2NGciLCJ1aWQiOiI5ODYzMTQyMDIifQ.DutSkIVYGGHlDqIUHBQe35CS9fIPv2p9l4cY55uRL4c'

}


def getParam(str1):
    list1 = str1.split('&')
    r = dict()
    for l in list1:
        r[l.split('=')[0]] = l.split('=')[1]
    return r

str_ = 'app=midu&dataEncStr=M0UxQ0MyM0NDRDgyNDNGQzlCMzRBQjA1QUQzMzhGREMuY0dGeVlXMGZOemxqTmpReU9UVXRNalZtT0MwMFpEWTNMVGhsWVdZdFl6SXlORE5oWldZMk9EUTFIblpsY25OcGIyNGZOQjV3YkdGMFptOXliUjloYm1SeWIybGtIbVZqSHpFPS4bntKDw5A9YxCb1b1BgZ2da8OF1kHm7roreZ7i6Y72Cgubf8Qn9moRO9SpbqA8412dmlfjS+N//nQsIb0BE1bKv7qJ/ySVjhr0/HsJlbFwArjuETc9KYQLB9lTpp1L0529DnbGjMmcm866Hg6K4qLjbl/dqcBweGs8O8JXgz9OmRa8VTLzSo5snjAy6zAGVeha1q13/GbUj/TsKlGz75kvQb8KbnXx69+vw/v9X26bcLRZ4IgxXFFvWWac6XAVCVa7ruJcWlNNRekFrIkrUzhMWfgB3K45HtNkfmyr773s9GHEoUy6g4AYo/evjhBRA9KJDikueupF+y61htUYVwi5+GsGw2hxtI39PT+u4NYYtuUpVGAL97qW9BMOtz7Cw4tc8KJPENy/8AyyY2PXS3QHSRkQaN0NBwqhUsuZU42CCOHzp00Ng39IBOoGBJnUNLyPWe1VQVRDgFWFaFz3JPYvFR8/qLDvgYx6TUBgi2zGHinFm6rR2t2R/SFAHVb92iMr0HGHXOEi4bWSO12xoLMnB2UKjyL+X8F57kGbJgXlnr5SAZwknSrIx69si4NDMpDmKwNK3hA/a135jJv6OrJi9h60F5mzqCdwlqcrdcGvu9whh9tR99jnNqutzU675ZMVI2hoTF3hgyy4wbB6CJQCsFyUPCs55RZKdIYND65S31z8CnAaU8hi01Z79b6GZWsBTwaY/ptovUmFzg84ZWi4iR+jSHPSWPF1a//+QBjO+hI3Kj/UPOkRxxuVR8Z9LnSPhPbYpTntq6piF8iq1F7+I/QZ0CchiEOGUX/CshWxPV8iEB6ZWA9Z19DbvyGJzIPaNpzVBV4NvPUmW/5/Y6O/F83h8JnXQYJodhKH/xVFKPjr9SuM3YkQiLBUjc15d/**ND7l/ADz3ey1tCPYc/7VL5MVxDB79IxO6sFORBh3sq7YxcjpjJW59CX+FsH3w8OsMLq49T7zNT+Y5mHPaqOdWTW0LaFaQPGVzw57vIZ+1iQ3qF2eJ2b1V4Uf7I9IjWXaEA=&dtu=yingyongbao&version=530&versionName=5.3.0.0117.1827&sign='


str_search1 = 'app=midu&dataEncStr=NDNBNUJDNUJDQzZEOTY2MjgzMzk0QTRGRTM5RTZBRDcuY0dGeVlXMGZPR00zWW1KaE1tWXROV0V4T0MwMFlXWTJMVGsyTXpNdE9EVmpZMk13WXpaa016WmtIblpsY25OcGIyNGZOQjV3YkdGMFptOXliUjloYm1SeWIybGtIbVZqSHpFPS7m95dM8ggb7HIo/GaytYzb1I6Q81l8JzFNx2oN92NhrgE4YsWTxyT8TxJ8Ja9Qsj7PY8/6JTscOAU1HIANVQfyO26MuE/XZupuwa4ZSL+LmMY/7PVW+4EYvV3vEo0A8JtTSo5EaBHVp8qxED6x/ACaL2qSFbsJakC79Ktew2T7VCuPoQX4pq+NsCF2vHRuTi2KhvL1Btqr0ZMr98Lt5xRt3vNhrHwd87Ddp8lPqSf3+O20B66ZxrAp2hvRC5VIgyGNOudKNPpzkTxGxgmSoDxnrEzlnx0ZZL1Ur8/IlvInEOpZEb+hXkeRorQ8SGoHucbRbKYBFmVgu7maeRRE02uBrWMFotckHng69rLd/RXeIhvVsrPUIFsSyU5ioo5ED2soNv4am6vMND1/OkV0VIC7eOWsBKWQYL+DCSsZcA+U8YL5LWYkO1A8Nwx8g3mSa1wIon4XauoVU9bYNmUK4/0QP+87RotGPgpFtpY3QF2nGzr/ZCiOQINu6L1/sM+EiDm4LQ1QfKr7yWyfqxXbzJ32q9Z+d2tQ3qhkF/fy465Nv7LACVqfOAKCOliBDCmNVYvUNlzImuzy9LAvzy9CIuz4OSBJcFWTC9eQKxVUw64TYOw94xh5m5rhAx0UxUjZSC43WtHhw24L2hbs2Mt0vNcD5AST+MNTW2zr3HMnxhWrFY3RzT1Femjog7E7ZNhPAoMLa0qnVJPGLuadTwsSNgepsQxYdYvNDL+HM27xrHz2hUIVp7qmLxwE/4AytONg6/OvAkHg9qj+L0bbovzkJ0oRBRO4pJiYbjmXfY/uz4RBs5IWlN0sELZk7v4Qo11IpTEXdHOnZMhP1y2C4M5JEU8d7BpNtBfENB7iOWQ5OasiTdbbJw7AvEBz8hefeGqzwAgdOIxK0q6cGIyDFEur4So4we3oAEObKSbuTzuyPK+Rz2jZhznVzp2QKY7JDEGowwHAx3pENVMtywejHxdTJHwaz7oW&dtu=yingyongbao&version=530&versionName=5.3.0.0117.1827&sign='

# str_ = 'app=midu&dataEncStr=RTc4RTBFQTRCNDk0MzE3NDYzNjRBNjc3MDY0MTQwNUQuY0dGeVlXMGZPV05qTVdRMk5tUXROVFExTXkwME9UUTBMV0ZpTW1NdE5tTmxORFV5T0RRek5ERmpIblpsY25OcGIyNGZOQjV3YkdGMFptOXliUjloYm1SeWIybGtIbVZqSHpFPS6/ylsJ2pdtVemDmhxzJ4+QY/vBpFIF3rqoBF5z9lENC99Y0nDcxqS+nG31avafmmEIzMnyQW7L4ItAmMa7e4VVwzsqmtEo4FdzLdQ1JkOTZgc3hMcnUwX0xlCbA41COcW8Gj36q/H1OyFwjFfVse4amcXRnjwYDezBZ5eU93snzyDXtj4pgEzH//z0oZWZP0Ss3HyVOCvsuGP9PUAgZmsgQY8U5gmN3zzDfpMUnkOqD39rmBqXxkEcdJZADuQz5V9BGBepg3krgVyuYPcPYYYuEoZUpKB7MkN+79xK2HPh6YlKJq8v3084wc8b2vZZXA1k1d4QkzDDrwQYPwXmfk2LzDmmC3TLmSmaqCp8+k5gpBL2o6Xtaiw4ZeD7uis9j/A59CPc9Snrg4beCQWA7Vwzv2QTJMEG1QMXppQvLJNAqO81lRyizq3xvt8qJobLlO141yr5PGRzkRIEto+KOns/CvGd7RQiqnkOVoY1wxFFNhWxdQ+F1iwvPDb7UD139LlefbPM5DH0p/8AKeiCFa4ojDiyGAWf+/YP1nJbqdvQdNaUdR5rrhRWIeSZc944y/Dbxh9RNEz0O+kxOSvKpcl5buM3GlkZH5bpRyjc4/OC56hBWoKnmypcLT6j/3Yqf5wkaG0qBpx+/8s7j8+AgO9N3jGfDCkcD3j6v4y+sbw2aqklpXvKNBx8mqte/EYZq8K+DTcILTqkB73ndnYFC/I2U5oPCYz4tQ2YXcU3dDFqOj/z3IB3WCMbHTy4f5BarIO0pjJxf1KjJDua5cbv0LsUDejbzbMnIz61FAC6rQOz4Rtt4ZPpcMm3GvKzegp3oS2c6ixkbeaTYq75Eh+a1guxS4eVD1e1Ggjt/gwkd9o3KT+mS2eQM7X3u0doSRXYfsONV4x21ugCE1vn1+SYEn+wBukpk+WJHnpr47NUREc3TrreGyKoCtVMeNwQS/NYC3XnRIISnNbIKQDn3a9jNo7/ORLBhK7hWbx6PNUDoN1hn7SOaB9DJKsaqhExXK+4TcyWWTSKTPZS50sSmr29zAYms9wcL6Tyt3+NTv2ZWYvdA2IlSgV40/0CsDg9TOHqJea7gLBqmM7CsQ8F/WerOMSKqsKE8h4Rd4zn3MibxN0HdlE8dg==&dtu=yingyongbao&version=530&versionName=5.3.0.0117.1827&sign='
str_ = 'app=midu&dataEncStr=NDYwQUI4NDI4MjJBMjMzOTg0NDEzRDY0N0FFNzE3ODYuY0dGeVlXMGZOemc1TjJRNFpXSXROelJtWkMwMFltUXdMVGxtT0RZdE1qbG1aV1ppTUdNMU56QTBIblpsY25OcGIyNGZOQjV3YkdGMFptOXliUjloYm1SeWIybGtIbVZqSHpFPS6lp84unwfxAnmaAzmks4Ur15jNdl2kqUSX+kW08xYP269RbPBpgVbkbWmEMa95NVX03QBrItCQzAvgMHuRnGQlonC4eAOhERI+Q5E2qY74tSaVTxOMSDas7Janadapl+SET+kzkAosS24W2h+k7Z+kfLYPfQ/oSKBnsLOMO+XpwIitOTT3D0MYhTQU1zZciodqhg+l35IGg8IcWy7u3xi7nq0uDZffVInJsQh4xE6HFJpdpLE7G+NVzA4HYYXS1MM9EwnOx/0MsBmMbBRh9NfE5IrCmtGbc0JYHhXRj+7MZGeNocujzYslV8Um9bpym5X/Fpv3kXLHF52iVIqAupyBXHkp4amLRIiRj7uALhHQsvuNhrDMqcjYJMaJPnFQqQFF8wh9x1mO3RVjPBuGhM+Dgd66jhlJ6kibeXduxfJN+rLuK5ZXQWvh2Jy+wDyDinZs+HSeeLJ2oyR0MEV2QRv2DH26BQ3D+By+pPjSh8DxVEKTr+M2WEJiu/gd+SQzsUuVJ2KSxkD2QVeZHSkk2oBsJ9bMzkYiIJoJtCoI5fFABXbdRvpMO7d/GpwfMBDtXzwNAuZBqVW+DgBNRt6RFh6kZwBjtVGJzd7N01SkNo8gl+zBVkdSELZuwxQmgFvNnh9lrnsVLVShdh2j8IlClARhKpgPbSshv29XsmKFZk7WR+1FR3nVT3lbo1f74eGrnzNQHt1tjUYxWDa6TXQnABXFBfD/3OVS9kbhtRHa+l/+IV7xaPWWzPI0/D/Qtqm1BZYCrOJPMCAEN7xWKFAusUTUA11HQZMEkUfnRQX8xmopAor3fyYebUtJUba0UACH2MTTk2PTLISYfsyC7P0RGLKOGc7wL9UdT00LzRkSk+qffpEfUI/BWG9QlXrd4dn/1afrzVWxHUE7Xt/xuGYwh16v4Pn9ntnKYj3aELMhciwl8P/g4Taw5VHT0TA7c9VOmPvv1tI2BthvlfLzJpT8EM9N0MrNzUKras3VtgZ7VrQXKrLm7PlGANk0NugwVNC7fLNiUsQ=&dtu=yingyongbao&version=530&versionName=5.3.0.0117.1827&sign='



str_detail = 'app=midu&dataEncStr=QzBGRjhBRUUyODAxNDBCMzgwNTgxMzA5REQ5MUNCMEIuY0dGeVlXMGZZV1l4TkRWaU5USXRNV0ZrTXkwMFl6VmxMV0poWVRNdFpXSmtNV1ZrTkRVMlkyWXpIblpsY25OcGIyNGZOQjV3YkdGMFptOXliUjloYm1SeWIybGtIbVZqSHpFPS4yEakVkhmBlAL+SbMGbXm18LTZnrim/2VzUcKg5XvZ6+iC74M1mjSdlNl/zkzZoteYg5RMDDVsxZyQln8i8UbsebfpUD+szpj6wvMfCuDkKwc5F1XaspGmKDYVX9wLJkYUSKnvTd9ByaEW0zU4suU3YFRKut/Fs6uqtuQ8yUIoXFNd5SNOf6I/j3pv66YHJVudzVzGZJX2S57wWTsMaE3xEkURUwYPvsKSxHC/tVXxPzbqq5wAvGDK1tI9**AO2j0NV99IFYsjaaeWR8ebGau+DQT0w/gdX40O0i176J10/PER5GEheN4rMJyyNubLZG0gKkjfxslkKlUQV0DIJYUllSAcnbj+Kpuu12XwJ5AS+PspOpZvtGg1UQRjiO5XMiE67bwYLOjVhRvmHb6kOwBtZH39mw58kwo1YAfxghUYXkWYGDe5r8mvS/70rSU0BHIjDs2B0Zqj0XlIvSXopA/3y6KaCN70BCQ8cZJW2U9ZNF9geVy2D8O/s/lmoJvYkV2AyhI/ZwWOglQ7pwU6C4/tCuy6nBGC0cyX4h5sqcxBTCB5XdJtKRFDSeB9wJDRlSM33B9rILwJLamoF2NwAXnue4TuhbfadHz9J3NHI87RLChBsOMc8pEOSi4EDG5c0q/7qdMIKOBOiDOzDEvX+ZtjaRi2kFSv76FyH8/TfXVcwmihr4a3cNA6iucFdb/vMYW/6XQqXMEVHCrDpC+gk+pZ7n3Po5CA9QPNYNXefaksgro1RP296k7HyvUQougYqlLrHu2eCuQbGcMqfunm13Vhe+VbXtOF9HeSpVgApBR2WBKJ+VZISefsRzH1hNbFPasaVnU2lVQ1t0bzUNq5la3HiituYsQvVhIIsKlOCIvsKMigYGUBCQJopn8PlE3XgBHWhM/IRlitCqHrg6maVdxgkkU41skeWQCKlSjj66h7XLGs3fp7Zd6o6jzYsccyxZCpVNQbPLj8HXyp+PAKYEiimJaCZ208QRNDyPW0qa4XRbmN6korOi9FV4aU/upjEbDAlsXJ1sSbkmn3F/WovTNaWFV7Jbkjca0SX/cpl5UQeIWuCbzlmG0JOe/fPJSc9SHf5Q+pE8DJYXnKwA+AmwCmMQD2fUFjq1pmM68K3greONJDw==&dtu=yingyongbao&version=530&versionName=5.3.0.0117.1827&sign='

param = getParam(str_search1)

# url = 'https://api.midukanshu.com/fiction/book/getChaptersCdn'
url = 'https://api.midukanshu.com/fiction/search/search'
# url = 'https://api.midukanshu.com/fiction/book/getDetail'  # 没有具体内容信息
# url = 'https://api.midukanshu.com/fiction/book/getTextCdn'

param['token'] = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHAiOiJNaWR1IiwiZGV2aWNlIjoiMzJiNGI4ZTg5MTU4NzIwZiIsImdlblRpbWUiOjE1ODE2NzUyMzgsIm5vbmNlIjoiYnAzNzVwamw1MzMzcmFkb3B2NGciLCJ1aWQiOiI5ODYzMTQyMDIifQ.DutSkIVYGGHlDqIUHBQe35CS9fIPv2p9l4cY55uRL4c'
r = session.post(url=url, data=param)

data = r.content
print data
