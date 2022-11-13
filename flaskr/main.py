from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, Flask
)
from werkzeug.exceptions import abort
import os
from auth import login_required
from db import get_db

bp = Blueprint('blog', __name__)

def getcountryname(countrycode):
    countryname = get_db().execute(
        'SELECT c.name, c.code'
        ' FROM countries c'
        ' WHERE code = ?',
        (countrycode,)
    ).fetchone()
    return countryname

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()

    return render_template('blog/index.html', posts=posts)


@bp.route('/viewcountry/<string:country>', methods=('GET', 'POST'))
def viewcountry(country):
    db = get_db()

    genres = db.execute(
        'SELECT g.id, g.name, c.code, g.imglink'
        ' FROM genres g JOIN countries c ON g.country = c.id'
        ' WHERE c.code = ?'
        ' ORDER BY g.name ASC',
        (country,)
    ).fetchall()

    countries  = db.execute(
        'SELECT c.id, c.name, c.code'
        ' FROM countries c'
        ' ORDER BY c.name ASC'
    ).fetchall()


    name = getcountryname(country)

    return render_template('blog/viewcountry.html',countries=countries, genres=genres, countryname=name["name"])

@bp.route('/genre/<string:genre>', methods=('GET', 'POST'))
def viewgenre(genre):
    db = get_db()

    # turn url into genre name
    genre = genre.replace("%20", " ").strip()

    songs = db.execute(
        'SELECT s.id, s.name, s.artist, s.genre, s.spotify_id'
        ' FROM songs s JOIN genres g ON s.genre = g.id'
        ' WHERE g.name = ?'
        ' ORDER BY s.name ASC',
        (genre,)
    ).fetchmany(16)


    genres = db.execute(
        'SELECT g.id, g.name'
        ' FROM genres g'
        ' ORDER BY g.name ASC'
    ).fetchall()

    description = db.execute(
        'SELECT g.description'
        ' FROM genres g'
        ' WHERE g.name = ?',
        (genre,)
    ).fetchone()

    return render_template('blog/viewgenre.html', genres=genres, songs=songs, name=genre, description=description)




@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')

def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))



def create_app(app,test_config=None):
    # create and configure the app
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    import db
    db.init_app(app)

    import auth
    app.register_blueprint(auth.bp)

    import main
    app.register_blueprint(main.bp)
    app.add_url_rule('/', endpoint='index')

    return app

app = Flask(__name__, instance_relative_config=True)
if __name__ == '__main__':
    app = create_app(app).run(debug=False, port=80)