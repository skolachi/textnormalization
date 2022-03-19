from num2words import num2words
import re

number = '\d+|[0-9,]+.?\d+'

UNITS_COMMON = [(re.compile('%s' % x[0]), x[1]) for x in [
	(r'\b(%s)\s?cm2\b'%(number), r'\1 square centimetres'),
	(r'\bcm2\b', r'square centimetres'),
	(r'\b(%s)\s?cm3\b'%(number), r'\1 cubic centimetres'),
	(r'\bcm3\b', r'cubic centimetres'),
	(r'\b(%s)\s?cm\b'%(number), r'\1 centimetres'),
	(r'\bcm\b', r'centimetres'),
	(r'\b(%s)\s?mm2\b'%(number), r'\1 square millimetres'),
	(r'\bmm2\b', r'square millimetres'),
	(r'\b(%s)\s?mm3\b'%(number), r'\1 cubic millimetres'),
	(r'\bmm3\b', r'cubic millimetres'),
	(r'\b(%s)\s?mm\b'%(number), r'\1 millimetres'),
	(r'\bmm\b', r'millimetres'),
	(r'\b(%s)\s?μm\b'%(number), r'\1 micrometres'),
	(r'\bμm\b', r'micrometres'),
	(r'\b(%s)\s?nm\b'%(number), r'\1 nanometres'),
	#(r'\bnm\b', r'nanometres'),
	(r'\b(%s)\s?m2\b'%(number), r'\1 square metres'),
	(r'\bm2\b', r'square metres'),
	(r'\b(%s)\s?m3\b'%(number), r'\1 cubic metres'),
	#(r'\bm3\b', r'cubic metres'),
	(r'\b(%s)\s?km/h\b'%(number), r"\1 kilometres per hour"),
	(r'\b(%s)\s?km/hr\b'%(number), r"\1 kilometres per hour"),
	(r'\b(%s)\s?m/s\b'%(number), r"\1 metres per second"),
	(r'\b(%s)\s?m\b'%(number), r'\1 metres'),
	#(r'\bm\b', r'metres'),
	(r'\b(%s)\s?km2\b'%(number), r'\1 square kilometres'),
	(r'\bkm2\b', r'square kilometres'),
	(r'\b(%s)\s?km\b'%(number), r'\1 kilometres'),
	#(r'\bkm\b', r'kilometres'),
	(r'\b(%s)\s?Mbps\b'%(number), r'\1 megabits per second'),
	(r'\bmbps\b', r'megabit per second'),
	(r'\b(%s)\s?kb\b'%(number), r'\1 kilobit'),
	#(r'\bkb\b', r'kilobit'),
	(r'\b(%s)\s?mb\b'%(number), r'\1 megabit'),
	#(r'\bmb\b', r'megabit'),
	(r'\b(%s)\s?kB\b'%(number), r'\1 kilobyte'),
	(r'\b(%s)\s?MB\b'%(number), r'\1 megabyte'),
	#(r'\bMB\b', r'megabyte'),
	(r'\b(%s)\s?GB\b'%(number), r'\1 gigabyte'),
	(r'\b(%s)\s?TB\b'%(number), r'\1 terabyte'),
	(r'\b(%s)\s?[Kk][Hh]z\b'%(number), r'\1 kilohertz'),
	(r'\b(%s)\s?[Mm][Hh]z\b'%(number), r'\1 megahertz'),
	(r'\b(%s)\s?[Gg][Hh]z\b'%(number), r'\1 gigahertz'),
	(r'\b(%s)\s?[Tt][Hh]z\b'%(number), r'\1 terahertz'),
	(r'\b(%s)\s?[Hh]z\b'%(number), r'\1 hertz'),
	(r'\b(%s)\s?[Vv]\b'%(number), r'\1 volt'),
	(r'\b(%s)\s?A\b'%(number), r'\1 ampere'),
	(r'\b(%s)\s?mA\b'%(number), r'\1 milliampere'),
	(r'\b(%s)\s?ltr\b'%(number), r'\1 litres'),
	#(r'\b(%s)\s?€'%(number), r'\1 euros'),
	#(r'€\s?(%s)\b'%(number), r'\1 euros'),
	(r'€', r' euro '),
	#(r'\b(%s)\s?£'%(number), r'\1 pounds sterling'),
	#(r'£\s?(%s)\b'%(number), r'\1 pounds sterling'),
	(r'£', r' pound sterling '),
	(r'￡', r' pound sterling '),
	#(r'\b(%s)\s?￥'%(number), r'\1 yuan '),
	#(r'￥\s?(%s)\b'%(number), r'\1 yuan '),
	(r'￥', r' yuan '),
	#(r'\b(%s)\s?\$'%(number), r'\1 dollars'),
	#(r'\$\s?(%s)\b'%(number), r'\1 dollars'),
	(r'\$', ' dollars '),
	(r'\b(%s)\s?lb\b'%(number), r'\1 pounds'),
	(r'\b(%s)\s?lbs\b'%(number), r'\1 pounds'),
	(r'\b(%s)\s?kg\b'%(number), r'\1 kilograms'),
	#(r'\b(%s)\s?%\b'%(number), r'\1 percent'),
	(r'\%', 'percent'),
	(r'/', ' per '),
	(r'±', 'plus or minus'),
	(r'\b(%s)\s?x\b'%(number), r'\1 times'),
	(r'\b(%s)\s?s\b'%(number), r'\1 seconds'),
	(r'\b(%s)\s?ms\b'%(number), r'\1 milliseconds'),
	(r'\b(%s)\s?ns\b'%(number), r'\1 nanoseconds'),
	(r'\b(%s)\s?μs\b'%(number), r'\1 microseconds'),
	(r'\b(%s)\s?mi\b'%(number), r'\1 miles'),
	(r'\b(%s)\s?[º°]\s?K\b'%(number), r'\1 degrees kelvin'),
	(r'\b(%s)\s?k\b'%(number), r'\1 thousand'),
	(r'\b(%s)\s?[º°]\s?F\b'%(number), r'\1 degrees fahrenheit'),
	(r'\b(%s)\s?F\b'%(number), r'\1 fala'),
	(r'\b(%s)\s?μF\b'%(number), r'\1 microfarad'),
	(r'\b(%s)\s?[º°]\s?C\b'%(number), r'\1 degrees centigrade'),
	(r'\b(%s)\s?H\b'%(number), r'\1 henry'),
	(r'\b(%s)\s?μH\b'%(number), r'\1 microhenry'),
	(r'\b(%s)\s?mH\b'%(number), r'\1 millihenry'),
	(r'\b(%s)°(\d+)'%(number), r'\1 degree \2'),
	(r'\b(%s)\'(\d+)'%(number), r'\1 minute \2'),
	(r'\b(%s)\"'%(number), r'\1 second'),
	#(r'\b(\d+)-(\d+)\b', r'\1 to \2'),
]]



class UnitConverter:
	def __init__(self,lang):
		super(UnitConverter,self).__init__()
		self.lang = lang

	def transform(self,text):
		text = self.convert_units(text)
		return text

	def convert_units(self,text):
		for regex, replacement in UNITS_COMMON:
			try:
				text = re.sub(regex, replacement, text)
			except:
				print('Unit conversion failed')

		text = self.cleanup_(text)
		return text
	
	def cleanup_(self,text):
		text = re.sub(r'\s+', ' ', text)
		text = text.strip()
		return text
