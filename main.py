import requests

# Kies opdracht: 'optel' of 'tekst_omkeren'
opdracht = 'write_database'  # of 'tekst_omkeren'

if opdracht == 'optel':
    json_data = {
        'opdracht': 'optel',
        'payload': {'a': 5, 'b': 7}
    }
elif opdracht == 'tekst_omkeren':
    json_data = {
        'opdracht': 'tekst_omkeren',
        'payload': {'tekst': 'Hallo wereld'}
    }
elif opdracht == 'read_database':
    json_data = {
        'opdracht': 'read_database',
        'payload': {'tabel': 'boeken'}
    }
elif opdracht == 'write_database':
    json_data = {
        'opdracht': 'write_database',
        'payload': {'tabel': 'boeken_tabel','schrijver':'jannetje geelgat','boek':'jannetjes nieuwe boek'}
    }

response = requests.post('http://127.0.0.1:5000/verwerk', json=json_data)

if response.ok:
    print('Resultaat:', response.json()['resultaat'])
else:
    print('Fout:', response.json())
