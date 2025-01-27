import unittest
import datetime
from src.persona import Persona
from sqlalchemy import text

class PersonaTestCase(unittest.TestCase):

   def setUp(self):
      self.persona1 = Persona(nombre='Alejandro', edad=45)
      self.persona2 = Persona(nombre='Diego', edad=22)
      self.persona3 = Persona(nombre='Alejandra', edad=25)
      self.persona4 = Persona(nombre='Diana', edad=25)
      self.persona5 = Persona(nombre='Juan', edad=55)

      self.grupo = [self.persona1, self.persona2, self.persona3]

   def test_constructor(self):
      self.assertEqual(self.persona1.dar_nombre(), 'Alejandro')
      self.assertEqual(self.persona1.dar_edad(), 45)

   def test_anio_nacimiento(self):
      self.assertEqual(self.persona1.calcular_anio_nacimiento(True), datetime.datetime.now().year - 45)
      self.assertNotEqual(self.persona1.calcular_anio_nacimiento(False), datetime.datetime.now().year - 45)
      self.assertEqual(self.persona1.calcular_anio_nacimiento(False), datetime.datetime.now().year - 45 + 1)
      self.assertNotEqual(self.persona1.calcular_anio_nacimiento(True), datetime.datetime.now().year - 45 + 1)

   def test_asingacion(self):
      self.persona2.asignar_edad(28)
      self.persona2.asignar_nombre("Felipe")
      self.assertFalse(self.persona2.dar_nombre()=='Diego')
      self.assertFalse(self.persona2.dar_edad()==22)
      self.assertTrue(self.persona2.dar_nombre()=='Felipe')
      self.assertTrue(self.persona2.dar_edad()==28)

   def test_objetos_iguales(self):
      persona_nueva = self.persona1
      self.assertIsNot(self.persona1, self.persona3)
      self.assertIs(self.persona1, persona_nueva)

   def test_elemento_en_conjunto(self):
      self.assertIn(self.persona3, self.grupo)
      self.assertNotIn(self.persona4, self.grupo)

   def test_instancia_clase(self):
      self.assertIsInstance(self.persona1, Persona)
      self.assertNotIsInstance(self.grupo, Persona)

   def test_persona2(self):
      self.assertIsInstance(self.persona2, Persona)
      self.assertIsInstance(self.persona3, Persona)
      self.assertIsInstance(self.persona4, Persona)
      self.assertIsInstance(self.persona5, Persona)
      self.assertIsInstance(self.persona1, Persona)
      self.assertIsInstance(self.persona4, Persona)
      self.assertNotIsInstance(self.grupo, Persona)
      self.assertNotIsInstance(self.grupo, Persona)

   def test_persona3(self):
      self.assertIsInstance(self.persona2, Persona)
      self.assertIsInstance(self.persona3, Persona)
      self.assertIsInstance(self.persona4, Persona)
      self.assertIsInstance(self.persona5, Persona)
