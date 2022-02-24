# ReduceMonomsRBC
ReduceMonomsRBC is a Python package that reduces the list of monomials in the auxiliary function for sum-of-squares (SOS) optimization of reduced-order models (ROMS). The monomials are reduced by applying highest-degree cancellation and symmetry conditions derived from the structure of the ROM. This package is built for ROMs of 2D Rayleigh&ndash;Bénard convection, but can be adapted to any ROM whose general structure is known.

## Features:
- Reduce list of monomials and save list for use in SOS optimization
- Generate ouptut file with number of monomials at each reduction step.

# Package Requirements
- numpy (Version 1.5 or later)
- sympy (Version 1.6 or later)
- csv (any version)
- scipy (Version 0.10 or later)

# Installation
To install the package, either:
- download or clone this repository and use `from ReduceMonomsRBC import monom_reduction` from the directory containing the package, OR
- install package directly using `pip install ReduceMonomsRBC` then `from ReduceMonomsRBC import monom_reduction`

# Instructions
To construct a system of ROMs, use the command `monom_reduction(*args)`. Options can be passed as function arguments as detailed below.

## Options:
  - `ode_name` : Name of ODE. If name is 'auto', name will be created as 'HKN' with N = num_vars
  - `monom_deg` : Maximum degree of auxilary functions. Typically an even number
  - `hk_hier` : If `True`, uses HK hierarchy for Rayleigh&ndash;Bénard
  - `hier_num` : Model number in the HK hierarchy. Only matters if `hk_hier=True`
  - `p_modes` : List of psi modes, represented as tuples
  - `t_modes` : List of theta modes, represented as tuples
  - `monom_stats` : If `True`, outputs stats on number of monomials after each step
  - `monom_dir` : Name of output directory for monomial data
  - `fQ_dir` : Name of output directory for file containing info on structure of ROM
        
## Examples:
`monom_reduction('HK4', 4, 6, hk_hier=True, hier_num=1)`  
Generates and reduces list of monomials of degree 6 for the HK4 model (in the HK hierarchy of ROMs)

## Output files:
ReduceMonomialsRBC creates several output files with a particular structure
- The monomials file is a .csv file with each row represnting a monomial in the auxiliary function. In each row, the nth column gives the power of the nth variable in the ROM. This file is created within `monom_dir`.
- Summary stats on the monomial reduction process can be generated if `monom_stats` is set to True. This is a .csv file that includes the number of variables, maximum degree of the auxiliary function, number of monomials remaining at each step (broken down by those of maximum degree and of lower degree), and the total time. This file is also created within `monom_dir`
- An ROM structure file is generated called `ode_name.txt` that is used internally to reduce monomials. The structure file is place in fQ_dir. The two objects in the file are:  
  - fQ: The list of quadratic terms in the ROM. This is a nested list where elements of the outer list represent the ROM equation where the quadratic term is located. Within the outer list is a list of the quadratic terms. Within this second list are lists of length 2, containing the indices of the variables in that term. For example, in the Lorenz equations, `fQ = [ [], [ [1, 3] ], [ [1, 2] ] ]`.
  - a: The list of coefficients of the above terms. This is also a nested list, but has only the two outer levels, and the innermost list in fQ is replaced by a symbolic expression. For example, in the Lorenz equations (with the traditional scaling), `a = [ [0], [-1], [1] ]`.
