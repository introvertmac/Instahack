from flask import Flask,render_template,request 
import requests
from bs4 import BeautifulSoup
import json
app= Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	if request.method=='POST' and 'iurl' in request.form:
		url=request.form['iurl'] #getting url from the template Form
		raw=requests.get(url) #making request to the URL
		soup=BeautifulSoup(raw.text,'html.parser') #scrap the page data

		data= soup.find_all('script')[5].contents #from list of scripts,we need 5th script tag's content
		info=data[0] #contents look like JSON array, we needed the first element
		json_data=json.loads(info[21:-1]) #for making perfect JSON syntax, removing {,},[,]



		final_data=json_data['entry_data']['PostPage'] #we needed display_src from nested JSON fields
		final=final_data[0]
		image=final['media']['display_src']
		while image!='':
			return "<img src="+image+" align='center'>" #render link in img tag

	return render_template('index.html')

if __name__=='__main__':
	app.run()
