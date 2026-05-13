from fastapi import FastAPI

app = FastAPI(title="My FastAPI App")


@app.get("/")
def root():
    return {"message": "Hello GitHub Actions! v1"}


@app.get("/health")
def health():
    return {"status": "ok"}
