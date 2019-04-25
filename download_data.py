import requests

url = 'http://www.mediafire.com/file/i3sk5aa2gal4d2x/employee_reviews.csv/file'
r = requests.get(url, allow_redirects=True)
open('employee_reviews.csv', 'wb').write(r.content)