class car2022:
    def roof(self):
        print("sun roof")
    def wheels(self):
        print("normal alloy wheels")
    def music(self):
        print('7" music touch player')
class car2023(car2022):
    def roof(self):
        print("panaromic sun roof")
        super().roof() # supper is another function that's used to retrieve data from previous class in this case
        # car 2022 is previous class. we can use this if we want the value for this particular def from previous class.
    def music(self):
        print('11" music touch player')
    def mobileconnect(self):
        print("hyundai blue mobile connect which can manage the car from phone")
obj1 = car2023()
obj1.roof()
obj1.music()
obj1.mobileconnect()
