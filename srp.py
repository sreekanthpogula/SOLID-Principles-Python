"""
Single Responsibility Principle
A class should have only one job.
If a class has more than one responsibility, it becomes coupled.
A change to one responsibility results to the modification of the other responsibility.
"""


class Organization:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def save(self, organization: Organization):
        pass


"""
The Organization class violates the Single Responsibility Principle.
How does it violates SRP?
SRP states that classes should have one responsibility, here, we can draw out two responsibilities: organization 
database management and organization properties management. 
The constructor and get_name manage the Organization properties while the save manages the Organization storage on a 
database.
How will this design cause issues in the future?
If the application changes in a way that it affects database management functions. The classes that make use of 
Organization properties will have to be touched and recompiled to compensate for the new changes.
You see this system smells of rigidity, it’s like a domino effect, touch one card it affects all other cards in line.
To make this conform to SRP, we create another class that will handle the sole responsibility of storing an organization
to a database.
"""


class Organization:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass


class OrganizationDB:
    def get_organization(self) -> Organization:
        pass

    def save(self, organization: Organization):
        pass


"""
"When designing our classes, we should aim to put related features together, 
so whenever they tend to change they change for the same reason. 
And we should try to separate features if they will change for different reasons. 
- Steve Fenton"
"""



