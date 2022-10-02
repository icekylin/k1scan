import os

# 检测 results 文件夹是否存在
path = 'results'
if not os.path.exists(path):
    os.mkdir(path)


def output(args):
    _type = type(args)
    print('=== 文件将保存为 txt 格式文件 ===')
    print(f'=== 数据类型为: {_type} ===')
    filename = input('请输入保存文件名称: ')
    if '.txt' not in filename:
        filename = filename + '.txt'
    with open('results/' + filename, 'w+') as f:
        if _type == list:
            for i in args:
                f.write(i + '\n')
            print(f'[Success] 保存成功, 文件路径: ./results/{filename}')
            f.close()


# 去重函数
# file_path 目标文件夹路径
# new_filename 保存后文件的名称
def merge_dedup(file_path='./', new_filename='all_results.txt'):
    filelist = os.listdir(file_path)
    # 合并结果, 将结果保存至 file_path/new_filename
    print(f'- 读取到 {filelist}, 共 [{len(filelist)}] 个文件')
    if '.txt' not in new_filename:
        new_filename = new_filename+'.txt'
    with open(f'{file_path}{new_filename}', 'w+') as f_all:
        for filename in filelist:
            # print(f'读取文件: [{filename}]')
            with open(f'{file_path}{filename}', 'r') as f_single:
                lines = f_single.readlines()
                for content in lines:
                    f_all.write(content)
            f_single.close()
        count_newfile = len(open(file_path + new_filename).readlines())
        print(f'写入成功, 文件路径为 [{file_path}{new_filename}], 共 {count_newfile} 条结果')
    f_all.close()
