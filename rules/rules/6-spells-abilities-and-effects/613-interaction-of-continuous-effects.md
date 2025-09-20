613.1. The values of an object’s characteristics are determined by starting with the actual object. For a card, that means the values of the characteristics printed on that card. For a token or a copy of a spell or card, that means the values of the characteristics defined by the effect that created it. Then all applicable continuous effects are applied in a series of layers in the following order:

613.1a Layer 1: Rules and effects that modify copiable values are applied.

613.1b Layer 2: Control-changing effects are applied.

613.1c Layer 3: Text-changing effects are applied. See rule 612, “Text-Changing Effects.”

613.1d Layer 4: Type-changing effects are applied. These include effects that change an object’s card type, subtype, and/or supertype.

613.1e Layer 5: Color-changing effects are applied.

613.1f Layer 6: Ability-adding effects, keyword counters, ability-removing effects, and effects that say an object can’t have an ability are applied.

613.1g Layer 7: Power- and/or toughness-changing effects are applied.

613.2. Within layer 1, apply effects in a series of sublayers in the order described below. Within each sublayer, apply effects in timestamp order (see rule 613.7). Note that dependency may alter the order in which effects are applied within a sublayer. (See rule 613.8.)

613.2a Layer 1a: Copiable effects are applied. This includes copy effects (see rule 707, “Copying Objects”) and changes to an object’s characteristics determined by merging an object with a permanent (see rule 729, “Merging with Permanents”). “As . . . enters” and “as . . . is turned face up” abilities generate copiable effects if they set power and toughness, even if they also define other characteristics.

613.2b Layer 1b: Face-down spells and permanents have their characteristics modified as defined in rule 708.2.

613.2c After all rules and effects in layer 1 have been applied, the object’s characteristics are its copiable values. (See rule 707.2.)

613.3. Within layers 2–6, apply effects from characteristic-defining abilities first (see rule 604.3), then all other effects in timestamp order (see rule 613.7). Note that dependency may alter the order in which effects are applied within a layer. (See rule 613.8.)

613.4. Within layer 7, apply effects in a series of sublayers in the order described below. Within each sublayer, apply effects in timestamp order. (See rule 613.7.) Note that dependency may alter the order in which effects are applied within a sublayer. (See rule 613.8.)

613.4a Layer 7a: Effects from characteristic-defining abilities that define power and/or toughness are applied. See rule 604.3.

613.4b Layer 7b: Effects that set power and/or toughness to a specific number or value are applied. Effects that refer to the base power and/or toughness of a creature apply in this layer.

613.4c Layer 7c: Effects and counters that modify power and/or toughness (but don’t set power and/or toughness to a specific number or value) are applied.

613.4d Layer 7d: Effects that switch a creature’s power and toughness are applied. Such effects take the value of power and apply it to the creature’s toughness, and take the value of toughness and apply it to the creature’s power.
Example: A 1/3 creature is given +0/+1 by an effect. Then another effect switches the creature’s power and toughness. Its new power and toughness is 4/1. A new effect gives the creature +5/+0. Its “unswitched” power and toughness would be 6/4, so its actual power and toughness is 4/6.
Example: A 1/3 creature is given +0/+1 by an effect. Then another effect switches the creature’s power and toughness. Its new power and toughness is 4/1. If the +0/+1 effect ends before the switch effect ends, the creature becomes 3/1.
Example: A 1/3 creature is given +0/+1 by an effect. Then another effect switches the creature’s power and toughness. Then another effect switches its power and toughness again. The two switches essentially cancel each other, and the creature becomes 1/4.

613.5. The application of continuous effects as described by the layer system is continually and automatically performed by the game. All resulting changes to an object’s characteristics are instantaneous.
Example: Honor of the Pure is an enchantment that reads “White creatures you control get +1/+1.” Honor of the Pure and a 2/2 black creature are on the battlefield under your control. If an effect then turns the creature white (layer 5), it gets +1/+1 from Honor of the Pure (layer 7c), becoming 3/3. If the creature’s color is later changed to red (layer 5), Honor of the Pure’s effect stops applying to it, and it will return to being 2/2.
Example: Gray Ogre, a 2/2 creature, is on the battlefield. An effect puts a +1/+1 counter on it (layer 7c), making it 3/3. A spell targeting it that says “Target creature gets +4/+4 until end of turn” resolves (layer 7c), making it 7/7. An enchantment that says “Creatures you control get +0/+2” enters the battlefield (layer 7c), making it 7/9. An effect that says “Target creature becomes 0/1 until end of turn” is applied to it (layer 7b), making it 5/8 (0/1, with +4/+4 from the resolved spell, +0/+2 from the enchantment, and +1/+1 from the counter).

613.6. If an effect should be applied in different layers and/or sublayers, the parts of the effect each apply in their appropriate ones. If an effect starts to apply in one layer and/or sublayer, it will continue to be applied to the same set of objects in each other applicable layer and/or sublayer, even if the ability generating the effect is removed during this process.
Example: An effect that reads “This creature gets +1/+1 and becomes the color of your choice until end of turn” is both a power- and toughness-changing effect and a color-changing effect. The “becomes the color of your choice” part is applied in layer 5, and then the “gets +1/+1” part is applied in layer 7c.
Example: Act of Treason has an effect that reads “Gain control of target creature until end of turn. Untap that creature. It gains haste until end of turn.” This is both a control-changing effect and an effect that adds an ability to an object. The “gain control” part is applied in layer 2, and then the “it gains haste” part is applied in layer 6.
Example: An effect that reads “All noncreature artifacts become 2/2 artifact creatures until end of turn” is both a type-changing effect and a power- and toughness-setting effect. The type-changing effect is applied to all noncreature artifacts in layer 4 and the power- and toughness-setting effect is applied to those same permanents in layer 7b, even though those permanents aren’t noncreature artifacts by then.
Example: Svogthos, the Restless Tomb, is on the battlefield. An effect that says “Until end of turn, target land becomes a 3/3 creature that’s still a land” is applied to it (layers 4 and 7b). An effect that says “Target creature gets +1/+1 until end of turn” is applied to it (layer 7c), making it a 4/4 land creature. Then while you have ten creature cards in your graveyard, you activate Svogthos’s ability: “Until end of turn, this land becomes a black and green Plant Zombie creature with ‘This creature’s power and toughness are each equal to the number of creature cards in your graveyard.’ It’s still a land.” (layers 4, 5, and 7b). It becomes an 11/11 land creature. If a creature card enters or leaves your graveyard, Svogthos’s power and toughness will be modified accordingly. If the first effect is applied to it again, it will become a 4/4 land creature again.

613.7. Within a layer or sublayer, determining which order effects are applied in is usually done using a timestamp system. An effect with an earlier timestamp is applied before an effect with a later timestamp.

613.7a A continuous effect generated by a static ability has the same timestamp as the object the static ability is on, or the timestamp of the effect that created the ability, whichever is later. If the effect that created the ability has the later timestamp and the object the ability is on receives a new timestamp, each continuous effect generated by static abilities of that object receives a new timestamp as well, but the relative order of those timestamps remains the same.
Example: Rune of Flight is an Aura that grants enchanted Equipment “Equipped creature has flying.” A player attaches Rune of Flight to Colossus Hammer, an Equipment with “Equipped creature gets +10/+10 and loses flying.” The ability granted by Rune of Flight shares Rune of Flight’s timestamp because it is later than Colossus Hammer’s timestamp. If Colossus Hammer becomes attached to a creature, both of its abilities receive new timestamps (see rule 613.7e), but the relative order of those timestamps remains the same.

613.7b A continuous effect generated by the resolution of a spell or ability receives a timestamp at the time it’s created.

613.7c Each counter receives a timestamp as it’s put on an object or player. If that object or player already has a counter of that kind on it, each counter of that kind receives a new timestamp identical to that of the new counter.

613.7d An object receives a timestamp at the time it enters a zone.

613.7e An Aura, Equipment, or Fortification receives a new timestamp each time it becomes attached to an object or player.

613.7f A permanent receives a new timestamp each time it turns face up or face down.

613.7g A double-faced permanent receives a new timestamp each time it transforms or converts.

613.7h A face-up plane card, phenomenon card, or scheme card receives a timestamp at the time it’s turned face up.

613.7i A face-up vanguard card receives a timestamp at the beginning of the game.

613.7j A conspiracy card receives a timestamp at the beginning of the game. If it’s face down, it receives a new timestamp at the time it turns face up.

613.7k A sticker receives a new timestamp each time it’s put on an object. If the object a sticker is on receives a new timestamp, the sticker receives a new timestamp immediately after that one. If the object a sticker is on becomes part of a merged permanent on the battlefield, the sticker receives a new timestamp at that time. If an object has more than one sticker on it as it enters a zone or becomes part of a merged permanent, the relative timestamp order of those stickers remains unchanged.

613.7m If two or more objects would receive a timestamp simultaneously, such as by entering a zone simultaneously or becoming attached simultaneously, their relative timestamps are determined in APNAP order (see rule 101.4). Objects controlled by the active player (or owned by the active player, if they have no controller) have an earlier relative timestamp in the order of that player’s choice, followed by each other player in turn order.

613.7n If a continuous effect generated by a static ability of an object and a continuous effect generated by a resolving spell or ability that applies to that object would receive a timestamp simultaneously, such as due to an effect that puts that object onto the battlefield and sets its characteristics (see rule 611.2e), the continuous effect from the object’s own static ability receives an earlier relative timestamp.

613.8. Within a layer or sublayer, determining which order effects are applied in is sometimes done using a dependency system. If a dependency exists, it will override the timestamp system.

613.8a An effect is said to “depend on” another if (a) it’s applied in the same layer (and, if applicable, sublayer) as the other effect; (b) applying the other would change the text or the existence of the first effect, what it applies to, or what it does to any of the things it applies to; and (c) neither effect is from a characteristic-defining ability or both effects are from characteristic-defining abilities. Otherwise, the effect is considered to be independent of the other effect.

613.8b An effect dependent on one or more other effects waits to apply until just after all of those effects have been applied. If multiple dependent effects would apply simultaneously in this way, they’re applied in timestamp order relative to each other. If several dependent effects form a dependency loop, then this rule is ignored and the effects in the dependency loop are applied in timestamp order.

613.8c After each effect is applied, the order of remaining effects is reevaluated and may change if an effect that has not yet been applied becomes dependent on or independent of one or more other effects that have not yet been applied.

613.9. One continuous effect can override another. Sometimes the results of one effect determine whether another effect applies or what another effect does.
Example: Two effects are affecting the same creature: one from an Aura that says “Enchanted creature has flying” and one from an Aura that says “Enchanted creature loses flying.” Neither of these depends on the other, since nothing changes what they affect or what they’re doing to it. Applying them in timestamp order means the one that was generated last “wins.” The same process would be followed, and the same result reached, if either of the effects had a duration (such as “Target creature loses flying until end of turn”) or came from a non-Aura source (such as “All creatures lose flying”).
Example: One effect reads, “White creatures get +1/+1,” and another reads, “Enchanted creature is white.” The enchanted creature gets +1/+1 from the first effect, regardless of its previous color.

613.10. Some continuous effects affect players rather than objects. For example, an effect might give a player protection from red. All such effects are applied in timestamp order after the determination of objects’ characteristics. See also the rules for timestamp order and dependency (rules 613.7 and 613.8).

613.11. Some continuous effects affect game rules rather than objects. For example, effects may modify a player’s maximum hand size, or say that a creature must attack this turn if able. These effects are applied after all other continuous effects have been applied. Continuous effects that affect the costs of spells or abilities are applied according to the order specified in rule 601.2f. All other such effects are applied in timestamp order. See also the rules for timestamp order and dependency (rules 613.7 and 613.8).