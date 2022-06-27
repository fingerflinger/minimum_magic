import unittest
import deploy

class TestDownloadCard(unittest.TestCase):

    def test_find_card(self):
        result = deploy.find_card("Black Lotus", set_code="vma") 
        self.assertEqual(result.data(0, "name"), "Black Lotus")
        #result = deploy.find_card("mountain", artist=) 

    '''def test_download_card(self):
        card_id = ""
        test_dir = ""
        verification_hash = ""
        file_path = ""
        deploy.download_card(card_id, test_dir, verification_hash)
        self.assertTrue(deploy.check_file(file_path))
        pass

    def test_hash_card(self):
        pass
    '''

if __name__ == "__main__":
    unittest.main()
