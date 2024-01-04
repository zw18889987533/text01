"""
编写函数，作用为数据处理方法

"""
import xlrd as xl

def list_DB(list1,list2):
    """
    两个列表比较，列表一是否有数据不在列表二中，如果有，输出列表一的数据
    :param list1: 需要被比较的列表
    :param list2: 比较列表
    :return: 返回列表1中不在列表2的id
    """

    list = []
    for i in list1:
        if i in list2:
            pass
        else:
            list.append(i)

    return list

def list_CFZ(list)->list:
    """
    查询列表内有没有重复值
    :return:返回一个结果，表示这个列表有没有重复值
    """
    set_id = set(list)
    if len(list) == len(set_id):
        print(f"{list}没有重复值！")
    else:
        print(f"{list}有重复值！")


def dict_K(dict)->dict:
    """
    删除字典中，键值为空的key
    :param dict: 需要操作的字典
    :return: 操作完成的字典
    """
    for key in list(dict.keys()):
        if not dict.get(key):
            del dict[key]

    return dict


def list_ArrayList(list1,list2):
    """
    输出两个列表中不同的部分
    :param list1:第一个列表
    :param list2:第二个列表
    :return:返回一个列表
    """
    diff = list(set(list1) ^ set(list2))

    return diff

def dict_DB(dict1,dict2):
    """
    两个key相同字典对比，输出key相同，value不同的key元素
    :param dict1: 字典1
    :param dict2: 字典2
    :return: 输出key列表
    """

    list = []
    for key in dict1:
        if key in dict2 and dict1[key] != dict2[key]:
            list.append(key)

    return list

def dict_TZ(dict,file):
    """
    写入一个嵌套字典｛xxx:{xxx:xxx,xxx:xxx}｝,输出｛id:xxx,id:xxx｝ 值只能是int
    :param dict:嵌套字典
    :return:外层字典{id:你所需要的值}
    """

    result_dict = {}

    for i in dict:
        deta = dict[i][file]
        result_dict[i] = int(deta)


    return result_dict

if __name__ == '__main__':

    list1 = [101010100,101010200,101010300]
    list2 = [101010100,101010200,101010400]
    a = list_ArrayList(list1,list2)
    print(a)

    dict = {111:{'ID':123,'武器':'好玩'},222:{'ID':444,'武器':'fsfas'}}

    print(dict_TZ(dict,'武器'))
