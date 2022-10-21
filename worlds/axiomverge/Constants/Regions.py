REGION_NAMES = {
    'Menu',

    'Eribu',
    'Lower Eribu',
    'Eribu Secret',

    'Absu',
    'Central Absu',
    'Inner Absu',

    'Zi',
    'Upper Zi',

    'Lower Kur',
    'Upper Kur',
    'Snowy Kur',

    'Indi',

    'Ukkin-Na',

    'Edin West',
    'Edin East',
    'Central Edin',
    'Edin Tower',

    'E-Kur-Mah',
    'Inner E-Kur-Mah',

    'Mar-Uru',
    }

VANILLA_REGION_CONNECTIONS = {
    ('Menu', 'Eribu'),
    
    ('Eribu', 'Lower Eribu'),
    ('Eribu', 'Eribu Secret',)
    ('Lower Eribu', 'Absu'),
    ('Lower Eribu', 'Ukkin-Na'),
    ('Lower Eribu', 'Indi'),

    ('Absu', 'Central Absu'),
    ('Central Absu', 'Indi'),
    ('Central Absu', 'Inner Absu'),
    ('Inner Absu', 'Zi'),

    ('Zi', 'Upper Zi'),
    ('Zi', 'Lower Kur'),
    ('Upper Zi', 'Indi'),

    ('Lower Kur', 'Upper Kur'),
    ('Lower Kur', 'Indi'),
    ('Lower Kur', 'Edin East'),
    ('Upper Kur', 'Snowy Kur'),
    ('Upper Kur', 'E-Kur-Mah'),
    ('Snowy Kur', 'E-Kur-Mah'),

    ('Ukkina-Na', 'Edin West'),
    ('Ukkin-Na', 'Mar-Uru'),

    ('Edin East', 'Central Edin'),
    ('Edin West', 'Central Edin'),
    ('Edin West', 'Edin Tower'),
    ('Central Edin', 'Indi'),
    }
