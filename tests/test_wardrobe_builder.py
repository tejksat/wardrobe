import unittest

import numpy as np

from builder.wardrobe_builder import WardrobeBuilder


class TestWardrobeBuilder(unittest.TestCase):
    def assertArrayEqual(self, first, second):
        self.assertTrue(np.array_equal(first, second))

    def test_to_absolute_vector(self):
        builder = WardrobeBuilder()
        self.assertArrayEqual(np.array([0, 0, 0]), builder._to_absolute_vector(np.array([0, 0, 0])))
        self.assertArrayEqual(np.array([1, 2, 3]), builder._to_absolute_vector(np.array([1, 2, 3])))

        builder.set_origin(1, 2, 3, 1, 1, 1)
        self.assertArrayEqual(np.array([1, 2, 3]), builder._to_absolute_vector(np.array([0, 0, 0])))
        self.assertArrayEqual(np.array([2, 4, 6]), builder._to_absolute_vector(np.array([1, 2, 3])))

        builder.set_origin(3, 0, 0, -1, 1, 1)
        builder.use_iXYZ()
        self.assertArrayEqual(np.array([3, 0, 0]), builder._to_absolute_vector(np.array([0, 0, 0])))
        self.assertArrayEqual(np.array([2, 2, 3]), builder._to_absolute_vector(np.array([1, 2, 3])))

        builder.set_origin(0, 0, 3, -1, 1, 1)
        builder.use_ZYiX()
        self.assertArrayEqual(np.array([0, 0, 3]), builder._to_absolute_vector(np.array([0, 0, 0])))
        self.assertArrayEqual(np.array([3, 2, 2]), builder._to_absolute_vector(np.array([1, 2, 3])))
