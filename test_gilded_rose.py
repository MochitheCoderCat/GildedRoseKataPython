# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)
    
    def test_conjured_items_degrade_normally(self):
        # Conjured items should degrade faster, but the original code doesn't handle them correctly
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality, "Conjured items degrade at the same rate as normal items")
    

    def test_quality_never_negative_after_sell_by_date(self):
        items = [Item("+5 Dexterity Vest", -1, -1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        print(gilded_rose.items[0])
        self.assertGreaterEqual(gilded_rose.items[0].quality, 0)


if __name__ == '__main__':
    unittest.main()
