from num2words import num2words
import re

countrycodes = {'United States of America': '+1', 'Afghanistan': '+93', 'Albania': '+355', 'Algeria': '+213', 'American Samoa': '+1-684', 'Andorra': '+376', 'Angola': '+244', 'Anguilla': '+1-264', 'Antarctica': '+672', 'Antigua': '+1-268', 'Argentina': '+54', 'Armenia': '+374', 'Aruba': '+297', 'Ascension': '+247', 'Australia': '+61', 'Australian External Territories': '+672', 'Austria': '+43', 'Azerbaijan': '+994', 'Bahamas': '+1-242', 'Bahrain': '+973', 'Bangladesh': '+880', 'Barbados': '+1-246', 'Barbuda': '+1-268', 'Belarus': '+375', 'Belgium': '+32', 'Belize': '+501', 'Benin': '+229', 'Bermuda': '+1-441', 'Bhutan': '+975', 'Bolivia': '+591', 'Bosnia & Herzegovina': '+387', 'Botswana': '+267', 'Brazil': '+55', 'British Virgin Islands': '+1-284', 'Brunei Darussalam': '+673', 'Bulgaria': '+359', 'Burkina Faso': '+226', 'Burundi': '+257', 'Cambodia': '+855', 'Cameroon': '+237', 'Canada': '+1', 'Cape Verde Islands': '+238', 'Cayman Islands': '+1-345', 'Central African Republic': '+236', 'Chad': '+235', 'Chatham Island (New Zealand)': '+64', 'Chile': '+56', 'China (PRC)': '+86', 'Christmas Island': '+61-8', 'Cocos-Keeling Islands': '+61', 'Colombia': '+57', 'Comoros': '+269', 'Congo': '+242', 'Congo, Dem. Rep. of (former Zaire)': '+243', 'Cook Islands': '+682', 'Costa Rica': '+506', "Côte d'Ivoire (Ivory Coast)": '+225', 'Croatia': '+385', 'Cuba': '+53', 'Cuba (Guantanamo Bay)': '+5399', 'Curaçao': '+599', 'Cyprus': '+357', 'Czech Republic': '+420', 'Denmark': '+45', 'Diego Garcia': '+246', 'Djibouti': '+253', 'Dominica': '+1-767', 'Dominican Republic +1-809 and': '+1-829', 'East Timor': '+670', 'Easter Island': '+56', 'Ecuador': '+593', 'Egypt': '+20', 'El Salvador': '+503', 'Ellipso (Mobile Satellite service) +8812 and': '+8813', 'EMSAT (Mobile Satellite service)': '+88213', 'Equatorial Guinea': '+240', 'Eritrea': '+291', 'Estonia': '+372', 'Ethiopia': '+251', 'Falkland Islands (Malvinas)': '+500', 'Faroe Islands': '+298', 'Fiji Islands': '+679', 'Finland': '+358', 'France': '+33', 'French Antilles': '+596', 'French Guiana': '+594', 'French Polynesia': '+689', 'Gabonese Republic': '+241', 'Gambia': '+220', 'Georgia': '+995', 'Germany': '+49', 'Ghana': '+233', 'Gibraltar': '+350', 'Global Mobile Satellite System (GMSS)': '+881', 'ICO Global +8810 and': '+8811', 'Ellipso 8812': '+8813', 'Iridium 8816': '+8817', 'Globalstar 8818 and': '8819', 'Globalstar (Mobile Satellite Service) +8818 and': '+8819', 'Greece': '+30', 'Greenland': '+299', 'Grenada': '+1-473', 'Guadeloupe': '+590', 'Guam': '+1-671', 'Guantanamo Bay': '+5399', 'Guatemala': '+502', 'Guinea-Bissau': '+245', 'Guinea': '+224', 'Guyana': '+592', 'Haiti': '+509', 'Honduras': '+504', 'Hong Kong': '+852', 'Hungary': '+36', 'ICO Global (Mobile Satellite Service) +8810 and': '+8811', 'Iceland': '+354', 'India': '+91', 'Indonesia': '+62', 'Inmarsat (Atlantic Ocean - East)': '+871', 'Inmarsat (Atlantic Ocean - West)': '+874', 'Inmarsat (Indian Ocean)': '+873', 'Inmarsat (Pacific Ocean)': '+872', 'Inmarsat SNAC': '+870', 'International Freephone Service': '+800', 'International Shared Cost Service (ISCS)': '+808', 'Iran': '+98', 'Iraq': '+964', 'Ireland': '+353', 'Iridium (Mobile Satellite service) +8816 and': '+8817', 'Israel': '+972', 'Italy': '+39', 'Ivory Coast': '+225', 'Jamaica': '+1-876', 'Japan': '+81', 'Jordan': '+962', 'Kazakhstan': '+7', 'Kenya': '+254', 'Kiribati': '+686', 'Korea (North)': '+850', 'Korea (South)': '+82', 'Kuwait': '+965', 'Kyrgyz Republic': '+996', 'Laos': '+856', 'Latvia': '+371', 'Lebanon': '+961', 'Lesotho': '+266', 'Liberia': '+231', 'Libya': '+218', 'Liechtenstein': '+423', 'Lithuania': '+370', 'Luxembourg': '+352', 'Macao': '+853', 'Macedonia (Former Yugoslav Rep of.)': '+389', 'Madagascar': '+261', 'Malawi': '+265', 'Malaysia': '+60', 'Maldives': '+960', 'Mali Republic': '+223', 'Malta': '+356', 'Marshall Islands': '+692', 'Martinique': '+596', 'Mauritania': '+222', 'Mauritius': '+230', 'Mayotte Island': '+269', 'Mexico': '+52', 'Micronesia (Federal States of)': '+691', 'Midway Island': '+1-808', 'Moldova': '+373', 'Monaco': '+377', 'Mongolia': '+976', 'Montenegro': '+382', 'Montserrat': '+1-664', 'Morocco': '+212', 'Mozambique': '+258', 'Myanmar': '+95', 'Namibia': '+264', 'Nauru': '+674', 'Nepal': '+977', 'Netherlands': '+31', 'Netherlands Antilles': '+599', 'Nevis': '+1-869', 'New Caledonia': '+687', 'New Zealand': '+64', 'Nicaragua': '+505', 'Niger': '+227', 'Nigeria': '+234', 'Niue': '+683', 'Norfolk Island': '+672', 'Northern Marianas Islands (Saipan, Rota & Tinian)': '+1-670', 'Norway': '+47', 'Oman': '+968', 'Pakistan': '+92', 'Palau': '+680', 'Palestinian Settlements': '+970', 'Panama': '+507', 'Papua New Guinea': '+675', 'Paraguay': '+595', 'Peru': '+51', 'Philippines': '+63', 'Poland': '+48', 'Portugal': '+351', 'Puerto Rico +1-787 or': '+1-939', 'Qatar': '+974', 'Réunion Island': '+262', 'Romania': '+40', 'Russia': '+7', 'Rwandese Republic': '+250', 'St. Helena': '+290', 'St. Kitts/Nevis': '+1-869', 'St. Lucia': '+1-758', 'St. Pierre & Miquelon': '+508', 'St. Vincent & Grenadines': '+1-784', 'Samoa': '+685', 'San Marino': '+378', 'São Tomé and Principe': '+239', 'Saudi Arabia': '+966', 'Senegal': '+221', 'Serbia': '+381', 'Seychelles Republic': '+248', 'Sierra Leone': '+232', 'Singapore': '+65', 'Slovak Republic': '+421', 'Slovenia': '+386', 'Solomon Islands': '+677', 'Somali Democratic Republic': '+252', 'South Africa': '+27', 'Spain': '+34', 'Sri Lanka': '+94', 'Sudan': '+249', 'Suriname': '+597', 'Swaziland': '+268', 'Sweden': '+46', 'Switzerland': '+41', 'Syria': '+963', 'Taiwan': '+886', 'Tajikistan': '+992', 'Tanzania': '+255', 'Thailand': '+66', 'Thuraya (Mobile Satellite service)': '+88216', 'Timor Leste': '+670', 'Togolese Republic': '+228', 'Tokelau': '+690', 'Tonga Islands': '+676', 'Trinidad & Tobago': '+1-868', 'Tunisia': '+216', 'Turkey': '+90', 'Turkmenistan': '+993', 'Turks and Caicos Islands': '+1-649', 'Tuvalu': '+688', 'Uganda': '+256', 'Ukraine': '+380', 'United Arab Emirates': '+971', 'United Kingdom': '+44', 'US Virgin Islands': '+1-340', 'Universal Personal Telecommunications (UPT)': '+878', 'Uruguay': '+598', 'Uzbekistan': '+998', 'Vanuatu': '+678', 'Vatican City +39 and': '+379', 'Venezuela': '+58', 'Vietnam': '+84', 'Wake Island': '+808', 'Wallis and Futuna Islands': '+681', 'Yemen': '+967', 'Zambia': '+260', 'Zanzibar': '+255', 'Zimbabwe': '+263'}

class NumberConverter:
	def __init__(self, lang):
		super(NumberConverter, self).__init__()
		self.lang = lang

	def transform(self,text):
		text = self.convert_phonenumbers(text)
		text = self.convert_zipcodes(text)
		text = self.convert_postcodes(text)
		text = self.convert_ordinals(text)
		text = self.reformat_bullet_numbers(text)
		#text = self.convert_decimals(text)
		text = self.convert_cardinals(text)
		text = self.convert_romannumerals(text)
			
		return text

	def convert_phonenumbers(self,text): # this also takes care of long number sequences like bank account numbers, etc 
		codes = [c[1:] for c in countrycodes.values()]
		#phone_patt1 = re.compile(r'(\+?(%s)?\s?(0?[0-9(\)\.\-\s]{9,}))'%('|'.join(codes)))
		phone_patt1 = re.compile('(\+?(%s)?[ -.]*(0?[0-9]{10,}|\(?[0-9]{3}\)?[ -.]\(?[0-9]{3}\)?[ -.]\(?[0-9]{4}\)?))'%('|'.join(codes)))
		#phone_patt = re.compile(r'(\+?%s\s+[0-9]{10})|(0?[0-9]{10})|([0-9]{3}[ -][0-9]{3}[ -][0-9]{4})'%('|'.join(codes)))
		for p in phone_patt1.finditer(text):
			#print(p.groups())
			if p.groups()[1] != None:
				if p.groups()[0][0] == '+':
					phone_string = ' plus '
				else:
					phone_string = ' '
				phone_string = phone_string + num2words(p.groups()[1],lang=self.lang) + ' '
			else:
				phone_string = ' '
			phone_string += self.spellout_number_pattern(p.groups()[2])
			phone_string = phone_string.replace('-', ' ')
			#for c in p.groups()[2]:
			#	if c.isdigit():
			#		phone_string += num2words(c,lang=self.lang) + ' '
			
			text = text.replace(p.groups()[0],phone_string)
			#text = re.sub(p.groups()[0],phone_string,text) #sre constants error

		phone_patt2 = re.compile(r'\b((phone|telephone|number|call)([A-Za-z, ]+)([0-9]{3,}))\b',re.IGNORECASE)
		for p in phone_patt2.finditer(text):
			phone_string = p.groups()[1] + ' ' + p.groups()[2] + ' ' + self.spellout_number_pattern(p.groups()[3])
			#for c in p.groups()[0]:
			#	if c.isdigit():
			#		phone_string += num2words(c,lang=self.lang) + ' ' 	

			text = text.replace(p.groups()[0],phone_string)

		phone_patt3 = re.compile(r'\b(\d{3}-\d{3})\b')
		for p in phone_patt3.finditer(text):
			#print(p.groups()[0])
			number_string = self.spellout_number_pattern(p.groups()[0].replace('-',' '))
			text = text.replace(p.groups()[0],number_string)

		text = self.cleanup_(text)
		return text

	def spellout_number_pattern(self,number):
		number_string = ' '
		for c in number:
			if c.isdigit():
				number_string += num2words(c,lang=self.lang) + ' '
			if c.isalpha():
				number_string += c + ' '
			
		return number_string


	def convert_zipcodes(self,text):
		zipcode_patt = re.compile(r'\bcode\b[a-zA-Z ]+([0-9]{5,6})\b',re.IGNORECASE)
		for p in zipcode_patt.finditer(text):
			#print(p.groups())
			zipcode_string = self.spellout_number_pattern(p.groups()[0]) 
			text = text.replace(p.groups()[0],zipcode_string)
				
		text = self.cleanup_(text)
		return text


	def convert_postcodes(self,text):
		postcode_patt = re.compile(r'\b([A-Z0-9]{6,15})\b')
		for p in postcode_patt.finditer(text):
			#print(p.groups())
			postcode_string = self.spellout_number_pattern(p.groups()[0]) 
			text = text.replace(p.groups()[0],postcode_string)
				
		text = self.cleanup_(text)
		return text
	
	def reformat_bullet_numbers(self,text):
		text = re.sub(r'([0-9]+)([a-z]+)\b',r'\1 \2',text)
		return text

	def roman_to_int(self,s):
		rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,\
					'i':1, 'v':5, 'x':10, 'd':500, 'm':1000}
		int_val = 0
		for i in range(len(s)):
			if i > 0 and rom_val[s[i]] > rom_val[s[i-1]]:
				int_val += rom_val[s[i]] - 2 * rom_val[s[i-1]]
			else:
				int_val += rom_val[s[i]]

		return int_val

	def convert_romannumerals(self,text):
		#roman_patt = re.compile(r'((sonnet|chapter|section|volume)\s+([IVXLCDM]+))\b',re.IGNORECASE)
		roman_patt = re.compile(r'((sonnet|chapter|section|volume)\s+([IVXLCDM]+))\b')
		for r in roman_patt.finditer(text):
			roman_string = r.groups()[1] + ' ' + num2words(self.roman_to_int(r.groups()[2]),lang=self.lang) + ' '
			roman_string = roman_string.replace('-',' ')	
			text = re.sub(r.groups()[0],roman_string,text)

		text = self.cleanup_(text)
		return text

	def convert_decimals(self,text):
		decimal_patt = re.compile(r'([.][0-9]+)\b')
		for d in decimal_patt.finditer(text):
			if d.groups()[0][1:] == '00':
				text = re.sub(d.groups()[0],'',text)
			else:
				decimal_string = ' point '+' '.join([num2words(c,lang=self.lang) for c in d.groups()[0][1:]])
				decimal_string = decimal_string.replace('-', ' ')
				text = re.sub(d.groups()[0],decimal_string,text)
		
		text = self.cleanup_(text)
		return text

	def convert_ordinals(self,text):
		ordinal_patt = re.compile(r'\b([0-9]+(st|rd|nd|th))\b')
		for d in ordinal_patt.finditer(text):
			ordinal_string = ' ' + num2words(d.groups()[0][:-2],lang=self.lang,ordinal=True) + ' '
			ordinal_string = ordinal_string.replace('-', ' ')
			text = re.sub(d.groups()[0],ordinal_string,text)
		
		text = self.cleanup_(text)
		return text

	def convert_cardinals(self,text):
		text = re.sub(r'\b(\d+)-(\d+)\b', r'\1 to \2', text)
		cardinal_patt = re.compile(r'\b([0-9,]+\.\d+|\d+)\b')
		for d in cardinal_patt.finditer(text):
			#print(d.groups())
			cardinal = d.groups()[0].replace(',','')
			if cardinal != '':
				cardinal_string = ' '+num2words(cardinal,lang=self.lang)+' '
				cardinal_string = cardinal_string.replace('-', ' ')
				text = re.sub(cardinal,cardinal_string,text,count=1)
		
		text = self.cleanup_(text)
		return text
		
	def cleanup_(self,text):
		#text = text.strip()
		#text = re.sub(r'-_',' ',text)
		text = re.sub(r',','',text)
		text = re.sub(r'\s+',' ',text)

		return text
