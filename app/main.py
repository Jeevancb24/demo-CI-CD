from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello CI/CD just deployed my 1st FastAPI app with GitHub Actions and Docker!"}