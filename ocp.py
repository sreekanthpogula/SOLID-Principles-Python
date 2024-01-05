"""
Open-Closed Principle
Software entities(Classes, modules, functions) should be open for extension, not modification.
"""


class Organization:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass


organizations = [
    Organization('IBM'),
    Organization('Intel')
]


def organization_client(organizations: list):
    for organization in organizations:
        if organization.name == 'IBM':
            print('World bank')

        elif organization.name == 'Intel':
            print('Core')


organization_client(organizations)

"""
The function organization_client does not conform to the open-closed principle because it cannot be closed against new 
kinds of organizations.
If we add a new organization, Snapchat, We have to modify the organization_client function.
You see, for every new organization, a new logic is added to the organization function. 
This is quite a simple example. When your application grows and becomes complex, 
you will see that the if statement would be repeated over and over again 
in the organization_client function each time a new organization is added, all over the application.
"""

organizations = [
    Organization('IBM'),
    Organization('Intel'),
    Organization('snapchat')
]


def organization_client(organizations: list):
    for organization in organizations:
        if organization.name == 'IBM':
            print('World bank')
        elif organization.name == 'Intel':
            print('Square-tech')
        elif organization.name == 'snapchat':
            print('hire-pro')


organization_client(organizations)

"""
How do we make it (the organization_client) conform to OCP?
"""


class Organization:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def get_client(self):
        pass


class IBM(Organization):
    def get_client(self):
        return 'World bank'


class Intel(Organization):
    def get_client(self):
        return 'square-tech'


class Snapchat(Organization):
    def get_client(self):
        return 'hire-pro'


def organization_client(organizations: list):
    for organization in organizations:
        print(organization.get_client())


organization_client(organizations)

"""
Organization now has a virtual method get_client. We have each organization extend the Organization class and implement 
the virtual get_client method.

Every organization adds its own implementation on how it makes a client in the get_client. 
The organization_client iterates through the array of organization and just calls its get_client method.

Now, if we add a new organization, organization_client doesn’t need to change. 
All we need to do is add the new organization to the organizations array.

organization_client now conforms to the OCP principle.
"""


"""
Another example:

Let’s imagine you have a store, and you give a discount of 20% to your favorite customers using this class:
When you decide to offer double the 20% discount to VIP customers. You may modify the class like this:
"""


class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == 'fav':
            return self.price * 0.2
        if self.customer == 'vip':
            return self.price * 0.4


"""
No, this fails the OCP principle. OCP forbids it. If we want to give a new percent discount maybe, to a diff. 
type of customers, you will see that a new logic will be added.

To make it follow the OCP principle, we will add a new class that will extend the Discount. 
In this new class, we would implement its new behavior:
"""


class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2


"""
If you decide 80% discount to super VIP customers, it should be like this:
You see, extension without modification.
"""


class SuperVIPDiscount(VIPDiscount):
    def get_discount(self):
        return super().get_discount() * 2
