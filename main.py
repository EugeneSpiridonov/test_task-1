from aiohttp import web


async def healthcheck(request):
    return web.json_response({})


app = web.Application()
app.router.add_get("/healthcheck", healthcheck)

if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1")
