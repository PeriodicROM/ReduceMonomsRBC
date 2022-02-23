"""
Created on Mon Feb 14 21:28:43 2022

@author: mlols
"""

from timeit import default_timer as timer
import csv
from construct_roms import hk_modes, construct_roms_quadratic
import reduce_monoms as rdm

def monom_reduction(ode_name, num_vars, monom_deg, hk_hier=True, hier_num=1,
                    monom_stats=True, out_file='auto', out_dir='Monoms'):
    """
    Generates list of monomials for auxiliary func ansatz in SDP computation. 
    Monomials are reduced using symmetry conditions and highest degree 
    cancellation.

    Parameters
    ----------
    ode_name : string
        Name of ODE.
    num_vars : int
        Number of variables in ODE.
    monom_deg : int
        Maximum degree of auxilary functions. Typically an even number.
    hk_hier : bool, optional
        If True, uses HK hierarchy for Rayleigh-Benard. The default is True.
    hier_num : int, optional
        Model number in the HK hierarchy. Only matters if hk_hier=True.
        The default is 1.
    monom_stats : bool, optional
        If True, outputs stats on number of monomials after each step.
        The default is True.
    out_file : string, optional
        Name of output file. The default is 'auto'.
    out_dir : string, optional
        Specify output directory. The default is 'Monoms'

    Returns
    -------
    None.
    
    Examples
    --------
    monom_reduction('HK4', 4, 6, hk_hier=True, hier_num=1)
        Generates and reduces list of monomials of degree 6 for the HK4 model

    """    
    if out_file == 'auto':
        out_file = 'Monoms_' + ode_name + '_deg_' + str(monom_deg) + '.csv'
        
    #Write data file with indices and coefficients of quadratic terms
    construct_roms_quadratic(mode_sel='hk', hier_num=hier_num)
    
    start = timer()
    #Generate and reduce monomial list
    V, V0, Monoms = rdm.reduceMonoms(num_vars, monom_deg)
    
    if V is None:
        return
        
    dirName = '../../Research/SDP/Periodic/Bounds/Monoms/'
    fileName = 'MonomStats.csv'
    end = timer()
    print('Time = ' + str(end-start))
    
    with open(dirName+fileName,'a+',newline='') as csv_file:
        csvwriter = csv.writer(csv_file)
        t = '{:.3f}'.format(end-start)
        row = [str(num_vars), str(monom_deg)]+[str(m) for m in Monoms]+[t]
        csvwriter.writerow(row)
        
    fileName2 = 'Monoms_HK'+str(num_vars)+'_deg_'+str(monom_deg)+'.csv'
    with open(dirName+fileName2,'w',newline='') as csv_file:
        csvwriter = csv.writer(csv_file)
        for v in V:
            csvwriter.writerow(v)
        for v in V0:
            csvwriter.writerow(v)
    
    return

    hier_num = 1
    p_modes, t_modes = hk_modes(hier_num)
    num_vars = len(p_modes) + len(t_modes)
    name = 'hk' + str(num_vars)

    monom_reduction('hk', num_vars, monom_deg=2, hier_num=hier_num)
    