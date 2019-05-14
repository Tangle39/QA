def find_max(dict):
    max_age = 0
    for key, value in dict.items():
        if value > max_age:
            max_age = value
            name = key
    print(name)
    print(max_age)
if __name__ == '__main__':
    person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22,"chao":100}
    m = 'li'
    #keys：键，items：键&值
    for key in person.keys():
        if person[m] < person[key]:
            m = key

    print('%s,%d' % (m, person[m]))


find_max(person)