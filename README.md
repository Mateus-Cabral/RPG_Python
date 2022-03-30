This program is a simple turn-based card game using Python built-in libraries.

Goal:
    Win the battle by finalizing your oponent's HP battling with creatures, magics and specials (joker) cards  

Main Mechanics:

    HP:
        HP_Player: player's life points, the game finishes when someone reaches 0. 
        HP_Creature: creature's life points, every time a creature takes more damage then his health it dies and it is replaced.
        Every time a creature card dies the player that controls it loses 1 point of hp 
    
    DEF: 
        Creature's defense is a atribute that reduces the damage received
    
    ATK:
        Creature's attack is a atribute that indicates damage caused
    
    SPD:
        Creature's priority on battle, highter speed means attacking first
    
    Battle:
        At the start of the game the player receives 3 cards (1 creature, 1 magic and 1 joker card) randomly.
        At the start of each turn the player can choose if he's going to use a magic and/or joker card but the creatures are always going to battle.
        When a player uses a magic/joker card and/or his creature dies he'll receive a new card randomly but always having only 1 of each
        Priorities:
            Joker Cards -> Magic Cards -> Battle 

Cards:
    Creatures: attacking mechanism, can be boosted by magic cards. Creatures atack head to head
        Elf Mage (alias "Mago Élfico") - A more attack focused character  
            HP:  3 
            DEF: 0
            ATK: 4
            SPD: 1

        Beastkin Swordsman (alias "Espadachim Bestial") - A balanced atk/def character
            HP:  4
            DEF: 1
            ATK: 3
            SPD: 2

         Dwarf Warrior (alias "Guerreiro Anão") - A more defense focused character
            HP:  5
            DEF: 2
            ATK: 2
            SPD: 0

    Magic cards: buffing/nerfing mechanism. You can use 1 magic card per turn
        Card_1 - Buffs the dmg in 1 point - "Aumenta o dano em 1"
        Card_2 - Buffs the resistance in 1 point - "Aumenta a resistência em 1 ponto"
        Card_3 - Buffs the creatures hp in 1 point - "Aumenta o hp em 1"
   
    Joker Cards: other mecanics. Alike magic cards but with more exotic effects.
        Card_1 - Skips the battle for 1 turn (used magic cards are still lost and replaced) - "Pula o turno"
        Card_2 - Blocks the magic from your oponent - "Nega a magia do oponente"
        Card_3 - Deals 1 dmg directly to your oponent's hp  

