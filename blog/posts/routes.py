from flask import Blueprint, render_template
from flask import current_app as app

# Blueprint Configuration
posts_bp = Blueprint(
    'posts_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@posts_bp.route('/posts', methods=['GET'])
def posts():
    """Homepage."""
    return render_template('posts.html')