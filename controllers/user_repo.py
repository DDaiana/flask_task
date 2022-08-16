from werkzeug.exceptions import BadRequest

savedRepo = [
    {}
]


def index(request):
    return [c for c in savedRepo], 200


def create(request):
    new_cat = request.get_json()
    new_cat['id'] = sorted([c['id'] for c in savedRepo][-1] + 1)
    savedRepo.append(new_cat)
    return new_cat, 201


def show(request, uid):
    return find_by_uid(uid), 200


def destroy(request, uid):
    cat = find_by_uid(uid)
    savedRepo.remove(cat)
    return cat, 204


def update(request, uid):
    sRepo = find_by_uid(uid)
    data = request.get_json()
    print(data)
    for key, val in data.items():
        sRepo[key] = val
    return sRepo, 200


def find_by_uid(uid):
    try:
        return next(c for c in savedRepo if c['id'] == uid)
    except:
        raise BadRequest(f'We dont have a cat with {uid}')
