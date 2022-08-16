from flask import Flask, request, jsonify, render_template, redirect, url_for

from flask_cors import CORS
from controllers import user_repo
from server import fetch_repos


app = Flask(__name__)

def page_not_found():
    return render_template('content.html')

@app.route('/', methods=['GET', 'POST'])
def Welcome():
    try:
        if request.method == 'POST':
            input = request.form['repos']
            data = fetch_repos(input)
            return render_template('content.html', data=data)
    except:
        return redirect(404, page_not_found())
    return render_template('forms.html')


@app.route('/cats', methods=['GET', 'POST'])
def repos():
    fns = {
        'GET': user_repo.index,
        'POST': user_repo.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code


@app.route('/repos/<int:repo_id>', methods=['GET', 'DELETE', 'PUT'])
def repo_handler(repo_id):
    fns = {
        'GET': user_repo.show,
        'DELETE': user_repo.destroy,
        'PUT': user_repo.update
    }

    resp, code = fns[request.method](request, repo_id)
    return jsonify(resp), code


if __name__ == '__main__':
    app.run(debug=True)
