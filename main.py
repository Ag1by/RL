from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

import uvicorn

async def homepage(request):
    return JSONResponse({"hello":"world"})
async def about(request):
    return JSONResponse({"message":"umamusumei"})
async def contect(request):
    return JSONResponse({"my number":"110"})
app = Starlette(
    debug = True,
    routes = [
        Route('/',homepage),
        Route('/message',about),
        Route('contect',contect)
    ]
)
uvicorn.run(app,port=8080)