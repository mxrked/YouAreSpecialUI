'''

    This will hold the global functions

'''

import sys

from resources.files import arrays_and_variables

def exitApp():
    sys.exit()

def getRemainingSkillPoints():

    # Getting all the current points added
    pointsUsed = sum(arrays_and_variables.sPoints + arrays_and_variables.pPoints + arrays_and_variables.ePoints + arrays_and_variables.cPoints + arrays_and_variables.iPoints + arrays_and_variables.aPoints + arrays_and_variables.lPoints)

    # Calculating the remaining points
    arrays_and_variables.remainingPoints.clear()
    arrays_and_variables.remainingPoints.append(arrays_and_variables.skillPoints - pointsUsed)

    return sum(arrays_and_variables.remainingPoints)

