603.1. Triggered abilities have a trigger condition and an effect. They are written as “[When/Whenever/At] [trigger condition or event], [effect]. [Instructions (if any).]”

603.1a A triggered ability may include instructions after its effects that limit what the ability may target or state that it can’t be countered. This text is not part of the ability’s effect. It functions while the ability is on the stack.

603.2. Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

603.2a Because they aren’t cast or activated, triggered abilities can trigger even when it isn’t legal to cast spells and activate abilities. Effects that preclude abilities from being activated don’t affect them.

603.2b When a phase or step begins, all abilities that trigger “at the beginning of” that phase or step trigger.

603.2c An ability triggers only once each time its trigger event occurs. However, it can trigger repeatedly if one event contains multiple occurrences.
Example: A permanent has an ability whose trigger condition reads, “Whenever a land is put into a graveyard from the battlefield, . . . .” If someone casts a spell that destroys all lands, the ability will trigger once for each land put into the graveyard during the spell’s resolution.

603.2d An ability may state that a triggered ability triggers additional times. In this case, rather than simply determining that such an ability has triggered, determine how many times it should trigger, then that ability triggers that many times. An effect that states that an ability triggers additional times doesn’t invoke itself repeatedly and doesn’t apply to other effects that affect how many times an ability triggers.

603.2e Some effects refer to a triggered ability of an object. Such effects refer only to triggered abilities the object has, not any delayed triggered abilities (see rule 603.7) that may be created by abilities the object has.

603.2f Some trigger events use the word “becomes” (for example, “becomes attached” or “becomes blocked”). These trigger only at the time the named event happens—they don’t trigger if that state already exists or retrigger if it persists. An ability that triggers when a permanent “becomes tapped” or “becomes untapped” doesn’t trigger if the permanent enters the battlefield in that state.
Example: An ability that triggers when a permanent “becomes tapped” triggers only when the status of a permanent that’s already on the battlefield changes from untapped to tapped.

603.2g If a triggered ability’s trigger condition is met, but the object with that triggered ability is at no time visible to all players, the ability does not trigger.

603.2h An ability triggers only if its trigger event actually occurs. An event that’s prevented or replaced won’t trigger anything.
Example: An ability that triggers on damage being dealt won’t trigger if all the damage is prevented.

603.2i A triggered ability may have an instruction followed by “Do this only once each turn.” This ability triggers only if its source’s controller has not yet taken the indicated action that turn.

603.3. Once an ability has triggered, its controller puts it on the stack as an object that’s not a card the next time a player would receive priority. See rule 117, “Timing and Priority.” The ability becomes the topmost object on the stack. It has the text of the ability that created it, and no other characteristics. It remains on the stack until it’s countered, it resolves, a rule causes it to be removed from the stack, or an effect moves it elsewhere.

603.3a A triggered ability is controlled by the player who controlled its source at the time it triggered, unless it’s a delayed triggered ability. To determine the controller of a delayed triggered ability, see rules 603.7d–f.

603.3b If multiple abilities have triggered since the last time a player received priority, the abilities are placed on the stack in a two-part process. First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn’t another ability triggering on the stack in any order they choose. (See rule 101.4.) Second, each player, in APNAP order, puts all remaining triggered abilities they control on the stack in any order they choose. Then the game once again checks for and performs state-based actions until none are performed, then abilities that triggered during this process go on the stack. This process repeats until no new state-based actions are performed and no abilities trigger. Then the appropriate player gets priority.

603.3c If a triggered ability is modal, its controller announces the mode choice when putting the ability on the stack. If one of the modes would be illegal (due to an inability to choose legal targets, for example), that mode can’t be chosen. If no mode is chosen, the ability is removed from the stack. (See rule 700.2.)

603.3d The remainder of the process for putting a triggered ability on the stack is identical to the process for casting a spell listed in rules 601.2c–d. If a choice is required when the triggered ability goes on the stack but no legal choices can be made for it, or if a rule or a continuous effect otherwise makes the ability illegal, the ability is simply removed from the stack.

603.4. A triggered ability may read “When/Whenever/At [trigger event], if [condition], [effect].” When the trigger event occurs, the ability checks whether the stated condition is true. The ability triggers only if it is; otherwise it does nothing. If the ability triggers, it checks the stated condition again as it resolves. If the condition isn’t true at that time, the ability is removed from the stack and does nothing. Note that this mirrors the check for legal targets. This rule is referred to as the “intervening ‘if’ clause” rule. (The word “if” has only its normal English meaning anywhere else in the text of a card; this rule only applies to an “if” that immediately follows a trigger condition.)
Example: Felidar Sovereign reads, “At the beginning of your upkeep, if you have 40 or more life, you win the game.” Its controller’s life total is checked as that player’s upkeep begins. If that player has 39 or less life, the ability doesn’t trigger at all. If that player has 40 or more life, the ability triggers and goes on the stack. As the ability resolves, that player’s life total is checked again. If that player has 39 or less life at this time, the ability is removed from the stack and has no effect. If that player has 40 or more life at this time, the ability resolves and that player wins the game.

603.5. Some triggered abilities’ effects are optional (they contain “may,” as in “At the beginning of your upkeep, you may draw a card”). These abilities go on the stack when they trigger, regardless of whether their controller intends to exercise the ability’s option or not. The choice is made when the ability resolves. Likewise, triggered abilities that have an effect “unless” something is true or a player chooses to do something will go on the stack normally; the “unless” part of the ability is dealt with when the ability resolves.

603.6. Trigger events that involve objects changing zones are called “zone-change triggers.” Many abilities with zone-change triggers attempt to do something to that object after it changes zones. During resolution, these abilities look for the object in the zone that it moved to. If the object is unable to be found in the zone it went to, the part of the ability attempting to do something to the object will fail to do anything. The ability could be unable to find the object because the object never entered the specified zone, because it left the zone before the ability resolved, or because it is in a zone that is hidden from a player, such as a library or an opponent’s hand. (This rule applies even if the object leaves the zone and returns again before the ability resolves.) The most common zone-change triggers are enters-the-battlefield triggers and leaves-the-battlefield triggers.

603.6a Enters-the-battlefield abilities trigger when a permanent enters the battlefield. These are written, “When [this object] enters, . . . “ or “Whenever a [type] enters, . . .” Each time an event puts one or more permanents onto the battlefield, all permanents on the battlefield (including the newcomers) are checked for any enters-the-battlefield triggers that match the event.

603.6b Continuous effects that modify characteristics of a permanent do so the moment the permanent is on the battlefield (and not before then). The permanent is never on the battlefield with its unmodified characteristics. Continuous effects don’t apply before the permanent is on the battlefield, however (see rule 603.6d).
Example: If an effect reads “All lands are creatures” and a land card is played, the effect makes the land card into a creature the moment it enters the battlefield, so it would trigger abilities that trigger when a creature enters the battlefield. Conversely, if an effect reads “All creatures lose all abilities” and a creature card with an enters-the-battlefield triggered ability enters the battlefield, that effect will cause it to lose its abilities the moment it enters the battlefield, so the enters-the-battlefield ability won’t trigger.

603.6c Leaves-the-battlefield abilities trigger when a permanent moves from the battlefield to another zone, or when a phased-in permanent leaves the game because its owner leaves the game. These are written as, but aren’t limited to, “When [this object] leaves the battlefield, . . .” or “Whenever [something] is put into a graveyard from the battlefield, . . . .” (See also rule 603.10.) An ability that attempts to do something to the card that left the battlefield checks for it only in the first zone that it went to. An ability that triggers when a card is put into a certain zone “from anywhere” is never treated as a leaves-the-battlefield ability, even if an object is put into that zone from the battlefield.

603.6d Some permanents have text that reads “[This permanent] enters with . . . ,” “As [this permanent] enters . . . ,” “[This permanent] enters as . . . ,” or “[This permanent] enters tapped.” Such text is a static ability—not a triggered ability—whose effect occurs as part of the event that puts the permanent onto the battlefield.

603.6e Some Auras have triggered abilities that trigger on the enchanted permanent leaving the battlefield. These triggered abilities can find the new object that permanent card became in the zone it moved to; they can also find the new object the Aura card became in its owner’s graveyard after state-based actions have been checked. See rule 400.7.

603.7. An effect may create a delayed triggered ability that can do something at a later time. A delayed triggered ability will contain “when,” “whenever,” or “at,” although that word won’t usually begin the ability.

603.7a Delayed triggered abilities are created during the resolution of spells or abilities, as the result of a replacement effect being applied, or as a result of a static ability that allows a player to take an action. A delayed triggered ability won’t trigger until it has actually been created, even if its trigger event occurred just beforehand. Other events that happen earlier may make the trigger event impossible.
Example: Part of an effect reads “When this creature leaves the battlefield,” but the creature in question leaves the battlefield before the spell or ability creating the effect resolves. In this case, the delayed ability never triggers.
Example: If an effect reads “When this creature becomes untapped” and the named creature becomes untapped before the effect resolves, the ability waits for the next time that creature untaps.

603.7b A delayed triggered ability will trigger only once—the next time its trigger event occurs—unless it has a stated duration, such as “this turn.” If its trigger event occurs more than once simultaneously and the ability doesn’t have a stated duration, the controller of the delayed triggered ability chooses which event causes the ability to trigger.

603.7c A delayed triggered ability that refers to a particular object still affects it even if the object changes characteristics. However, if that object is no longer in the zone it’s expected to be in at the time the delayed triggered ability resolves, the ability won’t affect it. (Note that if that object left that zone and then returned, it’s a new object and thus won’t be affected. See rule 400.7.)
Example: An ability that reads “Exile this creature at the beginning of the next end step” will exile the permanent even if it’s no longer a creature during the next end step. However, it won’t do anything if the permanent left the battlefield before then.

603.7d If a spell creates a delayed triggered ability, the source of that delayed triggered ability is that spell. The controller of that delayed triggered ability is the player who controlled that spell as it resolved.

603.7e If an activated or triggered ability creates a delayed triggered ability, the source of that delayed triggered ability is the same as the source of that other ability. The controller of that delayed triggered ability is the player who controlled that other ability as it resolved.

603.7f If a static ability generates a replacement effect which causes a delayed triggered ability to be created, the source of that delayed triggered ability is the object with that static ability. The controller of that delayed triggered ability is the same as the controller of that object at the time the replacement effect was applied.

603.7g If a static ability allows a player to take an action and creates a delayed triggered ability if that player does so, the source of that delayed triggered ability is the object with that static ability. The controller of that delayed triggered ability is the same as the controller of that object at the time the action was taken.

603.7h An activated or triggered ability may create a delayed triggered ability that triggers when the ability that created it has resolved a certain number of times in a turn. In that case, that delayed triggered ability is created only once, during the appropriate resolution of that ability.

603.8. Some triggered abilities trigger when a game state (such as a player controlling no permanents of a particular card type) is true, rather than triggering when an event occurs. These abilities trigger as soon as the game state matches the condition. They’ll go onto the stack at the next available opportunity. These are called state triggers. (Note that state triggers aren’t the same as state-based actions.) A state-triggered ability doesn’t trigger again until the ability has resolved, has been countered, or has otherwise left the stack. Then, if the object with the ability is still in the same zone and the game state still matches its trigger condition, the ability will trigger again.
Example: A permanent’s ability reads, “Whenever you have no cards in hand, draw a card.” If its controller plays the last card from their hand, the ability will trigger once and won’t trigger again until it has left the stack. If its controller casts a spell that reads “Discard your hand, then draw that many cards,” the ability will trigger during the spell’s resolution because the player’s hand was momentarily empty.

603.9. Some triggered abilities trigger specifically when a player loses the game. These abilities trigger when a player loses or leaves the game, regardless of the reason, unless that player leaves the game as the result of a draw. See rule 104.3.

603.10. Normally, objects that exist immediately after an event are checked to see if the event matched any trigger conditions, and continuous effects that exist at that time are used to determine what the trigger conditions are and what the objects involved in the event look like. However, some triggered abilities are exceptions to this rule; the game “looks back in time” to determine if those abilities trigger, using the existence of those abilities and the appearance of objects immediately prior to the event. The list of exceptions is as follows:

603.10a Some zone-change triggers look back in time. These are leaves-the-battlefield abilities, abilities that trigger when a card leaves a graveyard, and abilities that trigger when an object that all players can see is put into a hand or library.
Example: Two creatures are on the battlefield along with an artifact that has the ability “Whenever a creature dies, you gain 1 life.” Someone casts a spell that destroys all artifacts, creatures, and enchantments. The artifact’s ability triggers twice, even though the artifact goes to its owner’s graveyard at the same time as the creatures.

603.10b Abilities that trigger when a permanent phases out look back in time.

603.10c Abilities that trigger specifically when an object becomes unattached look back in time.

603.10d Abilities that trigger when a player loses control of an object or when a player’s opponent gains control of an object from that player look back in time.

603.10e Abilities that trigger when a spell is countered look back in time.

603.10f Abilities that trigger when a player loses the game look back in time.

603.10g Abilities that trigger when a player planeswalks away from a plane look back in time.

603.11. Some objects have a static ability that’s linked to one or more triggered abilities. (See rule 607, “Linked Abilities.”) These objects combine the abilities into one paragraph, with the static ability first, followed by each triggered ability that’s linked to it. A very few objects have triggered abilities which are written with the trigger condition in the middle of the ability, rather than at the beginning.
Example: An ability that reads “Reveal the first card you draw each turn. Whenever you reveal a basic land card this way, draw a card” is a static ability linked to a triggered ability.

603.12. A resolving spell or ability may allow or instruct a player to take an action and create a triggered ability that triggers “when [a player] [does or doesn’t]” take that action or “when [something happens] this way.” These reflexive triggered abilities follow the rules for delayed triggered abilities (see rule 603.7), except that they’re checked immediately after being created and trigger based on whether the trigger event or events occurred earlier during the resolution of the spell or ability that created them.
Example: Heart-Piercer Manticore has an ability that reads “When this creature enters, you may sacrifice another creature. When you do, this creature deals damage equal to that creature’s power to any target.” The reflexive triggered ability triggers only when you sacrifice another creature due to the original triggered ability, and not if you sacrifice a creature for any other reason.

603.12a Normally, if the trigger event or events occur multiple times during the resolution of the spell or ability that created it, the reflexive triggered ability will trigger once for each of those times. However, if a resolving spell or ability includes a choice to pay a cost “any number of times” and creates a triggered ability that triggers “when [a player] pays [that cost] one or more times,” paying that cost one or more times causes the reflexive triggered ability to trigger only once.