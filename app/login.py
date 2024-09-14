from flask_login import LoginManager


login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    from app.database import User
    return User.query.get(user_id)
