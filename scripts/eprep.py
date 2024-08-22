def calc_eprep(eixo_opt, macro_iso, macro_opt):
    EIXO_ISOLADO = -14.5807
    eprep_hartree = (eixo_opt - EIXO_ISOLADO) + (macro_opt - macro_iso)
    eprep = round(eprep_hartree * 627.509, 4)
    return eprep

# 1
eixo1_pos_opt = -14.5768
macro1_isolado = -16.0809
macro1_pos_opt = -16.0674

# 1a 
eixo2_pos_opt = -14.5836 
macro2_isolado = -17.8627
macro2_pos_opt = -17.8455

# 1b 
eixo0_pos_opt = -14.5778
macro0_isolado = -17.0626
macro0_pos_opt = -17.0520

# 1c 
eixo3_pos_opt = -14.5568
macro3_isolado = -18.3220
macro3_pos_opt = -18.3079

# 1d
eixo4_pos_opt = -14.5835
macro4_isolado = -17.9553 
macro4_pos_opt = -17.9459

# 2a
eixo5_pos_opt = -14.5766
macro5_isolado = -17.4092
macro5_pos_opt = -17.3962

# 2b
eixo6_pos_opt = -14.5775 
macro6_isolado = -16.8326
macro6_pos_opt = -16.8156

# 2c 
eixo7_pos_opt = -14.5777
macro7_isolado = -17.7427
macro7_pos_opt = -17.7257

# 2d
eixo8_pos_opt = -14.5764
macro8_isolado = -17.4763
macro8_pos_opt = -17.4648

# 3a 
eixo9_pos_opt = -14.5841
macro9_isolado = -19.1961
macro9_pos_opt = -19.1768

# 3b 
eixo10_pos_opt = -14.5759 
macro10_isolado = -17.8190 
macro10_pos_opt = -17.7974 

# 3c 
eixo11_pos_opt = -14.5760
macro11_isolado = -19.9764 
macro11_pos_opt = -19.9630

# 3d 
eixo12_pos_opt = -14.5762 
macro12_isolado = -19.3487
macro12_pos_opt = -19.3372 

Eprep1 = calc_eprep(eixo1_pos_opt, macro1_isolado, macro1_pos_opt)
Eprep2 = calc_eprep(eixo2_pos_opt, macro2_isolado, macro2_pos_opt)
Eprep0 = calc_eprep(eixo0_pos_opt, macro0_isolado, macro0_pos_opt)
Eprep3 = calc_eprep(eixo3_pos_opt, macro3_isolado, macro3_pos_opt)
Eprep4 = calc_eprep(eixo4_pos_opt, macro4_isolado, macro4_pos_opt)
Eprep5 = calc_eprep(eixo5_pos_opt, macro5_isolado, macro5_pos_opt)
Eprep6 = calc_eprep(eixo6_pos_opt, macro6_isolado, macro6_pos_opt)
Eprep7 = calc_eprep(eixo7_pos_opt, macro7_isolado, macro7_pos_opt)
Eprep8 = calc_eprep(eixo8_pos_opt, macro8_isolado, macro8_pos_opt)
Eprep9 = calc_eprep(eixo9_pos_opt, macro9_isolado, macro9_pos_opt)
Eprep10 = calc_eprep(eixo10_pos_opt, macro10_isolado, macro10_pos_opt)
Eprep11 = calc_eprep(eixo11_pos_opt, macro11_isolado, macro11_pos_opt)
Eprep12 = calc_eprep(eixo12_pos_opt, macro12_isolado, macro12_pos_opt)

print("""
      ---------------------------\n
      PREPARATION ENERGY RESULTS:\n
      ----------------------------\n
      structure 1: {} kcal/mol\n 
      structure 1a: {} kcal/mol\n 
      structure 1b: {} kcal/mol\n 
      structure 1c: {} kcal/mol\n 
      structure 1d: {} kcal/mol\n 
      structure 2a: {} kcal/mol\n 
      structure 2b: {} kcal/mol\n 
      structure 2c: {} kcal/mol\n 
      structure 2d: {} kcal/mol\n 
      structure 3a: {} kcal/mol\n 
      structure 3b: {} kcal/mol\n 
      structure 3c: {} kcal/mol\n 
      structure 3d: {} kcal/mol\n
      """.format(Eprep1, Eprep2, Eprep0, Eprep3, Eprep4, Eprep5, Eprep6,Eprep7, Eprep8, Eprep9, Eprep10, Eprep11, Eprep12))
