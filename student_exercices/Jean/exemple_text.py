texte = '''
	BJ	Bénin	10.323.000
	BF	Burkina Faso	17.322.796
	CM	Cameroun	20.386.799
	CF	République centrafricaine	4.616.000
	CG	République du Congo	4.448.000
	CI	Côte d'Ivoire	23.202.000
	GA	Gabon	1.672.000
	GW	Guinée Bissau	1.704.000
'''

for line in texte[1:-1].split('\n'):
    line_cleaned = line.strip().replace('\t', '|')

    abr, nom, chiffre = line_cleaned.split('|')
    print(abr, nom, chiffre, sep=' - ')
