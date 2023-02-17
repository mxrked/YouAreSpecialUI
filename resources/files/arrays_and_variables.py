'''

    This will hold the global arrays and variables

'''

from resources.files.classes import Perk

''' Variables '''
skillPoints = 28 # 21 + 7 = 28 (This is to prevent overflowing into extra numbers)

''' Arrays '''
remainingPoints = [] # Holds the remaining points

# Each attribute points holder
sPoints = [1]
pPoints = [1]
ePoints = [1]
cPoints = [1]
iPoints = [1]
aPoints = [1]
lPoints = [1]


# Perk instances
# Strength
ironFist = Perk("Iron Fist", "Damage boost when using unarmed melee attacks.", 5, 1, [0, 9, 18, 31, 46])
bigLeagues = Perk("Big Leagues", "Damage boost with using melee weapons.", 5, 2, [0, 7, 15, 27, 42])
armorer = Perk("Armorer", "Gain the ability to craft armour.", 4, 3, [0, 13, 25, 39])
blackSmith = Perk("Blacksmith", "Gain the ability to craft melee weapons.", 3, 4, [0, 16, 29])
heavyGunner = Perk("Heavy Gunner", "Damage boost when using big guns.", 5, 5, [0, 11, 21, 35, 47])
strongBack = Perk("Strong Back", "Carry more in your inventory and maintain sprint.", 5, 6, [0, 10, 20, 30, 40])
steadyAim = Perk("Steady Aim", "Bonuses to weapon stats e.g. recoil.", 3, 7, [0, 28, 49])
basher = Perk("Basher", "Bonus damage when using gun as melee attack.", 4, 8, [0, 5, 14, 26])
rooted = Perk("Rooted", "Bonus damage resistance plus melee and unarmed attacks do more damage.", 3, 9, [0, 22, 43])
painTrain = Perk("Pain Train", "Sprint and knockdown enemies while using power armour..", 3, 10, [0, 24, 50])
# Perception
pickPocket = Perk("Pickpocket", "Steal items from other people more easily e.g. keys, bottle caps.", 4, 1, [0, 6, 17, 30])
rifleman = Perk("Rifleman", "Enhance attacks with non-automatic weapons.", 5, 2, [0, 9, 18, 31, 46])
awareness = Perk("Awareness", "Understand the level of enemies before engaging in a fight.", 2, 3, [0, 14])
lockSmith = Perk("Locksmith", "Pick Advanced locks and gain access to locked areas.", 4, 4, [0, 7, 18, 41])
demolitionExpert = Perk("Demolition Expert", "Damage boost when using explosives/mines.", 4, 5, [0, 10, 22, 34])
nightPerson = Perk("Night Person", "Bonus +2 Intelligence and Perception between 6pm and 6am.", 3, 6, [0, 25, 37])
refractor = Perk("Refractor", "Gain resistance to energy weapons.", 5, 7, [0, 11, 21, 35, 42])
sniper = Perk("Sniper", "Enhance attacks with sniper rifles e.g. longer breath.", 3, 8, [0, 13, 26])
penetrator = Perk("Penetrator", "While in VATS, target enemy body parts that are blocked by cover e.g. walls.", 2, 9, [0, 28])
concentratedFire = Perk("Concentrated Fire", "Better accuracy and damage when hitting the same body parts in VATS.", 3, 10, [0, 26, 50])
# Endurance
toughness = Perk("Toughness", "Increased damage resistance.", 5, 1, [0, 9, 18, 31, 46])
leadBelly = Perk("Lead Belly", "Less radiation when drinking irradiated water.", 3, 2, [0, 6, 17])
lifeGiver = Perk("Life Giver", "Increased health (HP points).", 3, 3, [0, 8, 22])
chemResistant = Perk("Chem Resistant", "Less likely to become addicted to chems/drugs.", 2, 4, [0, 22])
aquaBoy = Perk("Aquaboy", "Immune to radiation via water and grants underwater breathing.", 2, 5, [0, 21])
radResistant = Perk("Rad Resistant", "Better resistance to radiation.", 4, 6, [0, 13, 26, 35])
adamantiumSkeleton = Perk("Adamantium Skeleton", "Reduced limb damage.", 3, 7, [0, 13, 26])
cannibal = Perk("Cannibal", "Allows player to each corpse to regain health.", 3, 8, [0, 19, 38])
ghoulish = Perk("Ghoulish", "Regenerate health with radiation.", 4, 9, [0, 24, 48, 50])
solarPowered = Perk("Solar Powered", "Bonus +2 to Strength and Endurance between 6am and 6pm.", 3, 10, [0, 27, 50])
# Charisma
capCollector = Perk("Cap Collector", "Receive a discount when trading.", 3, 1, [0, 20, 41])
ladyKiller = Perk("Lady Killer", "Deal more damage to the opposite sex. Also makes persuading the opposite sex easier.", 3, 2, [0, 7, 22])
loneWanderer = Perk("Lone Wanderer", "Bonuses for exploring without a companion e.g more carry weight.", 4, 3, [0, 17, 40, 50])
attackDog = Perk("Attack Dog", "Dogmeat gains enhancements e.g. holding off enemies for you.", 4, 4, [0, 9, 25, 31])
animalFriend = Perk("Animal Friend", "Animals can be pacified and will not attack you.", 3, 5, [0, 12, 28])
localLeader = Perk("Local Leader", "Enhances settlements, opens supply lines and trade routes.", 2, 6, [0, 14])
partyBoy = Perk("Party Boy", "Less likely to become addicted to alcohol.", 3, 7, [0, 15, 37])
inspirational = Perk("Inspirational", "Companions gain bonuses.", 3, 8, [0, 19, 43])
wastelandWhisperer = Perk("Wasteland Whisperer", "Tame wasteland creatures.", 3, 9, [0, 21, 49])
intimidation = Perk("Intimidation", "Pacify, instruct and force opponents to attack.", 3, 10, [0, 23, 50])
# Intelligence
vans = Perk("V.A.N.S", "Quests and targets are displayed on the radar.", 2, 1, [0, 36])
medic = Perk("Medic", "Health bonuses from medical supplies e.g. Stimpacks.", 4, 2, [0, 18, 30, 49])
gunNut = Perk("Gun Nut", "Gain access to weapon mods, each rank increases the type of mods you can create.", 4, 3, [0, 13, 25, 39])
hacker = Perk("Hacker", "Hack computer terminals to open doors, security systems etc.", 4, 4, [0, 9, 21, 33])
scrapper = Perk("Scrapper", "Salvage uncommon items such as screws, aluminium and copper when scrapping weapons and armour.", 3, 5, [0, 23, 40])
science = Perk("Science!", "Gain access to energy weapons and mods.", 4, 6, [0, 17, 28, 41])
chemist = Perk("Chemist", "Increase the duration for chems.", 4, 7, [0, 16, 32, 45])
roboticsExpert = Perk("Robotics Expert", "Hack robots to power on/off and initiate self destruct.", 3, 8, [0, 19, 44])
nuclearPhysicist = Perk("Nuclear Physicist", "Radiation weapons cause more damage and fusion cores last longer.", 3, 9, [0, 14, 26])
nerdRage = Perk("Nerd Rage!", "Bonus to damage resistance and damage output when health is less than 20%.", 3, 10, [0, 31, 50])
# Agility
gunslinger = Perk("Gunslinger", "Bonuses when using pistols.", 5, 1, [0, 7, 15, 27, 42])
commando = Perk("Commando", "Bonuses when using automatic weapons.", 5, 2, [0, 11, 21, 35, 49])
sneak = Perk("Sneak", "Reduce the chance of being detected when sneaking.", 5, 3, [0, 5, 12, 23, 38])
misterSandman = Perk("Mister Sandman", "Instantly kill sleeping enemies and silenced weapons do more damage in sneak.", 3, 4, [0, 17, 30])
actionBoy = Perk("Action Boy", "More Action Points and faster generation.", 3, 5, [0, 18, 38])
movingTarget = Perk("Moving Target", "Bonus damage resistance when sprinting.", 3, 6, [0, 24, 44])
ninja = Perk("Ninja", "Bonus damage when undetected.", 3, 7, [0, 14, 33])
quickHands = Perk("Quick Hands", "Faster reload.", 3, 8, [0, 28, 40])
blitz = Perk("Blitz", "VATS melee distance is increased.", 2, 9, [0, 29])
gunFu = Perk("Gun Fu", "More damage when hitting multiple targets in VATS. Instant criticals at high Rank.", 3, 10, [0, 26, 50])
# Luck
fortuneFinder = Perk("Fortune Finder", "Find more bottle caps (money).", 4, 1, [0, 5, 25, 40])
scrounger = Perk("Scrounger", "Find more ammo in containers.", 4, 2, [0, 7, 24, 37])
bloodyMess = Perk("Bloody Mess", "More damage plus a chance for enemies to explode in a gory mess.", 4, 3, [0, 9, 31, 47])
mysteriousStranger = Perk("Mysterious Stranger", "Chance that a stranger may help you in during VATS.", 4, 4, [0, 22, 41, 49])
idiotSavant = Perk("Idiot Savant", "Randomly gain more experience from actions (greater gain if intelligence is low).", 3, 5, [0, 11, 34])
betterCriticals = Perk("Better Criticals", "Criticals do more damage.", 3, 6, [0, 15, 40])
criticalBanker = Perk("Critical Banker", "Save a Critical hit, to be used in VATS when you need it later.", 4, 7, [0, 17, 43, 50])
grimReapersSprint = Perk("Grim Reaper's Sprint", "Chance to restore all Action Points after a kill.", 3, 8, [0, 19, 46])
fourLeafClover = Perk("Four Leaf Clover", "Each hit in VATS has a chance to fill Critical Meter.", 4, 9, [0, 13, 32, 48])
ricochet = Perk("Ricochet", "Chance that enemies ranged attacks will ricochet back and kill them. The closer to death you are, the more the probability", 3, 10, [0, 29, 50])

# Each attribute perks holder
strengthPerks = [ironFist, bigLeagues, armorer, blackSmith, heavyGunner, strongBack, steadyAim, basher, rooted, painTrain]
perceptionPerks = [pickPocket, rifleman, awareness, lockSmith, demolitionExpert, nightPerson, refractor, sniper, penetrator, concentratedFire]
endurancePerks = [toughness, leadBelly, lifeGiver, chemResistant, aquaBoy, radResistant, adamantiumSkeleton, cannibal, ghoulish, solarPowered]
charismaPerks = [capCollector, ladyKiller, loneWanderer, attackDog, animalFriend, localLeader, partyBoy, inspirational, wastelandWhisperer, intimidation]
intelligencePerks = [vans, medic, gunNut, hacker, scrapper, science, chemist, roboticsExpert, nuclearPhysicist, nerdRage]
agilityPerks = [gunslinger, commando, sneak, misterSandman, actionBoy, movingTarget, ninja, quickHands, blitz, gunFu]
luckPerks = [fortuneFinder, scrounger, bloodyMess, mysteriousStranger, idiotSavant, betterCriticals, criticalBanker, grimReapersSprint, fourLeafClover, ricochet]
