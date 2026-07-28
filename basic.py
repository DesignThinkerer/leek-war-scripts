# @version:3.12
me = Fight.me 
enemy = Fight.getNearestEnemy()

if Fight.turn == 1:
    me.setWeapon(Weapon.pistol)
    
me.moveToward(enemy)


me.useWeapon(enemy)
me.useWeapon(enemy)
me.useWeapon(enemy)
    
me.moveAwayFrom(enemy)
