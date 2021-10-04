def func(**kwargs):
    print(kwargs)


def func_2(one, two, three):
    print(one, two, three)


#           **kwargs                            kwargs
# **{'one': 1, 'two': 2, 'three': 3} --> {'one': 1, 'two': 2, 'three': 3}
func(**{'one': 1, 'two': 2, 'three': 3})
# one=1 two=2, three=3 = **{'one': 1, 'two': 2, 'three': 3}
func(one=1, two=2, three=3)
# **{'one': 1, 'two': 2, 'three': 3} = one=1 two=2, three=3
func_2(**{'one': 1, 'two': 2, 'three': 3})
