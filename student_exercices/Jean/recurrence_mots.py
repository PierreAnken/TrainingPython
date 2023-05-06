from collections import Counter
from pprint import pprint
import re
from collections import Counter

apocalypse = '''Introduction
APOC 1 Révélation de Jésus Christ :
Dieu la lui donna pour montrer à ses serviteurs ce qui doit arriver bientôt.
Il la fit connaître en envoyant son ange à Jean son serviteur,
2 lequel a attesté comme Parole de Dieu et témoignage de Jésus Christ tout ce qu’il a vu.
3 Heureux celui qui lit,
et ceux qui écoutent les paroles de la prophétie
et gardent ce qui s’y trouve écrit,
car le temps est proche.
Adresse
4 Jean aux sept Eglises qui sont en Asie :
Grâce et paix vous soient données,
de la part de celui qui est, qui était et qui vient,
de la part des sept esprits qui sont devant son trône,
5 et de la part de Jésus Christ, le témoin fidèle, le premier-né d’entre les morts et le prince des rois de la terre.
A celui qui nous aime,
qui nous a délivrés de nos péchés par son sang,
6 qui a fait de nous un royaume, des prêtres pour Dieu son Père,
à lui gloire et pouvoir pour les siècles des siècles. Amen.
7 Voici, il vient au milieu des nuées,
et tout œil le verra,
et ceux mêmes qui l’ont percé :
toutes les tribus de la terre seront en deuil à cause de lui.
Oui ! Amen !
8 Je suis l’Alpha et l’Oméga, dit le Seigneur Dieu,
celui qui est, qui était et qui vient,
le Souverain.
Vision du Fils de l’homme
9 Moi, Jean, votre frère et votre compagnon dans l’épreuve, la royauté et la persévérance en Jésus, je me trouvais dans l’île de Patmos à cause de la Parole de Dieu et du témoignage de Jésus.
10 Je fus saisi par l’Esprit au jour du Seigneur, et j’entendis derrière moi une puissante voix,
telle une trompette,
11 qui proclamait : Ce que tu vois, écris-le dans un livre, et envoie-le aux sept Eglises : à Ephèse, à Smyrne, à Pergame, à Thyatire, à Sardes, à Philadelphie et à Laodicée.
12 Je me retournai pour regarder la voix qui me parlait ; et, m’étant retourné, je vis sept chandeliers d’or ;
13 et, au milieu des chandeliers,
quelqu’un qui semblait un fils d’homme.
Il était vêtu d’une longue robe,
une ceinture d’or lui serrait la poitrine ;
14 sa tête et ses cheveux étaient blancs comme laine blanche, comme neige,
et ses yeux étaient comme une flamme ardente ;
15 ses pieds semblaient d’un bronze précieux, purifié au creuset,
et sa voix était comme la voix des océans ;
16 dans sa main droite, il tenait sept étoiles,
et de sa bouche sortait un glaive acéré, à deux tranchants.
Son visage resplendissait, tel le soleil dans tout son éclat.
17 A sa vue, je tombai comme mort à ses pieds,
mais il posa sur moi sa droite et dit :
Ne crains pas,
Je suis le Premier et le Dernier,
18 et le Vivant ;
je fus mort, et voici, je suis vivant pour les siècles des siècles,
et je tiens les clés de la mort et de l’Hadès.
19 Ecris donc ce que tu as vu, ce qui est et ce qui doit arriver ensuite.
20 Quant au mystère des sept étoiles que tu as vues dans ma droite et aux sept chandeliers d’or, voici : les sept étoiles sont les anges des sept Eglises, et les sept chandeliers sont les sept Eglises.'''

# utilisation de regex findall() qui compte les mots dans la chaîne Python
liste_mots = re.findall(r'\w+', apocalypse)
result = len(liste_mots)
print("Il y a " + str(result) + " mots dans l'extrait de l'Apocalypse.")

# chercher un mot spécifique et sa récurrence
print(f"Le mot étoiles apparaît {apocalypse.count('étoiles')} fois dans le texte de l'Apocalypse.")
print(f"On trouve {sum(word == ' ' for word in apocalypse)} mots dans les 2 premiers chapitres de l'Apocalypse.")

# frequence = dict(Counter(apocalypse))
counter_mot = dict(Counter(liste_mots))
# pprint(counter_mot)

x = "Jésus"
index_x = apocalypse.index(x)
print(apocalypse[index_x - 10:index_x + 10 + len(x)],'a la position', index_x)
