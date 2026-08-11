import openmc

def get_pnnl_mats(xs_lib: str = "endfb81") -> dict[int, openmc.Material]:
    """
    Returns a dictionary OpenMC materials of all PNNL-15870r2 entries indexed by ID.

    :param xs_lib: String for identifying the cross-section library that will be used. This is important for applying TSL s-alpha-beta tables.

    :return: A dictionary of openmc.Material objects indexed by their ID in the PNNL-15870r2 report.
    """

    mat_list = []

    # --- PNNL 1: A-150 Tissue-Equivalent Plastic ---
    mat = openmc.Material(material_id=1, name="A-150 Tissue-Equivalent Plastic")
    mat.set_density("g/cc", 1.127)
    mat.add_nuclide("H1", 0.101300, "wo")
    mat.add_nuclide("H2", 0.000023, "wo")
    mat.add_element("C", 0.775500, "wo")
    mat.add_nuclide("N14", 0.034920, "wo")
    mat.add_nuclide("N15", 0.000137, "wo")
    mat.add_nuclide("O16", 0.052174, "wo")
    mat.add_nuclide("O17", 0.000021, "wo")
    mat.add_nuclide("O18", 0.000121, "wo")
    mat.add_nuclide("F19", 0.017422, "wo")
    mat.add_element("Ca", 0.018378, "wo")
    mat_list.append(mat)


    # --- PNNL 2: Acetone ---
    mat = openmc.Material(material_id=2, name="Acetone")
    mat.set_density("g/cc", 0.7899)
    mat.add_nuclide("H1", 0.104104, "wo")
    mat.add_nuclide("H2", 0.000024, "wo")
    mat.add_element("C", 0.620393, "wo")
    mat.add_nuclide("O16", 0.274730, "wo")
    mat.add_nuclide("O17", 0.000111, "wo")
    mat.add_nuclide("O18", 0.000635, "wo")
    mat_list.append(mat)


    # --- PNNL 3: Acetylene ---
    mat = openmc.Material(material_id=3, name="Acetylene")
    mat.set_density("g/cc",0.0010967)
    mat.add_nuclide("H1", 0.077405, "wo")
    mat.add_nuclide("H2", 0.000018, "wo")
    mat.add_element("C", 0.922574, "wo")
    mat_list.append(mat)


    # --- PNNL 4: Air (dry, near sea level) ---
    mat = openmc.Material(material_id=4, name="Air (dry, near sea level)")
    mat.set_density("g/cc",0.001205)
    mat.add_element("C", 0.000124, "wo")
    mat.add_nuclide("N14", 0.752316, "wo")
    mat.add_nuclide("N15", 0.002944, "wo")
    mat.add_nuclide("O16", 0.231153, "wo")
    mat.add_nuclide("O17", 0.000094, "wo")
    mat.add_nuclide("O18", 0.000535, "wo")
    mat.add_element("Ar", 0.012827, "wo")
    mat_list.append(mat)


    # --- PNNL 5: Alanine ---
    mat = openmc.Material(material_id=5, name="Alanine")
    mat.set_density("g/cc", 1.42)
    mat.add_nuclide("H1", 0.079169, "wo")
    mat.add_nuclide("H2", 0.000018, "wo")
    mat.add_element("C", 0.404439, "wo")
    mat.add_nuclide("N14", 0.156598, "wo")
    mat.add_nuclide("N15", 0.000613, "wo")
    mat.add_nuclide("O16", 0.358185, "wo")
    mat.add_nuclide("O17", 0.000145, "wo")
    mat.add_nuclide("O18", 0.000828, "wo")
    mat_list.append(mat)


    # --- PNNL 6: Aluminum ---
    mat = openmc.Material(material_id=6, name="Aluminum")
    mat.set_density("g/cc", 2.6989)
    mat.add_nuclide("Al27", 1.000000, "wo")
    mat_list.append(mat)


    # --- PNNL 7: Aluminum Oxide ---
    mat = openmc.Material(material_id=7, name="Aluminum Oxide")
    mat.set_density("g/cc", 3.97)
    mat.add_nuclide("O16", 0.469474, "wo")
    mat.add_nuclide("O17", 0.000190, "wo")
    mat.add_nuclide("O18", 0.001086, "wo")
    mat.add_nuclide("Al27", 0.529251, "wo")
    mat_list.append(mat)


    # --- PNNL 8: Aluminum, alloy 2024-O ---
    mat = openmc.Material(material_id=8, name="Aluminum, alloy 2024-O")
    mat.set_density("g/cc", 2.78)
    mat.add_element("Mg", 0.015000, "wo")
    mat.add_nuclide("Al27", 0.927000, "wo")
    mat.add_element("Si", 0.002833, "wo")
    mat.add_element("Ti", 0.000850, "wo")
    mat.add_element("Cr", 0.000567, "wo")
    mat.add_nuclide("Mn55", 0.006000, "wo")
    mat.add_element("Fe", 0.002833, "wo")
    mat.add_element("Cu", 0.043500, "wo")
    mat.add_element("Zn", 0.001417, "wo")
    mat_list.append(mat)


    # --- PNNL 9: Aluminum, alloy 2090-T83 ---
    mat = openmc.Material(material_id=9, name="Aluminum, alloy 2090-T83")
    mat.set_density("g/cc", 2.59)
    mat.add_nuclide("Li6", 0.001474, "wo")
    mat.add_nuclide("Li7", 0.020937, "wo")
    mat.add_element("Mg", 0.001631, "wo")
    mat.add_nuclide("Al27", 0.944001, "wo")
    mat.add_element("Si", 0.000652, "wo")
    mat.add_element("Ti", 0.000979, "wo")
    mat.add_element("Cr", 0.000326, "wo")
    mat.add_nuclide("Mn55", 0.000326, "wo")
    mat.add_element("Fe", 0.000783, "wo")
    mat.add_element("Cu", 0.027000, "wo")
    mat.add_element("Zn", 0.000652, "wo")
    mat.add_nuclide("Zr90", 0.000583, "wo")
    mat.add_nuclide("Zr91", 0.000129, "wo")
    mat.add_nuclide("Zr92", 0.000199, "wo")
    mat.add_nuclide("Zr94", 0.000206, "wo")
    mat.add_nuclide("Zr96", 0.000034, "wo")
    mat_list.append(mat)


    # --- PNNL 10: Aluminum, alloy 3003 ---
    mat = openmc.Material(material_id=10, name="Aluminum, alloy 3003")
    mat.set_density("g/cc", 2.73)
    mat.add_nuclide("Al27", 0.978500, "wo")
    mat.add_element("Si", 0.003321, "wo")
    mat.add_nuclide("Mn55", 0.012500, "wo")
    mat.add_element("Fe", 0.003875, "wo")
    mat.add_element("Cu", 0.001250, "wo")
    mat.add_element("Zn", 0.000554, "wo")
    mat_list.append(mat)


    # --- PNNL 11: Aluminum, alloy 4043-O ---
    mat = openmc.Material(material_id=11, name="Aluminum, alloy 4043-O")
    mat.set_density("g/cc", 2.69)
    mat.add_nuclide("Be9", 0.000005, "wo")
    mat.add_element("Mg", 0.000283, "wo")
    mat.add_nuclide("Al27", 0.939000, "wo")
    mat.add_element("Si", 0.052500, "wo")
    mat.add_element("Ti", 0.001133, "wo")
    mat.add_nuclide("Mn55", 0.000283, "wo")
    mat.add_element("Fe", 0.004531, "wo")
    mat.add_element("Cu", 0.001699, "wo")
    mat.add_element("Zn", 0.000566, "wo")
    mat_list.append(mat)


    # --- PNNL 12: Aluminum, alloy 5086-O ---
    mat = openmc.Material(material_id=12, name="Aluminum, alloy 5086-O")
    mat.set_density("g/cc", 2.66)
    mat.add_element("Mg", 0.040000, "wo")
    mat.add_nuclide("Al27", 0.946499, "wo")
    mat.add_element("Si", 0.002143, "wo")
    mat.add_element("Ti", 0.000804, "wo")
    mat.add_element("Cr", 0.001500, "wo")
    mat.add_nuclide("Mn55", 0.004500, "wo")
    mat.add_element("Fe", 0.002679, "wo")
    mat.add_element("Cu", 0.000536, "wo")
    mat.add_element("Zn", 0.001339, "wo")
    mat_list.append(mat)


    # --- PNNL 13: Aluminum, alloy 6061-O ---
    mat = openmc.Material(material_id=13, name="Aluminum, alloy 6061-O")
    mat.set_density("g/cc", 2.70)
    mat.add_element("Mg", 0.010000, "wo")
    mat.add_nuclide("Al27", 0.972000, "wo")
    mat.add_element("Si", 0.006000, "wo")
    mat.add_element("Ti", 0.000876, "wo")
    mat.add_element("Cr", 0.001950, "wo")
    mat.add_nuclide("Mn55", 0.000876, "wo")
    mat.add_element("Fe", 0.004088, "wo")
    mat.add_element("Cu", 0.002750, "wo")
    mat.add_element("Zn", 0.001460, "wo")
    mat_list.append(mat)


    # --- PNNL 14: Aluminum, alloy 7075-O ---
    mat = openmc.Material(material_id=14, name="Aluminum, alloy 7075-O")
    mat.set_density("g/cc", 2.81)
    mat.add_element("Mg", 0.025000, "wo")
    mat.add_nuclide("Al27", 0.892500, "wo")
    mat.add_element("Si", 0.002343, "wo")
    mat.add_element("Ti", 0.001171, "wo")
    mat.add_element("Cr", 0.002300, "wo")
    mat.add_nuclide("Mn55", 0.001757, "wo")
    mat.add_element("Fe", 0.002929, "wo")
    mat.add_element("Cu", 0.016000, "wo")
    mat.add_element("Zn", 0.056000, "wo")
    mat_list.append(mat)


    # --- PNNL 15: Ammonia (liquid at T= -79 C) ---
    mat = openmc.Material(material_id=15, name="Ammonia (liquid at T= -79 C)")
    mat.set_density("g/cc", 0.771)
    mat.add_nuclide("H1", 0.177510, "wo")
    mat.add_nuclide("H2", 0.000041, "wo")
    mat.add_nuclide("N14", 0.819229, "wo")
    mat.add_nuclide("N15", 0.003206, "wo")
    mat_list.append(mat)


    # --- PNNL 16: Anthracene ---
    mat = openmc.Material(material_id=16, name="Anthracene")
    mat.set_density("g/cc", 1.28)
    mat.add_nuclide("H1", 0.056540, "wo")
    mat.add_nuclide("H2", 0.000013, "wo")
    mat.add_element("C", 0.943445, "wo")
    mat_list.append(mat)


    # --- PNNL 17: Argon ---
    mat = openmc.Material(material_id=17, name="Argon")
    mat.set_density("g/cc", 0.001662)
    mat.add_element("Ar", 1.000000, "wo")
    mat_list.append(mat)


    # --- PNNL 18: Asbestos (Chrysotile) ---
    mat = openmc.Material(material_id=18, name="Asbestos (Chrysotile)")
    mat.set_density("g/cc", 2.53)
    mat.add_nuclide("H1", 0.014546, "wo")
    mat.add_nuclide("H2", 0.000003, "wo")
    mat.add_nuclide("O16", 0.518216, "wo")
    mat.add_nuclide("O17", 0.000210, "wo")
    mat.add_nuclide("O18", 0.001198, "wo")
    mat.add_element("Mg", 0.263129, "wo")
    mat.add_element("Si", 0.202697, "wo")
    mat_list.append(mat)


    # --- PNNL 19: Asphalt ---
    mat = openmc.Material(material_id=19, name="Asphalt")
    mat.set_density("g/cc", 1.3)
    mat.add_nuclide("H1", 0.103697, "wo")
    mat.add_nuclide("H2", 0.000024, "wo")
    mat.add_element("C", 0.848048, "wo")
    mat.add_nuclide("N14", 0.006026, "wo")
    mat.add_nuclide("N15", 0.000024, "wo")
    mat.add_nuclide("O16", 0.004039, "wo")
    mat.add_nuclide("O17", 0.000002, "wo")
    mat.add_nuclide("O18", 0.000009, "wo")
    mat.add_element("S", 0.037700, "wo")
    mat.add_element("V", 0.000393, "wo")
    mat.add_element("Ni", 0.000034, "wo")
    mat_list.append(mat)


    # --- PNNL 20: Asphalt pavement ---
    mat = openmc.Material(material_id=20, name="Asphalt pavement")
    mat.set_density("g/cc", 2.5784)
    mat.add_nuclide("H1", 0.007508, "wo")
    mat.add_nuclide("H2", 0.000002, "wo")
    mat.add_element("C", 0.106744, "wo")
    mat.add_nuclide("N14", 0.000362, "wo")
    mat.add_nuclide("N15", 0.000001, "wo")
    mat.add_nuclide("O16", 0.423081, "wo")
    mat.add_nuclide("O17", 0.000171, "wo")
    mat.add_nuclide("O18", 0.000978, "wo")
    mat.add_nuclide("Na23", 0.013149, "wo")
    mat.add_element("Mg", 0.031061, "wo")
    mat.add_nuclide("Al27", 0.054927, "wo")
    mat.add_element("Si", 0.195830, "wo")
    mat.add_nuclide("P31", 0.000448, "wo")
    mat.add_element("S", 0.010764, "wo")
    mat.add_element("K", 0.016001, "wo")
    mat.add_element("Ca", 0.102275, "wo")
    mat.add_element("Ti", 0.003421, "wo")
    mat.add_element("V", 0.000024, "wo")
    mat.add_nuclide("Mn55", 0.000427, "wo")
    mat.add_element("Fe", 0.032824, "wo")
    mat.add_element("Ni", 0.000002, "wo")
    mat_list.append(mat)


    # --- PNNL 21: Bakelite ---
    mat = openmc.Material(material_id=21, name="Bakelite")
    mat.set_density("g/cc", 1.25)
    mat.add_nuclide("H1", 0.057429, "wo")
    mat.add_nuclide("H2", 0.000013, "wo")
    mat.add_element("C", 0.774588, "wo")
    mat.add_nuclide("O16", 0.167513, "wo")
    mat.add_nuclide("O17", 0.000068, "wo")
    mat.add_nuclide("O18", 0.000387, "wo")
    mat_list.append(mat)


    # --- PNNL 22: Barium Fluoride ---
    mat = openmc.Material(material_id=22, name="Barium Fluoride")
    mat.set_density("g/cc", 4.89)
    mat.add_nuclide("F19", 0.216724, "wo")
    mat.add_nuclide("Ba130", 0.000785, "wo")
    mat.add_nuclide("Ba132", 0.000760, "wo")
    mat.add_nuclide("Ba134", 0.018460, "wo")
    mat.add_nuclide("Ba135", 0.050723, "wo")
    mat.add_nuclide("Ba136", 0.060881, "wo")
    mat.add_nuclide("Ba137", 0.087708, "wo")
    mat.add_nuclide("Ba138", 0.563958, "wo")
    mat_list.append(mat)


    # --- PNNL 23: Barium sulfate ---
    mat = openmc.Material(material_id=23, name="Barium sulfate")
    mat.set_density("g/cc", 4.5)
    mat.add_nuclide("O16", 0.273463, "wo")
    mat.add_nuclide("O17", 0.000111, "wo")
    mat.add_nuclide("O18", 0.000632, "wo")
    mat.add_element("S", 0.137398, "wo")
    mat.add_nuclide("Ba130", 0.000590, "wo")
    mat.add_nuclide("Ba132", 0.000571, "wo")
    mat.add_nuclide("Ba134", 0.013867, "wo")
    mat.add_nuclide("Ba135", 0.038103, "wo")
    mat.add_nuclide("Ba136", 0.045734, "wo")
    mat.add_nuclide("Ba137", 0.065886, "wo")
    mat.add_nuclide("Ba138", 0.423645, "wo")
    mat_list.append(mat)


    # --- PNNL 24: Benzene ---
    mat = openmc.Material(material_id=24, name="Benzene")
    mat.set_density("g/cc", 0.8786)
    mat.add_nuclide("H1", 0.077405, "wo")
    mat.add_nuclide("H2", 0.000018, "wo")
    mat.add_element("C", 0.922574, "wo")
    mat_list.append(mat)


    # --- PNNL 25: Beryllium ---
    mat = openmc.Material(material_id=25, name="Beryllium")
    mat.set_density("g/cc", 1.848)
    mat.add_nuclide("Be9", 1.000000, "wo")
    mat_list.append(mat)


    # --- PNNL 26: Beryllium Carbide ---
    mat = openmc.Material(material_id=26, name="Beryllium Carbide")
    mat.set_density("g/cc", 1.9)
    mat.add_nuclide("Be9", 0.600113, "wo")
    mat.add_element("C", 0.399887, "wo")
    mat_list.append(mat)


    # --- PNNL 27: Beryllium Oxide ---
    mat = openmc.Material(material_id=27, name="Beryllium Oxide")
    mat.set_density("g/cc", 3.01)
    mat.add_nuclide("Be9", 0.360320, "wo")
    mat.add_nuclide("O16", 0.637946, "wo")
    mat.add_nuclide("O17", 0.000258, "wo")
    mat.add_nuclide("O18", 0.001475, "wo")
    mat_list.append(mat)


    # --- PNNL 28: Bismuth ---
    mat = openmc.Material(material_id=28, name="Bismuth")
    mat.set_density("g/cc", 9.747)
    mat.add_nuclide("Bi209", 1.000000, "wo")
    mat_list.append(mat)


    # --- PNNL 29: Bismuth Germanate (BGO) ---
    mat = openmc.Material(material_id=29, name="Bismuth Germanate (BGO)")
    mat.set_density("g/cc", 7.13)
    mat.add_nuclide("O16", 0.153694, "wo")
    mat.add_nuclide("O17", 0.000062, "wo")
    mat.add_nuclide("O18", 0.000355, "wo")
    mat.add_nuclide("Ge70", 0.034636, "wo")
    mat.add_nuclide("Ge72", 0.047542, "wo")
    mat.add_nuclide("Ge73", 0.013609, "wo")
    mat.add_nuclide("Ge74", 0.064973, "wo")
    mat.add_nuclide("Ge76", 0.014132, "wo")
    mat.add_nuclide("Bi209", 0.670989, "wo")
    mat_list.append(mat)


    # --- PNNL 30: Bismuth Iodide ---
    mat = openmc.Material(material_id=30, name="Bismuth Iodide")
    mat.set_density("g/cc", 5.778)
    mat.add_nuclide("I127", 0.645612, "wo")
    mat.add_nuclide("Bi209", 0.354388, "wo")
    mat_list.append(mat)


    # --- PNNL 31: Blood (ICRP) ---
    mat = openmc.Material(material_id=31, name="Blood (ICRP)")
    mat.set_density("g/cc", 1.06)
    mat.add_nuclide("H1", 0.101839, "wo")
    mat.add_nuclide("H2", 0.000023, "wo")
    mat.add_element("C", 0.100020, "wo")
    mat.add_nuclide("N14", 0.029524, "wo")
    mat.add_nuclide("N15", 0.000116, "wo")
    mat.add_nuclide("O16", 0.757356, "wo")
    mat.add_nuclide("O17", 0.000307, "wo")
    mat.add_nuclide("O18", 0.001751, "wo")
    mat.add_nuclide("Na23", 0.001850, "wo")
    mat.add_element("Mg", 0.000040, "wo")
    mat.add_element("Si", 0.000030, "wo")
    mat.add_nuclide("P31", 0.000350, "wo")
    mat.add_element("S", 0.001850, "wo")
    mat.add_nuclide("Cl35", 0.002077, "wo")
    mat.add_nuclide("Cl37", 0.000703, "wo")
    mat.add_element("K", 0.001630, "wo")
    mat.add_element("Ca", 0.000060, "wo")
    mat.add_element("Fe", 0.000460, "wo")
    mat.add_element("Zn", 0.000010, "wo")
    mat_list.append(mat)


    # --- PNNL 32: Bone Equivalent Plastic, B-100 ---
    mat = openmc.Material(material_id=32, name="Bone Equivalent Plastic, B-100")
    mat.set_density("g/cc", 1.45)
    mat.add_nuclide("H1", 0.065454, "wo")
    mat.add_nuclide("H2", 0.000015, "wo")
    mat.add_element("C", 0.536944, "wo")
    mat.add_nuclide("N14", 0.021416, "wo")
    mat.add_nuclide("N15", 0.000084, "wo")
    mat.add_nuclide("O16", 0.031998, "wo")
    mat.add_nuclide("O17", 0.000013, "wo")
    mat.add_nuclide("O18", 0.000074, "wo")
    mat.add_nuclide("F19", 0.167411, "wo")
    mat.add_element("Ca", 0.176589, "wo")
    mat_list.append(mat)


    # --- PNNL 33: Bone Equivalent Plastic, B-110 ---
    mat = openmc.Material(material_id=33, name="Bone Equivalent Plastic, B-110")
    mat.set_density("g/cc", 1.785)
    mat.add_nuclide("H1", 0.035491, "wo")
    mat.add_nuclide("H2", 0.000008, "wo")
    mat.add_element("C", 0.367300, "wo")
    mat.add_nuclide("N14", 0.039545, "wo")
    mat.add_nuclide("N15", 0.000155, "wo")
    mat.add_nuclide("O16", 0.045177, "wo")
    mat.add_nuclide("O17", 0.000018, "wo")
    mat.add_nuclide("O18", 0.000104, "wo")
    mat.add_nuclide("F19", 0.249300, "wo")
    mat.add_element("Ca", 0.262900, "wo")
    mat_list.append(mat)


    # --- PNNL 34: Bone, Compact (ICRU) ---
    mat = openmc.Material(material_id=34, name="Bone, Compact (ICRU)")
    mat.set_density("g/cc", 1.85)
    mat.add_nuclide("H1", 0.063967, "wo")
    mat.add_nuclide("H2", 0.000015, "wo")
    mat.add_element("C", 0.278000, "wo")
    mat.add_nuclide("N14", 0.026894, "wo")
    mat.add_nuclide("N15", 0.000105, "wo")
    mat.add_nuclide("O16", 0.408905, "wo")
    mat.add_nuclide("O17", 0.000166, "wo")
    mat.add_nuclide("O18", 0.000946, "wo")
    mat.add_element("Mg", 0.002000, "wo")
    mat.add_nuclide("P31", 0.070000, "wo")
    mat.add_element("S", 0.002000, "wo")
    mat.add_element("Ca", 0.147000, "wo")
    mat_list.append(mat)


    # --- PNNL 35: Bone, Cortical (ICRP) ---
    mat = openmc.Material(material_id=35, name="Bone, Cortical (ICRP)")
    mat.set_density("g/cc", 1.85)
    mat.add_nuclide("H1", 0.047222, "wo")
    mat.add_nuclide("H2", 0.000011, "wo")
    mat.add_element("C", 0.144330, "wo")
    mat.add_nuclide("N14", 0.041826, "wo")
    mat.add_nuclide("N15", 0.000164, "wo")
    mat.add_nuclide("O16", 0.444887, "wo")
    mat.add_nuclide("O17", 0.000180, "wo")
    mat.add_nuclide("O18", 0.001029, "wo")
    mat.add_element("Mg", 0.002200, "wo")
    mat.add_nuclide("P31", 0.104970, "wo")
    mat.add_element("S", 0.003150, "wo")
    mat.add_element("Ca", 0.209930, "wo")
    mat.add_element("Zn", 0.000100, "wo")
    mat_list.append(mat)


    # --- PNNL 36: Boral (65% Al-35% B4C) ---
    mat = openmc.Material(material_id=36, name="Boral (65% Al-35% B4C)")
    mat.set_density("g/cc", 2.53)
    mat.add_nuclide("B10", 0.050489, "wo")
    mat.add_nuclide("B11", 0.223448, "wo")
    mat.add_element("C", 0.076000, "wo")
    mat.add_nuclide("Al27", 0.650000, "wo")
    mat_list.append(mat)


    # --- PNNL 37: Boral (Aluminum 10% boron alloy) ---
    mat = openmc.Material(material_id=37, name="Boral (Aluminum 10% boron alloy)")
    mat.set_density("g/cc", 2.6)
    mat.add_nuclide("B10", 0.018427, "wo")
    mat.add_nuclide("B11", 0.081550, "wo")
    mat.add_nuclide("Na23", 0.005000, "wo")
    mat.add_nuclide("Al27", 0.879000, "wo")
    mat.add_element("Si", 0.002500, "wo")
    mat.add_element("K", 0.010000, "wo")
    mat.add_element("Ti", 0.000500, "wo")
    mat.add_element("Fe", 0.003000, "wo")
    mat_list.append(mat)


    # --- PNNL 38: Boral (Aluminum 5% boron alloy) ---
    mat = openmc.Material(material_id=38, name="Boral (Aluminum 5% boron alloy)")
    mat.set_density("g/cc", 2.6)
    mat.add_nuclide("B10", 0.009225, "wo")
    mat.add_nuclide("B11", 0.040828, "wo")
    mat.add_nuclide("Na23", 0.005007, "wo")
    mat.add_nuclide("Al27", 0.929407, "wo")
    mat.add_element("Si", 0.002003, "wo")
    mat.add_element("K", 0.010013, "wo")
    mat.add_element("Ti", 0.000501, "wo")
    mat.add_element("Fe", 0.003004, "wo")
    mat_list.append(mat)


    # --- PNNL 39: Borax ---
    mat = openmc.Material(material_id=39, name="Borax")
    mat.set_density("g/cc", 1.73)
    mat.add_nuclide("Na23", 0.120560, "wo")
    mat.add_nuclide("B10", 0.020898, "wo")
    mat.add_nuclide("B11", 0.092489, "wo")
    mat.add_nuclide("O16", 0.711235, "wo")
    mat.add_nuclide("O17", 0.000288, "wo")
    mat.add_nuclide("O18", 0.001645, "wo")
    mat.add_nuclide("H1", 0.052845, "wo")
    mat.add_nuclide("H2", 0.000012, "wo")
    mat_list.append(mat)


    # --- PNNL 40: Boric Acid ---
    mat = openmc.Material(material_id=40, name="Boric Acid")
    mat.set_density("g/cc", 1.5)
    mat.add_nuclide("H1", 0.048890, "wo")
    mat.add_nuclide("H2", 0.000011, "wo")
    mat.add_nuclide("B10", 0.032224, "wo")
    mat.add_nuclide("B11", 0.142611, "wo")
    mat.add_nuclide("O16", 0.774119, "wo")
    mat.add_nuclide("O17", 0.000313, "wo")
    mat.add_nuclide("O18", 0.001790, "wo")
    mat_list.append(mat)


    # --- PNNL 41: Boron ---
    mat = openmc.Material(material_id=41, name="Boron")
    mat.set_density("g/cc", 2.37)
    mat.add_nuclide("B10", 0.184267, "wo")
    mat.add_nuclide("B11", 0.815504, "wo")
    mat_list.append(mat)


    # --- PNNL 42: Boron Carbide ---
    mat = openmc.Material(material_id=42, name="Boron Carbide")
    mat.set_density("g/cc", 2.52)
    mat.add_nuclide("B10", 0.144221, "wo")
    mat.add_nuclide("B11", 0.638271, "wo")
    mat.add_element("C", 0.217329, "wo")
    mat_list.append(mat)


    # --- PNNL 43: Boron Fluoride (B2F4) ---
    mat = openmc.Material(material_id=43, name="Boron Fluoride (B2F4)")
    mat.set_density("g/cc", 0.004058)
    mat.add_nuclide("B10", 0.040823, "wo")
    mat.add_nuclide("B11", 0.180668, "wo")
    mat.add_nuclide("F19", 0.778459, "wo")
    mat_list.append(mat)


    # --- PNNL 44: Boron Fluoride (BF3) ---
    mat = openmc.Material(material_id=44, name="Boron Fluoride (BF3)")
    mat.set_density("g/cc", 0.002831)
    mat.add_nuclide("B10", 0.029385, "wo")
    mat.add_nuclide("B11", 0.130049, "wo")
    mat.add_nuclide("F19", 0.840529, "wo")
    mat_list.append(mat)


    # --- PNNL 45: Boron Oxide ---
    mat = openmc.Material(material_id=45, name="Boron Oxide")
    mat.set_density("g/cc", 1.812)
    mat.add_nuclide("B10", 0.057237, "wo")
    mat.add_nuclide("B11", 0.253312, "wo")
    mat.add_nuclide("O16", 0.687512, "wo")
    mat.add_nuclide("O17", 0.000278, "wo")
    mat.add_nuclide("O18", 0.001590, "wo")
    mat_list.append(mat)


    # --- PNNL 46: Brain (ICRP) ---
    mat = openmc.Material(material_id=46, name="Brain (ICRP)")
    mat.set_density("g/cc", 1.03)
    mat.add_nuclide("H1", 0.110638, "wo")
    mat.add_nuclide("H2", 0.000025, "wo")
    mat.add_element("C", 0.125420, "wo")
    mat.add_nuclide("N14", 0.013228, "wo")
    mat.add_nuclide("N15", 0.000052, "wo")
    mat.add_nuclide("O16", 0.735724, "wo")
    mat.add_nuclide("O17", 0.000298, "wo")
    mat.add_nuclide("O18", 0.001701, "wo")
    mat.add_nuclide("Na23", 0.001840, "wo")
    mat.add_element("Mg", 0.000150, "wo")
    mat.add_nuclide("P31", 0.003540, "wo")
    mat.add_element("S", 0.001770, "wo")
    mat.add_nuclide("Cl35", 0.001764, "wo")
    mat.add_nuclide("Cl37", 0.000597, "wo")
    mat.add_element("K", 0.003100, "wo")
    mat.add_element("Ca", 0.000090, "wo")
    mat.add_element("Fe", 0.000050, "wo")
    mat.add_element("Zn", 0.000010, "wo")
    mat_list.append(mat)


    # --- PNNL 47: Brass (typical composition) ---
    mat = openmc.Material(material_id=47, name="Brass (typical composition)")
    mat.set_density("g/cc", 8.07)
    mat.add_element("Fe", 0.000868, "wo")
    mat.add_element("Cu", 0.665384, "wo")
    mat.add_element("Zn", 0.325699, "wo")
    mat.add_element("Sn", 0.002672, "wo")
    mat.add_nuclide("P31", 0.005377, "wo")
    mat_list.append(mat)


    # --- PNNL 48: Brick, Common Silica ---
    mat = openmc.Material(material_id=48, name="Brick, Common Silica")
    mat.set_density("g/cc", 1.8)
    mat.add_nuclide("O16", 0.523577, "wo")
    mat.add_nuclide("O17", 0.000212, "wo")
    mat.add_nuclide("O18", 0.001211, "wo")
    mat.add_nuclide("Al27", 0.005000, "wo")
    mat.add_element("Si", 0.449000, "wo")
    mat.add_element("Ca", 0.014000, "wo")
    mat.add_element("Fe", 0.007000, "wo")
    mat_list.append(mat)


    # --- PNNL 49: Brick, Fire ---
    mat = openmc.Material(material_id=49, name="Brick, Fire")
    mat.set_density("g/cc", 2.1)
    mat.add_nuclide("O16", 0.495653, "wo")
    mat.add_nuclide("O17", 0.000201, "wo")
    mat.add_nuclide("O18", 0.001146, "wo")
    mat.add_element("Mg", 0.006000, "wo")
    mat.add_nuclide("Al27", 0.212000, "wo")
    mat.add_element("Si", 0.252000, "wo")
    mat.add_element("Ca", 0.007000, "wo")
    mat.add_element("Ti", 0.012000, "wo")
    mat.add_element("Fe", 0.014000, "wo")
    mat_list.append(mat)


    # --- PNNL 50: Brick, Kaolin (white) ---
    mat = openmc.Material(material_id=50, name="Brick, Kaolin (white)")
    mat.set_density("g/cc", 2.1)
    mat.add_nuclide("O16", 0.498963, "wo")
    mat.add_nuclide("O17", 0.000202, "wo")
    mat.add_nuclide("O18", 0.001154, "wo")
    mat.add_element("Mg", 0.001205, "wo")
    mat.add_nuclide("Al27", 0.240568, "wo")
    mat.add_element("Si", 0.242823, "wo")
    mat.add_element("Ca", 0.000714, "wo")
    mat.add_element("Ti", 0.010179, "wo")
    mat.add_element("Fe", 0.004192, "wo")
    mat_list.append(mat)


    # --- PNNL 51: Bronze (typical composition) ---
    mat = openmc.Material(material_id=51, name="Bronze (typical composition)")
    mat.set_density("g/cc", 8.4)
    mat.add_nuclide("Al27", 0.028528, "wo")
    mat.add_element("Si", 0.003339, "wo")
    mat.add_nuclide("Mn55", 0.003555, "wo")
    mat.add_element("Fe", 0.010208, "wo")
    mat.add_element("Ni", 0.006718, "wo")
    mat.add_element("Cu", 0.874155, "wo")
    mat.add_element("Zn", 0.036037, "wo")
    mat.add_element("Sn", 0.024503, "wo")
    mat.add_element("Pb", 0.012957, "wo")
    mat_list.append(mat)


    # --- PNNL 52: C-552 Air-Equivalent Plastic ---
    mat = openmc.Material(material_id=52, name="C-552 Air-Equivalent Plastic")
    mat.set_density("g/cc", 1.76)
    mat.add_nuclide("H1", 0.024674, "wo")
    mat.add_nuclide("H2", 0.000006, "wo")
    mat.add_element("C", 0.501611, "wo")
    mat.add_nuclide("O16", 0.004515, "wo")
    mat.add_nuclide("O17", 0.000002, "wo")
    mat.add_nuclide("O18", 0.000010, "wo")
    mat.add_nuclide("F19", 0.465209, "wo")
    mat.add_element("Si", 0.003973, "wo")
    mat_list.append(mat)


    # --- PNNL 53: CELOTEX (Lignocellulosic Fiberboard) ---
    mat = openmc.Material(material_id=53, name="CELOTEX (Lignocellulosic Fiberboard)")
    mat.set_density("g/cc", 0.25)
    mat.add_element("C", 0.444452, "wo")
    mat.add_nuclide("H1", 0.062150, "wo")
    mat.add_nuclide("H2", 0.000014, "wo")
    mat.add_nuclide("O16", 0.492044, "wo")
    mat.add_nuclide("O17", 0.000199, "wo")
    mat.add_nuclide("O18", 0.001138, "wo")
    mat_list.append(mat)


    # --- PNNL 54: CLLB(Ce) - Cesium Lithium Lanthanum Bromide - 0.3 wt% Cerium doped ---
    mat = openmc.Material(material_id=54, name="CLLB(Ce) - Cesium Lithium Lanthanum Bromide - 0.3 wt% Cerium doped")
    mat.set_density("g/cc", 4.2)
    mat.add_nuclide("Cs133", 0.298151, "wo")
    mat.add_nuclide("Li6", 0.000512, "wo")
    mat.add_nuclide("Li7", 0.007272, "wo")
    mat.add_nuclide("La138", 0.000137, "wo")
    mat.add_nuclide("La139", 0.155668, "wo")
    mat.add_nuclide("Br79", 0.269225, "wo")
    mat.add_nuclide("Br81", 0.268526, "wo")
    mat.add_nuclide("Ce136", 0.000001, "wo")
    mat.add_nuclide("Ce138", 0.000001, "wo")
    mat.add_nuclide("Ce140", 0.000418, "wo")
    mat.add_nuclide("Ce142", 0.000053, "wo")
    mat_list.append(mat)


    # --- PNNL 55: Cadmium ---
    mat = openmc.Material(material_id=55, name="Cadmium")
    mat.set_density("g/cc", 8.65)
    mat.add_nuclide("Cd106", 0.011776, "wo")
    mat.add_nuclide("Cd108", 0.008543, "wo")
    mat.add_nuclide("Cd110", 0.122110, "wo")
    mat.add_nuclide("Cd111", 0.126281, "wo")
    mat.add_nuclide("Cd112", 0.240203, "wo")
    mat.add_nuclide("Cd113", 0.122733, "wo")
    mat.add_nuclide("Cd114", 0.291106, "wo")
    mat.add_nuclide("Cd116", 0.077226, "wo")
    mat_list.append(mat)


    # --- PNNL 56: Cadmium Nitrate Tetrahydrate ---
    mat = openmc.Material(material_id=56, name="Cadmium Nitrate Tetrahydrate")
    mat.set_density("g/cc", 2.45)
    mat.add_nuclide("H1", 0.026133, "wo")
    mat.add_nuclide("H2", 0.000006, "wo")
    mat.add_nuclide("N14", 0.090455, "wo")
    mat.add_nuclide("N15", 0.000354, "wo")
    mat.add_nuclide("O16", 0.517239, "wo")
    mat.add_nuclide("O17", 0.000209, "wo")
    mat.add_nuclide("O18", 0.001196, "wo")
    mat.add_nuclide("Cd106", 0.004291, "wo")
    mat.add_nuclide("Cd108", 0.003113, "wo")
    mat.add_nuclide("Cd110", 0.044498, "wo")
    mat.add_nuclide("Cd111", 0.046018, "wo")
    mat.add_nuclide("Cd112", 0.087531, "wo")
    mat.add_nuclide("Cd113", 0.044725, "wo")
    mat.add_nuclide("Cd114", 0.106081, "wo")
    mat.add_nuclide("Cd116", 0.028142, "wo")
    mat_list.append(mat)


    # --- PNNL 57: Cadmium Telluride ---
    mat = openmc.Material(material_id=57, name="Cadmium Telluride")
    mat.set_density("g/cc", 6.2)
    mat.add_nuclide("Cd106", 0.005516, "wo")
    mat.add_nuclide("Cd108", 0.004001, "wo")
    mat.add_nuclide("Cd110", 0.057192, "wo")
    mat.add_nuclide("Cd111", 0.059145, "wo")
    mat.add_nuclide("Cd112", 0.112502, "wo")
    mat.add_nuclide("Cd113", 0.057484, "wo")
    mat.add_nuclide("Cd114", 0.136344, "wo")
    mat.add_nuclide("Cd116", 0.036170, "wo")
    mat.add_nuclide("Te120", 0.000450, "wo")
    mat.add_nuclide("Te122", 0.012951, "wo")
    mat.add_nuclide("Te123", 0.004557, "wo")
    mat.add_nuclide("Te124", 0.024469, "wo")
    mat.add_nuclide("Te125", 0.036793, "wo")
    mat.add_nuclide("Te126", 0.098828, "wo")
    mat.add_nuclide("Te128", 0.169144, "wo")
    mat.add_nuclide("Te130", 0.184456, "wo")
    mat_list.append(mat)


    # --- PNNL 58: Cadmium Tungstate (CWO) ---
    mat = openmc.Material(material_id=58, name="Cadmium Tungstate (CWO)")
    mat.set_density("g/cc", 7.9)
    mat.add_nuclide("O16", 0.177166, "wo")
    mat.add_nuclide("O17", 0.000072, "wo")
    mat.add_nuclide("O18", 0.000410, "wo")
    mat.add_nuclide("Cd106", 0.003675, "wo")
    mat.add_nuclide("Cd108", 0.002666, "wo")
    mat.add_nuclide("Cd110", 0.038104, "wo")
    mat.add_nuclide("Cd111", 0.039405, "wo")
    mat.add_nuclide("Cd112", 0.074954, "wo")
    mat.add_nuclide("Cd113", 0.038298, "wo")
    mat.add_nuclide("Cd114", 0.090838, "wo")
    mat.add_nuclide("Cd116", 0.024098, "wo")
    mat.add_element("W", 0.510310, "wo")
    mat_list.append(mat)


    # --- PNNL 59: Cadmium Zinc Telluride (CZT) ---
    mat = openmc.Material(material_id=59, name="Cadmium Zinc Telluride (CZT)")
    mat.set_density("g/cc", 5.78)
    mat.add_nuclide("Cd106", 0.004335, "wo")
    mat.add_nuclide("Cd108", 0.003145, "wo")
    mat.add_nuclide("Cd110", 0.044948, "wo")
    mat.add_nuclide("Cd111", 0.046483, "wo")
    mat.add_nuclide("Cd112", 0.088417, "wo")
    mat.add_nuclide("Cd113", 0.045177, "wo")
    mat.add_nuclide("Cd114", 0.107155, "wo")
    mat.add_nuclide("Cd116", 0.028426, "wo")
    mat.add_element("Zn", 0.214084, "wo")
    mat.add_nuclide("Te120", 0.000353, "wo")
    mat.add_nuclide("Te122", 0.010179, "wo")
    mat.add_nuclide("Te123", 0.003582, "wo")
    mat.add_nuclide("Te124", 0.019231, "wo")
    mat.add_nuclide("Te125", 0.028916, "wo")
    mat.add_nuclide("Te126", 0.077671, "wo")
    mat.add_nuclide("Te128", 0.132933, "wo")
    mat.add_nuclide("Te130", 0.144967, "wo")
    mat_list.append(mat)


    # --- PNNL 60: Calcium Carbonate ---
    mat = openmc.Material(material_id=60, name="Calcium Carbonate")
    mat.set_density("g/cc", 2.8)
    mat.add_element("C", 0.120002, "wo")
    mat.add_nuclide("O16", 0.478266, "wo")
    mat.add_nuclide("O17", 0.000194, "wo")
    mat.add_nuclide("O18", 0.001106, "wo")
    mat.add_element("Ca", 0.400432, "wo")
    mat_list.append(mat)


    # --- PNNL 61: Calcium Fluoride ---
    mat = openmc.Material(material_id=61, name="Calcium Fluoride")
    mat.set_density("g/cc", 3.18)
    mat.add_nuclide("F19", 0.486672, "wo")
    mat.add_element("Ca", 0.513328, "wo")
    mat_list.append(mat)


    # --- PNNL 62: Calcium Oxide ---
    mat = openmc.Material(material_id=62, name="Calcium Oxide")
    mat.set_density("g/cc", 3.3)
    mat.add_nuclide("O16", 0.284536, "wo")
    mat.add_nuclide("O17", 0.000115, "wo")
    mat.add_nuclide("O18", 0.000658, "wo")
    mat.add_element("Ca", 0.714691, "wo")
    mat_list.append(mat)


    # --- PNNL 63: Calcium Sulfate ---
    mat = openmc.Material(material_id=63, name="Calcium Sulfate")
    mat.set_density("g/cc", 2.96)
    mat.add_nuclide("O16", 0.468802, "wo")
    mat.add_nuclide("O17", 0.000190, "wo")
    mat.add_nuclide("O18", 0.001084, "wo")
    mat.add_element("S", 0.235543, "wo")
    mat.add_element("Ca", 0.294381, "wo")
    mat_list.append(mat)


    # --- PNNL 64: Calcium Tungstate ---
    mat = openmc.Material(material_id=64, name="Calcium Tungstate")
    mat.set_density("g/cc", 7.9)
    mat.add_element("Ca", 0.139201, "wo")
    mat.add_element("W", 0.638520, "wo")
    mat.add_nuclide("O16", 0.221677, "wo")
    mat.add_nuclide("O17", 0.000090, "wo")
    mat.add_nuclide("O18", 0.000513, "wo")
    mat_list.append(mat)


    # --- PNNL 65: Carbon Dioxide ---
    mat = openmc.Material(material_id=65, name="Carbon Dioxide")
    mat.set_density("g/cc", 0.001842)
    mat.add_element("C", 0.272910, "wo")
    mat.add_nuclide("O16", 0.725120, "wo")
    mat.add_nuclide("O17", 0.000294, "wo")
    mat.add_nuclide("O18", 0.001677, "wo")
    mat_list.append(mat)


    # --- PNNL 66: Carbon Tetrachloride ---
    mat = openmc.Material(material_id=66, name="Carbon Tetrachloride")
    mat.set_density("g/cc", 1.594)
    mat.add_element("C", 0.078084, "wo")
    mat.add_nuclide("Cl35", 0.688935, "wo")
    mat.add_nuclide("Cl37", 0.233019, "wo")
    mat_list.append(mat)


    # --- PNNL 67: Carbon, Activated ---
    mat = openmc.Material(material_id=67, name="Carbon, Activated")
    mat.set_density("g/cc", 0.45)
    mat.add_nuclide("B10", 0.000000, "wo")
    mat.add_nuclide("B11", 0.000001, "wo")
    mat.add_element("C", 0.999999, "wo")
    mat_list.append(mat)


    # --- PNNL 68: Carbon, Amorphous ---
    mat = openmc.Material(material_id=68, name="Carbon, Amorphous")
    mat.set_density("g/cc", 2.0)
    mat.add_nuclide("B10", 0.000000, "wo")
    mat.add_nuclide("B11", 0.000001, "wo")
    mat.add_element("C", 0.999999, "wo")
    mat_list.append(mat)


    # --- PNNL 69: Carbon, Graphite (reactor grade) ---
    mat = openmc.Material(material_id=69, name="Carbon, Graphite (reactor grade)")
    mat.set_density("g/cc", 1.7)
    mat.add_nuclide("B10", 0.000000, "wo")
    mat.add_nuclide("B11", 0.000001, "wo")
    mat.add_element("C", 0.999999, "wo")
    mat_list.append(mat)


    # --- PNNL 70: Cat litter (clumping) ---
    mat = openmc.Material(material_id=70, name="Cat litter (clumping)")
    mat.set_density("g/cc", 1.1)
    mat.add_nuclide("H1", 0.040385, "wo")
    mat.add_nuclide("H2", 0.000009, "wo")
    mat.add_nuclide("O16", 0.639299, "wo")
    mat.add_nuclide("O17", 0.000259, "wo")
    mat.add_nuclide("O18", 0.001478, "wo")
    mat.add_nuclide("Na23", 0.008399, "wo")
    mat.add_nuclide("Al27", 0.098290, "wo")
    mat.add_element("Si", 0.204580, "wo")
    mat.add_element("Ca", 0.007299, "wo")
    mat_list.append(mat)


    # --- PNNL 71: Cat litter (non-clumping) ---
    mat = openmc.Material(material_id=71, name="Cat litter (non-clumping)")
    mat.set_density("g/cc", 0.8)
    mat.add_nuclide("H1", 0.013726, "wo")
    mat.add_nuclide("H2", 0.000003, "wo")
    mat.add_nuclide("O16", 0.538452, "wo")
    mat.add_nuclide("O17", 0.000218, "wo")
    mat.add_nuclide("O18", 0.001245, "wo")
    mat.add_nuclide("Na23", 0.043270, "wo")
    mat.add_element("Mg", 0.050469, "wo")
    mat.add_nuclide("Al27", 0.052129, "wo")
    mat.add_element("Si", 0.293187, "wo")
    mat.add_element("K", 0.003770, "wo")
    mat.add_element("Ca", 0.001340, "wo")
    mat.add_element("Fe", 0.002190, "wo")
    mat_list.append(mat)


    # --- PNNL 72: Cellulose ---
    mat = openmc.Material(material_id=72, name="Cellulose")
    mat.set_density("g/cc", 1.5)
    mat.add_nuclide("H1", 0.062150, "wo")
    mat.add_nuclide("H2", 0.000014, "wo")
    mat.add_element("C", 0.444452, "wo")
    mat.add_nuclide("O16", 0.492044, "wo")
    mat.add_nuclide("O17", 0.000199, "wo")
    mat.add_nuclide("O18", 0.001138, "wo")
    mat_list.append(mat)


    # --- PNNL 73: Cellulose Acetate ---
    mat = openmc.Material(material_id=73, name="Cellulose Acetate")
    mat.set_density("g/cc", 1.42)
    mat.add_nuclide("H1", 0.062148, "wo")
    mat.add_nuclide("H2", 0.000014, "wo")
    mat.add_element("C", 0.444459, "wo")
    mat.add_nuclide("O16", 0.492039, "wo")
    mat.add_nuclide("O17", 0.000199, "wo")
    mat.add_nuclide("O18", 0.001138, "wo")
    mat_list.append(mat)


    # --- PNNL 74: Ceric Sulfate Dosimeter Solution ---
    mat = openmc.Material(material_id=74, name="Ceric Sulfate Dosimeter Solution")
    mat.set_density("g/cc", 1.03)
    mat.add_nuclide("H1", 0.107568, "wo")
    mat.add_nuclide("H2", 0.000025, "wo")
    mat.add_nuclide("N14", 0.000797, "wo")
    mat.add_nuclide("N15", 0.000003, "wo")
    mat.add_nuclide("O16", 0.872605, "wo")
    mat.add_nuclide("O17", 0.000353, "wo")
    mat.add_nuclide("O18", 0.002018, "wo")
    mat.add_element("S", 0.014627, "wo")
    mat.add_nuclide("Ce136", 0.000004, "wo")
    mat.add_nuclide("Ce138", 0.000005, "wo")
    mat.add_nuclide("Ce140", 0.001767, "wo")
    mat.add_nuclide("Ce142", 0.000225, "wo")
    mat_list.append(mat)


    # --- PNNL 75: Cerium Bromide ---
    mat = openmc.Material(material_id=75, name="Cerium Bromide")
    mat.set_density("g/cc", 5.2)
    mat.add_nuclide("Ce136", 0.000662, "wo")
    mat.add_nuclide("Ce138", 0.000911, "wo")
    mat.add_nuclide("Ce140", 0.325796, "wo")
    mat.add_nuclide("Ce142", 0.041524, "wo")
    mat.add_nuclide("Br79", 0.315962, "wo")
    mat.add_nuclide("Br81", 0.315141, "wo")
    mat_list.append(mat)


    # --- PNNL 76: Cerium Fluoride ---
    mat = openmc.Material(material_id=76, name="Cerium Fluoride")
    mat.set_density("g/cc", 6.16)
    mat.add_nuclide("F19", 0.289153, "wo")
    mat.add_nuclide("Ce136", 0.001276, "wo")
    mat.add_nuclide("Ce138", 0.001756, "wo")
    mat.add_nuclide("Ce140", 0.627800, "wo")
    mat.add_nuclide("Ce142", 0.080015, "wo")
    mat_list.append(mat)


    # --- PNNL 77: Cesium Iodide - 1 wt% Sodium doped ---
    mat = openmc.Material(material_id=77, name="Cesium Iodide - 1 wt% Sodium doped")
    mat.set_density("g/cc", 4.51)
    mat.add_nuclide("Cs133", 0.511097, "wo")
    mat.add_nuclide("I127", 0.488019, "wo")
    mat.add_nuclide("Na23", 0.000884, "wo")
    mat_list.append(mat)


    # --- PNNL 78: Cesium Iodide - 1 wt% Thalium doped ---
    mat = openmc.Material(material_id=78, name="Cesium Iodide - 1 wt% Thalium doped")
    mat.set_density("g/cc", 4.51)
    mat.add_nuclide("Cs133", 0.507556, "wo")
    mat.add_nuclide("I127", 0.484639, "wo")
    mat.add_nuclide("Tl203", 0.002288, "wo")
    mat.add_nuclide("Tl205", 0.005517, "wo")
    mat_list.append(mat)


    # --- PNNL 79: Cesium Lithium Yttrium Chloride (CLYC) ---
    mat = openmc.Material(material_id=79, name="Cesium Lithium Yttrium Chloride (CLYC)")
    mat.set_density("g/cc", 3.31)
    mat.add_nuclide("Cs133", 0.462768, "wo")
    mat.add_nuclide("Li6", 0.000795, "wo")
    mat.add_nuclide("Li7", 0.011288, "wo")
    mat.add_nuclide("Y89", 0.154782, "wo")
    mat.add_nuclide("Cl35", 0.276734, "wo")
    mat.add_nuclide("Cl37", 0.093600, "wo")
    mat_list.append(mat)


    # --- PNNL 80: Cesium Lithium Yttrium Chloride (CLYC) with 95% Li6 Enrichment ---
    mat = openmc.Material(material_id=80, name="Cesium Lithium Yttrium Chloride (CLYC) with 95% Li6 Enrichment")
    mat.set_density("g/cc", 3.31)
    mat.add_nuclide("Cs133", 0.463502, "wo")
    mat.add_nuclide("Li6", 0.010036, "wo")
    mat.add_nuclide("Li7", 0.000528, "wo")
    mat.add_nuclide("Y89", 0.155028, "wo")
    mat.add_nuclide("Cl35", 0.277173, "wo")
    mat.add_nuclide("Cl37", 0.093748, "wo")
    mat_list.append(mat)


    # --- PNNL 81: Chromium ---
    mat = openmc.Material(material_id=81, name="Chromium")
    mat.set_density("g/cc", 7.18)
    mat.add_element("Cr", 1.000000, "wo")
    mat_list.append(mat)


    # --- PNNL 82: Clay ---
    mat = openmc.Material(material_id=82, name="Clay")
    mat.set_density("g/cc", 2.2)
    mat.add_nuclide("O16", 0.483035, "wo")
    mat.add_nuclide("O17", 0.000196, "wo")
    mat.add_nuclide("O18", 0.001117, "wo")
    mat.add_nuclide("Na23", 0.007608, "wo")
    mat.add_element("Mg", 0.010691, "wo")
    mat.add_nuclide("Al27", 0.122125, "wo")
    mat.add_element("Si", 0.294195, "wo")
    mat.add_nuclide("P31", 0.000113, "wo")
    mat.add_element("K", 0.020427, "wo")
    mat.add_element("Ca", 0.018957, "wo")
    mat.add_element("Ti", 0.004668, "wo")
    mat.add_nuclide("Mn55", 0.000064, "wo")
    mat.add_element("Fe", 0.036804, "wo")
    mat_list.append(mat)

    return {m.id: m for m in mat_list}

test = get_pnnl_mats()
