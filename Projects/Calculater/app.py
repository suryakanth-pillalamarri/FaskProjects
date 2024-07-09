from flask import Flask
import json
from flask import request
from flask import jsonify



# __name__ is used for determining root path of the application
app=Flask(__name__)


@app.route("/calculate",methods=["POST"])
def calculate():
    data=request.get_json()
    number1=data.get("number1")
    number2=data.get("number2")
    
    if number1 is None or number2 is None:
        return jsonify({"error":"number1 or number2 is missing"}),400
    else:
        result={
            "Addition": number1+number2,
            "Substraction": number1-number2,
            "Multiplication": number1*number2,
            "Division": number1/number2 if number2!=0 else "division by zero error",
            "Remainder": number1%number2 if number2!=0 else "division by zero error"
        }
        return jsonify(result),200
    
    


if __name__=="__main__":
    app.run(debug=True)
        