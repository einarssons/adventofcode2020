import unittest

from dec21 import m21

example = '''\
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)'''


class Test21(unittest.TestCase):

    def test_find_good_food(self):
        foods = m21.parse_foods(example)
        self.assertEquals(m21.reduce_foods(foods), 5)
