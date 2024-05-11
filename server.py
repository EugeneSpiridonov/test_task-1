from aiohttp import web
import hashlib


async def healthcheck(request):
    return web.json_response({})


async def hash_string(request):
    try:
        data = await request.json()
        string_to_hash = data.get("string")
        if string_to_hash is None:
            return web.json_response(
                {"validation_errors": 'Требуется поле "string"'}, status=400
            )

        hashed_string = hashlib.sha256(string_to_hash.encode()).hexdigest()
        return web.json_response({"hash_string": hashed_string})

    except Exception as e:
        return web.json_response({"error": str(e)}, status=500)


def create_app():
    app = web.Application()
    app.router.add_get("/healthcheck", healthcheck)
    app.router.add_post("/hash", hash_string)
    return app


def run_app(host="127.0.0.1", port=8080):
    app = create_app()
    web.run_app(app, host=host, port=port)
