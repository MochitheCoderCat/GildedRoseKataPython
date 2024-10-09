# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class QualityUpdater:
    """Base class for item quality update strategies."""
    def update(self, item):
        raise NotImplementedError("Subclasses must override the update method")


class RegularItemUpdater(QualityUpdater):
    def update(self, item):
        item.sell_in -= 1
        if item.quality > 0:
            item.quality -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1


class AgedBrieUpdater(QualityUpdater):
    def update(self, item):
        item.sell_in -= 1
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 0 and item.quality < 50:
                item.quality += 1


class BackstagePassUpdater(QualityUpdater):
    def update(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
        else:
            item.quality += 1
            if item.sell_in < 10:
                item.quality += 1
            if item.sell_in < 5:
                item.quality += 1


class SulfurasUpdater(QualityUpdater):
    def update(self, item):
        # Legendary item, quality and sell_in do not change
        pass


class ConjuredItemUpdater(QualityUpdater):
    def update(self, item):
        item.sell_in -= 1
        if item.quality > 0:
            item.quality -= 2
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 2


class GildedRose:
    def __init__(self, items: list[Item]):
        self.items = items
        self.updater_map = {
            "Aged Brie": AgedBrieUpdater(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassUpdater(),
            "Sulfuras, Hand of Ragnaros": SulfurasUpdater(),
            "Conjured Mana Cake": ConjuredItemUpdater()
        }
        self.default_updater = RegularItemUpdater()

    def update_quality(self):
        for item in self.items:
            updater = self.updater_map.get(item.name, self.default_updater)
            updater.update(item)
            item.quality = max(0, item.quality)
            item.quality = min(50, item.quality)
