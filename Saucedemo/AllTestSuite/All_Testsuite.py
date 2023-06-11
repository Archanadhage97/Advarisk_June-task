import unittest
import pytest
from SwagLbsTestPage.Login import Login
from SwagLbsTestPage.Cart_Funct import CartPage
from SwagLbsTestPage.Checkout import Checkout

ts1 = unittest.TestLoader().loadTestsFromTestCase(Login)
ts2 = unittest.TestLoader().loadTestsFromTestCase(CartPage)
ts3 = unittest.TestLoader().loadTestsFromTestCase(Checkout)

sanitestsuite = unittest.TestSuite(ts1)
functiontestsuite = unittest.TestSuite([ts2,ts3])
Mastersuite = unittest.TestSuite([ts1,ts2,ts3])

unittest.TextTestRunner(verbosity=2).run(Mastersuite)

if __name__ == "__main__":
    unittest.main()