from opganization import Organization
class Factory(Organization):
    def __init__(self, __id, name, kind_of_aktivity, director, accountant, count_worker) -> None:
        super().__init__(__id, name, kind_of_aktivity, director, accountant, count_worker)
        