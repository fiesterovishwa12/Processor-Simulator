#!/usr/bin/python

import stage_buffer
import unittest
import Instruction

class StageBufferTest(unittest.TestCase):
    def setUp(self):
        self.foo = 4
        self.bar = [3, 7]
        self.input_dict = {
            'foo': self.foo,
            'bar': self.bar,
            }
        self.stage_buffer = stage_buffer.StageBuffer(self.input_dict)

    def tearDown(self):
        pass
    
    def test_init(self): 
        self.assertEqual(self.stage_buffer.foo, self.foo)
        self.assertEqual(self.stage_buffer.bar, self.bar)

    def test_getitem(self): 
        for attr in self.stage_buffer.__dict__.keys():
            self.assertEqual(self.stage_buffer[attr], 
                             self.__getattribute__(attr))

    def test_setitem(self): 
        f = stage_buffer.StageBuffer()
        for attr in self.stage_buffer.__dict__.keys():
            f[attr] = self.stage_buffer[attr]
            self.assertEqual(f[attr],
                             self.stage_buffer[attr])

    def test_eq(self): 
        f = stage_buffer.StageBuffer()
        f2 = stage_buffer.StageBuffer()
        self.assertEqual(f, f2)
        
        f3 = stage_buffer.StageBuffer(self.input_dict)
        self.assertEqual(f3, self.stage_buffer)
	
def get_suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(StageBufferTest)
    return suite

if __name__ == '__main__':
    suite = get_suite()
    unittest.TextTestRunner(verbosity=2).run(suite)