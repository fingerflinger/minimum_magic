import unittest
import deploy
from testfixtures import tempdir
import os

class TestDownloadCard(unittest.TestCase):

    def test_find_card(self):
        result = deploy.find_card("Black Lotus", set_code="vma") 
        self.assertEqual(result.data(0, "name"), "Black Lotus")
        #result = deploy.find_card("mountain", artist=) 

    
    @tempdir()
    def test_download_card(self, dir):
        card_id = "bd8fa327-dd41-4737-8f19-2cf5eb1f7cdd"
        verification_hash = ""
        deploy.download_card(card_id, dir.path, verification_hash)
        # TODO check for file exists 
        self.assertTrue(True)
    
    
    @tempdir()
    def test_hash_card(self, dir):
        card_id = "bd8fa327-dd41-4737-8f19-2cf5eb1f7cdd"
        verification_hash = ""
        deploy.download_card(card_id, dir.path, verification_hash)
        file_hash = deploy.hash_file(os.path.join(dir.path, "Black Lotus_small.jpg"))
        self.assertEqual('c926302157cd9de7f6fcc6f5b75036d3', file_hash)

if __name__ == "__main__":
    unittest.main()
