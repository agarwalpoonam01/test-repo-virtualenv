from flask import Flask, jsonify, json, request
import time

app=Flask(__name__)

@app.route('/server-speed',methods=['POST'])
def hello_world():
	t = 20
	test = int(request.args.get('test'))
	if test < t:
		time.sleep(1)
		return json.dumps({'success':False}), 408, {'ContentType':'application/json'}
	else:
		return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
	#test = time.sleep(0.5)
	#print(test)	
		
	#try:
	#time.sleep(3)
	
		#return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
	#except:
	return json.dumps({'success':False}), 408, {'ContentType':'application/json'}



if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000,debug=True)

