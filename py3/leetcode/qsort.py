def qsort(l:list):
    if len(l) <= 1:return l
    else:
        return qsort([x for x in l[1:] if x <=l[0]])+[l[0]]+qsort([x for x in l[1:] if x >l[0]])

print(qsort([1,3,2,4]))

'''
列表推导式
使用[]生成list
variable = [out_exp_res for out_exp in input_list if out_exp == 2]
'''