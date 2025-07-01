from sqladmin import Admin, ModelView
from models import User, Post

class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username, User.email, User.is_active, User.created_at]
    column_searchable_list = [User.username, User.email]
    column_sortable_list = [User.id, User.username, User.email, User.is_active, User.created_at]
    column_details_exclude_list = [User.hashed_password]
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True

class PostAdmin(ModelView, model=Post):
    column_list = [Post.id, Post.title, Post.author, Post.created_at]
    column_searchable_list = [Post.title]
    column_sortable_list = [Post.id, Post.title, Post.created_at]
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True 