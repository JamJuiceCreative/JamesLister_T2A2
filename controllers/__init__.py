from controllers.corkboard_controller import corkboard
from controllers.rescues_controller import rescues
from controllers.auth_controller import auth

registerable_controllers = [
    auth,
    corkboard,
    rescues
]