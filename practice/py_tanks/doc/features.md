## PyTanks Mini Game Features

### Description
The game will simulate battle between tanks in battles.

### Features

#### Tank traits
- **Tank Destroyer**: Critical hit chance, dealing 50% extra damage
- **Heavy**: Armor resistance chance to reduce damage taken by 50%
- **Medium**: The random modifiers for penetration and damaging can't be negative
- **Light**: Chance to dodge damage, making hit to miss
- **Artillery**: Chance to stun tanks, making them unable to shoot for a turn

#### Tank attributes
- Armor by side: Resistance against hits damages
- Penetration: Ability to penetrate other tanks armor
- Precision: Chance of hitting target
- Damage: Raw damage dealt by ammunition
- Health: Life of the tank
- Type: Type of tank
- Model: Model name

#### Battle mechanics
General
- Each tank shoot a random target, arty are the last one targeted
- The fight order depends on the tank initiative (top/down)
- A random side will be chosen on target when shooting
- When the health is reduced to 0, the tank is removed from battle
- When only thanks from one side remains, the time is victorious
- The human player can choose a tank to play with at the start of each battle
- The IA are piking random tanks, with a maximum from 2 arty by team

Hitting
- The precision define the accuracy of the shoot. 
If a side is shot, then we increase it due to the size of the surface.

Penetration:
- If the difference between the armor and the penetration is:
  - < 20% then there is no modifier
  - < 50% then there is a bonus/malus to penetration from 50%
  - else the penetration is automatic
- There is a random modifier of +/- 20% in the chance of penetrating

Damage:
- The damage dealt to the remote tank has random modifier from +/- 20%

Player progression:
- The player can earn experience and money in battle
- The experience can be spent on improving the tanks characteristics with modules
- The progression is saved in a local file, including tanks and experience
- The player start with a medium tank, new tank can be purchased
- Destroying a tank give money and experience
- Losing the battle reduce rewards by 50% and winning it increase it by 50%.