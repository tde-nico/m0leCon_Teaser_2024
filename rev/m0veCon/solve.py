pairs = 'scoligainelespniitrocomolothllchewrtteeaalsadofoaysteessasfiadidctatepenrinoacofhaveiotrshheimicontiiliramemsumiulecreedsosiopdepaieusiaouhondgetteslyowtonsarwetyortaryyoinuntusencanhingdabeiscameotrsoselceliermaviwiagraeiivlatspromdipewaoopletntnaurpoutab'
pairs = [pairs[i:i+2].encode() for i in range(0, len(pairs), 2)]

words = [
	b"could", b"message", b"international", b"read", b"family",
	b"event", b"store", b"detail", b"system", b"version", b"last",
	b"national", b"need", b"link", b"travel", b"member", b"each",
	b"click", b"access", b"over", b"general", b"black", b"south",
	b"address", b"program", b"high", b"that", b"shopping", b"said",
	b"download", b"forum", b"another", b"number", b"only", b"comment",
	b"main", b"subject", b"data", b"site", b"following", b"hotel",
	b"year", b"center", b"view", b"must", b"well", b"product",
	b"computer", b"internet", b"software", b"back", b"there", b"about",
	b"just", b"phone", b"price", b"next", b"like", b"some", b"between",
	b"part", b"management", b"county", b"within", b"will", b"still",
	b"text", b"development", b"those", b"small", b"january",
	b"information", b"such", b"location", b"water", b"result",
	b"child", b"work", b"related", b"city", b"want", b"before",
	b"security", b"size", b"education", b"very", b"than", b"world",
	b"women", b"since", b"project", b"even", b"health", b"support",
	b"open", b"order", b"government", b"show", b"case", b"info",
	b"then", b"total", b"ebay", b"company", b"from", b"rating",
	b"house", b"first", b"type", b"more", b"down", b"which", b"real",
	b"please", b"where", b"group", b"level", b"days", b"have", b"long",
	b"north", b"digital", b"profile", b"directory", b"using", b"during",
	b"personal", b"white", b"business", b"report", b"them", b"most",
	b"area", b"home", b"item", b"video", b"care", b"many", b"privacy",
	b"local", b"people", b"account", b"make", b"free", b"including",
	b"shipping", b"service", b"history", b"contact", b"design",
	b"control", b"would", b"media", b"mail", b"sign", b"does", b"your",
	b"available", b"resource", b"through", b"review", b"network",
	b"send", b"into", b"music", b"sport", b"life", b"here", b"guide",
	b"file", b"user", b"post", b"technology", b"university", b"place",
	b"great", b"reserved", b"full", b"date", b"board", b"office",
	b"list", b"what", b"both", b"also", b"same", b"american", b"form",
	b"game", b"based", b"code", b"today", b"index", b"being", b"united",
	b"when", b"help", b"section", b"state", b"name", b"policy", b"current",
	b"return", b"think", b"know", b"much", b"found", b"posted", b"under",
	b"special", b"page", b"this", b"news", b"student", b"good", b"used",
	b"book", b"online", b"right", b"public", b"rate", b"community",
	b"three", b"with", b"term", b"line", b"been", b"love", b"time",
	b"while", b"their", b"power", b"without", b"website", b"best", b"should",
	b"search", b"copyright", b"research", b"other", b"class", b"previous",
	b"these", b"they", b"change", b"shop", b"find", b"because", b"picture",
	b"after", b"school", b"were", b"made", b"take", b"check", b"email", 
]

def decompress(data):
	res = bytearray()
	i = 0
	while i < len(data):
		code = data[i]
		i += 1
		
		if code >= 128:
			res += pairs[code - 128]
		
		elif code >= 9:
			res.append(code)
		
		elif code >= 6:
			word = words[data[i]]
			if code == 8:
				res += b' '
			res += word
			if code == 7:
				res += b' '
			i += 1
		
		elif code >= 1:
			res += data[i:i+code]
			i += code
		
		else:
			raise ValueError("Unexpected code: %d" % code)
	return res



key = {'a': 'normal', 'b': 'hunter', 'c': 'attack', 'd': 'vessel', 'e': 'tunnel', 'f': 'method', 'g': 'cancel', 'h': 'format', 'i': 'gravel', 'j': 'origin', 'k': 'rescue', 'l': 'rotate', 'm': 'burden', 'n': 'palace', 'o': 'flower', 'p': 'guitar', 'q': 'ballot', 'r': 'ribbon', 's': 'jacket', 't': 'bishop', 'u': 'hungry', 'v': 'monday', 'w': 'velvet', 'x': 'pillow', 'y': 'insane', 'z': 'purple', '0': 'expert', '1': 'friend', '2': 'medium', '3': 'silent', '4': 'bitter', '5': 'pencil', '6': 'sprint', '7': 'cousin', '8': 'gallon', '9': 'stable', '_': 'proton', '{': 'future', '}': 'wealth'}
out = '0x677588ce2062dfc5702062fcbf6e2066fefc6520a572e96c20a46262b020bd85fa20f2e2b020a96ca97420bd85fa20f2e2b02062fcbf6e206578f591208bc6982066a4a36420c0f0e620e0d9e520f2e2b020a1d2636b20a46262b020d5958420677588ce2062dfc570206578f59120f2e2b020d5958420bd85fa2062dfc57020cf948d'
out = bytes.fromhex(out.replace('0x', ''))

decompressed = decompress(out).decode().split(' ')
inv_key = {v: k for k, v in key.items()}
for word in decompressed:
	print(inv_key[word], end='')
print()

# ptm{ar3_w3_m0v1ng_crypt0_y3t}
