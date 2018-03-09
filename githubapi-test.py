import unittest
from githubapi import commitsGET, repositoryGET

class TestGithub(unittest.TestCase):
    
    def testcommitsGET(self):
        self.assertEqual(commitsGET('hselim567', 'triangle567'), 9)
    
    def testrepositoryGET(self):
        repositoryList = repositoryGET('hselim567')
        self.assertIn('Triangle567', repositoryList)
    
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()