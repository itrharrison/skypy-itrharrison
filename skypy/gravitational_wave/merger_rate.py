  
r"""Binary merger rate module.
This module provides facilities to produce compact binary merger rates per
year for individual galaxies.

"""

import numpy as np
from astropy import units


__all__ = [
           'abadie_tableIII_merger_rates',
]


def abadie_tableIII_merger_rates(luminosity,
                                 population='NS-NS',
                                 optimism='low'):

    r"""Model of Abadie et al (2010), Table III

      Compact binary merger rates as a linear function of L_10 blue light
      luminosity.

      Parameters
      ----------
      luminosity : (ngal,) array-like
          The blue light luminosity L_10 of the galaxies to generate merger
          rates for, where L_10 = 10^10 * 2.16e33 erg/s.
      population : {'NS-NS', 'NS-BH', 'BH-BH'}
          Compact binary population to get rate for.
          'NS-NS' is neutron star - neutron star
          'NS-BH' is neutron star - black hole
          'BH-BH' is black hole - black hole
      optimism : {'low', 'realistic', 'high'}
          Optimism of predicted merger rates.
          For 'NS-NS' there is an extra option 'max'.

      Returns
      -------
      merger_rate : array_like
          Merger rates for the galaxies in units of year^-1

      Notes
      -----


      References
      ----------
      .. Abadie et al. 2010, Classical and Quantum Gravity,
          Volume 27, Issue 17, article id. 173001 (2010)

      Examples
      --------
      >>> import skypy.galaxy.luminosity as lum
      >>> import skypy.gravitational_waves.merger_rate as merg

      Sample 100 luminosity values at redshift z = 1.0 with
      a_m = -0.9408582, b_m = -20.40492365, alpha = -1.3.

      >>> luminosities = lum.herbel_luminosities(1.0, -1.3, -0.9408582,
      ...                                         -20.40492365, size=100)

      Generate merger rates for these luminosities.

      >>> rates = merg.abadie_tableIII_merger_rates(luminosities,
      ...                                           population='NS-NS',
      ...                                           optimism='low')



      """
    abadie_tableIII_dict = {
                            'NS-NS': {'low': 0.6,
                                      'realistic': 60,
                                      'high': 600,
                                      'max': 2000},
                            'NS-BH': {'low': 0.03,
                                      'realistic': 2,
                                      'high': 60},
                            'BH-BH': {'low': 0.006,
                                      'realistic': 0.2,
                                      'high': 20}
                            }

    merger_rate = abadie_tableIII_dict[population, optimism] * luminosity
    merger_rate = merger_rate / units.year

    return merger_rate
