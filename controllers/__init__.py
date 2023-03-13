from controllers.corkboard_controller import corkboards
from controllers.rescues_controller import rescues
from controllers.auth_controller import auth
from controllers.animal_controller import animals
from controllers.user_controller import users

registerable_controllers = [
    auth,
    corkboards,
    rescues,
    animals,
    users
]