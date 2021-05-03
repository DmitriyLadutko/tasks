"""Функция удваивания ключей словаря"""


def double_dict_keys(**kwargs):
    result = {}
    for key, value in kwargs.items():
        result.update({f'{key}{key}': value})
    return result


"""Функция удваивания ключей словаря используя lambda"""

double_dict_keys_lambda = lambda **kwargs: {f'{key}{key}': value for key, value in kwargs.items()}

print(double_dict_keys_lambda(a=2))
print(double_dict_keys(a=2))
