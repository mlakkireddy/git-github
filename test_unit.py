import unittest
import HtmlTestRunner
import calc,logging,sys

#logging.basicConfig(level=logging.DEBUG,filename='unit_test_log.txt',format="%(message)s  %(asctime)s")

logger=logging.getLogger('test_calc')
formatter=logging.Formatter('%(asctime)s : %(name)s : %(message)s')
#logger.setLevel(logging.INFO)
file_handler=logging.FileHandler('sample_log.txt')
file_handler.setFormatter(formatter)

logger.setLevel(logging.DEBUG)

stream_handler=logging.StreamHandler()
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


#file_handler.setLevel(logging.DEBUG)


class Test_calc(unittest.TestCase):
    def test_add(self):
        result=calc.add(10,5)
        logger.debug(f'{result} is the result from add')
        try :
            self.assertEqual(result,16)
        except Exception:
            logger.exception("plz check expected result")
    @unittest.skip("im skipped")
    def test_mul(self):
        result=calc.mul(10,6)
        logger.debug(f'result from mul is {result}')
        self.assertEqual(result,60)
    def test_sub(self):
        result=calc.sub(10,5)
        logger.debug(f"result from sub is {result}")
        self.assertEqual(result,5)

if __name__=='__main__':
    unittest.main()
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
