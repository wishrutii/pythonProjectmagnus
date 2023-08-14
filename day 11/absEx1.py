from abc import ABC,abstractmethod
class accounts:
    def savings(self):
        print("no min balance and earn upto 7.5% monthly int")
class loans(ABC):  # we inherited from ABC bc of abst method in library
    @abstractmethod  # this will hide this class and to display it again simply just remove this.
    def pl(self):
        print("personal loan")
    @abstractmethod
    def hl(self):
        print("house loan")
class finalaccount(accounts,loans):
    def pl(self):
        print("personal loan with 11% int")
    def hl(self):
        print("home loan with 8% floating loan")
obj1 = finalaccount()
obj1.pl()
obj2 = loans()
obj2.pl()


