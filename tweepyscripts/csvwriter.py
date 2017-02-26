import csv
#political words
political = ['many', 'local', 'professional', 'most', 'american', 
	'few', 'prominent', 'conservative', 'british', 'democratic', 
	'corrupt', 'southern', 'liberal', 'republican', 'practical', 'french', 
	'national', 'indian', 'civilian','white', 'black', 'english', 
	'ambitious', 'individual', 'influential', 'powerful', 'senior', 
	'western', 'wing', 'northern', 'german', 'irish', 'successful', 
	'unscrupulous', 'japanese', 'african', 'male', 'european','active', 
	'radical', 'female', 'whig', 'moderate', 'contemporary', 'canadian', 
	'bourgeois', 'top', 'federal', 'provincial', 'minded', 'astute', 
	'crooked', 'muslim', 'russian', 'mexican', 'italian', 'experienced', 
	'seeking', 'progressive', 'petty', 'rival', 'west', 'younger', 'time',
	'responsible', 'eminent', 'israeli', 'colonial', 'able', 'known', 
	'communist', 'socialist', 'class', 'regional', 'mainstream', 'shrewd', 
	'greek', 'australian'] 
with open('related_politics.csv', 'wb') as f:
			writer = csv.writer(f)
			writer.writerow(political)

#news words

news = ['good', 'bad', 'latest', 'local', 'sad', 'important', 'big', 
	'national', 'foreign', 'terrible', 'welcome', 'wonderful', 
	'international', 'daily', 'page', 'better', 'exciting', 'joyful', 
	'startling', 'happy', 'hard', 'false', 'unexpected', 'ill', 'glad', 
	'dreadful', 'nightly', 'interesting', 'shocking', 'alarming', 
	'tragic', 'glorious', 'fresh', 'unwelcome', 'official', 'sensational', 
	'definite', 'strange', 'encouraging', 'unpleasant', 'front', 'fatal', 
	'awful', 'pleasant', 'disturbing', 'worse', 'distressing', 'worst', 
	'melancholy', 'surprising', 'weekly', 'grim', 'astounding', 
	'authentic', 'disastrous', 'reliable', 'operative', 'astonishing', 
	'disquieting', 'straight', 'disappointing', 'evil']
with open('related_news.csv', 'wb') as f:
			writer = csv.writer(f)
			writer.writerow(political)

celebs = ['great', 'local', 'international', 'literary', 'national', 
	'wide', 'much', 'considerable', 'instant', 'minor', 'european', 
	'greatest', 'greater', 'certain', 'equal', 'future', 'famous', 
	'popular', 'sudden', 'historical', 'less', 'overnight', 'highest', 
	'ancient', 'worldwide', 'deserved', 'big', 'chief', 'favorite', 
	'known', 'universal', 'wider', 'immediate', 'melancholy', 
	'extraordinary', 'contemporary', 'temporary', 'musical', 
	'distinguished', 'posthumous', 'female', 'lasting', 'intellectual', 
	'poetical', 'extensive', 'genuine', 'infamous', 'historic', 'merited', 
	'global', 'biggest', 'sad', 'provincial', 'theatrical', 'immense', 
	'unhappy']
with open('related_celebs.csv', 'wb') as f:
			writer = csv.writer(f)
			writer.writerow(political)

sports = ['other', 'professional', 'competitive', 'outdoor', 'athletic', 
	'many', 'various', 'intramural', 'popular', 'most', 'individual', 
	'major', 'intercollegiate', 'active', 'american', 'manly', 'favorite', 
	'rural', 'modern', 'extreme', 'field', 'door', 'traditional', 
	'recreational', 'aquatic', 'amateur', 'indoor', 'interscholastic', 
	'strenuous', 'wild', 'rough', 'dangerous', 'vigorous', 'pro', 'minor', 
	'childish', 'usual', 'youthful', 'violent', 'cruel', 'favourite', 
	'time', 'collegiate', 'olympic', 'equestrian', 'male', 'noncontact', 
	'boyish', 'risk', 'brutal', 'rustic', 'water', 'all', 'innocent', 
	'called', 'martial', 'aggressive', 'healthful', 'amorous', 'combative', 
	'respective', 'rude']
with open('related_sports.csv', 'wb') as f:
			writer = csv.writer(f)
			writer.writerow(political)