from shipcraft.ai.ship import DefaultShipAI
from shipcraft.model import Action

class PythonAI(DefaultShipAI):
    def __init__(self):
        pass

    def getUpgrade(myShipId):
        return Action('width++')

# Должен возвращать имя корабля (EN: Must return ship name)
    def getShipName():
        return 'PythonShip'

    # Должен возвращать название команды корабля (EN: Must return ship crew name)
    def getTeamName():
        return 'PythonShipTeam'

pythonAi = PythonAI()
#print pythonAi
    
