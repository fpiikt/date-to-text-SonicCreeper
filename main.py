"""
  Автор: Кашпур Николай, группа №P3355

"""

class DateToTextClass():
	def __init__(self, date):
		splitted = date.split(' ')
		self.date = splitted[0].split('.')
		self.time = splitted[1].split(':')

	def convert(self):
	"""
	    Transforms date in numerical format into russian text.
	    Returns (str): russian text
    	"""
		day = self.date[0]
		month = self.date[1]
		year = self.date[2]
		return self.convertDay(day) + ' ' + self.convertMonth(month) + ' ' + self.convertYear(year) + self.convertTime(self.time)

	def convertTime(self, time):
	"""
	    Transforms time in numerical format into russian text.
	    Args:
	    	time (str[]): contains hours, minutes and seconds as elements of an array, should be ['HH', 'MM', 'SS']
	    Returns (str): russian text
    	"""
		unitDict = {
			'0': 'ноль',
			'1': 'одна',
			'2': 'две',
			'3': 'три',
			'4': 'четыре',
			'5': 'пять',
			'6': 'шесть',
			'7': 'семь',
			'8': 'восемь',
			'9': 'девять',
		}
		x = [{
			'num': time[0],
			'word1': ' часов',
			'word2': ' час',
			'word3': ' часа',
			'unic': {'1': 'один', '2': 'два'}
		},
		{
			'num': time[1],
			'word1': ' минут',
			'word2': ' минута',
			'word3': ' минуты'
		},
		{
			'num': time[2],
			'word1': ' секунд',
			'word2': ' секунда',
			'word3': ' секунды'
		}]
		res = ''
		for i in x:
			num = i['num']
			if num[0] == '1':
				res += ' ' + self.get10Word(num, 1) + i['word1']
			elif num[1] == '0' and num[0] != '0':
				res += ' ' + self.getDozenWord(num[0], 1) + i['word1']
			else:
				unic = i.get('unic')
				unit = unic and unic.get(num[1]) or unitDict.get(num[1])
				if unit == 'один' or unit == 'одна':
					numWord = i['word2']
				else:
					numWord = i['word1'] if unit[-1] == 'ь' else i['word3']
				dozen = self.getDozenWord(num[0], 1)
				res += ' ' + (dozen and (dozen + ' ' + unit + numWord) or (unit + numWord))
		return res

	def convertDay(self, day):
	"""
	    Transforms day in numerical format into russian text.
	    Args:
	    	day (str): should be in format DD
	    Returns (str): russian text
    	"""
		res = ''
		unitDict = {
			'1': 'первое',
			'2': 'второе',
			'3': 'третье',
			'4': 'четвертое',
			'5': 'пятое',
			'6': 'шестое',
			'7': 'седьмое',
			'8': 'восьмое',
			'9': 'девятое',
		}
		unit = unitDict.get(day[1])

		if day[0] == '0':
			return unit
		elif day[0] == '1':
			return self.get10Word(day, 2)
		elif day[1] == '0':
			return self.getDozenWord(day[0], 2)
		else:
			res = self.getDozenWord(day[0], 1)
			return res != '' and res + ' ' + unit or unit

	def convertYear(self, year):
	"""
	    Transforms year in numerical format into russian text.
	    Args:
	    	year (str): should be in format YYYY
	    Returns (str): russian text
    	"""
		unitDict = {
			'0': '',
			'1': 'первого',
			'2': 'второго',
			'3': 'третьего',
			'4': 'четвертого',
			'5': 'пятого',
			'6': 'шестого',
			'7': 'седьмого',
			'8': 'восьмого',
			'9': 'девятого',
		}
		if year[2] == '1':
			res = self.get10Word(year[-2:], 3)
		else:
			res = unitDict.get(year[3])
			if res == '':
				res = self.getDozenWord(year[2], 3)
			else:
				dozen = self.getDozenWord(year[2], 1)
				res = dozen and (dozen + ' ' + res) or res

		if res == '':
			res = self.getHundredWord(year[1], 2)
		else:
			hundred = self.getHundredWord(year[1], 1)
			res = hundred and (hundred + ' ' + res) or res

		if res == '':
			res = self.getThousandWord(year[0], 2)
		else:
			thousand = self.getThousandWord(year[0], 1)
			res = thousand and (thousand + ' ' + res) or res

		return res + ' года'

	def convertMonth(self, month):
	"""
	    Transforms month in numerical format into russian text.
	    Args:
	    	month (str): should be in format MM
	    Returns (str): russian text
    	"""
		monthDict = {
		'01': 'января',
		'02': 'февраля',
		'03': 'марта',
		'04': 'апреля',
		'05': 'мая',
		'06': 'июня',
		'07': 'июля',
		'08': 'августа',
		'09': 'сентября',
		'10': 'октября',
		'11': 'ноября',
		'12': 'декабря',
		}
		return monthDict.get(month)

	def getThousandWord(self, num, mod = 1):
	"""
	    Transforms number of thousands into russian text.
	    Args:
	    	num (str): number of thousands
				mod (number): defines type of noun
	    Returns (str): russian text
    	"""
		dictOfThousand = {
			'0': '',
			'1': 'тысяча/тысячного',
			'2': 'две тысячи/двухтысячного'
		}

		words = dictOfThousand.get(num) and dictOfThousand.get(num).split('/')
		if mod == 2:
			return words[1]
		else:
			return words[0]

	def getHundredWord(self, num, mod):
	"""
	    Transforms number of hundreds into russian text.
	    Args:
	    	num (str): number of hundreds
				mod (number): defines type of noun
	    Returns (str): russian text
   	"""
		dictOfHundred = {
			'0': '/',
			'1': 'сто/',
			'2': 'двести/двух',
			'3': 'триста/трёх',
			'4': 'четыреста/четырёх',
			'5': 'пятьсот/пяти',
			'6': 'шестьсот/шести',
			'7': 'семьсот/семи',
			'8': 'восемьсот/восьми',
			'9': 'девятьсот/девяти',
		}

		words = dictOfHundred.get(num) and dictOfHundred.get(num).split('/')
		if mod == 2:
			pre = words[1]
			return pre and pre + 'сотого' or pre
		else:
			return words[0]

	def getDozenWord(self, num, mod):
	"""
	    Transforms number of dozens into russian text.
	    Args:
	    	num (str): number of dozens
				mod (number): defines type of noun
	    Returns (str): russian text
    	"""
		dictOfDozens = {
			'0': '',
			'2': 'двадцат',
			'3': 'тридцат',
			'4': 'сорок',
			'5': 'пятьдесят',
			'6': 'шестьдесят',
			'7': 'семьдесят',
			'8': 'восемьдесят',
			'9': 'девяносто',
		}
		res = dictOfDozens.get(num)
		if res and res != None:
			if mod == 1:
				return res[-2] == 'а' and res + 'ь' or res
			elif mod == 2:
				return res + 'ое'
			else:
				return num == '4' and res + 'ового' or res.replace('ь', 'и').replace('восеми', 'восьми') + 'ого'
		else:
			return res

	def get10Word(self, num, mod):
	"""
	    Transforms number in range from 10 to 19 into russian text.
	    Args:
	    	num (str): number of dozens
				mod (number): defines type of noun
	    Returns (str): russian text
    	"""
		dictOf10 = {
			'10': 'десят',
			'11': 'одиннадцат',
			'12': 'двенадцат',
			'13': 'тринадцат',
			'14': 'четырнадцат',
			'15': 'пятнадцат',
			'16': 'шестнадцат',
			'17': 'семнадцат',
			'18': 'восемнадцат',
			'19': 'девятнадцат',
		}
		post = 'ое' if mod == 2 else 'ого'
		res = dictOf10.get(num)
		if res != 'error':
			if mod == 1:
				return res + 'ь'
			else:
				return res + post
		else:
			return res

if __name__ == '__main__':
	assert DateToTextClass('25.09.2019 08:17:59').convert() == "двадцать пятое сентября две тысячи девятнадцатого года восемь часов семнадцать минут пятьдесят девять секунд", 'ошибка в тестовом примере 1'
	assert DateToTextClass('20.01.1901 10:21:39').convert() == "двадцатое января тысяча девятьсот первого года десять часов двадцать одна минута тридцать девять секунд", 'ошибка в тестовом примере 2'
	assert DateToTextClass('02.03.1800 15:11:50').convert() == "второе марта тысяча восьмисотого года пятнадцать часов одиннадцать минут пятьдесят секунд", 'ошибка в тестовом примере 3'
	assert DateToTextClass('11.12.2000 23:52:22').convert() == "одиннадцатое декабря двухтысячного года двадцать три часа пятьдесят две минуты двадцать две секунды", 'ошибка тестовом примере 4'
