import requests
import yaml


class PocCheck:
    def __init__(self):
        self.test_list = []  # 发现的待执行用例
        # self.api_client = PocCheck()

        with open("poc.yaml") as f:
            # 以安全的模式加载 yaml, 作为待执行用例
            self.test_list.append(yaml.safe_load(f))

    def run_test(self, url):  # 执行用例
        # 调用 yaml
        case = self.test_list[0]
        # 获取 URL
        # url = "http://jsfhjtcpa.com/"
        # 获取 request 参数
        method = case['request']['method']
        method = method.upper()
        path = case['request']['path']
        # 获取 resp 结果
        resp = self.hit_request(url, method, path)
        # 获取 response 条件
        hit_content = case['response']['hit_content']
        url = self.hit_check(url, resp, hit_content)
        return url

    @staticmethod
    def hit_request(url, method, path, timeout=5, **kwargs):
        test_url = url + path
        if method == "GET":
            try:
                resp = requests.get(test_url, timeout=timeout)
                return resp
            except Exception as e:
                pass
        elif method == "POST":
            try:
                resp = requests.post(test_url, timeout=timeout)
                return resp
            except Exception as e:
                pass

    @staticmethod
    def hit_check(url, resp, hit_content):
        hit_list = []
        try:
            if hit_content in resp.text:
                hit_list.append(url)
                print(url)
                return url
        except:
            pass

