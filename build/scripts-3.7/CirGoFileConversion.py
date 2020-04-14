""" CirGO
    Version 1.0 01/03/2018

    CirGO (Circular Gene Ontologies) is an alternative way of visualizing GO terms in 2D space
    that is suitable for publishing and presenting gene expression ontologies data.

    Copyright (C) 2018 Irina Kuznetsova
    This software is licensed under the terms of the GNU general public license (version 3).
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    If you are using the softwareas a part of your research work, please cite the following publication
    Kuznetsova I, Lugmayr A, Siira SJ, Rackham O, Filipovska A.
    CirGO: an alternative circular way of visualising gene ontology terms. BMC Bioinformatics [Internet].
    2019 Feb 18;20(1):84. Available from: https://doi.org/10.1186/s12859-019-2671-2

    Conract info:   irina.kuznetsova@uwa.edu.au
    GitHub:         https://github.com/IrinaVKuznetsova/CirGO.git
"""

##----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
## I. Import required modules
## ----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
from operator import abs
import pandas as pd
import os.path

def ConvertToThreeCoulmnsInput(inputfilename, outputfilename='', outputfilepath=''):

    if (outputfilename == ''):
        outputfilename, ex = os.path.splitext(inputfilename)
        outputfilename = outputfilename + "_converted.csv"
    outputfilename = outputfilepath + outputfilename
    print("Converting input file " + inputfilename + " to intermediate three columns input file " + outputfilename + " in path " + outputfilepath + " ...")

    data = pd.read_csv(inputfilename,sep=",",skiprows=4,header=0,index_col=0)
    selected = data[[data.columns[0],data.columns[2],data.columns[-1]]]
    selected.to_csv(outputfilename,sep="\t",header=True,index=False)
    print("Input file " + inputfilename + " cleaned and converted to tab deliminated file " + outputfilename + " in path " + outputfilepath + " ...")
