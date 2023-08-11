

from aiohttp import web

PORT = 3000

routes = web.RouteTableDef()

@routes.get("/")
async def handler(req: web.Request) -> web.Response:
    return web.Response(status= 200, text="Welcome to async python")

@routes.get("/{language}")
async def get_language(req: web.Request) -> web.Request:
    print(req.raw_path)
    lang = req.match_info.get("language", " ")
    other_info = req.query.get("other", "")
    return web.Response(text=f"You chose {lang} \n Other info: {other_info}")

@routes.post("/{lang}")
async def post_lang(req: web.Request) -> web.Response:
    data = await req.post()
    lang = data.get("language")
    # do database stuff
    return web.Response(text=f"{lang} was added to the data base.")

async def init():
    app = web.Application()
    app.add_routes(routes)
    return app


web.run_app(init(), host="localhost", port=PORT)