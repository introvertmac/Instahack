from flask import Flask,render_template,request
import requests
from bs4 import BeautifulSoup
app= Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	if request.method=='POST' and 'iurl' in request.form: #basic Flask structure 
		url=request.form['iurl'] 
		raw=requests.get(url) #make a request to the URL
		soup=BeautifulSoup(raw.text,'html.parser') #get the HTML

		links= soup.find(property="og:image") #find meta with property=og:image
		image=links.get('content') #get its content
		while image!='':
			return '<img src="'+image+'"'+ 'align="center">' #insert content in img tag

	return render_template('index.html')

if __name__=='__main__':
	app.run()
