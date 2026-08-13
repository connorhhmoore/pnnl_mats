# PNNL-15870 Rev. 2 Materials for OpenMC
This repo provides a simple means of accessing materials defined in the [PNNL-15870 revision 2](https://www.pnnl.gov/main/publications/external/technical_reports/PNNL-15870Rev2.pdf) report for OpenMC. These materials were copied from the PDF mostly by hand with the help of Vim macros for automatically formatting the tables into OpenMC Python inputs. All materials are added using their isotopic weight% formulations from the report.

## Installation
The only thing required to use this library is to clone a local version of it. Starting in the directory that has your OpenMC input:
```
git clone git@github.com:connorhhmoore/pnnl_mats.git
```
**NOTE:** If you are already version controlling your OpenMC input with Git, it is preferable to add the repo as a submodule instead:
```
git submodule add git@github.com:connorhhmoore/pnnl_mats.git
```
The final directory should look something like this:
```
your-openmc-project
    ├── openmc_input.py
    └── pnnl_mats
        ├── __init__.py
        └── lib.py
```
## Usage
With the structure defined above it is easy to use the library inside your OpenMC model. To access it you must import it:
```python
from pnnl_mats import get_pnnl_mats
```
The function `get_pnnl_mats` returns a dictionary of PNNL-15870 materials keyed using their IDs from the report. First assign the dictionary to a variable:
```python
mat_dict = get_pnnl_mats()
```
From there, access whatever material is necessary. For example we can access ID 374 which is Uranium Hydride:
```python
mat_uh3 = mat_dict[374]
```
Locally, `mat_uh3` now contains the `openmc.Material` for UH3:
```
Material
	ID             =	374
	Name           =	Uranium Hydride
	Temperature    =	None
	Density        =	11.1 [g/cc]
	Volume         =	None [cm^3]
	Depletable     =	True
	S(a,b) Tables
	S(a,b)         =	('c_H_in_UH3', 1.0)
	Nuclides
	H1             =	0.012545     [wo]
	H2             =	3e-06        [wo]
	U234           =	0.000264     [wo]
	U235           =	0.029624     [wo]
	U236           =	0.000136     [wo]
	U238           =	0.957428     [wo]
```
Note that the material has the ENDF/B-VIII.1 TSL data applied by default. It is possible to turn this off by supplying any string other than `"endfb81"` as an argument to the function call, e.g. `get_pnnl_mats("none")`. To use the materials you will still need to export everything to XML. An easy way to do this is to add them to a list as you add materials to your project:
```python
import openmc
from pnnl_mats import get_pnnl_mats

mat_dict = get_pnnl_mats()
mat_list = []

# Natural Uranium Metal
mat_nu = mat_dict[385]
mat_list.append(mat_nu)

# Zircaloy-4
mat_zr4 = mat_dict[306]
mat_list.append(mat_zr4)

# Heavy Water
mat_d2o = mat_dict[391]
mat_list.append(mat_d2o)

# Export to XML
materials = openmc.Materials(mat_list)
materials.export_to_xml()
```
Now it is possible to use the materials as you build your model without exporting the full library as an XML.
