import pickle
from tqdm import tqdm

wikimap = {}
with open('page_ids_en.ttl', 'r') as filein:
	for line in tqdm(filein, total=16000000):
		try:
			res, _, pageID, _ = [x.strip() for x in line.split(' ')]
			pageID = int(pageID.split('^^')[0].strip('"'))
			res = res.strip('<').strip('>')
			wikimap[pageID] = res
		except Exception as E:
			print(line)
			continue

#print(wikimap)

with open('wiki2dbr.pkl','wb') as fileout:
	pickle.dump(wikimap, fileout, protocol=pickle.HIGHEST_PROTOCOL)
