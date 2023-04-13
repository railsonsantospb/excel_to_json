import pandas as pd
import json
from flask import Flask, render_template, request, abort
from flask import Flask,jsonify,request
from werkzeug.utils import secure_filename
  
app =   Flask(__name__)
 
@app.route('/')
def index():
	try:
		return render_template('upload.html')
	except IndexError:
		abort(404)
  
        
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
	try:
		if request.method == 'POST':
			try:
				#recebe o arquivo atravez de uma requisição POST
				f = request.files['file']
				f.save(secure_filename(f.filename))
				
				#obter os dados do arquivo excel
				dados_excel = pd.read_excel(f)
				
				#converter os dados para JSON e facilitar na comunicação com qualquer API
				dados_para_json = dados_excel.to_dict(orient="records")
			except:
				abort(403)
			return jsonify(dados_para_json)
	except IndexError:
		abort(403)
  
if __name__=='__main__':
    app.run(debug=True)


