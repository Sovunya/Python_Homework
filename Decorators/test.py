def decorate(func):
    def wrapper():
        print('я декоратор')
        func()
        print('я выполнил свою работу')
    return wrapper

@decorate
def func_to_decor():
    print('я функция')

decorator = decorate(func_to_decor)
decorator()
