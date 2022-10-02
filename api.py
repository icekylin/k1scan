import base64
import httpx
import yaml


def fofa(rules):
    fofa_results = []
    rules_cache = rules
    # 基础配置
    test_list = []  # 发现的待执行用例

    with open("api.yaml") as f:
        # 以安全的模式加载 yaml, 作为待执行用例
        test_list.append(yaml.safe_load(f))
        case = test_list[0]
        print(case)
        fofa_email = case['fofa_api']['fofa_email']
        fofa_key = case['fofa_api']['fofa_key']
        fofa_api = f'https://fofa.info/api/v1/search/all?email={fofa_email}&key={fofa_key}'
    # 将规则转换为 str 格式的 base64
    fofa_rules = str('&qbase64='+str(base64.b64encode(rules.encode('utf-8')), 'utf-8'))
    fofa_api = fofa_api+fofa_rules
    # 定义一些规则
    fofa_size = '&size=10000'   # 数据数量: 10000
    fofa_fields = '&fields=host'    # 返回字段: host
    # 拼接请求 URL
    fofa_api = fofa_api+fofa_fields+fofa_size
    try:    # 仅 return results 的 json 结果
        print(f'请求链接: [{fofa_api}]')
        print(f'请求规则: [{rules_cache}]')
        resp = httpx.get(fofa_api)
        # 返回 json 数据
        fofa_results = resp.json()['results']
        _len = len(fofa_results)
        if _len == 0:
            print('未搜索到相关数据')
        else:
            print(f'共返回: [{_len}] 条数据')
            return fofa_results
    except Exception as e:
        print(e)

