from app import app


@app.route('/api/health', methods=['GET', 'POST'])
def Health():
    response = app.response_class(
        status=200,
    )
    return response


@app.route('/')
def index():
    return 'Привет'


@app.route('/main/')
def hello():
    return 'Hello!'


@app.route('/user/<int:id>/')
def user_profile(id):
    return f"Profile page of user #{id}"
