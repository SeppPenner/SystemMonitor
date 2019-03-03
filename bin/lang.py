from multimethod import multimethod

class Lang:
	def __init__(self, language):
		self.language = language
		self.german = {
			'DatabaseConnecting': 'Verbindungsaufbau zur MySQL-Datenbank.',
			'GettingCursor': 'Hole einen MySQL-Cursor.',
			'ExecutingQuery': 'Führe die Abfrage aus.',
			'GettingResults': 'Empfange Ergebnisse.',
			'Done': 'Fertig.',
			'SerialNumber': 'Seriennummer: {0}.',
			'SerialId': 'Seriennummern-Id: {0}.',
			'NumberOfCPUCoresIsBiggerThan8': 'Die Anzahl der CPU-Kerne ist größer als 8.'
		}
		english = {
			'DatabaseConnecting': 'Connecting to MySQL database.',
			'GettingCursor': 'Getting a cursor.',
			'ExecutingQuery': 'Executing query.',
			'GettingResults': 'Getting results.',
			'Done': 'Done.',
			'SerialNumber': 'Serial number: {0}.',
			'SerialId': 'Serial id: {0}.',
			'NumberOfCPUCoresIsBiggerThan8': 'The number of CPU cores is bigger than 8.'
		}
		
	def setLanguage(self, language: str):
		"Sets the language to the given value, currently valid: 'german' and 'english'"
		self.language = language

	@multimethod
	def getString(self, key: str):
		"Gets the text from the specified key in the specified language"
		if self.language == 'german':
			if key in self.german:
				return self.german.get(key)
			else:
				raise ValueError('Der Key wurde nicht gefunden: ' + key)
		elif self.language == 'english':
			if key in self.english:
				return self.english.get(key)
			else:
				raise ValueError('The key was not found: ' + key)
		else:
			raise ValueError('Wrong language specified.')

	@multimethod
	def getString(self, key: str, value: str):
		"Gets the text from the specified key in the specified language"
		if self.language == 'german':
			if key in self.german:
				return self.german.get(key).format(value)
			else:
				raise ValueError('Der Key wurde nicht gefunden: ' + key)
		elif self.language == 'english':
			if key in self.english:
				return self.english.get(key).format(value)
			else:
				raise ValueError('The key was not found: ' + key)
		else:
			raise ValueError('Wrong language specified.')

	@multimethod
	def getString(self, key: str, value: str, value2: str):
		"Gets the text from the specified key in the specified language"
		if self.language == 'german':
			if key in self.german:
				return self.german.get(key).format(value, value2)
			else:
				raise ValueError('Der Key wurde nicht gefunden: ' + key)
		elif self.language == 'english':
			if key in self.english:
				return self.english.get(key).format(value, value2)
			else:
				raise ValueError('The key was not found: ' + key)
		else:
			raise ValueError('Wrong language specified.')

	@multimethod
	def getString(self, key: str, value: str, value2: str, value3: str):
		"Gets the text from the specified key in the specified language"
		if self.language == 'german':
			if key in self.german:
				return self.german.get(key).format(value, value2, value3)
			else:
				raise ValueError('Der Key wurde nicht gefunden: ' + key)
		elif self.language == 'english':
			if key in self.english:
				return self.english.get(key).format(value, value2, value3)
			else:
				raise ValueError('The key was not found: ' + key)
		else:
			raise ValueError('Wrong language specified.')

	@multimethod
	def getString(self, key: str, value: str, value2: str, value3: str, value4: str):
		"Gets the text from the specified key in the specified language"
		if self.language == 'german':
			if key in self.german:
				return self.german.get(key).format(value, value2, value3, value4)
			else:
				raise ValueError('Der Key wurde nicht gefunden: ' + key)
		elif self.language == 'english':
			if key in self.english:
				return self.english.get(key).format(value, value2, value3, value4)
			else:
				raise ValueError('The key was not found: ' + key)
		else:
			raise ValueError('Wrong language specified.')

	@multimethod
	def getString(self, key: str, value: str, value2: str, value3: str, value4: str, value5: str):
		"Gets the text from the specified key in the specified language"
		if self.language == 'german':
			if key in self.german:
				return self.german.get(key).format(value, value2, value3, value4, value5)
			else:
				raise ValueError('Der Key wurde nicht gefunden: ' + key)
		elif self.language == 'english':
			if key in self.english:
				return self.english.get(key).format(value, value2, value3, value4, value5)
			else:
				raise ValueError('The key was not found: ' + key)
		else:
			raise ValueError('Wrong language specified.')

	@multimethod
	def getString(self, key: str, value: str, value2: str, value3: str, value4: str, value5: str, value6: str):
		"Gets the text from the specified key in the specified language"
		if self.language == 'german':
			if key in self.german:
				return self.german.get(key).format(value, value2, value3, value4, value5, value6)
			else:
				raise ValueError('Der Key wurde nicht gefunden: ' + key)
		elif self.language == 'english':
			if key in self.english:
				return self.english.get(key).format(value, value2, value3, value4, value5, value6)
			else:
				raise ValueError('The key was not found: ' + key)
		else:
			raise ValueError('Wrong language specified.')

	@multimethod
	def getString(self, key: str, value: str, value2: str, value3: str, value4: str, value5: str, value6: str, value7: str):
		"Gets the text from the specified key in the specified language"
		if self.language == 'german':
			if key in self.german:
				return self.german.get(key).format(value, value2, value3, value4, value5, value6, value7)
			else:
				raise ValueError('Der Key wurde nicht gefunden: ' + key)
		elif self.language == 'english':
			if key in self.english:
				return self.english.get(key).format(value, value2, value3, value4, value5, value6, value7)
			else:
				raise ValueError('The key was not found: ' + key)
		else:
			raise ValueError('Wrong language specified.')