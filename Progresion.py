def create_generator():
    my_list = range(1000)
    for i in my_list:
        yield i + i


my_generator = create_generator()
for i in my_generator:
    print(i)