me = Fight.me
enemy = Fight.getNearestEnemy()

if Fight.turn == 1:
    me.setWeapon(Weapon.pistol)

if me.life < (me.maxLife - 50): 
    if Chip.bandage in me.chips and me.canUseChip:
        me.useChip(Chip.bandage)

if enemy.distance(me) < 10:
    for buff in [Chip.motivation, Chip.protein, Chip.helmet]:
        if buff in me.chips and me.canUseChip:
            me.useChip(buff)

pistol_range = 7

if enemy.distance(me) > pistol_range:
    me.moveToward(enemy)

for _ in range(3):
    me.useWeapon(enemy)
    
if enemy.distance(me) <= pistol_range: 
    me.moveAwayFrom(enemy)
