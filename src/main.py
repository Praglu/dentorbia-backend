from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def index():
    return {
        'Hello world': 'Guten Tag der Welt'
    }
