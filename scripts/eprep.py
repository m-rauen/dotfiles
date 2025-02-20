def calc_eprep(val):
    iso = -33.80004
    eprep_hartree = (val - iso) 
    eprep = round(eprep_hartree * 627.509, 4)
    return eprep

s1_h_bromo = -33.79524
s1_h_cloro = -33.79425
#s1_h_fluor = 
s1_h_iodo = -33.79587

#eprep_fluor = calc_eprep(s1_h_fluor)
eprep_cloro = calc_eprep(s1_h_cloro)
eprep_bromo = calc_eprep(s1_h_bromo)
eprep_iodo = calc_eprep(s1_h_iodo)

print("""
      ---------------------------\n
      PREPARATION ENERGY RESULTS:\n
      ----------------------------\n
      structure w/ Cl: {} kcal/mol\n 
      structure w/ Br: {} kcal/mol\n 
      structure w/ I: {} kcal/mol\n 
      """.format(eprep_cloro, eprep_bromo, eprep_iodo))
