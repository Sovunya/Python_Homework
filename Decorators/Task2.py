#encoding:utf-8
"""
Напишите программу добавляющую в рецепт бутерброда ингридиенты "Салат" и "Ананасы" с помощью декораторов.
"""
def decorate(function_to_decorate):
    def recipe(salad, pineapple):
        print('Я помидорка')
        print('Я кукурузка')
        function_to_decorate(salad, pineapple)
        print('Я курочка копченая')
    return recipe

@decorate
def ingredience(salad, pineapple):
    print(salad)
    print(pineapple)

ingredience('Я салатик свеженький', 'Я ананасик')