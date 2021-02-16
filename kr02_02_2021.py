def task_1(two_dim_words):
    two_dim_words = [['яблоко', 'груша', 'апельсин'],
     ['морковь', 'огурец', 'картошка'],
     ['арбуз', 'ежевика', 'малина',]]
    new=[]
    for i in two_dim_words:
        new.extend(i)
        new.sort()
        new.sort(key = len)
    return sorted_words


def task_3(numbers):
    """
        Здесь должен быть ваш код.
        Переменная numbers - ваша строка чисел.
        Финальное значение должно быть помещено в переменную dict_min.
        """

    return dict_min


def task_4_1(words):
    words = ('Alaska', 'auto', 'arc', 'agenda', 'arugula', 'caveman')
    res = []
    for i in words:
        if i.count('a') >= 2:
            kv= str(i.count('a') ** 2)
            res += kv
res = tuple(words_1)

    return res


def task_4_2(words):  # можно сделать тесты
    words = ('Alaska', 'auto', 'arc', 'agenda', 'arugula', 'caveman')
    res = []
    for i in words:
        if len(i) > 3:
            res += str(len(i))
    res = set(res)

    return res


def task_4_3(words):
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    return res


def task_5(lst1, lst2):
    lst1= set([1,2,3,55,76,23,43,4])
    lst2= set([65,464,21,1,4,76,23])
    s3 = list(lst1 - lst2)
    diff = sorted(s3)

    return diff


def task_6(lst):
    lst = input().split()
    new_set = set(new_list)
    new_list2 = list(new_set)
    res = tuple(reversed(new_list2))
    return res

