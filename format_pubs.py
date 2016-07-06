import bibtexparser
import sys

input_bibtex='pubs_AJ.txt'

with open(input_bibtex) as bibtex_file:
    bibtex_str = bibtex_file.read()

bib_database = bibtexparser.loads(bibtex_str)

#maximum number of authors to print before appending 'et al'
num_max_authors = 5

counter = 1

for entry in bib_database.entries:
	if entry['journal']=='\\apj':
		journal = "The Astrophysical Journal"
	elif entry['journal']=='\\apjl':
		journal = "The Astrophysical Journal Letters"
	elif entry['journal']=='\\apjs':
		journal = "The Astrophysical Journal Supplements"
	elif entry['journal']=='\\nat':
		journal = "Nature"
	elif entry['journal']=='\\mnras':
		journal = "Monthly Notices of the Royal Astronomical Society"
	elif entry['journal']=='\\pasp':
		journal = "Publications of the Astronomical Society of the Pacific"
	elif entry['journal']=='\\aap':
		journal = "Astronomy and Astrophysics"
	elif entry['journal']=='\\aj':
		journal = "The Astronomical Journal"
	elif entry['journal']=='ArXiv e-prints':
		journal = "arXiv:"+entry['eprint']
	elif entry['journal']=='\\na':
		journal = "New Astronomy"		
	else:
		journal="Unknown"
	w = entry['author'].split('and')
	Na = len(w)
	bis = min(num_max_authors,Na)
	authors = ""
	for i in range(bis):
		authors += w[i].replace('{','').replace('}','').replace('\\','').replace("'",'').replace("^",'').replace("~",'').replace("\n",'').rstrip()
		if (i < (bis-1)):
			authors+=','
	if (Na > num_max_authors):
		authors += " et al."
	authors+=','
	outstr=""
	outstr+= str(counter)+". "+'"'+entry['title']+'", '+authors+" "+entry['year']+", "+journal
	if ('volume' in entry):
		outstr += (", "+entry['volume'])
	if ('pages' in entry):
		outstr += (", "+entry['pages']+".")
	if ('doi' in entry):
		outstr += " DOI:"+entry['doi']
	print outstr
	print ""

	counter += 1
