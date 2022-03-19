# textnorm-en 

This is a simple Python package for English text normalization.

It is based on rule based detection and expansion of Non-standard words. 

Requirements-

pip3 install spacy 
python3 -m spacy download en_core_web_md 
pip3 install num2words

Github repo-
https://github.com/skolachi/textnormalization

Sample Usage-

from textnorm_en import TextNorm
normalizer = TextNorm()

normalizer.transform(example)

Examples-
John has lunch at 12:30 pm daily. -> john has lunch at half past noon daily
The cat sat on the mat... -> the cat sat on the mat
The lockdown was announced on 20/03/2020. -> the lockdown was announced on twentieth of march two thousand and twenty
I bought 5 apples from the market. -> i bought five apples from the market
John works on cutting-edge AI. -> john works on cutting edge artificial intelligence
Germany started WW1  -> germany started world war one
I usually go to bed at 11:00 PM and wake up at 7:00 AM. -> i usually go to bed at eleven o'clock at night and wake up at seven o'clock in the morning
You can call me on 999-666-3333. -> you can call me on nine nine nine six six six three three three three
The car was speeding at 120 km/hr -> the car was speeding at one hundred and twenty kilometres per hour
The expected speed of internet is 350 Mbps. -> the expected speed of internet is three hundred and fifty megabits per second
I want to visit Hyderabad హైదరాబాద్ sometime this year -> i want to visit hyderabad sometime this year
