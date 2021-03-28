from appl.app import app, db
from appl.models import User

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}
app.run(debug=True, use_reloader=False)