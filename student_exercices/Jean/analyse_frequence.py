from collections import Counter
from pprint import pprint

parabole = '''11 Il dit encore : « Un homme avait deux fils. 12 Le plus jeune dit à son père : “Père, donne-moi la 
part de bien qui doit me revenir.” Et le père leur partagea son avoir. 13 Peu de jours après, le plus jeune fils, 
ayant tout réalisé, partit pour un pays lointain et il y dilapida son bien dans une vie de désordre. 14 Quand il eut 
tout dépensé, une grande famine survint dans ce pays, et il commença à se trouver dans l’indigence. 15 Il alla se 
mettre au service d’un des citoyens de ce pays qui l’envoya dans ses champs garder les porcs. 16 Il aurait bien voulu 
se remplir le ventre des gousses que mangeaient les porcs, mais personne ne lui en donnait. 17 Rentrant alors en 
lui-même, il se dit : “Combien d’ouvriers de mon père ont du pain de reste, tandis que moi, ici, je meurs de faim ! 
18 Je vais aller vers mon père et je lui dirai : Père, j’ai péché envers le ciel et contre toi. 19 Je ne mérite plus 
d’être appelé ton fils. Traite-moi comme un de tes ouvriers.” 20 Il alla vers son père. Comme il était encore loin, 
son père l’aperçut et fut pris de pitié : il courut se jeter à son cou et le couvrit de baisers. 21 Le fils lui dit : 
“Père, j’ai péché envers le ciel et contre toi. Je ne mérite plus d’être appelé ton fils...” 22 Mais le père dit à 
ses serviteurs : “Vite, apportez la plus belle robe, et habillez-le ; mettez-lui un anneau au doigt, des sandales aux 
pieds. 23 Amenez le veau gras, tuez-le, mangeons et festoyons, 24 car mon fils que voici était mort et il est revenu 
à la vie, il était perdu et il est retrouvé. '''

characters = '1234567890.,?`!¨-;:”"«“'

for x in range(len(characters)):
    parabole = parabole.replace(characters[x], " ")
    parabole = ''.join(x for x in parabole if x not in characters)
    parabole = parabole.replace("   ", " ")
    parabole = parabole.replace("   ", " ")
    parabole = parabole.replace("  ", " ")
    parabole = parabole.replace(" ", ", ")

import re

list = parabole
separators = "; ", ", "


def custom_split(sepr_list, str_to_split):
    regular_exp = '|'.join(map(re.escape, sepr_list))
    return re.split(regular_exp, str_to_split)


print(custom_split(separators, list))

text = list
result = len(text.split())

print("On trouve " + str(result) + " mots dans ce texte.")


print(list.count(" "))
pprint(Counter(text.split()))
