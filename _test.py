list_atts = set(dir(list))
tuple_atts = set(dir(tuple))
dict_atts = set(dir(dict))

r = dict_atts - (dict_atts & tuple_atts) - (dict_atts & list_atts)

print(r)