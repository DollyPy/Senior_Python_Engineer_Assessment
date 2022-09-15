import unittest
from main import schema_extract

class TestSchemaExtractor(unittest.TestCase):
    def test_Schema1(self):
        schema1 = schema_extract("./data/data_1.json")
        #Test for number of keys
        self.assertEqual(len(schema1.keys()), 3, "incorrect number of Keys")
        #Test for the data type of each key
        self.assertEqual(schema1["battle"]["type"], "array", "incorrect datatype")
        self.assertEqual(schema1["joiner"]["type"], "array", "incorrect datatype")
        self.assertEqual(schema1["participantIds"]["type"], "enum", "incorrect datatype")

    def test_Schema2(self):
        schema2 = schema_extract("./data/data_2.json")
        #Test for number of keys
        self.assertEqual(len(schema2.keys()), 6, "incorrect number of Keys")
        #Test for the data type of each key
        self.assertEqual(schema2["user"]["type"], "array", "incorrect datatype")
        self.assertEqual(schema2["time"]["type"], "integer", "incorrect datatype")
        self.assertEqual(schema2["acl"]["type"], "enum", "incorrect datatype")
        self.assertEqual(schema2["publicFeed"]["type"], "boolean", "incorrect datatype")
        self.assertEqual(schema2["internationalCountries"]["type"], "enum", "incorrect datatype")
        self.assertEqual(schema2["topTraderFeed"]["type"], "boolean", "incorrect datatype")

unittest.main()

