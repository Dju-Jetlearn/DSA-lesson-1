class Katana:
    def __init__(self,primary,secondary,tertiary,blade,spine,habaki,tsuba,hilt,hilt_tips,accesory,binding,aesthetic,strength):
        
        self.primary = primary
        self.secondary = secondary
        self.tertiary = tertiary
        self.blade = blade
        self.spine = spine
        self.habaki = habaki
        self.tsuba = tsuba
        self.hilt = hilt
        self.hilt_tips = hilt_tips
        self.accesory = accesory
        self.binding = binding
        self.aesthetic = aesthetic
        self.strength = strength
        self.total_aesthetic = 0
        self.total_strength = 0
        self.total_binding = 0

    def calculate_aesthetic(self):
            sum_value = 0
            for i in self.aesthetic:
                sum_value += i
            return sum_value
        
    def calculate_strength(self):
            sum_value = 0
            for i in self.strength:
                sum_value += i
            return sum_value
        
    def calculate_binding(self):
            sum_value = 0
            for i in self.binding:
                sum_value += i
            print(sum_value)
            return sum_value

    def calculate_total_aesthetic(self):
        self.total_aesthetic = self.calculate_aesthetic()
        self.average = self.total_aesthetic / len(self.aesthetic)

    def calculate_total_strength(self):
        self.total_strength = self.calculate_strength()
        self.average = self.total_strength / len(self.strength)

    def calculate_total_binding(self):
        self.total_binding = self.calculate_binding()

        self.average = self.total_binding / len(self.binding)
        print(self.total_binding)



    def display_details(self):
        self.calculate_aesthetic()
        self.calculate_strength()
        self.calculate_binding()
        print("The primary color of the katana is",{self.primary})
        print("The secondary color of the katana is",{self.secondary})
        print("The tertiary color of the katana is",{self.tertiary})
        print("The blade of the katana is",{self.blade})
        print("The spine of the katana is",{self.spine})
        print("The habaki of the katana is",{self.habaki})
        print("The tsuba of the katana is",{self.tsuba})
        print("The hilt of the katana is",{self.hilt})
        print("The hilt tips of the katana are",{self.hilt_tips})
        print("The accesory of the katana is",{self.accesory})
        print("The total binding of the katana is",{self.total_binding})
        print("The total aesthetic of the katana is",{self.total_aesthetic})
        print("The total strength of the katana is",{self.total_strength})

katana_1=Katana("black","green","white","sharp and glow","standard", "standard", "Shadow 2","gripped","standard","heart",[10,5,7,9],[8,9],[8,5,4,10,10,])
katana_1.display_details()