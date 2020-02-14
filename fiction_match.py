# coding: utf-8

import csv


def fiction_match(file1, file2):
    l = list()
    c1, list1 = csv2list(file1, 0)  # 授权书单
    c2, list2 = csv2list(file2, 1)  # 导出书单

    print c1, list1
    print c2, list2

    if c1 == c2:
        print "数量一样"
    else:
        for fic in list1:
            if fic not in list2:
                l.append(fic)
    if l:
        print len(l), l


def csv2list(file, type):
    c_list = set()
    if type == 1:  # type =1 为export_fiction.csv
        index = 4
    else:
        index = 1

    with open(file) as f:
        rows = csv.reader(f)
        count = 0
        for row in rows:
            if count == 0:
                count += 1
                continue

            if not row or len(row) <= index:
                break
            c_list.add(row[index])
            count += 1
    ret = map(int, list(c_list))
    return count, ret


if __name__ == '__main__':
    file1 = "/Users/zhouyikai/Downloads/授权/南京落尘文化传媒有限公司.csv"  # 授权书单
    file2 = "/Users/zhouyikai/Downloads/export_fiction.csv"  # 导出的书单
    fiction_match(file1, file2)
    # csv2list(file2)
