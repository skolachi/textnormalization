import re
import spacy
import string
from .date_converter import DateConverter
from .time_converter import TimeConverter
from .abbreviation_converter import AbbreviationConverter
from .unit_converter import UnitConverter
from .number_converter import NumberConverter

nlp = spacy.load('en_core_web_md')

ascii = set(string.printable)
vocab = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '"


class TextNorm:
	def __init__(self):
		super(TextNorm, self).__init__()

	def transform(self,text):
		#cleaned = self.clean_text(text)
		normalised = self.normalise_text(text)
		
		return normalised

	def clean_text(self,text):
		return ''.join([c for c in text if c in ascii])
	
	def normalise_text(self,text):
		date_conv = DateConverter(lang='en')
		time_conv = TimeConverter(lang='en')
		abbr_conv = AbbreviationConverter(lang='en')
		unit_conv = UnitConverter(lang='en')
		number_conv = NumberConverter(lang='en')
		normalised = []
		doc = nlp(text)
		for s in doc.sents:
		#for s in text.split('\n'):
			#sent = s
			sent = s.text
			for ent in s.ents:
				if ent.label_ == "DATE":
					expanded = date_conv.transform(ent.text)
					sent = re.sub(ent.text,expanded,sent)
				if ent.label_ == "TIME":
					expanded = time_conv.transform(ent.text)
					sent = re.sub(ent.text,expanded,sent)
			
			#sent = date_conv.transform(sent)
			#sent = time_conv.transform(sent)
			sent = abbr_conv.transform(sent)
			sent = unit_conv.transform(sent)
			sent = number_conv.transform(sent)
			sent = ''.join([c if c in vocab else ' ' for c in sent])
			sent = re.sub('\s+',' ',sent)
				
			normalised.append(sent)

		normalised = [l.strip().lower() for l in normalised if l.strip() != '']
		
		return '\n'.join(normalised)		
