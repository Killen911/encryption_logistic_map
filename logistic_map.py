print("ДАННЫЕ ДЛЯ ШИФРОВАНИЯ")
k = ""
while len(str(k)) < 1:
	try:
		k = int(input("Введите число значимых знаков после точки (запятой):\n"))
	except ValueError:
		print("Ввод некорректный")
		k = ""

a = ""
while len(str(a)) != k+2:
	try:
		a = float(input("Введите a (3.57 < a < 4) в формате: 3.57" + "1"*(k-2) + "\nЧисло знаков после точки - %s!\n" % k))
		if 4.0 < a or a < 3.57:
			a = ""
			print("a должно быть больше 3.57, но меньше 4!")
	except ValueError:
		print("Ввод некорректный")
		a = ""

x0 = ""
while len(str(x0)) != k+2:
	x0 = input("Введите начальное значение x в формате 0.12" + "1"*(k-2) + "\nЧисло знаков после точки - %s!\n" % k)
	try:
		x = x0 = float(x0)
	except ValueError:
		print("Ввод некорректный")
		x0 = ""

n0 = 0
while n0 == 0:
	try:
		n0 = n = int(input("Введите начальное значение n. Например: 87587\n"))
	except ValueError:
		print("Ввод некорректный")
		n0 = 0

m = 0
while m == 0:
	try:
		m = int(input("Введите начальное значение m. Например: 2746\n"))
	except ValueError:
		print("Ввод некорректный")
		m = 0

mydict = {
	'А': 74752,
	'Б': 99843,
	'В': 35332,
	'Г': 76293,
	'Д': 35339,
	'Е': 89612,
	'Ё': 18446,
	'Ж': 78351,
	'З': 52758,
	'И': 47642,
	'Й': 72732,
	'К': 15904,
	'Л': 71201,
	'М': 20513,
	'Н': 25636,
	'О': 66596,
	'П': 74795,
	'Р': 36398,
	'С': 71733,
	'Т': 71734,
	'У': 11319,
	'Ф': 90681,
	'Х': 70719,
	'Ц': 12352,
	'Ч': 45121,
	'Ш': 66113,
	'Щ': 65605,
	'Ъ': 90701,
	'Ы': 82510,
	'Ь': 44626,
	'Э': 68178,
	'Ю': 67668,
	'Я': 45651,
	'A': 77910,
	'B': 42071,
	'C': 16984,
	'D': 85082,
	'E': 19040,
	'F': 35426,
	'G': 97378,
	'H': 90722,
	'I': 46178,
	'J': 46693,
	'K': 67687,
	'L': 16483,
	'M': 50790,
	'N': 87146,
	'O': 30836,
	'P': 41588,
	'Q': 94847,
	'R': 64639,
	'S': 63105,
	'T': 79489,
	'U': 35967,
	'V': 72836,
	'W': 29318,
	'X': 66699,
	'Y': 65164,
	'Z': 98459,
	'!': 87707,
	'@': 17055,
	'"': 11938,
	'\'': 41635,
	'#': 93870,
	'№': 79023,
	'$': 94387,
	';': 32949,
	',': 30903,
	'.': 58040,
	'$': 11449,
	'%': 47290,
	'#': 86200,
	'^': 61628,
	':': 60605,
	'&': 88253,
	'?': 37567,
	'*': 33474,
	'(': 11459,
	')': 57538,
	'-': 85701,
	'_': 28871,
	'+': 59085,
	'=': 42195,
	'/': 88788,
	'0': 10001,
	'1': 11111,
	'2': 22222,
	'3': 33333,
	'4': 44444,
	'5': 55555,
	'6': 66666,
	'7': 77777,
	'8': 88888,
	'9': 99999,
	' ': 99998
}
phrase = input("Введите текст для шифрования.\n").upper()

print("\nk =", k)
print("a =", a)
print("x = ", x)
print("n = ", n)
print("m =", m)
print("Текст для шифрования:", phrase)


def func(x):
	"""return Xn+1"""
	return a*x*(1-x)


logist = list()
cipher = [mydict[letter] for letter in phrase]
print("\nКод:", cipher)
print("Шифрование...")
try:

	for i in range(len(phrase)):
		n = n0 + i*m
		for j in range(n):
			x = func(x)
			if j % n == 0:
				logist.append(round(x*10**k))

	for i in range(len(logist)):
		cipher[i] += logist[i]
	print("Шифр:", cipher)


	print("\nДАННЫЕ ДЛЯ ДЕШИФРОВАНИЯ")
	a = ""
	while len(str(a)) != k+2:
		try:
			a = float(input("Введите a. \nЧисло знаков после точки - %s!\n" % k))
		except ValueError:
			print("Ввод некорректный")
			a = ""

	x0 = ""
	while len(str(x0)) != k+2:
		x0 = input("Введите начальное значение x.\nЧисло знаков после точки - %s!\n" % k)
		try:
			x = x0 = float(x0)
		except ValueError:
			print("Ввод некорректный")
			x0 = ""

	n0 = 0
	while n0 == 0:
		try:
			n0 = n = int(input("Введите начальное значение n:\n"))
		except ValueError:
			print("Ввод некорректный")
			n0 = 0

	m = 0
	while m == 0:
		try:
			m = int(input("Введите начальное значение m:\n"))
		except ValueError:
			print("Ввод некорректный")
			m = 0

	print("Дешифрование...")
	logist = list()
	for i in range(len(phrase)):
		n = n0 + i*m
		for j in range(n):
			x = func(x)
			if j % n == 0:
				logist.append(round(x*10**k))
	for i in range(len(logist)):
		cipher[i] -= logist[i]

	decrypt = ""
	for code in cipher:
		for k in mydict.keys():
			if mydict[k] == code:
				decrypt += k
	print(decrypt)
	if phrase != decrypt:
		print("Дешифрование не успешно.")
	else:
		print("Дешифрование успешно.")
	input("Нажмите Enter, чтобы закрыть консоль.")
except OverflowError:
	print("Были введены слишком большие значения!")
	input()
