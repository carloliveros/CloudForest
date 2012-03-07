import textwrap
import unittest
from cloudforest import phylip2oneliner

class TestPhylip2OnelinerFunctions(unittest.TestCase):

	def setUp(self):
		self.phylip = """\
		10 430
		mus_mus    ----TCCTAG CTGAACAGAG AAGGGTGATT AACGATAGCA ATTTATTGTA
		oto_gar    GTAATCATAG TTGAACCGAG AAAGGTGATT AACGATAGCA ATTTATTGTA
		cal_jac    GTAATCATAG TTGAACCAAG AAGGGTGATT AACGATAGCA ATTTATTGTA
		gor_gor    ---ATCATAG TTGAACCAAG AAGAGTGATT AACGATAGCA ATTTATTGTA
		hom_sap    GTAATCATAG TTGAACCAAG AAGAGTGATT AACGATAGCA ATTTATTGTA
		pan_tro    GTAATCACAG TTGAACCAAG AAGAGTGATT AACGATAGCA ATTTATTGTA
		pon_abe    GTAATCATAG TTGAACCAAG AAGGGTGATT AACGATAGCA ATTTATTGTA
		nom_leu    GTAATCATAG TTGAACCAAG AAGGGTGATT AACGATAGCA ATTTATTGTA
		pap_ham    GTAATCATGG TTGAACCAAG AAGGGTGATT AACGATAGCA ATTTATTGTA
		rhe_mac    GTAATCATGG TTGAACCAAG AAGGGTGATT AACGATAGCA ATTTATTGTA
		
		AACGATAGCA ATTT------
		AACGATAGCA ATTT------
		AACGATAGCA ATTT------
		AACGATAGCA ATTT------
		AACGATAGCA ATTT------
		AACGATAGCA ATT------N
		AACGATAGCA ATTT------
		AACGATAGCA ATTT------
		AACGATAGCA ATTT------
		AACGATAGCA ATTT------
		"""
		self.name = 'test_phylip'

		self.result = """\
						chrm=test_phylip:\
						gor_gor,---ATCATAGTTGAACCAAGAAGAGTGATTAACGATAGCAATTTATTGTAAACGATAGCAATTT------,\
						oto_gar,GTAATCATAGTTGAACCGAGAAAGGTGATTAACGATAGCAATTTATTGTAAACGATAGCAATTT------,\
						pan_tro,GTAATCACAGTTGAACCAAGAAGAGTGATTAACGATAGCAATTTATTGTAAACGATAGCAATT------N,\
						nom_leu,GTAATCATAGTTGAACCAAGAAGGGTGATTAACGATAGCAATTTATTGTAAACGATAGCAATTT------,\
						hom_sap,GTAATCATAGTTGAACCAAGAAGAGTGATTAACGATAGCAATTTATTGTAAACGATAGCAATTT------,\
						mus_mus,----TCCTAGCTGAACAGAGAAGGGTGATTAACGATAGCAATTTATTGTAAACGATAGCAATTT------,\
						pon_abe,GTAATCATAGTTGAACCAAGAAGGGTGATTAACGATAGCAATTTATTGTAAACGATAGCAATTT------,\
						pap_ham,GTAATCATGGTTGAACCAAGAAGGGTGATTAACGATAGCAATTTATTGTAAACGATAGCAATTT------,\
						rhe_mac,GTAATCATGGTTGAACCAAGAAGGGTGATTAACGATAGCAATTTATTGTAAACGATAGCAATTT------,\
						cal_jac,GTAATCATAGTTGAACCAAGAAGGGTGATTAACGATAGCAATTTATTGTAAACGATAGCAATTT------;\n"""
		self.result =  textwrap.dedent(self.result).replace("\t", "")

	def test_parsePhylip(self):
		lines = textwrap.dedent(self.phylip).split("\n")
		oneliner = phylip2oneliner.parsePhylip(lines, self.name)
		self.assertEqual(oneliner, self.result)


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestPhylip2OnelinerFunctions)
	unittest.TextTestRunner(verbosity=3).run(suite)
