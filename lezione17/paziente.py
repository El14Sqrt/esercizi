from ...esercizi.lezione17.persona import Persona

class Paziente(Persona):
    def __init__(self, __first_name: str, __last_name: str, __id: str):
        super().__init__(__first_name, __last_name)

        self.__id = __id

    
    def setIdCode(self, idCode: str):
        self.__id = idCode

    def getidCode(self):
        return self.__id
    
    def patientInfo(self):
        print(f"Paziente: {self.__first_name} {self.__last_name} \nID: {self.__id}")