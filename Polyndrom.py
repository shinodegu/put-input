inputdata = ['Страна', 'шалаш', 'Летел', 'вертолет', 'УЧУ', 'мэм', 'язык']

b = list(filter(lambda word: word != word[::-1], inputdata))
print(b)