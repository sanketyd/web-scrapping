import urllib2
from bs4 import BeautifulSoup
import sqlite3
conn=sqlite3.connect('students.db')
c=conn.cursor()
#c.execute('''ALTER TABLE students
		#ADD username text''')
for i in range(13001,13820):
	url="http://home.iitk.ac.in/~romit/studentsearch/profile.php?view="+str(i)
	page=urllib2.urlopen(url).read()
	soup=BeautifulSoup(page,'html.parser')
	div1=soup.find_all("div",{"id":"values"})
	for elements in div1:
		div2=elements.text

	x=div2.split('\n')
	c.execute("UPDATE students SET gender=? WHERE roll_no=?",(str(x[4]),str(x[2])))
	conn.commit()
	print(x[1])
