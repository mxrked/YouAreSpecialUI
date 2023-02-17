'''

    This will hold the classes and objects

'''


class Perk:

    def __init__(self, perkName, perkDesc, perkRanks, perkStat, perkLevel):
        self._perkName = perkName
        self._perkDesc = perkDesc
        self._perkRanks = perkRanks
        self._perkStat = perkStat
        self._perkLevel = perkLevel


    # Setters
    def setPerkName(self, perkName):
        self._perkName = perkName
    def setPerkDesc(self, perkDesc):
        self._perkDesc = perkDesc
    def setPerkRanks(self, perkRanks):
        self._perkRanks = perkRanks
    def setPerkStat(self, perkStat):
        self._perkStat = perkStat
    def setPerkLevel(self, perkLevel):
        self._perkLevel = perkLevel

    # Getters
    def getPerkName(self):
        return self._perkName
    def getPerkDesc(self):
        return self._perkDesc
    def getPerkRanks(self):
        return self._perkRanks
    def getPerkStat(self):
        return self._perkStat
    def getPerkLevel(self):
        return self._perkLevel


    def __str__(self):
        perkDetails = "Perk Name: " + self.getPerkName() + "\nPerk Desc: " + self.getPerkDesc() + "\nNumber of Ranks: " + str(self.getPerkRanks()) + "\nAttribute Requirement: " + str(self.getPerkStat()) + "\nLevel Requirement: " + self.getPerkLevel()
        return perkDetails



