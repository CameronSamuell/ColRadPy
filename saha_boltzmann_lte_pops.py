import numpy as np


def boltzmann_population(w,energy,temp,norm_tot=False):
    """ Calculates the LTE boltzmann populations given level spin, level energies and a temperature array
        returns the boltzmann populations relative to the ground state.


    Args:
      :param w: array of the level spins
      :type w: float array

      :param energy: array of the energy levels (cm-1)
      :type energy: float array

      :param temp: array of temperatures for calculation (eV)
      :type temp: float array

      :param norm_tot: If true normalizes to the total population instead of the ground
      :type norm_tot: boolean



    :returns: float array populations of levels relative to the ground [len(levels),len(temp)]

    """
    stat_weight = (w[1:]*2 + 1) / (w[0]*2 + 1)
    boltz_pop = stat_weight[:,None]*np.exp(-(engergy[1:,None] - energy[0,None])/(temp*8065.313546745508))


    if(
    
    return boltz_pop







