120.1. Objects can deal damage to battles, creatures, planeswalkers, and players. This is generally detrimental to the object or player that receives that damage. An object that deals damage is the source of that damage.

120.1a Damage can’t be dealt to an object that’s not a battle, a creature, or a planeswalker.

120.2. Any object can deal damage.

120.2a Damage may be dealt as a result of combat. Each attacking and blocking creature deals combat damage equal to its power during the combat damage step.

120.2b Damage may be dealt as an effect of a spell or ability. The spell or ability will specify which object deals that damage.

120.3. Damage may have one or more of the following results, depending on whether the recipient of the damage is a player or permanent, the characteristics of the damage’s source, and the characteristics of the damage’s recipient (if it’s a permanent).

120.3a Damage dealt to a player by a source without infect causes that player to lose that much life.

120.3b Damage dealt to a player by a source with infect causes that source’s controller to give the player that many poison counters.

120.3c Damage dealt to a planeswalker causes that many loyalty counters to be removed from that planeswalker.

120.3d Damage dealt to a creature by a source with wither and/or infect causes that source’s controller to put that many -1/-1 counters on that creature.

120.3e Damage dealt to a creature by a source with neither wither nor infect causes that much damage to be marked on that creature.

120.3f Damage dealt by a source with lifelink causes that source’s controller to gain that much life, in addition to the damage’s other results.

120.3g Combat damage dealt to a player by a creature with toxic causes that creature’s controller to give the player a number of poison counters equal to that creature’s total toxic value, in addition to the damage’s other results. See rule 702.164, “Toxic.”

120.3h Damage dealt to a battle causes that many defense counters to be removed from that battle.

120.4. Damage is processed in a four-part sequence.

120.4a First, if an effect that’s causing damage to be dealt states that excess damage that would be dealt to a permanent is dealt to another permanent or player instead, the damage event is modified accordingly. If the first permanent is a creature, the excess damage is the amount of damage in excess of what would be lethal damage, taking into account damage already marked on the creature and damage from other sources that would be dealt at the same time. (See rule 120.6.) Any amount of damage greater than 1 is excess damage if the source dealing that damage to a creature has deathtouch. (See rule 702.2.) If the first permanent is a planeswalker, the excess damage is the amount of damage in excess of that planeswalker’s loyalty, taking into account damage from other sources that would be dealt at the same time. If the first permanent is a battle, the excess damage is the amount of damage in excess of that battle’s defense, taking into account damage from other sources that would be dealt at the same time. If the first permanent has multiple card types from among the list of creature, planeswalker, and battle, the excess damage is the greatest of the calculated amounts for each of the card types it has.

120.4b Second, damage is dealt, as modified by replacement and prevention effects that interact with damage. (See rule 614, “Replacement Effects,” and rule 615, “Prevention Effects.”) Abilities that trigger when damage is dealt trigger now and wait to be put on the stack.

120.4c Third, damage that’s been dealt is processed into its results, as modified by replacement effects that interact with those results (such as life loss or counters).

120.4d Finally, the damage event occurs.
Example: A player who controls Boon Reflection, an enchantment that says “If you would gain life, you gain twice that much life instead,” attacks with a 3/3 creature with wither and lifelink. It’s blocked by a 2/2 creature, and the defending player casts a spell that prevents the next 2 damage that would be dealt to the blocking creature. The damage event starts out as [3 damage is dealt to the 2/2 creature, 2 damage is dealt to the 3/3 creature]. The prevention effect is applied, so the damage event becomes [1 damage is dealt to the 2/2 creature, 2 damage is dealt to the 3/3 creature]. That’s processed into its results, so the damage event is now [one -1/-1 counter is put on the 2/2 creature, the active player gains 1 life, 2 damage is marked on the 3/3 creature]. Boon Reflection’s effect is applied, so the damage event becomes [one -1/-1 counter is put on the 2/2 creature, the active player gains 2 life, 2 damage is marked on the 3/3 creature]. Then the damage event occurs.
Example: The defending player controls a creature and Worship, an enchantment that says “If you control a creature, damage that would reduce your life total to less than 1 reduces it to 1 instead.” That player is at 2 life, and is being attacked by two unblocked 5/5 creatures. The player casts Awe Strike, which says “The next time target creature would deal damage this turn, prevent that damage. You gain life equal to the damage prevented this way,” targeting one of the attackers. The damage event starts out as [10 damage is dealt to the defending player]. Awe Strike’s effect is applied, so the damage event becomes [5 damage is dealt to the defending player, the defending player gains 5 life]. That’s processed into its results, so the damage event is now [the defending player loses 5 life, the defending player gains 5 life]. Worship’s effect sees that the damage event would not reduce the player’s life total to less than 1, so Worship’s effect is not applied. Then the damage event occurs.

120.5. Damage dealt to a creature, planeswalker, or battle doesn’t destroy it. Likewise, the source of that damage doesn’t destroy it. Rather, state-based actions may destroy a creature or otherwise put a permanent into its owner’s graveyard, due to the results of the damage dealt to that permanent. See rule 704.
Example: A player casts Lightning Bolt, an instant that says “Lightning Bolt deals 3 damage to any target,” targeting a 2/2 creature. After Lightning Bolt deals 3 damage to that creature, the creature is destroyed as a state-based action. Neither Lightning Bolt nor the damage dealt by Lightning Bolt destroyed that creature.

120.6. Damage marked on a creature remains until the cleanup step, even if that permanent stops being a creature. If the total damage marked on a creature is greater than or equal to its toughness, that creature has been dealt lethal damage and is destroyed as a state-based action (see rule 704). All damage marked on a permanent is removed when it regenerates (see rule 701.19, “Regenerate”) and during the cleanup step (see rule 514.2).

120.7. The source of damage is the object that dealt it. If an effect requires a player to choose a source of damage, they may choose a permanent; a spell on the stack (including a permanent spell); any object referred to by an object on the stack, by a prevention or replacement effect that’s waiting to apply, or by a delayed triggered ability that’s waiting to trigger (even if that object is no longer in the zone it used to be in); or a face-up object in the command zone. A source doesn’t need to be capable of dealing damage to be a legal choice. See rule 609.7, “Sources of Damage.”

120.8. If a source would deal 0 damage, it does not deal damage at all. That means abilities that trigger on damage being dealt won’t trigger. It also means that replacement effects that would increase the damage dealt by that source, or would have that source deal that damage to a different object or player, have no event to replace, so they have no effect.

120.9. If an ability triggers on damage being dealt by a specific source or sources, and the effect refers to the “damage dealt,” it refers only to the damage dealt by the specified sources and not to any damage dealt at the same time by other sources.

120.10. Some triggered abilities check whether a permanent has been dealt excess damage. These abilities check after the permanent has been dealt damage by one or more sources. If those sources together dealt an amount of damage to a creature greater than lethal damage, excess damage equal to the difference was dealt to that creature. If those sources together dealt an amount of damage to a planeswalker greater than that planeswalker’s loyalty before the damage was dealt, excess damage equal to the difference was dealt to that planeswalker. If those sources together dealt an amount of damage to a battle greater than that battle’s defense before the damage was dealt, excess damage equal to the difference was dealt to that battle. If a permanent has multiple card types from among the list of creature, planeswalker, and battle, the excess damage dealt to that permanent is the greatest of the calculated amounts for each of the card types it has.