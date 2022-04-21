from flask import Flask, request, render_template
from keras.models import load_model
import pickle
import numpy as np
app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def hello_world1():
  if request.method == "POST":
      myDict = request.form
      Dist_id = int(myDict['Dist_id'])
      Mandal_Code = int(myDict['Mandal_Code'])
      Humidity_min = int(myDict['Humidity_min'])
      CropSeason_id = int(myDict['CropSeason_id'])
      Temp_min = int(myDict['Temp_min'])
      Date_month = int(myDict['Date_month'])
      Rainfall = int(myDict['Rainfall'])
      #X=np.array([[Dist_id,MandalCode,Humidity_min,CropSeason_id,Temp_min,Temp_max,Date_month,Rainfall]])
      hum_model = load_model("pickle file\\humi2.h5")
      Total=hum_model.predict(np.array([[Dist_id,Mandal_Code,Humidity_min,CropSeason_id,Temp_min,Date_month,Rainfall]]))

      return render_template("show.html",inf=Total)
  return render_template('humi.html')

@app.route('/humi',methods=["GET","POST"])
def humi():
  if request.method == "POST":
      myDict = request.form
      Dist_id = int(myDict['Dist_id'])
      Mandal_Code = int(myDict['Mandal_Code'])
      Humidity_min = int(myDict['Humidity_min'])
      CropSeason_id = int(myDict['CropSeason_id'])
      Temp_min = int(myDict['Temp_min'])
      Date_month = int(myDict['Date_month'])
      Rainfall = int(myDict['Rainfall'])
      #X=np.array([[Dist_id,MandalCode,Humidity_min,CropSeason_id,Temp_min,Temp_max,Date_month,Rainfall]])
      hum_model = load_model("pickle file\\humi2.h5")
      Total=hum_model.predict(np.array([[Dist_id,Mandal_Code,Humidity_min,CropSeason_id,Temp_min,Date_month,Rainfall]]))

      return render_template("show.html",inf=Total)
  return render_template('humi.html')

if __name__ == "__main__":
     app.run(debug=True)