from tools.api import request_tool

# post请求json数据 用户注册
# def test_post_json(pub_data):
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '用户注册'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/signup"  # 接口地址
#     # post请求json数据，注意数据格式为字典或者为json串 为空写None
#     json_data = '''
#     {
#
#   "phone": "15266667666",
#   "pwd": "t1234567",
#   "rePwd": "t1234567",
#   "userName": "t1234567"
#
# }
#     '''
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)


# post请求json数据 用户登录
from tools.security.md5_tool import md5_passwd


def test_post_jsonn(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
  "pwd": "t1234567",
  "userName": "t1234567"

}
    '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)


# # get请求键值对数据 查询单个商品
# def test_get_params(pub_data):
#     method = "GET"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '查询单个用户'  # allure报告中二级分类
#     title = "查询单个用户_全字段正常流_1"  # allure报告中用例名字
#     uri = "/acc/getAccInfo"  # 接口地址
#     # post请求json数据，注意数据格式为字典或者为json串 为空写None
#     params = {"accountName":'t1234567'}
#     headers={"token":"eyJ0aW1lT3V0IjoxNTcxMzgyNTQ3MTI1LCJ1c2VySWQiOjQ4LCJ1c2VyTmFtZSI6Inh1ZXBsMTIzIn0=",}
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     request_tool.request(method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

# 增加产品
def test_addprod(pub_data):
    print(pub_data)
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {'token':pub_data['token']}
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
  "brand": "五菱宏光",
  "colors": [
    "红色","黑色"
  ],
  "price": 1,
  "productCode": "自动生成 字符串 4 数字字母 11",
  "productName": "车子",
  "sizes": [
    "100"
  ],
  "type": "工具"
}
    '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    json_path = [{"skuCode": '$.data[0].skuCode'},{"productCode":"$.data[0].productCode"}]
    request_tool.request(json_path=json_path,headers=headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
   # pub_data["skuCode"] = r.json()["data"][0]["skuCode"]
    #pub_data["productCode"] = r.json()["data"][0]["productCode"]
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据


# 修改商品价格，POST请求键值对数据
# def test_changePrice(pub_data):
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '修改价格'  # allure报告中二级分类
#     title = "锁定用户_全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/changePrice"  # 接口地址
#     # post请求json数据，注意数据格式为字典或者为json串 为空写None
#     data = {"SKU":pub_data["skuCode"],"price":6000}
#     headers={"token":pub_data["token"]}
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)






# #根据产品编码批量修改商品价格
# def test_ByprodCode(pub_data):
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '根据编码改价格'  # allure报告中二级分类
#     title = "锁定用户_全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/changePriceByProdCode"  # 接口地址
#     # post请求json数据，注意数据格式为字典或者为json串 为空写None
#     data = {"prodCode":pub_data["productCode"],"price":5555}
#     headers={"token":pub_data['token']}
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)
    # pub_data["productCode"] = r.json()["data"][0]["productCode"]

#全量调整单个商品库存
def test_product_fullSku(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品库存模块模块"  # allure报告中一级分类
    story = '全量修改库存'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/fullSku"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"skuCode":"${skuCode}","qty":"350"}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)


#
# def test_addOrder(pub_data):
#     method = "POST"  #请求方法，全部大写
#     feature = "订单模块"  # allure报告中一级分类
#     story = '无签名无加密下单'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/order/addOrder"  # 接口地址
#     # post请求json数据，注意数据格式为字典或者为json串 为空写None
#     headers = {"token": pub_data["token"]}
#     json_data = '''
#     {
#   "ordeerPrice": "1",
#   "orderLineList": [
#     {
#       "qty": 1,
#       "skuCode": "${skuCode}"
#     }
#   ],
#   "receiver": "xuepl1111",
#   "receiverPhone": "15216668455",
#   "receivingAddress": "安徽省",
#   "sign": "",
#   "userName": "xuepl1111"
# }
#     '''
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     request_tool.request(headers=headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)

#自动生成数据
'''
# 自动生成 数字 20,80   #生成20到80之间的数字 例：56
# 自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
# 自动生成 地址
# 自动生成 姓名
# 自动生成 手机号
# 自动生成 邮箱
# 自动生成 身份证号
# '''

def test_signbody(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "签名下单模块"  # allure报告中一级分类
    story = '签名加密下单'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/order/addOrderSignBody"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    headers = {"token": pub_data["token"]}
    s = "receiver=xuepl1111&ordeerPrice=1&receiverPhone=15216668455&key=guoya"
    sign=md5_passwd(s,"")
    pub_data["sign"] = sign
    json_data = '''
    {
  "ordeerPrice": "1",
  "orderLineList": [
    {
      "qty": 1,
      "skuCode": "${skuCode}"
    }
  ],
  "receiver": "xuepl1111",
  "receiverPhone": "15216668455",
  "receivingAddress": "安徽省",
  "sign": "${sign}",
  "userName": "xuepl1111"
}
    '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(headers=headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
git config --global user.email "1456181121@qq.com"
git config --global user.name "tanjf1"