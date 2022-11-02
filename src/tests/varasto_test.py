import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto() #Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)   

    def test_varastosta_otetaan_liikaa(self):
        varaston_saldo = self.varasto.saldo
        self.varasto.ota_varastosta(varaston_saldo+1)

    def test_varastoon_laitetaan_liikaa(self):
        varastossa_tilaa = self.varasto.paljonko_mahtuu()
        self.varasto.lisaa_varastoon(varastossa_tilaa+1)

    def test_varastosta_otetaan_neg_maara(self):
        saatu_maara = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(saatu_maara, 0)

    def test_varastoon_lisataan_neg_maara(self):
        varasto_saldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, varasto_saldo)
        
    def test_luodaan_varasto_tilavuus_neg(self):
        self.varasto = Varasto(-1)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_luodaan_varasto_saldo_neg(self):
        self.varasto = Varasto(10, -1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test__str__(self):
        saldo = self.varasto.saldo
        tilaa = self.varasto.paljonko_mahtuu()
        self.assertEqual(str(self.varasto), f"saldo = {saldo}, vielä tilaa {tilaa}")
         