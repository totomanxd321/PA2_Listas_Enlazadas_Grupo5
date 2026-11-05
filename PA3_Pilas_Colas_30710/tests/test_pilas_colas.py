"""22 pruebas automatizadas para pilas, colas y el caso aplicado."""
import unittest
from app.estructuras import Cola, Pila
from app.servicio_academico import ServicioAcademico

class PruebasPila(unittest.TestCase):
    def test_inicialmente_vacia(self):
        p = Pila()
        self.assertTrue(p.esta_vacia())
        self.assertEqual(len(p), 0)

    def test_orden_lifo(self):
        p = Pila()
        for x in ("A1", "A2", "A3"): p.apilar(x)
        self.assertEqual([p.desapilar() for _ in range(3)], ["A3", "A2", "A1"])

    def test_ver_tope_no_extrae(self):
        p = Pila(); p.apilar("A1")
        self.assertEqual(p.ver_tope(), "A1")
        self.assertEqual(len(p), 1)

    def test_extraer_pila_vacia(self):
        with self.assertRaises(IndexError): Pila().desapilar()

    def test_consultar_tope_vacio(self):
        with self.assertRaises(IndexError): Pila().ver_tope()

    def test_iterar_desde_tope(self):
        p = Pila(); p.apilar("A1"); p.apilar("A2")
        self.assertEqual(list(p), ["A2", "A1"])

class PruebasCola(unittest.TestCase):
    def test_inicialmente_vacia(self):
        c = Cola()
        self.assertTrue(c.esta_vacia())
        self.assertEqual(len(c), 0)

    def test_orden_fifo(self):
        c = Cola()
        for x in ("S101", "S102", "S103"): c.encolar(x)
        self.assertEqual([c.desencolar() for _ in range(3)], ["S101", "S102", "S103"])

    def test_ver_frente_no_extrae(self):
        c = Cola(); c.encolar("S101")
        self.assertEqual(c.ver_frente(), "S101")
        self.assertEqual(len(c), 1)

    def test_desencolar_cola_vacia(self):
        with self.assertRaises(IndexError): Cola().desencolar()

    def test_frente_cola_vacia(self):
        with self.assertRaises(IndexError): Cola().ver_frente()

    def test_reiniciar_despues_de_vaciar(self):
        c = Cola(); c.encolar(1)
        self.assertEqual(c.desencolar(), 1)
        self.assertTrue(c.esta_vacia())
        c.encolar(2)
        self.assertEqual(c.desencolar(), 2)

    def test_recorrido_de_frente_a_final(self):
        c = Cola()
        for x in (1, 2, 3): c.encolar(x)
        self.assertEqual(list(c), [1, 2, 3])

class PruebasCasoAcademico(unittest.TestCase):
    def test_deshacer_restaura_el_valor_anterior(self):
        s = ServicioAcademico(); anterior = s.ficha["telefono"]
        s.modificar_ficha("telefono", "999888777"); s.deshacer_ultima_modificacion()
        self.assertEqual(s.ficha["telefono"], anterior)

    def test_deshacer_ultimo_cambio_primero(self):
        s = ServicioAcademico()
        s.modificar_ficha("estado", "En revisión")
        s.modificar_ficha("estado", "Aprobado")
        s.deshacer_ultima_modificacion()
        self.assertEqual(s.ficha["estado"], "En revisión")
        s.deshacer_ultima_modificacion()
        self.assertEqual(s.ficha["estado"], "Pendiente")

    def test_no_apilar_cambio_idempotente(self):
        s = ServicioAcademico()
        self.assertFalse(s.modificar_ficha("estado", "Pendiente"))
        self.assertTrue(s.historial.esta_vacia())

    def test_campo_inexistente(self):
        with self.assertRaises(KeyError): ServicioAcademico().modificar_ficha("documento", "ABC")

    def test_atencion_en_orden_de_llegada(self):
        s = ServicioAcademico()
        for cod in ("S101", "S102", "S103"): s.recibir_solicitud(cod, "Trámite")
        self.assertEqual([s.atender_siguiente_solicitud().codigo for _ in range(3)], ["S101", "S102", "S103"])

    def test_no_admitir_codigos_duplicados(self):
        s = ServicioAcademico(); s.recibir_solicitud("S101", "Constancia")
        with self.assertRaises(ValueError): s.recibir_solicitud("S101", "Reclamo")

    def test_no_admitir_solicitud_sin_codigo(self):
        with self.assertRaises(ValueError): ServicioAcademico().recibir_solicitud("  ", "Consulta")

    def test_vacio_no_deshace(self):
        with self.assertRaises(IndexError): ServicioAcademico().deshacer_ultima_modificacion()

    def test_vacio_no_atiende(self):
        with self.assertRaises(IndexError): ServicioAcademico().atender_siguiente_solicitud()

if __name__ == "__main__": unittest.main()
