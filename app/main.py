from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title='FastAPI sample project.',
    version='0.0.1',
)


@app.get('/')
def root():
    return JSONResponse(content={'message': 'Hello World.'})
