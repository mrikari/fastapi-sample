from fastapi.routing import APIRoute


def override_route(base: list[APIRoute], override_routes: list[APIRoute]):
    result = []
    override = set([(tuple(o.methods) + (o.path,)) for o in override_routes])
    for b in base:
        if tuple(b.methods) + (b.path,) in override:
            pass
        else:
            result.append(b)
    return result
