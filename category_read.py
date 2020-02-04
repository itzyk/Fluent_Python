# coding: utf-8

import openpyxl
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def get_category_map(url, cate_rank):
    wb = openpyxl.load_workbook(url)
    # 获取当前活跃表单
    ws = wb.active

    category_map = ''

    cp_cate_index1, cp_cate_index2, dk_cate_id_index, dk_cate_index = None, None, None, None
    for row in list(ws.rows)[0]:
        index = row.col_idx - 1
        if row.value == '一级分类':
            cp_cate_index1 = index
        elif row.value == '二级分类':
            cp_cate_index2 = index
        elif row.value == '全民id':
            dk_cate_id_index = index
        elif row.value == '全民分类':
            dk_cate_index = index

    if cate_rank == 1:
        cp_cate_index = cp_cate_index1
    else:
        cp_cate_index = cp_cate_index2

    cp_categorys = set()

    for row in list(ws.rows)[1:]:
        cp_cate = row[cp_cate_index].value  # cp分类
        dk_cate_id = row[dk_cate_id_index].value  # 多看分类id
        dk_cate = row[dk_cate_index].value   # 多看分类
        channel = 2 if len(dk_cate) > 2 else 1
        category = "u'" + str(cp_cate) + "': [" + str(channel) + ", [25000000, " +\
                       str(dk_cate_id) + "], [u'免费', u'" + dk_cate + "']]," + "\n"
        if category in cp_categorys:
            continue
        else:
            cp_categorys.add(category)
            category_map += category

    print category_map


if __name__ == "__main__":
    url = '/Users/zhouyikai/Downloads/落尘分类映射表.xlsx'
    cate_rank = 2  # 用cp的1级还是2级分类做映射
    get_category_map(url, cate_rank)



