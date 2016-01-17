from flask import Flask,render_template,request #importing Flask elements
import requests
import re
from bs4 import BeautifulSoup
app= Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	if request.method=='POST' and 'iurl' in request.form:
		url=request.form['iurl'] #url from the form
		raw=requests.get(url) #URL from form goes inside requests
		soup=BeautifulSoup(raw.text,'html.parser')#scraped the HTML

		links= soup.find_all('meta')[9] #we want 9th meta tag
		link=str(links)
		image_links=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',link) #extracting URL from meta using regex
		image=image_links[0]


		while image!='':
			return '<img src="'+image+'"'+ 'align="center">' #render inside the image tag

	return render_template('index.html')

if __name__=='__main__':
	app.run()
