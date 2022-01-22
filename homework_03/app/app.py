from fastapi import FastAPI

app = FastAPI()

@app.get("/ping", status_code=200)
def ping():
	return {"message":"pong"}

@app.get("/help", status_code=200)
def ping():
	help = {
		"Build image": "docker build . -t ping",
		"Start container": "docker run -p 8000:8000 ping",
		"Check api": "curl -X GET http://127.0.0.1:8000/ping"
	}
	return help
