##
# This software was developed and / or modified by Raytheon Company,
# pursuant to Contract DG133W-05-CQ-1067 with the US Government.
#
# U.S. EXPORT CONTROLLED TECHNICAL DATA
# This software product contains export-restricted data whose
# export/transfer/disclosure is restricted by U.S. law. Dissemination
# to non-U.S. persons whether in the United States or abroad requires
# an export license or other authorization.
#
# Contractor Name:        Raytheon Company
# Contractor Address:     6825 Pine Street, Suite 340
#                         Mail Stop B8
#                         Omaha, NE 68106
#                         402.291.0100
#
# See the AWIPS II Master Rights File ("Master Rights File.pdf") for
# further licensing information.
##

#
# SOFTWARE HISTORY
#
# Date           Ticket#      Engineer      Description
# ------------   ----------   -----------   -----------
#                             ????          Initial creation
# Aug 05, 2015   4703         njensen       Removed unused import
#

from numpy import power

def execute(*args):
    ##
    # Calculate temperature from pressure and theta.
    # or from pressure, virtual theta, and specific humidity
    # This function accepts numpy arrays
    #
    # @param P: Pressure in millibars
    # @param PoT: theta in degrees Kelvin
    # @return: Potential temperature in degrees Kelvin
    #
    "Calculate temperature from pressure and theta(PoT)."
    # use numpy masked arrays to prevent operating on sentinel values
    P = args[0]
    PoT = args[1]

    pComponent = P/1000.0
    pComponent = power(pComponent, 0.286)
    T = PoT * pComponent

    if len(args) == 3:
        "Calculated VT from pressure and virtual theta, also need to process specific humidity"
        SHx = args[2]
        T = T / (1 + 0.000608 * SHx)

    return T
