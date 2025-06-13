import requests

# Kies opdracht: 'optel' of 'tekst_omkeren' Dit is alleen een voorbeeld
opdracht = 'write_database'  # of 'tekst_omkeren'


if  opdracht == 'read_database':
    json_data = {
        'opdracht': 'read_database',
        'payload': {'tabel': 'boeken'}
    }
elif opdracht == 'write_database':
    json_data = {
        'opdracht': 'write_database',
        'payload': {'tabel': 'boeken_tabel','schrijver':'Jannetje Geelgat','boek':'Jannetjes nieuwe boek'}
    }
#
response = requests.post('http://127.0.0.1:5000/Boeken', json=json_data)

if response.ok:
    print('Resultaat:', response.json()['resultaat'])
else:
    print('Fout:', response.json())
