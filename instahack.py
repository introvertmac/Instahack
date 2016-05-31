from flask import Flask,render_template,request
import requests
from bs4 import BeautifulSoup
app= Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	if request.method=='POST' and 'iurl' in request.form:
		url=request.form['iurl']
		raw=requests.get(url)
		soup=BeautifulSoup(raw.text,'html.parser')

		links= soup.find(property="og:image")
		image=links.get('content')
		while image!='':
			return '<img src="'+image+'"'+ 'align="center">'

	return render_template('index.html')

if __name__=='__main__':
	app.run()
