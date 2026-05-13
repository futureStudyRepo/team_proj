from fastapi import FastAPI
import uvicorn

app = FastAPI(title="My FastAPI App")


@app.get("/")
def root():
    return {"message": "Hello GitHub Actions! v1"}


@app.get("/health")
def health():
    return {"status": "ok2"}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)