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
    mat.set_density("g/cc",1.127)
    mat.add_nuclide("H1",     0.101300,   "wo")
    mat.add_nuclide("H2",     0.000023,   "wo")
    mat.add_element("C",      0.775500,   "wo")
    mat.add_nuclide("N14",    0.034920,   "wo")
    mat.add_nuclide("N15",    0.000137,   "wo")
    mat.add_nuclide("O16",    0.052174,   "wo")
    mat.add_nuclide("O17",    0.000021,   "wo")
    mat.add_nuclide("O18",    0.000121,   "wo")
    mat.add_nuclide("F19",    0.017422,   "wo")
    mat.add_element("Ca",     0.018378,   "wo")
    mat_list.append(mat)

    # --- PNNL 2: Acetone ---
    mat = openmc.Material(material_id=2, name="Acetone")
    mat.set_density("g/cc", 0.7899)
    mat.add_nuclide("H1", 0.104104,"wo")
    mat.add_nuclide("H2", 0.000024,"wo")
    mat.add_element("C", 0.620393,"wo")
    mat.add_nuclide("O16", 0.274730,"wo")
    mat.add_nuclide("O17", 0.000111,"wo")
    mat.add_nuclide("O18", 0.000635,"wo")
    mat_list.append(mat)

    
