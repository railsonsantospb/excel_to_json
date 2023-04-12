import pandas as pd
import json


from flask import Flask,jsonify,request
  
app =   Flask(__name__)
  
@app.route('/excelTojson', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        #obter os dados do arquivo excel presente na mesma pasta desse script
        dados_excel = pd.read_excel("file_example_XLS_1000.xls")

        #converter os dados para JSON e facilitar na comunicação com qualquer API
        dados_para_json = dados_excel.to_dict(orient="records")

        return jsonify(dados_para_json)
  
if __name__=='__main__':
    app.run(debug=True)


