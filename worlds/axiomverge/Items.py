from typing import Dict, NamedTuple

class ItemData(NamedTuple):
    category: str
    code: int
    count: int = 1
    progression: bool = False
    useful: bool = False

item_table: Dict[str, ItemData] = {
        'Axiom Disruptor': ItemData('Weapon', 4101000),
        'Nova': ItemData('Weapon', 4101001, progression=True),
        'Multi-Disruptor': ItemData('Weapon', 4101002),
        'Kilver': ItemData('Weapon', 4101003, progression=True),
        'Firewall': ItemData('Weapon', 4101004),
        'Hypo-Atomizer': ItemData('Weapon', 4101005, progression=True),
        'Voranj': ItemData('Weapon', 4101006),
        'Reflector': ItemData('Weapon', 4101007, progression=True),
        'Inertial Pulse': ItemData('Weapon', 4101008),
        'Orbital Discharge': ItemData('Weapon', 4101009, progression=True),
        'Lightning Gun': ItemData('Weapon', 4101010),
        'Turbine Pulse': ItemData('Weapon', 4101011),
        'Shards': ItemData('Weapon', 4101012),
        'Distortion Field': ItemData('Weapon', 4101013, progression=True),
        'Data Bomb': ItemData('Weapon', 4101014),
        'Tethered Charge': ItemData('Weapon', 4101015),
        'Quantum Variegator': ItemData('Weapon', 4101016),
        'Ion Beam': ItemData('Weapon', 4101017),
        'Reverse Slicer': ItemData('Weapon', 4101018, progression=True),
        'Flamethrower': ItemData('Weapon', 4101019, progression=True),
        'Heat Seeker': ItemData('Weapon', 4101020),
        'Scissor Beam': ItemData('Weapon', 4101021, progression=True),
        'Fat Beam': ItemData('Weapon', 4101022, progression=True),

        'Laser Drill': ItemData('Upgrade', 4101100, progression=True),
        'Sudran Key': ItemData('Upgrade', 4101101, progression=True),
        'Field Disruptor': ItemData('Upgrade', 4101102, progression=True),
        'Bioflux Accelerator 1': ItemData('Upgrade', 4101103),
        'Lab Coat': ItemData('Upgrade', 4101104, progression=True),
        'Trenchcoat': ItemData('Upgrade', 4101105, progression=True),
        'Red Coat': ItemData('Upgrade', 4101106, progression=True),
        'Remote Drone': ItemData('Upgrade', 4101107, progression=True),
        'Enhanced Drone Launch': ItemData('Upgrade', 4101108, progression=True),
        'Drone Teleport': ItemData('Upgrade', 4101109, progression=True),
        'Address Disruptor 1': ItemData('Upgrade', 4101110, progression=True),
        'Address Disruptor 2': ItemData('Upgrade', 4101111, progression=True),
        'Address Bomb': ItemData('Upgrade', 4101112, progression=True),
        'Grapple': ItemData('Upgrade', 4101113, progression=True),
        'Passcode Tool': ItemData('Upgrade', 4101114, progression=True),
        'Bioflux Accelerator 2': ItemData('Upgrade', 4101115),

        'Health Node': ItemData('Powerup', 4101200, count=9),
        'Health Node Fragment': ItemData('Powerup', 4101201, count=20),
        'Power Node': ItemData('Powerup', 4101202, count=6),
        'Power Node Fragment': ItemData('Powerup', 4101203, count=18),
        'Size Node': ItemData('Powerup', 4101204, count=4),
        'Range Node': ItemData('Powerup', 4101205, count=4),

        'Note': ItemData('Note', 4101300, count=18),
}
