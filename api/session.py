from requests import Session

user = 'Jack'
password = 'Jones'

hostname = "127.0.0.1:5000/"
session = Session()
session.auth = (user, password)

auth = session.post('http://' + hostname)
response = session.get('http://' + hostname + '/api/user')

