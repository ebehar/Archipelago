from typing import Dict
from BaseClasses import Item, ItemClassification
from .Options import is_option_enabled

class AxiomVergeItem(Item):
    game: str = "Axiom Verge"

code_offset = 4103000


BASIC_WEAPONS = {
    'Axiom Disruptor',
    'Multi-Disruptor',
    'Firewall',
    'Voranj',
    'Inertial Pulse',
    'Lightning Gun',
    'Turbine Pulse',
    'Shards',
    'Data Bomb',
    'Tethered Charge',
    'Quantum Variegator',
    'Ion Beam',
    'Heat Seeker',
    }

NOVAISH_WEAPONS = {
    'Nova',
    'Hypo-Atomizer',
    'Reflector',
    'Orbital Discharge',
    }

KILVERISH_WEAPONS = {
    'Kilver',
    'Distortion Field',
    'Reverse Slicer',
    'Flamethrower',
    'Scissor Beam',
    'Fat Beam',
    }

FILLER_UPGRADES = {
    'Bioflux Accelerator 1',
    'Bioflux Accelerator 2',
    }

USEFUL_UPGRADES = {
    'Enhanced Drone Launch',
    }

PROGRESSION_UPGRADES = {
    'Laser Drill',
    'Sudran Key',
    'Field Disruptor',
    'Lab Coat',
    'Trenchcoat',
    'Red Coat',
    'Remote Drone',
    'Drone Teleport',
    'Address Disruptor 1',
    'Address Disruptor 2',
    'Address Bomb',
    'Grapple',
    'Passcode Tool',
    }

FRAGMENTS = {
    'Health Node Fragment',
    'Power Node Fragment',
    }

USEFUL_NODES = {
    'Health Node',
    'Power Node',
    }

FILLER_NODES = {
    'Size Node',
    'Range Node',
    }

NOTES = {
    'Note'
    }
