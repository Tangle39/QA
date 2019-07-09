*** Settings ***
Documentation     接口测试
Suite Setup
Library           RequestsLibrary
Library           Collections

*** Variables ***
${api}            https://bot.testing2.ifchange.com/api    # api
${data}           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

*** Test Cases ***
登录
    create session    api    ${api}
    ${req_url}    Set Variable    /dhr_auth/login/account
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"account": "ze.dong@ifchange.com", "password": "aipm2018"}}}    #登录之后返回session，一周有效
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    To Json    ${response.text}
    ${return_response}    get from dictionary    ${result}    response
    ${return_results}    get from dictionary    ${return_response}    results
    ${return_session}    get from dictionary    ${return_results}    session    #利用Collections中的get from dictionary获取session
    ${return_err_no}    get from dictionary    ${return_response}    err_no
    should be equal as strings    ${return_err_no}    0
    set suite variable    ${Session}    ${return_session}    #似乎不区分大小写    #设置suite变量

添加员工
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/staffs/create
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "${session}", "name": "位娟", "no": "14", "sex": 2, "phone": 18966668848, "email": "weijuan@ifchange.com", "department_id": 7, "position_id": 8, "status": 2}}}
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}
    ${result_json}    To json    ${response.text}    pretty_print=True
    Should Contain    ${result}    该工号已存在
    Delete All Sessions

添加部门
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/departments/create
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "${session}", "name": "AI测试", "parent_id": 6}}}
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}

添加岗位
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/positions/create
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "${session}", "name": "岗位2"}}}
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}

部门列表
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/departments/list
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "${Session}"}}}
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}
    ${result}    To json    ${response.text}    pretty_print=True

新增部门
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/departments/create
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "${session}", "name": "AI测试1", "parent_id": 5}}}
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}
    ${result_json}    To json    ${response.text}    pretty_print=True
    Should Contain    ${result}    部门最多

图片验证码
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_auth/captcha/get
    ${data}    Set Variable
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    To json    ${response.text}    pretty_print=True

更新员工
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/staffs/update
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "${session}", "id": 101, "name": "卢唐乐", "no": "1114", "sex": 1, "phone": 15221286041, "email": "tangle.lu@ifchange.com", "department_id": 7, "position_id": 8, "parent_id": 16, \ "birthday": 745977600, "education": 7}}}
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}
    ${result_json_2}    To json    ${response.text}    pretty_print=True
    Should Contain    ${result}    "err_no":0
    Delete All Sessions

员工列表
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/staffs/list
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "eyJmcm9tIjoiQiIsInNyY19pZCI6MSwibWFuYWdlcl9pZCI6ODAsImNvbXBhbnlfaWQiOjgwLCJ1c2VyX2lkIjo3NCwiZXhwaXJlIjoxNTYyNjM4NDgxLCJzaWduYXR1cmUiOiI5ODA4YTM3ZDMxODI5YmE2NDY4ODAzNGNlMmYyM2EyYzk4OTJlYjg4IiwidXNlcl90eXBlIjoxfQ=="}}}
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}
    ${result_json_2}    To json    ${response.text}    pretty_print=True
    Should Contain    ${result}    0
    Delete All Sessions

下载模板
    create session    api    https://bot.testing2.ifchange.com/api/dhr_manager/staffs/download_template
    ${response}    Get Request    api    ?session=eyJmcm9tIjoiQiIsInNyY19pZCI6MSwibWFuYWdlcl9pZCI6ODAsImNvbXBhbnlfaWQiOjgwLCJ1c2VyX2lkIjo3NCwiZXhwaXJlIjoxNTYyNTY1NTc4LCJzaWduYXR1cmUiOiI5ZWQ2OWFiYzI3NmJkNWE5NzUwZTAyMjU1NDg1OWY3OGMyMzQ5NzBiIiwidXNlcl90eXBlIjoxfQ==
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}
    Delete All Sessions

批量导入
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/staffs/import
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "${session}", "data": "${data}"}}}    #data为excel转码的字符串，数据过大，输入会闪退，采用了变量的形式
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}
    ${result_json}    To json    ${response.text}    pretty_print=True
    Should Contain    ${result}    "err_no":0

员工离职
    ${headers}    create dictionary    content-Type=application/json    #定义头部信息
    create session    api    https://bot.testing2.ifchange.com/api    ${headers}
    ${req_url}    Set Variable    /dhr_manager/staffs/quit
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "${session}", "id": 79}}}    #已离职的员工则是拒绝请求
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}
    ${result_json}    To json    ${response.text}    pretty_print=True
    Should Contain    ${result}    拒绝请求
    Delete All Sessions

岗位下拉列表
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/positions/drop_list
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "eyJmcm9tIjoiQiIsInNyY19pZCI6MSwibWFuYWdlcl9pZCI6ODAsImNvbXBhbnlfaWQiOjgwLCJ1c2VyX2lkIjo3NCwiZXhwaXJlIjoxNTYyNjM4NDgxLCJzaWduYXR1cmUiOiI5ODA4YTM3ZDMxODI5YmE2NDY4ODAzNGNlMmYyM2EyYzk4OTJlYjg4IiwidXNlcl90eXBlIjoxfQ=="}}}
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}

部门更新
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/departments/update
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "eyJmcm9tIjoiQiIsInNyY19pZCI6MSwibWFuYWdlcl9pZCI6ODAsImNvbXBhbnlfaWQiOjgwLCJ1c2VyX2lkIjo3NCwiZXhwaXJlIjoxNTYyNTY1NTc4LCJzaWduYXR1cmUiOiI5ZWQ2OWFiYzI3NmJkNWE5NzUwZTAyMjU1NDg1OWY3OGMyMzQ5NzBiIiwidXNlcl90eXBlIjoxfQ==", "id": 7, "name": "AI测试", "leader_id": 16, "hrbp_id": 15}}}
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}
    ${result_json}    To json    ${response.text}    pretty_print=True
    Should Contain    ${result}    0

部门下拉列表
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/departments/droplist
    ${data}    Set Variable
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}
    ${result_json}    To json    ${response.text}    pretty_print=True
    Should Contain    ${result}    0

岗位删除
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/positions/delete
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "eyJmcm9tIjoiQiIsInNyY19pZCI6MSwibWFuYWdlcl9pZCI6ODAsImNvbXBhbnlfaWQiOjgwLCJ1c2VyX2lkIjo3NCwiZXhwaXJlIjoxNTYyNjM4NDgxLCJzaWduYXR1cmUiOiI5ODA4YTM3ZDMxODI5YmE2NDY4ODAzNGNlMmYyM2EyYzk4OTJlYjg4IiwidXNlcl90eXBlIjoxfQ==", "id": 1020}}}
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}

检查部门
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/departments/check
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "${session}"}}}    #检查部门数是否超出限制100个（不传 name） 检查是否存在相同名称的部门（传 name）
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}
    ${result_json}    To json    ${response.text}    pretty_print=True
    Should Contain    ${result}    部门最多添加100个

部门删除
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/departments/delete
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "${session}", "id": 135}}}
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}
    ${result_json}    To json    ${response.text}    pretty_print=True

岗位更新
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/positions/update
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "eyJmcm9tIjoiQiIsInNyY19pZCI6MSwibWFuYWdlcl9pZCI6ODAsImNvbXBhbnlfaWQiOjgwLCJ1c2VyX2lkIjo3NCwiZXhwaXJlIjoxNTYyNjM4NDgxLCJzaWduYXR1cmUiOiI5ODA4YTM3ZDMxODI5YmE2NDY4ODAzNGNlMmYyM2EyYzk4OTJlYjg4IiwidXNlcl90eXBlIjoxfQ==", "id": 10, "name": "前端开发"}}}
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}

检查岗位
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/positions/check
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "eyJmcm9tIjoiQiIsInNyY19pZCI6MSwibWFuYWdlcl9pZCI6ODAsImNvbXBhbnlfaWQiOjgwLCJ1c2VyX2lkIjo3NCwiZXhwaXJlIjoxNTYyNjM4NDgxLCJzaWduYXR1cmUiOiI5ODA4YTM3ZDMxODI5YmE2NDY4ODAzNGNlMmYyM2EyYzk4OTJlYjg4IiwidXNlcl90eXBlIjoxfQ=="}}}    #检查岗位数是否超出限制1000个（不传 name） 检查是否存在相同名称的岗位（传 name）
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}

员工下拉列表
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/staffs/drop_list
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "eyJmcm9tIjoiQiIsInNyY19pZCI6MSwibWFuYWdlcl9pZCI6ODAsImNvbXBhbnlfaWQiOjgwLCJ1c2VyX2lkIjo3NCwiZXhwaXJlIjoxNTYyNjM4NDgxLCJzaWduYXR1cmUiOiI5ODA4YTM3ZDMxODI5YmE2NDY4ODAzNGNlMmYyM2EyYzk4OTJlYjg4IiwidXNlcl90eXBlIjoxfQ=="}}}
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}
    ${result_json_2}    To json    ${response.text}    pretty_print=True
    Should Contain    ${result}    0
    Delete All Sessions

岗位列表
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/positions/list
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "eyJmcm9tIjoiQiIsInNyY19pZCI6MSwibWFuYWdlcl9pZCI6ODAsImNvbXBhbnlfaWQiOjgwLCJ1c2VyX2lkIjo3NCwiZXhwaXJlIjoxNTYyNjM4NDgxLCJzaWduYXR1cmUiOiI5ODA4YTM3ZDMxODI5YmE2NDY4ODAzNGNlMmYyM2EyYzk4OTJlYjg4IiwidXNlcl90eXBlIjoxfQ==", "page": 2, "page_size": 20}}}
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}
    ${result_json}    To json    ${response.text}    pretty_print=True

检查员工
    ${headers}    create dictionary    content-Type=application/json    #定义头部信息
    create session    api    https://bot.testing2.ifchange.com/api    ${headers}
    ${req_url}    Set Variable    /dhr_manager/staffs/check
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "${session}", "no": "1114"}}}    #只能传一个 检查工号是否用过（传 no） 检查手机号是否用过（传 phone） 检查邮箱是否用过（传 email）
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}
    ${result_json}    To json    ${response.text}    pretty_print=True
    Should Contain    ${result}    已
    Delete All Sessions

员工详情
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/staffs/detail
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "${session}", "id": 17}}}
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}
    ${result_json_2}    To json    ${response.text}    pretty_print=True
    Should Contain    ${result}    卢唐乐    #17号的名字
    Delete All Sessions

登出
    ${headers}    create dictionary    content-Type=application/json    #定义头部信息
    create session    api    https://bot.testing2.ifchange.com/api    ${headers}
    ${req_url}    Set Variable    /dhr_auth/logout
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "eyJmcm9tIjoiQiIsInNyY19pZCI6MSwibWFuYWdlcl9pZCI6ODAsImNvbXBhbnlfaWQiOjgwLCJ1c2VyX2lkIjo3NCwiZXhwaXJlIjoxNTYyNjY2MjE4LCJzaWduYXR1cmUiOiIwMGY3OWU0MWJhYTZkNTE4NjI3YzU4NzYzMzhjZGIyZWY0NzMyOWI1IiwidXNlcl90eXBlIjoxfQ=="}}}
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}
    ${result_json}    To json    ${response.text}    pretty_print=True
    Should Contain    ${result}    "err_no":0
    Delete All Sessions

新增岗位
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/positions/create
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "${session}", "name": 1020}}}
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}

更新企业账号
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/accounts/update
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "eyJmcm9tIjoiQiIsInNyY19pZCI6MSwibWFuYWdlcl9pZCI6ODAsImNvbXBhbnlfaWQiOjgwLCJ1c2VyX2lkIjo3NCwiZXhwaXJlIjoxNTYyNjM4NDgxLCJzaWduYXR1cmUiOiI5ODA4YTM3ZDMxODI5YmE2NDY4ODAzNGNlMmYyM2EyYzk4OTJlYjg4IiwidXNlcl90eXBlIjoxfQ==", "realname": "董择", "phone": ""}}}
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}
    ${result_json}    To json    ${response.text}    pretty_print=True

企业账号列表
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/accounts/search
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "${session}"}}}
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}
    ${result_json}    To json    ${response.text}    pretty_print=True

企业账号详情
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/accounts/detail
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "eyJmcm9tIjoiQiIsInNyY19pZCI6MSwibWFuYWdlcl9pZCI6ODAsImNvbXBhbnlfaWQiOjgwLCJ1c2VyX2lkIjo3NCwiZXhwaXJlIjoxNTYyNjM4NDgxLCJzaWduYXR1cmUiOiI5ODA4YTM3ZDMxODI5YmE2NDY4ODAzNGNlMmYyM2EyYzk4OTJlYjg4IiwidXNlcl90eXBlIjoxfQ=="}}}
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}
    ${result_json}    To json    ${response.text}    pretty_print=True

验证账号密码
    create session    api    https://bot.testing2.ifchange.com/api
    ${req_url}    Set Variable    /dhr_manager/accounts/verify
    ${data}    Set Variable    {"request": {"c": "", "m": "", "p": {"session": "${session}", "email": "ze.dong@ifchange.com", "password": "aipm2018"}}}
    ${response}    Post Request    api    ${req_url}    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    ${result}    Set Variable    ${response.text}
    ${result_json}    To json    ${response.text}    pretty_print=True

*** Keywords ***
