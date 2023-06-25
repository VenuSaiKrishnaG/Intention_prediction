import numpy as np
import pandas as pd
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
palette_color = sns.color_palette('bright')
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
from methods import *
# from werkzeug import secure_filename
model=pickle.load(open('model2.pkl','rb'))
cv=pickle.load(open('vectorizer.pkl','rb'))
from flask import Flask,request,jsonify,render_template
app=Flask(__name__)
@app.route('/')
def home():
	return render_template('index.html')
@app.route('/train')
def train():
	return render_template('train.html')
@app.route('/test')
def test():
	return render_template('test.html')
@app.route('/about')
def about():
	return render_template('about.html')
@app.route('/analysis')
def analysis():
	return render_template('analysis.html')
@app.route('/predict',methods=['POST'])
def pre():
	if (request.method=="POST"):
		file=request.files['file']
		file.save(file.filename)
		df=pd.read_csv(file.filename)
		l=[]
		l1=list(df['text'])
		if np.nan in l1:
			l1.remove(np.nan)
		l2=list(df['TweetDate'])
		def convert_and_merge():
			new_l1=l1[:]
			l2=convert_date(l2)
			l2=MinMaxScaler1(l2)
			for i in range(len(new_l1)):
				new_l1[i]=compute_hash(new_l1[i])
			new_l1=MinMaxScaler2(new_l1)
			l1=[]
			for i in range(len(new_l1)):
				l1[i]=(l2[i],new_l1[i])
		zc=0
		oc=0
		for i in range(len(l1)):
			x=[l1[i]]
			# print(x)
			m=cv.transform(x).toarray()
			#print(x,)
			x=model.predict(m)
			print(x)
			#print(i,predict_values[i])
			if (x==[0]):
				zc+=1
			else:
				oc+=1
		plt.pie([zc,oc],labels=['Negative','Positive'],autopct="%0.1f%%")
		plt.savefig("./static/fig.png")
	return render_template('predict.html',zc=zc,oc=oc,x=x)
if __name__=='__main__':
	app.run(debug=True)

#predicting the intention of the consumer product purchase using twitter data