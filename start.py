import uvicorn

if __name__ == "__main__":
    uvicorn.run("src.main.server.server:app", port=8000, reload=True)
