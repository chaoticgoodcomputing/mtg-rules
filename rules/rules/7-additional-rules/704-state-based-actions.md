704.1. State-based actions are game actions that happen automatically whenever certain conditions (listed below) are met. State-based actions don’t use the stack.

704.1a Abilities that watch for a specified game state are triggered abilities, not state-based actions. (See rule 603, “Handling Triggered Abilities.”)

704.2. State-based actions are checked throughout the game and are not controlled by any player.

704.3. Whenever a player would get priority (see rule 117, “Timing and Priority”), the game checks for any of the listed conditions for state-based actions, then performs all applicable state-based actions simultaneously as a single event. If any state-based actions are performed as a result of a check, the check is repeated; otherwise all triggered abilities that are waiting to be put on the stack are put on the stack, then the check is repeated. Once no more state-based actions have been performed as the result of a check and no triggered abilities are waiting to be put on the stack, the appropriate player gets priority. This process also occurs during the cleanup step (see rule 514), except that if no state-based actions are performed as the result of the step’s first check and no triggered abilities are waiting to be put on the stack, then no player gets priority and the step ends.

704.4. Unlike triggered abilities, state-based actions pay no attention to what happens during the resolution of a spell or ability.
Example: A player controls Maro, a creature with the ability “Maro’s power and toughness are each equal to the number of cards in your hand” and casts a spell whose effect is “Discard your hand, then draw seven cards.” Maro will temporarily have toughness 0 in the middle of the spell’s resolution but will be back up to toughness 7 when the spell finishes resolving. Thus Maro will survive when state-based actions are checked. In contrast, an ability that triggers when the player has no cards in hand goes on the stack after the spell resolves, because its trigger event happened during resolution.

704.5. The state-based actions are as follows:

704.5a If a player has 0 or less life, that player loses the game.

704.5b If a player attempted to draw a card from a library with no cards in it since the last time state-based actions were checked, that player loses the game.

704.5c If a player has ten or more poison counters, that player loses the game. Ignore this rule in Two-Headed Giant games; see rule 704.6b instead.

704.5d If a token is in a zone other than the battlefield, it ceases to exist.

704.5e If a copy of a spell is in a zone other than the stack, it ceases to exist. If a copy of a card is in any zone other than the stack or the battlefield, it ceases to exist.

704.5f If a creature has toughness 0 or less, it’s put into its owner’s graveyard. Regeneration can’t replace this event.

704.5g If a creature has toughness greater than 0, it has damage marked on it, and the total damage marked on it is greater than or equal to its toughness, that creature has been dealt lethal damage and is destroyed. Regeneration can replace this event.

704.5h If a creature has toughness greater than 0, and it’s been dealt damage by a source with deathtouch since the last time state-based actions were checked, that creature is destroyed. Regeneration can replace this event.

704.5i If a planeswalker has loyalty 0, it’s put into its owner’s graveyard.

704.5j If two or more legendary permanents with the same name are controlled by the same player, that player chooses one of them, and the rest are put into their owners’ graveyards. This is called the “legend rule.”

704.5k If two or more permanents have the supertype world, all except the one that has had the world supertype for the shortest amount of time are put into their owners’ graveyards. In the event of a tie for the shortest amount of time, all are put into their owners’ graveyards. This is called the “world rule.”

704.5m If an Aura is attached to an illegal object or player, or is not attached to an object or player, that Aura is put into its owner’s graveyard.

704.5n If an Equipment or Fortification is attached to an illegal permanent or to a player, it becomes unattached from that permanent or player. It remains on the battlefield.

704.5p If a battle or creature is attached to an object or player, it becomes unattached and remains on the battlefield. Similarly, if any nonbattle, noncreature permanent that’s neither an Aura, an Equipment, nor a Fortification is attached to an object or player, it becomes unattached and remains on the battlefield.

704.5q If a permanent has both a +1/+1 counter and a -1/-1 counter on it, N +1/+1 and N -1/-1 counters are removed from it, where N is the smaller of the number of +1/+1 and -1/-1 counters on it.

704.5r If a permanent with an ability that says it can’t have more than N counters of a certain kind on it has more than N counters of that kind on it, all but N of those counters are removed from it.

704.5s If the number of lore counters on a Saga permanent is greater than or equal to its final chapter number and it isn’t the source of a chapter ability that has triggered but not yet left the stack, that Saga’s controller sacrifices it. See rule 714, “Saga Cards.”

704.5t If a player’s venture marker is on the bottommost room of a dungeon card, and that dungeon card isn’t the source of a room ability that has triggered but not yet left the stack, the dungeon card’s owner removes it from the game. See rule 309, “Dungeons.”

704.5u If a permanent with space sculptor and any creatures without a sector designation are on the battlefield, each player who controls one or more of those creatures and doesn’t control a permanent with space sculptor chooses a sector designation for each of those creatures they control. Then, each other player who controls one or more of those creatures chooses a sector designation for each of those creatures they control. See rule 702.158, “Space Sculptor.”

704.5v If a battle has defense 0 and it isn’t the source of an ability that has triggered but not yet left the stack, it’s put into its owner’s graveyard.

704.5w If a battle has no player in the game designated as its protector and no attacking creatures are currently attacking that battle, that battle’s controller chooses an appropriate player to be its protector based on its battle type. If no player can be chosen this way, the battle is put into its owner’s graveyard. See rule 310, “Battles.”

704.5x If a Siege’s controller is also its designated protector, that player chooses an opponent to become its protector. If no player can be chosen this way, the battle is put into its owner’s graveyard. See rule 310, “Battles.”

704.5y If a permanent has more than one Role controlled by the same player attached to it, each of those Roles except the one with the most recent timestamp is put into its owner’s graveyard.

704.5z If a player controls a permanent with start your engines! and that player has no speed, that player’s speed becomes 1. See rule 702.179, “Start Your Engines!”

704.6. Some variant games include additional state-based actions that aren’t normally applicable:

704.6a In a Two-Headed Giant game, if a team has 0 or less life, that team loses the game. See rule 810, “Two-Headed Giant Variant.”

704.6b In a Two-Headed Giant game, if a team has fifteen or more poison counters, that team loses the game. See rule 810, “Two-Headed Giant Variant.”

704.6c In a Commander game, a player who’s been dealt 21 or more combat damage by the same commander over the course of the game loses the game. See rule 903, “Commander.”

704.6d In a Commander game, if a commander is in a graveyard or in exile and that object was put into that zone since the last time state-based actions were checked, its owner may put it into the command zone. See rule 903, “Commander.” 

704.6e In an Archenemy game, if a non-ongoing scheme card is face up in the command zone, and no triggered abilities of any scheme are on the stack or waiting to be put on the stack, that scheme card is turned face down and put on the bottom of its owner’s scheme deck. See rule 904, “Archenemy.”

704.6f In a Planechase game, if a phenomenon card is face up in the command zone, and it isn’t the source of a triggered ability that has triggered but not yet left the stack, the planar controller planeswalks. See rule 901, “Planechase.”

704.7. If multiple state-based actions would have the same result at the same time, a single replacement effect will replace all of them.
Example: You control Lich’s Mirror, which says “If you would lose the game, instead shuffle your hand, your graveyard, and all permanents you own into your library, then draw seven cards and your life total becomes 20.” There’s one card in your library and your life total is 1. A spell causes you to draw two cards and lose 2 life. The next time state-based actions are checked, you’d lose the game due to rule 704.5a and rule 704.5b. Instead, Lich’s Mirror replaces that game loss and you keep playing.

704.8. If a state-based action results in a permanent leaving the battlefield at the same time other state-based actions were performed, that permanent’s last known information is derived from the game state before any of those state-based actions were performed.
Example: You control Young Wolf, a 1/1 creature with undying, and it has a +1/+1 counter on it. A spell puts three -1/-1 counters on Young Wolf. Before state-based actions are performed, Young Wolf has one +1/+1 counter and three -1/-1 counters on it. After state-based actions are performed, Young Wolf is in the graveyard. When it was last on the battlefield, it had a +1/+1 counter on it, so undying will not trigger.