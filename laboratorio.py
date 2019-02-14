class Medicamento():
    def __init__(self, nombre, sustancia, porcentaje):
        self.nombre = nombre
        self.sustancia= sustancia
        self.porcentaje = porcentaje
    def get_med(self):
        return self.nombre, self.sustancia,self.porcentaje

paracetamol = Medicamento("parecetamol", "Ácido 1", 0.35)
ibuprofeno = Medicamento("ibuprofeno", "Ácido 2" , 0.40)
aspirina = Medicamento("aspirina", "Ácido 3", 0.30)

medic = []
medic.append(paracetamol)
medic.append(ibuprofeno)
medic.append(aspirina)


class Laboratorio():
    def __init__(self, laboratorio, med1, med2, med3):
        self.laboratorio = laboratorio
        self.med1 = med1
        self.med2 = med2
        self.med3 = med3
    def get_lab(self):
        return self.laboratorio, self.med1,self.med2, self.med3
Roche = Laboratorio("Roche",medic[0], medic[1], medic[2])
print("En el laboratorio tenemos los siguientes medicamentos:", Roche.med1.nombre, Roche.med2.nombre, Roche.med3.nombre)
print( Roche.med1.nombre, "tiene", Roche.med1.sustancia, "en un", Roche.med1.porcentaje)
print( Roche.med2.nombre, "tiene", Roche.med2.sustancia, "en un", Roche.med2.porcentaje)
print( Roche.med3.nombre, "tiene", Roche.med3.sustancia, "en un", Roche.med3.porcentaje)
