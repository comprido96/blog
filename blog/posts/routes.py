from flask import Blueprint, render_template
from flask import current_app as app
from ..models import db, Post


# Blueprint Configuration
posts_bp = Blueprint(
    'posts_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@posts_bp.route('/posts', methods=['GET'])
def posts():
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)