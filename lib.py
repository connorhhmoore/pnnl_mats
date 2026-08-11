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


    # --- PNNL 83: Coal, Anthracite ---
    mat = openmc.Material(material_id=83, name="Coal, Anthracite")
    mat.set_density("g/cc", 0.84)
    mat.add_nuclide("H1", 0.023994, "wo")
    mat.add_nuclide("H2", 0.000006, "wo")
    mat.add_element("C", 0.937000, "wo")
    mat.add_nuclide("N14", 0.008965, "wo")
    mat.add_nuclide("N15", 0.000035, "wo")
    mat.add_nuclide("O16", 0.023935, "wo")
    mat.add_nuclide("O17", 0.000010, "wo")
    mat.add_nuclide("O18", 0.000055, "wo")
    mat.add_element("S", 0.006000, "wo")
    mat_list.append(mat)


    # --- PNNL 84: Coal, Bituminous ---
    mat = openmc.Material(material_id=84, name="Coal, Bituminous")
    mat.set_density("g/cc", 0.75)
    mat.add_nuclide("H1", 0.055985, "wo")
    mat.add_nuclide("H2", 0.000013, "wo")
    mat.add_element("C", 0.845000, "wo")
    mat.add_nuclide("N14", 0.015937, "wo")
    mat.add_nuclide("N15", 0.000062, "wo")
    mat.add_nuclide("O16", 0.069810, "wo")
    mat.add_nuclide("O17", 0.000028, "wo")
    mat.add_nuclide("O18", 0.000161, "wo")
    mat.add_element("S", 0.013000, "wo")
    mat_list.append(mat)


    # --- PNNL 85: Coal, Lignite ---
    mat = openmc.Material(material_id=85, name="Coal, Lignite")
    mat.set_density("g/cc", 0.75)
    mat.add_nuclide("H1", 0.041989, "wo")
    mat.add_nuclide("H2", 0.000010, "wo")
    mat.add_element("C", 0.727000, "wo")
    mat.add_nuclide("N14", 0.011953, "wo")
    mat.add_nuclide("N15", 0.000047, "wo")
    mat.add_nuclide("O16", 0.212423, "wo")
    mat.add_nuclide("O17", 0.000086, "wo")
    mat.add_nuclide("O18", 0.000491, "wo")
    mat.add_element("S", 0.006000, "wo")
    mat_list.append(mat)


    # --- PNNL 86: Concrete [Los Alamos (MCNP) Mix] ---
    mat = openmc.Material(material_id=86, name="Concrete [Los Alamos (MCNP) Mix]")
    mat.set_density("g/cc", 2.25)
    mat.add_nuclide("H1", 0.004529, "wo")
    mat.add_nuclide("H2", 0.000001, "wo")
    mat.add_nuclide("O16", 0.511211, "wo")
    mat.add_nuclide("O17", 0.000207, "wo")
    mat.add_nuclide("O18", 0.001182, "wo")
    mat.add_element("Si", 0.360360, "wo")
    mat.add_nuclide("Al27", 0.035550, "wo")
    mat.add_nuclide("Na23", 0.015270, "wo")
    mat.add_element("Ca", 0.057910, "wo")
    mat.add_element("Fe", 0.013780, "wo")
    mat_list.append(mat)


    # --- PNNL 87: Concrete, Barite (Type BA) ---
    mat = openmc.Material(material_id=87, name="Concrete, Barite (Type BA)")
    mat.set_density("g/cc", 3.35)
    mat.add_nuclide("H1", 0.003584, "wo")
    mat.add_nuclide("H2", 0.000001, "wo")
    mat.add_nuclide("O16", 0.310778, "wo")
    mat.add_nuclide("O17", 0.000126, "wo")
    mat.add_nuclide("O18", 0.000719, "wo")
    mat.add_element("Mg", 0.001195, "wo")
    mat.add_nuclide("Al27", 0.004183, "wo")
    mat.add_element("Si", 0.010457, "wo")
    mat.add_element("S", 0.107858, "wo")
    mat.add_element("Ca", 0.050194, "wo")
    mat.add_element("Fe", 0.047505, "wo")
    mat.add_nuclide("Ba130", 0.000465, "wo")
    mat.add_nuclide("Ba132", 0.000450, "wo")
    mat.add_nuclide("Ba134", 0.010921, "wo")
    mat.add_nuclide("Ba135", 0.030009, "wo")
    mat.add_nuclide("Ba136", 0.036018, "wo")
    mat.add_nuclide("Ba137", 0.051890, "wo")
    mat.add_nuclide("Ba138", 0.333648, "wo")
    mat_list.append(mat)


    # --- PNNL 88: Concrete, Barytes-Limonite ---
    mat = openmc.Material(material_id=88, name="Concrete, Barytes-Limonite")
    mat.set_density("g/cc", 3.36)
    mat.add_nuclide("H1", 0.010237, "wo")
    mat.add_nuclide("H2", 0.000002, "wo")
    mat.add_nuclide("O16", 0.377450, "wo")
    mat.add_nuclide("O17", 0.000153, "wo")
    mat.add_nuclide("O18", 0.000873, "wo")
    mat.add_nuclide("Na23", 0.000904, "wo")
    mat.add_element("Mg", 0.002309, "wo")
    mat.add_nuclide("Al27", 0.005020, "wo")
    mat.add_element("Si", 0.013553, "wo")
    mat.add_element("S", 0.076097, "wo")
    mat.add_element("Ca", 0.053910, "wo")
    mat.add_nuclide("Mn55", 0.001405, "wo")
    mat.add_element("Fe", 0.137135, "wo")
    mat.add_nuclide("Ba130", 0.000322, "wo")
    mat.add_nuclide("Ba132", 0.000311, "wo")
    mat.add_nuclide("Ba134", 0.007564, "wo")
    mat.add_nuclide("Ba135", 0.020784, "wo")
    mat.add_nuclide("Ba136", 0.024946, "wo")
    mat.add_nuclide("Ba137", 0.035939, "wo")
    mat.add_nuclide("Ba138", 0.231085, "wo")
    mat_list.append(mat)


    # --- PNNL 89: Concrete, Boron Frits-baryte ---
    mat = openmc.Material(material_id=89, name="Concrete, Boron Frits-baryte")
    mat.set_density("g/cc", 3.1)
    mat.add_nuclide("H1", 0.005625, "wo")
    mat.add_nuclide("H2", 0.000001, "wo")
    mat.add_nuclide("B10", 0.001925, "wo")
    mat.add_nuclide("B11", 0.008521, "wo")
    mat.add_nuclide("O16", 0.338676, "wo")
    mat.add_nuclide("O17", 0.000137, "wo")
    mat.add_nuclide("O18", 0.000783, "wo")
    mat.add_nuclide("F19", 0.002311, "wo")
    mat.add_nuclide("Na23", 0.012157, "wo")
    mat.add_element("Mg", 0.002311, "wo")
    mat.add_nuclide("Al27", 0.006430, "wo")
    mat.add_element("Si", 0.033256, "wo")
    mat.add_element("S", 0.091932, "wo")
    mat.add_element("K", 0.001005, "wo")
    mat.add_element("Ca", 0.062896, "wo")
    mat.add_nuclide("Mn55", 0.000201, "wo")
    mat.add_element("Fe", 0.022003, "wo")
    mat.add_element("Zn", 0.006631, "wo")
    mat.add_nuclide("Ba130", 0.000404, "wo")
    mat.add_nuclide("Ba132", 0.000391, "wo")
    mat.add_nuclide("Ba134", 0.009502, "wo")
    mat.add_nuclide("Ba135", 0.026110, "wo")
    mat.add_nuclide("Ba136", 0.031339, "wo")
    mat.add_nuclide("Ba137", 0.045148, "wo")
    mat.add_nuclide("Ba138", 0.290300, "wo")
    mat_list.append(mat)


    # --- PNNL 90: Concrete, Colemanite-baryte ---
    mat = openmc.Material(material_id=90, name="Concrete, Colemanite-baryte")
    mat.set_density("g/cc", 3.2)
    mat.add_nuclide("H1", 0.008562, "wo")
    mat.add_nuclide("H2", 0.000002, "wo")
    mat.add_nuclide("B10", 0.001819, "wo")
    mat.add_nuclide("B11", 0.008052, "wo")
    mat.add_nuclide("O16", 0.350584, "wo")
    mat.add_nuclide("O17", 0.000142, "wo")
    mat.add_nuclide("O18", 0.000811, "wo")
    mat.add_nuclide("Na23", 0.001108, "wo")
    mat.add_element("Mg", 0.002217, "wo")
    mat.add_nuclide("Al27", 0.006146, "wo")
    mat.add_element("Si", 0.017733, "wo")
    mat.add_element("S", 0.097028, "wo")
    mat.add_element("Ca", 0.085239, "wo")
    mat.add_nuclide("Mn55", 0.000101, "wo")
    mat.add_element("Fe", 0.010378, "wo")
    mat.add_nuclide("Ba130", 0.000411, "wo")
    mat.add_nuclide("Ba132", 0.000398, "wo")
    mat.add_nuclide("Ba134", 0.009665, "wo")
    mat.add_nuclide("Ba135", 0.026556, "wo")
    mat.add_nuclide("Ba136", 0.031874, "wo")
    mat.add_nuclide("Ba137", 0.045918, "wo")
    mat.add_nuclide("Ba138", 0.295254, "wo")
    mat_list.append(mat)


    # --- PNNL 91: Concrete, Ferro-phosphorus ---
    mat = openmc.Material(material_id=91, name="Concrete, Ferro-phosphorus")
    mat.set_density("g/cc", 4.8)
    mat.add_nuclide("H1", 0.004999, "wo")
    mat.add_nuclide("H2", 0.000001, "wo")
    mat.add_nuclide("O16", 0.103718, "wo")
    mat.add_nuclide("O17", 0.000042, "wo")
    mat.add_nuclide("O18", 0.000240, "wo")
    mat.add_element("Mg", 0.002000, "wo")
    mat.add_nuclide("Al27", 0.004000, "wo")
    mat.add_element("Si", 0.034000, "wo")
    mat.add_nuclide("P31", 0.197000, "wo")
    mat.add_element("Ca", 0.042000, "wo")
    mat.add_element("Fe", 0.612000, "wo")
    mat_list.append(mat)


    # --- PNNL 92: Concrete, Hanford Dry ---
    mat = openmc.Material(material_id=92, name="Concrete, Hanford Dry")
    mat.set_density("g/cc", 2.18)
    mat.add_nuclide("H1", 0.003999, "wo")
    mat.add_nuclide("H2", 0.000001, "wo")
    mat.add_nuclide("O16", 0.480796, "wo")
    mat.add_nuclide("O17", 0.000195, "wo")
    mat.add_nuclide("O18", 0.001112, "wo")
    mat.add_nuclide("Na23", 0.002168, "wo")
    mat.add_element("Mg", 0.014094, "wo")
    mat.add_nuclide("Al27", 0.069387, "wo")
    mat.add_element("Si", 0.277549, "wo")
    mat.add_element("K", 0.013010, "wo")
    mat.add_element("Ca", 0.080229, "wo")
    mat.add_element("Fe", 0.057461, "wo")
    mat_list.append(mat)


    # --- PNNL 93: Concrete, Hanford Wet ---
    mat = openmc.Material(material_id=93, name="Concrete, Hanford Wet")
    mat.set_density("g/cc", 2.35)
    mat.add_nuclide("H1", 0.012306, "wo")
    mat.add_nuclide("H2", 0.000003, "wo")
    mat.add_nuclide("O16", 0.511968, "wo")
    mat.add_nuclide("O17", 0.000207, "wo")
    mat.add_nuclide("O18", 0.001184, "wo")
    mat.add_nuclide("Na23", 0.002001, "wo")
    mat.add_element("Mg", 0.013009, "wo")
    mat.add_nuclide("Al27", 0.064045, "wo")
    mat.add_element("Si", 0.256179, "wo")
    mat.add_element("K", 0.012008, "wo")
    mat.add_element("Ca", 0.074052, "wo")
    mat.add_element("Fe", 0.053037, "wo")
    mat_list.append(mat)


    # --- PNNL 94: Concrete, Iron-Portland ---
    mat = openmc.Material(material_id=94, name="Concrete, Iron-Portland")
    mat.set_density("g/cc", 5.9)
    mat.add_nuclide("H1", 0.003320, "wo")
    mat.add_nuclide("H2", 0.000001, "wo")
    mat.add_nuclide("O16", 0.058404, "wo")
    mat.add_nuclide("O17", 0.000024, "wo")
    mat.add_nuclide("O18", 0.000135, "wo")
    mat.add_element("Mg", 0.001308, "wo")
    mat.add_nuclide("Al27", 0.003321, "wo")
    mat.add_element("Si", 0.009157, "wo")
    mat.add_element("S", 0.000503, "wo")
    mat.add_element("Ca", 0.039847, "wo")
    mat.add_nuclide("Mn55", 0.003522, "wo")
    mat.add_element("Fe", 0.880458, "wo")
    mat_list.append(mat)


    # --- PNNL 95: Concrete, Iron-limonite ---
    mat = openmc.Material(material_id=95, name="Concrete, Iron-limonite")
    mat.set_density("g/cc", 4.4)
    mat.add_nuclide("H1", 0.000500, "wo")
    mat.add_nuclide("H2", 0.000000, "wo")
    mat.add_nuclide("O16", 0.179422, "wo")
    mat.add_nuclide("O17", 0.000073, "wo")
    mat.add_nuclide("O18", 0.000415, "wo")
    mat.add_element("Mg", 0.001999, "wo")
    mat.add_nuclide("Al27", 0.004998, "wo")
    mat.add_element("Si", 0.013993, "wo")
    mat.add_element("S", 0.001000, "wo")
    mat.add_element("Ca", 0.060970, "wo")
    mat.add_nuclide("Mn55", 0.015992, "wo")
    mat.add_element("Fe", 0.720638, "wo")
    mat_list.append(mat)


    # --- PNNL 96: Concrete, Limonite and steel ---
    mat = openmc.Material(material_id=96, name="Concrete, Limonite and steel")
    mat.set_density("g/cc", 4.54)
    mat.add_nuclide("H1", 0.006838, "wo")
    mat.add_nuclide("H2", 0.000002, "wo")
    mat.add_nuclide("O16", 0.155799, "wo")
    mat.add_nuclide("O17", 0.000063, "wo")
    mat.add_nuclide("O18", 0.000360, "wo")
    mat.add_element("Mg", 0.001545, "wo")
    mat.add_nuclide("Al27", 0.006399, "wo")
    mat.add_element("Si", 0.014784, "wo")
    mat.add_element("K", 0.000883, "wo")
    mat.add_element("Ca", 0.057590, "wo")
    mat.add_element("V", 0.000883, "wo")
    mat.add_element("Fe", 0.754854, "wo")
    mat_list.append(mat)


    # --- PNNL 97: Concrete, Luminite-Portland-colemanite-baryte ---
    mat = openmc.Material(material_id=97, name="Concrete, Luminite-Portland-colemanite-baryte")
    mat.set_density("g/cc", 3.1)
    mat.add_nuclide("H1", 0.011123, "wo")
    mat.add_nuclide("H2", 0.000003, "wo")
    mat.add_nuclide("B10", 0.001901, "wo")
    mat.add_nuclide("B11", 0.008413, "wo")
    mat.add_nuclide("O16", 0.373009, "wo")
    mat.add_nuclide("O17", 0.000151, "wo")
    mat.add_nuclide("O18", 0.000863, "wo")
    mat.add_nuclide("Na23", 0.001113, "wo")
    mat.add_element("Mg", 0.002023, "wo")
    mat.add_nuclide("Al27", 0.013351, "wo")
    mat.add_element("Si", 0.015070, "wo")
    mat.add_element("S", 0.090724, "wo")
    mat.add_element("Ca", 0.077576, "wo")
    mat.add_element("Ti", 0.000718, "wo")
    mat.add_nuclide("Mn55", 0.000405, "wo")
    mat.add_element("Fe", 0.018914, "wo")
    mat.add_nuclide("Ba130", 0.000386, "wo")
    mat.add_nuclide("Ba132", 0.000373, "wo")
    mat.add_nuclide("Ba134", 0.009065, "wo")
    mat.add_nuclide("Ba135", 0.024909, "wo")
    mat.add_nuclide("Ba136", 0.029897, "wo")
    mat.add_nuclide("Ba137", 0.043071, "wo")
    mat.add_nuclide("Ba138", 0.276942, "wo")
    mat_list.append(mat)


    # --- PNNL 98: Concrete, Luminite-colemanite-baryte ---
    mat = openmc.Material(material_id=98, name="Concrete, Luminite-colemanite-baryte")
    mat.set_density("g/cc", 3.1)
    mat.add_nuclide("H1", 0.010954, "wo")
    mat.add_nuclide("H2", 0.000003, "wo")
    mat.add_nuclide("B10", 0.001630, "wo")
    mat.add_nuclide("B11", 0.007214, "wo")
    mat.add_nuclide("O16", 0.370425, "wo")
    mat.add_nuclide("O17", 0.000150, "wo")
    mat.add_nuclide("O18", 0.000857, "wo")
    mat.add_nuclide("Na23", 0.001106, "wo")
    mat.add_element("Mg", 0.001407, "wo")
    mat.add_nuclide("Al27", 0.017692, "wo")
    mat.add_element("Si", 0.009650, "wo")
    mat.add_element("S", 0.091074, "wo")
    mat.add_element("Ca", 0.055086, "wo")
    mat.add_element("Ti", 0.012766, "wo")
    mat.add_nuclide("Mn55", 0.001206, "wo")
    mat.add_element("Fe", 0.030860, "wo")
    mat.add_nuclide("Ba130", 0.000389, "wo")
    mat.add_nuclide("Ba132", 0.000376, "wo")
    mat.add_nuclide("Ba134", 0.009142, "wo")
    mat.add_nuclide("Ba135", 0.025121, "wo")
    mat.add_nuclide("Ba136", 0.030151, "wo")
    mat.add_nuclide("Ba137", 0.043437, "wo")
    mat.add_nuclide("Ba138", 0.279300, "wo")
    mat_list.append(mat)


    # --- PNNL 99: Concrete, M-1 ---
    mat = openmc.Material(material_id=99, name="Concrete, M-1")
    mat.set_density("g/cc", 4.5)
    mat.add_nuclide("H1", 0.007998, "wo")
    mat.add_nuclide("H2", 0.000002, "wo")
    mat.add_nuclide("B10", 0.001658, "wo")
    mat.add_nuclide("B11", 0.007340, "wo")
    mat.add_nuclide("O16", 0.106710, "wo")
    mat.add_nuclide("O17", 0.000043, "wo")
    mat.add_nuclide("O18", 0.000247, "wo")
    mat.add_element("Mg", 0.043000, "wo")
    mat.add_nuclide("Cl35", 0.015693, "wo")
    mat.add_nuclide("Cl37", 0.005308, "wo")
    mat.add_nuclide("Mn55", 0.003000, "wo")
    mat.add_element("Ca", 0.011000, "wo")
    mat.add_element("Fe", 0.798000, "wo")
    mat_list.append(mat)


    # --- PNNL 100: Concrete, MO ---
    mat = openmc.Material(material_id=100, name="Concrete, MO")
    mat.set_density("g/cc", 5.5)
    mat.add_nuclide("H1", 0.004999, "wo")
    mat.add_nuclide("H2", 0.000001, "wo")
    mat.add_nuclide("O16", 0.059837, "wo")
    mat.add_nuclide("O17", 0.000024, "wo")
    mat.add_nuclide("O18", 0.000138, "wo")
    mat.add_element("Mg", 0.037000, "wo")
    mat.add_nuclide("Mn55", 0.004000, "wo")
    mat.add_nuclide("Cl35", 0.009715, "wo")
    mat.add_nuclide("Cl37", 0.003286, "wo")
    mat.add_element("Fe", 0.881000, "wo")
    mat_list.append(mat)


    # --- PNNL 101: Concrete, Magnetite ---
    mat = openmc.Material(material_id=101, name="Concrete, Magnetite")
    mat.set_density("g/cc", 3.53)
    mat.add_nuclide("H1", 0.003112, "wo")
    mat.add_nuclide("H2", 0.000001, "wo")
    mat.add_nuclide("O16", 0.329608, "wo")
    mat.add_nuclide("O17", 0.000133, "wo")
    mat.add_nuclide("O18", 0.000762, "wo")
    mat.add_element("Mg", 0.009338, "wo")
    mat.add_nuclide("Al27", 0.023486, "wo")
    mat.add_element("Si", 0.025750, "wo")
    mat.add_element("S", 0.001415, "wo")
    mat.add_element("Ca", 0.071024, "wo")
    mat.add_element("Ti", 0.054329, "wo")
    mat.add_element("V", 0.003113, "wo")
    mat.add_element("Cr", 0.001698, "wo")
    mat.add_nuclide("Mn55", 0.001981, "wo")
    mat.add_element("Fe", 0.474250, "wo")
    mat_list.append(mat)


    # --- PNNL 102: Concrete, Magnetite and steel ---
    mat = openmc.Material(material_id=102, name="Concrete, Magnetite and steel")
    mat.set_density("g/cc", 4.64)
    mat.add_nuclide("H1", 0.002373, "wo")
    mat.add_nuclide("H2", 0.000001, "wo")
    mat.add_nuclide("O16", 0.137305, "wo")
    mat.add_nuclide("O17", 0.000056, "wo")
    mat.add_nuclide("O18", 0.000318, "wo")
    mat.add_element("Mg", 0.003669, "wo")
    mat.add_nuclide("Al27", 0.010358, "wo")
    mat.add_element("Si", 0.015753, "wo")
    mat.add_element("Ca", 0.055675, "wo")
    mat.add_element("Ti", 0.015969, "wo")
    mat.add_element("V", 0.000647, "wo")
    mat.add_element("Fe", 0.757877, "wo")
    mat_list.append(mat)


    # --- PNNL 103: Concrete, Magnuson's ---
    mat = openmc.Material(material_id=103, name="Concrete, Magnuson's")
    mat.set_density("g/cc", 2.147)
    mat.add_nuclide("H1", 0.003318, "wo")
    mat.add_nuclide("H2", 0.000001, "wo")
    mat.add_element("C", 0.105320, "wo")
    mat.add_nuclide("O16", 0.498074, "wo")
    mat.add_nuclide("O17", 0.000202, "wo")
    mat.add_nuclide("O18", 0.001152, "wo")
    mat.add_nuclide("Na23", 0.001411, "wo")
    mat.add_element("Mg", 0.094200, "wo")
    mat.add_nuclide("Al27", 0.007859, "wo")
    mat.add_element("Si", 0.042101, "wo")
    mat.add_element("S", 0.002483, "wo")
    mat.add_nuclide("Cl35", 0.000391, "wo")
    mat.add_nuclide("Cl37", 0.000132, "wo")
    mat.add_element("K", 0.009445, "wo")
    mat.add_element("Ca", 0.226317, "wo")
    mat.add_element("Ti", 0.001488, "wo")
    mat.add_nuclide("Mn55", 0.000512, "wo")
    mat.add_element("Fe", 0.005595, "wo")
    mat_list.append(mat)


    # --- PNNL 104: Concrete, Oak Ridge (ORNL) ---
    mat = openmc.Material(material_id=104, name="Concrete, Oak Ridge (ORNL)")
    mat.set_density("g/cc", 2.2994)
    mat.add_nuclide("H1", 0.006185, "wo")
    mat.add_nuclide("H2", 0.000001, "wo")
    mat.add_element("C", 0.175193, "wo")
    mat.add_nuclide("O16", 0.409071, "wo")
    mat.add_nuclide("O17", 0.000166, "wo")
    mat.add_nuclide("O18", 0.000946, "wo")
    mat.add_nuclide("Na23", 0.000271, "wo")
    mat.add_element("Mg", 0.032649, "wo")
    mat.add_nuclide("Al27", 0.010830, "wo")
    mat.add_element("Si", 0.034479, "wo")
    mat.add_element("K", 0.001138, "wo")
    mat.add_element("Ca", 0.321286, "wo")
    mat.add_element("Fe", 0.007784, "wo")
    mat_list.append(mat)


    # --- PNNL 105: Concrete, Ordinary (NBS 03) ---
    mat = openmc.Material(material_id=105, name="Concrete, Ordinary (NBS 03)")
    mat.set_density("g/cc", 2.35)
    mat.add_nuclide("H1", 0.008483, "wo")
    mat.add_nuclide("H2", 0.000002, "wo")
    mat.add_element("C", 0.050064, "wo")
    mat.add_nuclide("O16", 0.472200, "wo")
    mat.add_nuclide("O17", 0.000191, "wo")
    mat.add_nuclide("O18", 0.001092, "wo")
    mat.add_element("Mg", 0.024183, "wo")
    mat.add_nuclide("Al27", 0.036063, "wo")
    mat.add_element("Si", 0.145100, "wo")
    mat.add_element("S", 0.002970, "wo")
    mat.add_element("K", 0.001697, "wo")
    mat.add_element("Ca", 0.246924, "wo")
    mat.add_element("Fe", 0.011031, "wo")
    mat_list.append(mat)


    # --- PNNL 106: Concrete, Ordinary (NBS 04) ---
    mat = openmc.Material(material_id=106, name="Concrete, Ordinary (NBS 04)")
    mat.set_density("g/cc", 2.35)
    mat.add_nuclide("H1", 0.005557, "wo")
    mat.add_nuclide("H2", 0.000001, "wo")
    mat.add_nuclide("O16", 0.496727, "wo")
    mat.add_nuclide("O17", 0.000201, "wo")
    mat.add_nuclide("O18", 0.001149, "wo")
    mat.add_nuclide("Na23", 0.017101, "wo")
    mat.add_element("Mg", 0.002565, "wo")
    mat.add_nuclide("Al27", 0.045746, "wo")
    mat.add_element("Si", 0.315092, "wo")
    mat.add_element("S", 0.001283, "wo")
    mat.add_element("K", 0.019239, "wo")
    mat.add_element("Ca", 0.082941, "wo")
    mat.add_element("Fe", 0.012398, "wo")
    mat_list.append(mat)


    # --- PNNL 107: Concrete, Ordinary (NIST) ---
    mat = openmc.Material(material_id=107, name="Concrete, Ordinary (NIST)")
    mat.set_density("g/cc", 2.3)
    mat.add_nuclide("H1", 0.022094, "wo")
    mat.add_nuclide("H2", 0.000005, "wo")
    mat.add_element("C", 0.002484, "wo")
    mat.add_nuclide("O16", 0.573373, "wo")
    mat.add_nuclide("O17", 0.000232, "wo")
    mat.add_nuclide("O18", 0.001326, "wo")
    mat.add_nuclide("Na23", 0.015208, "wo")
    mat.add_element("Mg", 0.001266, "wo")
    mat.add_nuclide("Al27", 0.019953, "wo")
    mat.add_element("Si", 0.304627, "wo")
    mat.add_element("K", 0.010045, "wo")
    mat.add_element("Ca", 0.042951, "wo")
    mat.add_element("Fe", 0.006435, "wo")
    mat_list.append(mat)


    # --- PNNL 108: Concrete, Portland ---
    mat = openmc.Material(material_id=108, name="Concrete, Portland")
    mat.set_density("g/cc", 2.3)
    mat.add_nuclide("H1", 0.009997, "wo")
    mat.add_nuclide("H2", 0.000002, "wo")
    mat.add_element("C", 0.001000, "wo")
    mat.add_nuclide("O16", 0.527673, "wo")
    mat.add_nuclide("O17", 0.000214, "wo")
    mat.add_nuclide("O18", 0.001220, "wo")
    mat.add_nuclide("Na23", 0.016000, "wo")
    mat.add_element("Mg", 0.002000, "wo")
    mat.add_nuclide("Al27", 0.033872, "wo")
    mat.add_element("Si", 0.337021, "wo")
    mat.add_element("K", 0.013000, "wo")
    mat.add_element("Ca", 0.044000, "wo")
    mat.add_element("Fe", 0.014000, "wo")
    mat_list.append(mat)


    # --- PNNL 109: Concrete, Regulatory Concrete (developed for U.S. NRC) ---
    mat = openmc.Material(material_id=109, name="Concrete, Regulatory Concrete (developed for U.S. NRC)")
    mat.set_density("g/cc", 2.3)
    mat.add_nuclide("H1", 0.009997, "wo")
    mat.add_nuclide("H2", 0.000002, "wo")
    mat.add_nuclide("O16", 0.530558, "wo")
    mat.add_nuclide("O17", 0.000215, "wo")
    mat.add_nuclide("O18", 0.001227, "wo")
    mat.add_nuclide("Na23", 0.029000, "wo")
    mat.add_nuclide("Al27", 0.034000, "wo")
    mat.add_element("Si", 0.337000, "wo")
    mat.add_element("Ca", 0.044000, "wo")
    mat.add_element("Fe", 0.014000, "wo")
    mat_list.append(mat)


    # --- PNNL 110: Concrete, Rocky Flats ---
    mat = openmc.Material(material_id=110, name="Concrete, Rocky Flats")
    mat.set_density("g/cc", 2.321)
    mat.add_nuclide("H1", 0.007498, "wo")
    mat.add_nuclide("H2", 0.000002, "wo")
    mat.add_element("C", 0.055200, "wo")
    mat.add_nuclide("N14", 0.000199, "wo")
    mat.add_nuclide("N15", 0.000001, "wo")
    mat.add_nuclide("O16", 0.483586, "wo")
    mat.add_nuclide("O17", 0.000196, "wo")
    mat.add_nuclide("O18", 0.001118, "wo")
    mat.add_nuclide("Na23", 0.006300, "wo")
    mat.add_element("Mg", 0.012500, "wo")
    mat.add_nuclide("Al27", 0.021700, "wo")
    mat.add_element("Si", 0.155000, "wo")
    mat.add_element("S", 0.001900, "wo")
    mat.add_element("K", 0.013700, "wo")
    mat.add_element("Ca", 0.230000, "wo")
    mat.add_element("Ti", 0.001000, "wo")
    mat.add_element("Fe", 0.010100, "wo")
    mat_list.append(mat)


    # --- PNNL 111: Concrete, Serpentine ---
    mat = openmc.Material(material_id=111, name="Concrete, Serpentine")
    mat.set_density("g/cc", 2.1)
    mat.add_nuclide("H1", 0.015905, "wo")
    mat.add_nuclide("H2", 0.000004, "wo")
    mat.add_element("C", 0.000909, "wo")
    mat.add_nuclide("O16", 0.510432, "wo")
    mat.add_nuclide("O17", 0.000207, "wo")
    mat.add_nuclide("O18", 0.001180, "wo")
    mat.add_nuclide("Na23", 0.004092, "wo")
    mat.add_element("Mg", 0.135003, "wo")
    mat.add_nuclide("Al27", 0.019090, "wo")
    mat.add_element("Si", 0.209087, "wo")
    mat.add_element("K", 0.004091, "wo")
    mat.add_element("Ca", 0.068182, "wo")
    mat.add_element("Cr", 0.000910, "wo")
    mat.add_element("Fe", 0.030908, "wo")
    mat_list.append(mat)


    # --- PNNL 112: Copper ---
    mat = openmc.Material(material_id=112, name="Copper")
    mat.set_density("g/cc", 8.96)
    mat.add_element("Cu", 1.000000, "wo")
    mat_list.append(mat)


    # --- PNNL 113: Diatomaceous Earth ---
    mat = openmc.Material(material_id=113, name="Diatomaceous Earth")
    mat.set_density("g/cc", 0.2563)
    mat.add_nuclide("H1", 0.008954, "wo")
    mat.add_nuclide("H2", 0.000002, "wo")
    mat.add_nuclide("O16", 0.545098, "wo")
    mat.add_nuclide("O17", 0.000221, "wo")
    mat.add_nuclide("O18", 0.001261, "wo")
    mat.add_nuclide("Na23", 0.009896, "wo")
    mat.add_element("Mg", 0.002774, "wo")
    mat.add_nuclide("Al27", 0.015581, "wo")
    mat.add_element("Si", 0.394761, "wo")
    mat.add_element("K", 0.011074, "wo")
    mat.add_element("Ca", 0.003945, "wo")
    mat.add_element("Fe", 0.006434, "wo")
    mat_list.append(mat)


    # --- PNNL 114: Diesel Fuel ---
    mat = openmc.Material(material_id=114, name="Diesel Fuel")
    mat.set_density("g/cc", 0.849)
    mat.add_nuclide("H1", 0.138529, "wo")
    mat.add_nuclide("H2", 0.000032, "wo")
    mat.add_element("C", 0.861435, "wo")
    mat_list.append(mat)


    # --- PNNL 115: Earth, Typical Western U.S. ---
    mat = openmc.Material(material_id=115, name="Earth, Typical Western U.S.")
    mat.set_density("g/cc", 1.52)
    mat.add_nuclide("H1", 0.023828, "wo")
    mat.add_nuclide("H2", 0.000005, "wo")
    mat.add_nuclide("O16", 0.597276, "wo")
    mat.add_nuclide("O17", 0.000242, "wo")
    mat.add_nuclide("O18", 0.001381, "wo")
    mat.add_nuclide("Al27", 0.080446, "wo")
    mat.add_element("Si", 0.296821, "wo")
    mat_list.append(mat)


    # --- PNNL 116: Earth, U.S. Average ---
    mat = openmc.Material(material_id=116, name="Earth, U.S. Average")
    mat.set_density("g/cc", 1.52)
    mat.add_nuclide("O16", 0.512323, "wo")
    mat.add_nuclide("O17", 0.000207, "wo")
    mat.add_nuclide("O18", 0.001185, "wo")
    mat.add_nuclide("Na23", 0.006140, "wo")
    mat.add_element("Mg", 0.013304, "wo")
    mat.add_nuclide("Al27", 0.068564, "wo")
    mat.add_element("Si", 0.271180, "wo")
    mat.add_element("K", 0.014327, "wo")
    mat.add_element("Ca", 0.051166, "wo")
    mat.add_element("Ti", 0.004604, "wo")
    mat.add_nuclide("Mn55", 0.000715, "wo")
    mat.add_element("Fe", 0.056285, "wo")
    mat_list.append(mat)


    # --- PNNL 117: Ethane ---
    mat = openmc.Material(material_id=117, name="Ethane")
    mat.set_density("g/cc", 0.001253)
    mat.add_nuclide("H1", 0.201079, "wo")
    mat.add_nuclide("H2", 0.000046, "wo")
    mat.add_element("C", 0.798868, "wo")
    mat_list.append(mat)


    # --- PNNL 118: Ethyl Acetate ---
    mat = openmc.Material(material_id=118, name="Ethyl Acetate")
    mat.set_density("g/cc", 0.901)
    mat.add_nuclide("H1", 0.091501, "wo")
    mat.add_nuclide("H2", 0.000021, "wo")
    mat.add_element("C", 0.545286, "wo")
    mat.add_nuclide("O16", 0.362205, "wo")
    mat.add_nuclide("O17", 0.000147, "wo")
    mat.add_nuclide("O18", 0.000838, "wo")
    mat_list.append(mat)


    # --- PNNL 119: Ethyl Alcohol ---
    mat = openmc.Material(material_id=119, name="Ethyl Alcohol")
    mat.set_density("g/cc", 0.7893)
    mat.add_nuclide("H1", 0.131245, "wo")
    mat.add_nuclide("H2", 0.000030, "wo")
    mat.add_element("C", 0.521424, "wo")
    mat.add_nuclide("O16", 0.346355, "wo")
    mat.add_nuclide("O17", 0.000140, "wo")
    mat.add_nuclide("O18", 0.000801, "wo")
    mat_list.append(mat)


    # --- PNNL 120: Ethylene ---
    mat = openmc.Material(material_id=120, name="Ethylene")
    mat.set_density("g/cc", 0.001174)
    mat.add_nuclide("H1", 0.143686, "wo")
    mat.add_nuclide("H2", 0.000033, "wo")
    mat.add_element("C", 0.856276, "wo")
    mat_list.append(mat)


    # --- PNNL 121: Ethylene Glycol ---
    mat = openmc.Material(material_id=121, name="Ethylene Glycol")
    mat.set_density("g/cc", 1.114)
    mat.add_nuclide("H1", 0.097414, "wo")
    mat.add_nuclide("H2", 0.000022, "wo")
    mat.add_element("C", 0.387015, "wo")
    mat.add_nuclide("O16", 0.514150, "wo")
    mat.add_nuclide("O17", 0.000208, "wo")
    mat.add_nuclide("O18", 0.001189, "wo")
    mat_list.append(mat)


    # --- PNNL 122: Explosive Compound, AN ---
    mat = openmc.Material(material_id=122, name="Explosive Compound, AN")
    mat.set_density("g/cc", 1.72)
    mat.add_nuclide("H1", 0.050358, "wo")
    mat.add_nuclide("H2", 0.000012, "wo")
    mat.add_nuclide("N14", 0.348612, "wo")
    mat.add_nuclide("N15", 0.001364, "wo")
    mat.add_nuclide("O16", 0.598024, "wo")
    mat.add_nuclide("O17", 0.000242, "wo")
    mat.add_nuclide("O18", 0.001383, "wo")
    mat_list.append(mat)


    # --- PNNL 123: Explosive Compound, EGDN ---
    mat = openmc.Material(material_id=123, name="Explosive Compound, EGDN")
    mat.set_density("g/cc", 1.49)
    mat.add_nuclide("H1", 0.026508, "wo")
    mat.add_nuclide("H2", 0.000006, "wo")
    mat.add_element("C", 0.157969, "wo")
    mat.add_nuclide("N14", 0.183504, "wo")
    mat.add_nuclide("N15", 0.000718, "wo")
    mat.add_nuclide("O16", 0.629581, "wo")
    mat.add_nuclide("O17", 0.000255, "wo")
    mat.add_nuclide("O18", 0.001456, "wo")
    mat_list.append(mat)


    # --- PNNL 124: Explosive Compound, HMX ---
    mat = openmc.Material(material_id=124, name="Explosive Compound, HMX")
    mat.set_density("g/cc", 1.91)
    mat.add_nuclide("H1", 0.027221, "wo")
    mat.add_nuclide("H2", 0.000006, "wo")
    mat.add_element("C", 0.162220, "wo")
    mat.add_nuclide("N14", 0.376885, "wo")
    mat.add_nuclide("N15", 0.001475, "wo")
    mat.add_nuclide("O16", 0.431017, "wo")
    mat.add_nuclide("O17", 0.000174, "wo")
    mat.add_nuclide("O18", 0.000997, "wo")
    mat_list.append(mat)


    # --- PNNL 125: Explosive Compound, NC ---
    mat = openmc.Material(material_id=125, name="Explosive Compound, NC")
    mat.set_density("g/cc", 1.49)
    mat.add_nuclide("H1", 0.029208, "wo")
    mat.add_nuclide("H2", 0.000007, "wo")
    mat.add_element("C", 0.271296, "wo")
    mat.add_nuclide("N14", 0.120802, "wo")
    mat.add_nuclide("N15", 0.000473, "wo")
    mat.add_nuclide("O16", 0.576645, "wo")
    mat.add_nuclide("O17", 0.000233, "wo")
    mat.add_nuclide("O18", 0.001333, "wo")
    mat_list.append(mat)


    # --- PNNL 126: Explosive Compound, NG ---
    mat = openmc.Material(material_id=126, name="Explosive Compound, NG")
    mat.set_density("g/cc", 1.6)
    mat.add_nuclide("H1", 0.022188, "wo")
    mat.add_nuclide("H2", 0.000005, "wo")
    mat.add_element("C", 0.158670, "wo")
    mat.add_nuclide("N14", 0.184319, "wo")
    mat.add_nuclide("N15", 0.000721, "wo")
    mat.add_nuclide("O16", 0.632376, "wo")
    mat.add_nuclide("O17", 0.000256, "wo")
    mat.add_nuclide("O18", 0.001462, "wo")
    mat_list.append(mat)


    # --- PNNL 127: Explosive Compound, PETN ---
    mat = openmc.Material(material_id=127, name="Explosive Compound, PETN")
    mat.set_density("g/cc", 1.77)
    mat.add_nuclide("H1", 0.025501, "wo")
    mat.add_nuclide("H2", 0.000006, "wo")
    mat.add_element("C", 0.189959, "wo")
    mat.add_nuclide("N14", 0.176532, "wo")
    mat.add_nuclide("N15", 0.000691, "wo")
    mat.add_nuclide("O16", 0.605663, "wo")
    mat.add_nuclide("O17", 0.000245, "wo")
    mat.add_nuclide("O18", 0.001401, "wo")
    mat_list.append(mat)


    # --- PNNL 128: Explosive Compound, RDX ---
    mat = openmc.Material(material_id=128, name="Explosive Compound, RDX")
    mat.set_density("g/cc", 1.858)
    mat.add_nuclide("H1", 0.027221, "wo")
    mat.add_nuclide("H2", 0.000006, "wo")
    mat.add_element("C", 0.162220, "wo")
    mat.add_nuclide("N14", 0.376885, "wo")
    mat.add_nuclide("N15", 0.001475, "wo")
    mat.add_nuclide("O16", 0.431017, "wo")
    mat.add_nuclide("O17", 0.000174, "wo")
    mat.add_nuclide("O18", 0.000997, "wo")
    mat_list.append(mat)


    # --- PNNL 129: Explosive Compound, TNT ---
    mat = openmc.Material(material_id=129, name="Explosive Compound, TNT")
    mat.set_density("g/cc", 1.654)
    mat.add_nuclide("H1", 0.022183, "wo")
    mat.add_nuclide("H2", 0.000005, "wo")
    mat.add_element("C", 0.370157, "wo")
    mat.add_nuclide("N14", 0.184283, "wo")
    mat.add_nuclide("N15", 0.000721, "wo")
    mat.add_nuclide("O16", 0.421502, "wo")
    mat.add_nuclide("O17", 0.000171, "wo")
    mat.add_nuclide("O18", 0.000975, "wo")
    mat_list.append(mat)


    # --- PNNL 130: Eye Lens (ICRP) ---
    mat = openmc.Material(material_id=130, name="Eye Lens (ICRP)")
    mat.set_density("g/cc", 1.1)
    mat.add_nuclide("H1", 0.099243, "wo")
    mat.add_nuclide("H2", 0.000023, "wo")
    mat.add_element("C", 0.193710, "wo")
    mat.add_nuclide("N14", 0.053062, "wo")
    mat.add_nuclide("N15", 0.000208, "wo")
    mat.add_nuclide("O16", 0.651980, "wo")
    mat.add_nuclide("O17", 0.000264, "wo")
    mat.add_nuclide("O18", 0.001508, "wo")
    mat_list.append(mat)


    # --- PNNL 131: Felt ---
    mat = openmc.Material(material_id=131, name="Felt")
    mat.set_density("g/cc", 0.185)
    mat.add_nuclide("H1", 0.044188, "wo")
    mat.add_nuclide("H2", 0.000010, "wo")
    mat.add_element("C", 0.434600, "wo")
    mat.add_nuclide("N14", 0.175810, "wo")
    mat.add_nuclide("N15", 0.000688, "wo")
    mat.add_nuclide("O16", 0.343766, "wo")
    mat.add_nuclide("O17", 0.000139, "wo")
    mat.add_nuclide("O18", 0.000795, "wo")
    mat_list.append(mat)


    # --- PNNL 132: Ferric Oxide ---
    mat = openmc.Material(material_id=132, name="Ferric Oxide")
    mat.set_density("g/cc", 5.2)
    mat.add_nuclide("O16", 0.299760, "wo")
    mat.add_nuclide("O17", 0.000121, "wo")
    mat.add_nuclide("O18", 0.000693, "wo")
    mat.add_element("Fe", 0.699426, "wo")
    mat_list.append(mat)


    # --- PNNL 133: Ferrous Sulfate Dosimeter Solution ---
    mat = openmc.Material(material_id=133, name="Ferrous Sulfate Dosimeter Solution")
    mat.set_density("g/cc", 1.024)
    mat.add_nuclide("H1", 0.108230, "wo")
    mat.add_nuclide("H2", 0.000025, "wo")
    mat.add_nuclide("N14", 0.000027, "wo")
    mat.add_nuclide("N15", 0.000000, "wo")
    mat.add_nuclide("O16", 0.876255, "wo")
    mat.add_nuclide("O17", 0.000355, "wo")
    mat.add_nuclide("O18", 0.002026, "wo")
    mat.add_nuclide("Na23", 0.000022, "wo")
    mat.add_element("S", 0.012968, "wo")
    mat.add_nuclide("Cl35", 0.000025, "wo")
    mat.add_nuclide("Cl37", 0.000009, "wo")
    mat.add_element("Fe", 0.000054, "wo")
    mat_list.append(mat)


    # --- PNNL 134: Fertilizer (Muriate of Potash) ---
    mat = openmc.Material(material_id=134, name="Fertilizer (Muriate of Potash)")
    mat.set_density("g/cc", 1.121)
    mat.add_nuclide("H1", 0.000050, "wo")
    mat.add_nuclide("H2", 0.000000, "wo")
    mat.add_nuclide("O16", 0.000716, "wo")
    mat.add_nuclide("O17", 0.000000, "wo")
    mat.add_nuclide("O18", 0.000002, "wo")
    mat.add_nuclide("Na23", 0.008487, "wo")
    mat.add_element("Mg", 0.000206, "wo")
    mat.add_element("S", 0.000159, "wo")
    mat.add_nuclide("Cl35", 0.357144, "wo")
    mat.add_nuclide("Cl37", 0.120797, "wo")
    mat.add_element("K", 0.511852, "wo")
    mat.add_element("Ca", 0.000276, "wo")
    mat.add_nuclide("Br79", 0.000165, "wo")
    mat.add_nuclide("Br81", 0.000165, "wo")
    mat_list.append(mat)


    # --- PNNL 135: Fiberglass, Type C ---
    mat = openmc.Material(material_id=135, name="Fiberglass, Type C")
    mat.set_density("g/cc", 2.54)
    mat.add_nuclide("B10", 0.003424, "wo")
    mat.add_nuclide("B11", 0.015151, "wo")
    mat.add_nuclide("O16", 0.477334, "wo")
    mat.add_nuclide("O17", 0.000193, "wo")
    mat.add_nuclide("O18", 0.001104, "wo")
    mat.add_nuclide("Na23", 0.059171, "wo")
    mat.add_element("Mg", 0.018037, "wo")
    mat.add_nuclide("Al27", 0.021107, "wo")
    mat.add_element("Si", 0.302924, "wo")
    mat.add_element("S", 0.000399, "wo")
    mat.add_element("Ca", 0.099757, "wo")
    mat.add_element("Fe", 0.001395, "wo")
    mat_list.append(mat)


    # --- PNNL 136: Fiberglass, Type E ---
    mat = openmc.Material(material_id=136, name="Fiberglass, Type E")
    mat.set_density("g/cc", 2.57)
    mat.add_nuclide("B10", 0.004202, "wo")
    mat.add_nuclide("B11", 0.018596, "wo")
    mat.add_nuclide("O16", 0.470671, "wo")
    mat.add_nuclide("O17", 0.000191, "wo")
    mat.add_nuclide("O18", 0.001088, "wo")
    mat.add_nuclide("F19", 0.004895, "wo")
    mat.add_nuclide("Na23", 0.007262, "wo")
    mat.add_element("Mg", 0.014759, "wo")
    mat.add_nuclide("Al27", 0.072536, "wo")
    mat.add_element("Si", 0.247102, "wo")
    mat.add_element("K", 0.008127, "wo")
    mat.add_element("Ca", 0.143428, "wo")
    mat.add_element("Ti", 0.004400, "wo")
    mat.add_element("Fe", 0.002739, "wo")
    mat_list.append(mat)


    # --- PNNL 137: Fiberglass, Type R ---
    mat = openmc.Material(material_id=137, name="Fiberglass, Type R")
    mat.set_density("g/cc", 2.52)
    mat.add_nuclide("O16", 0.485405, "wo")
    mat.add_nuclide("O17", 0.000197, "wo")
    mat.add_nuclide("O18", 0.001122, "wo")
    mat.add_element("Mg", 0.036183, "wo")
    mat.add_nuclide("Al27", 0.132313, "wo")
    mat.add_element("Si", 0.280457, "wo")
    mat.add_element("Ca", 0.064322, "wo")
    mat_list.append(mat)


    # --- PNNL 138: Freon-12 ---
    mat = openmc.Material(material_id=138, name="Freon-12")
    mat.set_density("g/cc", 1.12)
    mat.add_element("C", 0.099335, "wo")
    mat.add_nuclide("F19", 0.314256, "wo")
    mat.add_nuclide("Cl35", 0.438215, "wo")
    mat.add_nuclide("Cl37", 0.148218, "wo")
    mat_list.append(mat)


    # --- PNNL 139: Freon-12B2 ---
    mat = openmc.Material(material_id=139, name="Freon-12B2")
    mat.set_density("g/cc", 1.8)
    mat.add_element("C", 0.057244, "wo")
    mat.add_nuclide("F19", 0.181096, "wo")
    mat.add_nuclide("Br79", 0.381323, "wo")
    mat.add_nuclide("Br81", 0.380333, "wo")
    mat_list.append(mat)


    # --- PNNL 140: Freon-13 ---
    mat = openmc.Material(material_id=140, name="Freon-13")
    mat.set_density("g/cc", 0.95)
    mat.add_element("C", 0.114981, "wo")
    mat.add_nuclide("F19", 0.545632, "wo")
    mat.add_nuclide("Cl35", 0.253619, "wo")
    mat.add_nuclide("Cl37", 0.085782, "wo")
    mat_list.append(mat)


    # --- PNNL 141: Freon-13B1 ---
    mat = openmc.Material(material_id=141, name="Freon-13B1")
    mat.set_density("g/cc", 1.5)
    mat.add_element("C", 0.080657, "wo")
    mat.add_nuclide("F19", 0.382750, "wo")
    mat.add_nuclide("Br79", 0.268644, "wo")
    mat.add_nuclide("Br81", 0.267946, "wo")
    mat_list.append(mat)


    # --- PNNL 142: Freon-13I1 ---
    mat = openmc.Material(material_id=142, name="Freon-13I1")
    mat.set_density("g/cc", 1.8)
    mat.add_element("C", 0.061307, "wo")
    mat.add_nuclide("F19", 0.290925, "wo")
    mat.add_nuclide("I127", 0.647768, "wo")
    mat_list.append(mat)


    # --- PNNL 143: GAGG(CE) ---
    mat = openmc.Material(material_id=143, name="GAGG(CE)")
    mat.set_density("g/cc", 6.63)
    mat.add_element("Gd", 0.508969, "wo")
    mat.add_nuclide("Al27", 0.058220, "wo")
    mat.add_element("Ga", 0.225671, "wo")
    mat.add_nuclide("O16", 0.206579, "wo")
    mat.add_nuclide("O17", 0.000084, "wo")
    mat.add_nuclide("O18", 0.000478, "wo")
    mat_list.append(mat)


    # --- PNNL 144: Gadolinium ---
    mat = openmc.Material(material_id=144, name="Gadolinium")
    mat.set_density("g/cc", 7.9004)
    mat.add_element("Gd", 1.000000, "wo")
    mat_list.append(mat)


    # --- PNNL 145: Gadolinium Aluminum Galium Oxide - 0.5 atom% Cerium doped ---
    mat = openmc.Material(material_id=145, name="Gadolinium Aluminum Galium Oxide - 0.5 atom% Cerium doped")
    mat.set_density("g/cc", 6.6)
    mat.add_element("Gd", 0.501351, "wo")
    mat.add_nuclide("Al27", 0.057349, "wo")
    mat.add_element("Ga", 0.222294, "wo")
    mat.add_nuclide("O16", 0.203487, "wo")
    mat.add_nuclide("O17", 0.000082, "wo")
    mat.add_nuclide("O18", 0.000471, "wo")
    mat.add_nuclide("Ce136", 0.000027, "wo")
    mat.add_nuclide("Ce138", 0.000037, "wo")
    mat.add_nuclide("Ce140", 0.013217, "wo")
    mat.add_nuclide("Ce142", 0.001685, "wo")
    mat_list.append(mat)


    # --- PNNL 146: Gadolinium Oxysulfide ---
    mat = openmc.Material(material_id=146, name="Gadolinium Oxysulfide")
    mat.set_density("g/cc", 7.44)
    mat.add_nuclide("O16", 0.084297, "wo")
    mat.add_nuclide("O17", 0.000034, "wo")
    mat.add_nuclide("O18", 0.000195, "wo")
    mat.add_element("S", 0.084708, "wo")
    mat.add_element("Gd", 0.830766, "wo")
    mat_list.append(mat)


    # --- PNNL 147: Gadolinium Silicate (GSO) ---
    mat = openmc.Material(material_id=147, name="Gadolinium Silicate (GSO)")
    mat.set_density("g/cc", 6.71)
    mat.add_nuclide("O16", 0.188792, "wo")
    mat.add_nuclide("O17", 0.000076, "wo")
    mat.add_nuclide("O18", 0.000437, "wo")
    mat.add_element("Si", 0.066460, "wo")
    mat.add_element("Gd", 0.744235, "wo")
    mat_list.append(mat)


    # --- PNNL 148: Gafchromic Sensor (GS) ---
    mat = openmc.Material(material_id=148, name="Gafchromic Sensor (GS)")
    mat.set_density("g/cc", 1.3)
    mat.add_nuclide("H1", 0.089676, "wo")
    mat.add_nuclide("H2", 0.000021, "wo")
    mat.add_element("C", 0.605800, "wo")
    mat.add_nuclide("N14", 0.111761, "wo")
    mat.add_nuclide("N15", 0.000437, "wo")
    mat.add_nuclide("O16", 0.191779, "wo")
    mat.add_nuclide("O17", 0.000078, "wo")
    mat.add_nuclide("O18", 0.000443, "wo")
    mat_list.append(mat)


    # --- PNNL 149: Gallium Arsenide ---
    mat = openmc.Material(material_id=149, name="Gallium Arsenide")
    mat.set_density("g/cc", 5.31)
    mat.add_element("Ga", 0.482030, "wo")
    mat.add_nuclide("As75", 0.517970, "wo")
    mat_list.append(mat)

    
    # --- PNNL 150: Gasoline ---
    mat = openmc.Material(material_id=150, name="Gasoline")
    mat.set_density("g/cc", 0.721)
    mat.add_nuclide("H1", 0.158794, "wo")
    mat.add_nuclide("H2", 0.000036, "wo")
    mat.add_element("C", 0.841164, "wo")
    mat_list.append(mat)

    return {m.id: m for m in mat_list}

test = get_pnnl_mats()
