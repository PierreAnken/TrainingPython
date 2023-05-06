import datetime

ajd = datetime.datetime.now()
date_definie_str = '1985-02-16 12'
date_naissance = datetime.datetime.strptime(date_definie_str, '%Y-%m-%d %H')
# timedelta
date_delta = (ajd - date_naissance)
jours = date_delta.days

reste_seconde = int(date_delta.seconds % (3600 * 24))
heures = reste_seconde // 3600
minutes = (reste_seconde - (heures * 3600)) // 60
secondes = reste_seconde - (heures * 3600) - (minutes * 60)

print('Naissance:', date_naissance.strftime('%d-%m-%Y %Hh'),
      f'Vous êtes né il y a {jours} jours {heures} heures {minutes} minutes {secondes} seconde(s)')
