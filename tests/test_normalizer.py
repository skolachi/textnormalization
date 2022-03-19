import pytest
from textnorm_en import TextNorm

normalizer = TextNorm()

def test_normalizer():
	assert normalizer.transform('I sleep at 11:00 pm daily.') == 'i sleep at eleven o'clock at night daily'
	assert normalizer.transform('John has lunch at 12:30 pm daily.') == 'john has lunch at half past noon daily'
	assert	normalizer.transform('The cat sat on the mat...') == 'the cat sat on the mat'
	assert	normalizer.transform('The lockdown was announced on 20/03/2020.') == 'the lockdown was announced on twentieth of march two thousand and twenty'
	assert	normalizer.transform('I bought 5 apples from the market.') == 'i bought five apples from the market'
	assert	normalizer.transform('John works on cutting-edge AI.') == 'john works on cutting edge artificial intelligence'
	assert	normalizer.transform('Germany started WW1 ') == 'germany started world war one'
	assert	normalizer.transform('I usually go to bed at 11:00 PM and wake up at 7:00 AM.') == 'i usually go to bed at eleven o'clock at night and wake up at seven o'clock in the morning'
	assert	normalizer.transform('You can call me on 999-666-3333.') == 'you can call me on nine nine nine six six six three three three three'
	assert	normalizer.transform('The car was speeding at 120 km/hr') == 'the car was speeding at one hundred and twenty kilometres per hour'
	assert	normalizer.transform('The expected speed of internet is 350 Mbps.') == 'the expected speed of internet is three hundred and fifty megabits per second'
	assert	normalizer.transform('I want to visit Hyderabad హైదరాబాద్ sometime this year') == 'i want to visit hyderabad sometime this year'
