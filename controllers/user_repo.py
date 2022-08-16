from werkzeug.exceptions import BadRequest

savedRepo = [
    {}
]


def index(request):
    return [r for r in savedRepo], 200


def create(request):
    new_repo = request.get_json()
    new_repo['id'] = sorted([s['id'] for s in savedRepo][-1] + 1)
    savedRepo.append(new_repo)
    return new_repo, 201


def show(request, uid):
    return find_by_uid(uid), 200


def destroy(request, uid):
    repo = find_by_uid(uid)
    savedRepo.remove(repo)
    return repo, 204


def update(request, uid):
    sRepo = find_by_uid(uid)
    data = request.get_json()
    print(data)
    for key, val in data.items():
        sRepo[key] = val
    return sRepo, 200


def find_by_uid(uid):
    try:
        return next(r for r in savedRepo if r['id'] == uid)
    except:
        raise BadRequest(f'We dont have a cat with {uid}')
