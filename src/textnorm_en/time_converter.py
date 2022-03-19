from num2words import num2words
import re

class TimeConverter:
	def __init__(self,lang):
		super(TimeConverter,self).__init__()
		self.lang = lang

	def transform(self,text):
		text = self.convert_time(text)

		return text

	def cleanup_(self,text):
		return re.sub('[-_]',' ',text)

	def generate_time_string(self, hrs, mins, secs=None, ampm=None):
		ampm_suffix = ""
		if secs == None:
			secs = '00'
		if ampm == None:
			ampm = ''
		time_expansion = ''
		#if ampm == '':
			#if 3 <= int(hrs) <= 11:
			#	ampm_suffix = "in the morning"
			#if int(hrs) > 11:
			#	ampm_suffix = ""
			#else:
			#	ampm_suffix = " du soir"
		#else:
		if ampm != '':
			if ampm.lower() == 'am':
				if 4 <= int(hrs) <= 11:
					ampm_suffix = "in the morning"
				elif int(hrs) <= 4:
					ampm_suffix = "at night"
				else:
					ampm_suffix = ""
			if ampm.lower() == "pm":
				if int(hrs) <= 4:
					ampm_suffix = "after noon"
				elif 5 <= int(hrs) <= 8:
					ampm_suffix = "in the evening"
				else:
					ampm_suffix = "at night"
	
		if hrs in ['0','00']:
			if ampm_suffix == "after noon":
				hours = 'noon'
			else:
				hours = 'midnight'
		elif hrs == '12' and ampm_suffix == "at night":
			hours = 'midnight'
		elif hrs == '12' and ampm_suffix == "after noon":
			hours = 'noon'
		else:
			hours = "%s"%(num2words(hrs,lang=self.lang))
		if mins == '00':
			if hours in ['midnight','noon']:
				time_expansion = hours 
				ampm_suffix = ''
			else:
				time_expansion = hours + " o'clock"
		elif mins == '15' and secs == '00' and int(hrs) < 12:
			time_expansion = "a quarter past %s"%(hours)
			if hours in ['midnight','noon']:ampm_suffix = ''
		elif mins == '30' and secs == '00' and int(hrs) < 12:
			time_expansion = "half past %s"%(hours)
			if hours in ['midnight','noon']:ampm_suffix = ''
		elif mins == '45' and secs == '00' and int(hrs) < 12:
			if hours == 'eleven':
				if ampm_suffix == 'in the morning':
					time_expansion = "a quarter to noon"
				if ampm_suffix == "at night":
					time_expansion = "a quarter to midnight"
				ampm_suffix = ''
			else:
				time_expansion = "a quarter to %s"%(num2words(int(hrs)+1,lang=self.lang))
		else:
			minutes = num2words(mins,lang=self.lang)
			if hours in ['midnight','noon']:
				time_expansion = "%s minutes past %s"%(minutes,hours)
				ampm_suffix = ''
			else:
				time_expansion = "%s %s"%(hours,minutes)
		if secs == '00':
			seconds = ''
		elif secs in ['1','01']:
			seconds = ' and one second'
		else:
			seconds = ' and %s seconds'%(num2words(secs,lang=self.lang))
		
		if time_expansion.endswith('past noon'):
			time_expansion = ' '.join(time_expansion.split()[:-2]) + seconds + ' past noon'
		elif time_expansion.endswith('past midnight'):
			time_expansion = ' '.join(time_expansion.split()[:-2]) + seconds + ' past midnight'
		else:
			time_expansion = time_expansion + seconds
		
		return time_expansion+' '+ampm_suffix 

	def convert_time(self,text):
		text = re.sub(r'\b(\d+) min\b', r'\1 minutes', text)
		time_pat = re.compile(r'\b((0?[0-9]|1[0-9]|2[0-3])[:h]([0-5][0-9])[:m]?([0-5][0-9])?\s?(am|pm|AM|PM)?)\b')
		for t in time_pat.finditer(text):
			time_string, hrs, mins, secs, ampm = t.groups()
			time_expansion = self.generate_time_string(hrs,mins,secs,ampm)
			text = re.sub(time_string, time_expansion, text)
		
			text = self.cleanup_(text).strip()		
		return text
