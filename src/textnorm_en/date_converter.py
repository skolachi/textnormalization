from num2words import num2words
import re

#TO DO: Get month names for different locales using python (calendar, locale)
months = {'january':'January', 'february':'February', 'march':'March', \
			'april':'April', 'may':'May', 'june':'June', 'july':'July', \
			'august':'August', 'september':'September', 'october':'October', \
			'november':'November', 'december':'December', \
			'jan':'January','feb':'February','aug':'August','sep':'September', \
			'oct':'October','nov':'November','dec':'December', \
			'1':'January', '2':'February', '3':'March', \
			'01':'January', '02':'February', '03':'March', \
			'4':'April', '5':'May', '6':'June', '7':'July', \
			'04':'April', '05':'May', '06':'June', '7':'July', \
			'8':'August', '9':'September', '10':'October', \
			'08':'August', '09':'September', \
			'11':'November', '12':'December'}



class DateConverter:
	def __init__(self,lang):
		super(DateConverter, self).__init__()
		self.lang = lang

	def transform(self,text):
		text = self.formatdates_(text)
		text = self.textdates_(text)		

		return text
		
	def textdates_(self,text):
		year_patt = re.compile(r'\b((%s)([0-9a-z, ]+)(1[0-9]|20)([0-9]{2}))\b'%('|'.join(list(months.keys()))),re.IGNORECASE)
		for d in year_patt.finditer(text):
			year = d.groups()[1] + d.groups()[2] + self.convertdate_(d.groups()[3]+d.groups()[4],'year')
			text = re.sub(d.groups()[0],year,text)
		day_patt1 = re.compile(r'\b(([1-9]|[12][0-9]|3[0-1])(st|rd|nd|th)? (%s))\b'%('|'.join(list(months.keys()))),re.IGNORECASE)
		day_patt2 = re.compile(r'\b((%s) ([1-9]|[12][0-9]|3[0-1])(st|rd|nd|th)?)\b'%('|'.join(list(months.keys()))),re.IGNORECASE)
		for d in day_patt1.finditer(text):
			day = self.convertdate_(d.groups()[1],'day')
			month = months[d.groups()[3].lower()]
			date_expansion = '%s of %s'%(day,month)
			text = re.sub(d.groups()[0],date_expansion,text)
		for d in day_patt2.finditer(text):
			day = self.convertdate_(d.groups()[2],'day')
			month = months[d.groups()[1].lower()]
			date_expansion = '%s of %s'%(day,month)
			text = re.sub(d.groups()[0],date_expansion,text)	
		
		return text

	def formatdates_(self,text):
		#ddmmyyyy
		date_patt1 = re.compile(r'\b((\d{1,2})[\.\-\/](\d{1,2})[\.\-\/](1[0-9]|20)([0-9]{2}))\b')
		for d in date_patt1.finditer(text):
			date_string, day, month, year1, year2 = d.groups()
			if 1 <= int(day) <= 31 and 1 <= int(month) <= 12:
				date_expansion = self.generate_date_string(day,month,year1,year2,'ddmmyyyy')
				date_expansion = self.cleanup_(date_expansion)
				text = re.sub(date_string,date_expansion,text)
		#mmddyyyy
		#date_patt2 = re.compile('(0?[1-9]|1[012])[\.\-\/]([1-9]|[12][0-9]|3[01])[\.\-\/](1[0-9]|20)([0-9]{2})')

		return text

	def cleanup_(self,text):
		text = re.sub('[-_]',' ',text)
		return text

	def convertdate_(self,date_attr,attr_type='day'):
		if attr_type == 'day':
			return self.cleanup_(num2words(date_attr,lang=self.lang,to='ordinal'))
		if attr_type == 'year':
			if int(date_attr[:2]) < 20:
				return self.cleanup_(num2words(date_attr[:2],lang=self.lang)) + ' ' + self.cleanup_(num2words(date_attr[2:],lang=self.lang))
			else:
				return self.cleanup_(num2words(date_attr,lang=self.lang))
			
	def generate_date_string(self,day,month,year1,year2,dateformat):
		month_string = months[month]
		day_string = num2words(day,lang=self.lang,to='ordinal')

		if int(year1) < 20:
			year_string = num2words(year1,lang=self.lang) + ' ' + num2words(year2,lang=self.lang)
		else:
			year_string = num2words(year1+year2,lang=self.lang)

		if dateformat == 'ddmmyyyy':
			date_string = day_string+' of '+month_string+' '+year_string
		if dateformat == 'mmddyyyy':
			date_string = month_string+' '+day_string+' '+year_string

		date_string = self.cleanup_(date_string)
		return date_string
