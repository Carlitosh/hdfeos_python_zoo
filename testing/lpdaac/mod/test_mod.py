"""
Tests for LPDAAC MODIS codes.
"""
import inspect
import os
import unittest

import matplotlib.pyplot as plt

import zoo

def fullpath(fname):
    """
    Short cut for creating the full path.
    """
    return os.path.join(os.environ['HDFEOS_ZOO_DIR'], fname)


class TestSwaths(unittest.TestCase):
    """
    Run LPDAAC/MOD swath examples.
    """
    def tearDown(self):
        """
        Clear any open figure windows.
        """
        plt.close()

    def test_MOD11_L2_LST(self):
        """
        """
        hdffile = 'MOD11_L2.A2007278.0350.005.2007280073443.hdf'
        hdffile = fullpath(hdffile)
        zoo.lpdaac.mod.MOD11_L2_LST.run(hdffile)

class TestGrids(unittest.TestCase):
    """
    Run LPDAAC/MOD grid examples.
    """
    def tearDown(self):
        """
        Clear any open figure windows.
        """
        plt.close()

    def test_MOD13C2_CMG_0_05_Deg_Monthly_NDVI(self):
        """
        """
        hdffile = 'MOD13C2.A2007001.005.2007108072029.hdf'
        hdffile = fullpath(hdffile)
        zoo.lpdaac.mod.MOD13C2_CMG_0_05_Deg_Monthly_NDVI.run(hdffile)

if __name__ == "__main__":
    unittest.main()