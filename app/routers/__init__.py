from fastapi.routing import APIRoute


def override_route(base: list[APIRoute], override_routes: list[APIRoute]):
    override = set([(tuple(o.methods) + (o.path,)) for o in override_routes])
    return [b for b in base if tuple(b.methods) + (b.path,) not in override]
