inputdata = ['Страна', 'шалаш', 'Летел', 'вертолет', 'УЧУ', 'мэм', 'язык']

b = list(filter(lambda word: word.upper() != word.upper()[::-1], inputdata))
print(b)
