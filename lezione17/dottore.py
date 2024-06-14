from ...esercizi.lezione17.persona import Persona

class Dottore(Persona):
    def __init__(self, __first_name: str, __last_name: str, __specialization: str, __parcel: float):
        super().__init__(__first_name, __last_name)

        if isinstance(__parcel, float) and isinstance(__specialization, str) is True:
            self.__specialization = __specialization
            self.__parcel = __parcel

        elif isinstance(__parcel, float) is False and isinstance(__specialization, str) is True:
            print("La parcella non è un float!")
            self.__specialization = __specialization
            self.__parcel = None

        elif isinstance(__parcel, float) is True and isinstance(__specialization, str) is False:
            print("La specializzazione non è una stringa!")
            self.__specialization = None
            self.__parcel = __parcel


    def setSpecialization(self, specialization: str):
        if isinstance(specialization, str) is True:
            self.__specialization = specialization
        else:
            print("La specializzazione inserita non è una stringa!")

    def setParcel(self, parcel: float):
        if isinstance(parcel, float) is True:
            self.__parcel = parcel
        else:
            print("La parcella inserita non è un float!")
    

    def getSpecialization(self):
        return self.__specialization
    
    def getParcel(self):
        return self.__parcel
    

    def isAValidDoctor(self):
        if self.__age >= 30:
            print(f"Doctor {self.__first_name} e {self.__last_name} is valid!")
        else:
            print(f"Doctor {self.__first_name} e {self.__last_name} is not valid!")


    def doctorGreet(self):
        self.greet()
        print(f"Sono un medico {self.__specialization}")



dottore1: Dottore = Dottore("Mario", "Rossi", "Cardiologia", 3000.0)
dottore1.getName()
dottore1.getLastname()

dottore1.setAge(45)
dottore1.getAge()

dottore1.getSpecialization()
dottore1.getParcel()
dottore1.doctorGreet()