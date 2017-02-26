from rolepermissions.roles import AbstractUserRole

class Visitor(AbstractUserRole):
    available_permissions = {
        'visit_website': True
    }


class Buyer(AbstractUserRole):
    available_permissions = {
        'place_bid': True,
        'modify_bid': True
    }

class Seller(AbstractUserRole):
    available_permissions = {
        'place_offer': True,
        'modify_offer': True,
    }

class BackendUser(AbstractUserRole):
    available_permissions = {
        'modify_request': False,
        'modify_offer': False,
    }
