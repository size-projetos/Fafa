---
name: budo-seedance-fight-scene
description: Generate fight scene and combat video prompts for Seedance 2.0 on Higgsfield. Use whenever the user wants action combat, martial arts, fight choreography, sword fight, brawl, melee combat, or any physical confrontation video. Triggers on: fight scene, combat, martial arts, sword fight, kung fu, karate, MMA, brawl, action sequence, boxing, fight choreography, weapon clash, or any fighting/combat video request. Use even for "make an action fight" or "two characters battle." Reads BUDOSKILL_Seedance_Base.md first for platform specs, the 2-Second Hook framework, the visual-quality vocabulary library, prompt principles, common mistakes, platform table, master template, and output workflow.
---

# BUDO — Fight Scene & Combat Videos for Seedance 2.0 on Higgsfield

> **Inherits from `BUDOSKILL_Seedance_Base.md`.** Read that file first for the shared foundation. This file adds only what's **specific to combat / fight choreography.**

---

## 1. What this vertical optimizes for

Cinematic fight scenes demand **precise choreography, dramatic camera work, and visceral impact**. The difference between amateur and professional combat video is *clarity* — the viewer must be able to read every strike, dodge, and reaction. Confusion kills tension.

Choreography is language: each strike is a phoneme, each combination is a sentence, the whole fight is a paragraph. Plan the conversation.

Quality vocabulary from Base §3 is crucial — fight scenes live on §3.2 (high-fps for slow-mo impacts), §3.4 (anamorphic + Steadicam/handheld), and §3.7 (grain for grit).

---

## 2. Fight hook library (10 hooks)

1. **Mid-Action Freeze Frame** — Cut directly into the apex of a strike — fist or blade mid-impact, combatants at maximum extension. Hold 0.5s before explosive continuation.
2. **Weapon Clash with Spark Explosion** — Two blades collide dead-center screen. Orange sparks burst radially. Camera pulls back slightly as shockwave rings.
3. **Character Charging Directly at Camera** — Aggressor sprints toward camera with wild intensity, limbs extended. Camera shakes from proximity. Stop just before impact, cut to actual fight.
4. **Slow-Motion Punch Impact** — Centered punch connects with face/body in slow motion (0.25x speed). Show skin deformation, head whipping back, eyes widening.
5. **Shockwave from Ground Slam** — Combatant slams fist or body into earth. Visible shockwave radiates outward, kicking up dust in a perfect circle.
6. **Blade Unsheathing with Metallic Flash** — Draw katana/longsword. Blade catches light with brilliant flash. Metallic ring sound (post).
7. **Aerial Kick Descending** — Combatant launches vertically, leg extended in axe kick or flying kick. Descends toward opponent at camera's eye level. Dust cloud on impact.
8. **Dual-Wield Weapon Twirl** — Character spins twin weapons in rapid succession — blades blur. Stops in power stance, weapons crossing chest.
9. **Rope/Chain Snap** — Whip or chain weapon snaps through frame with violent acceleration. Auditory crack required.
10. **Opponent Stumble/Dodge Backward** — One combatant charges; the other pivots explosively and sidesteps. Attacker's momentum carries them past camera. Chase-cam follows the dodge.

---

## 3. Fight Choreography Philosophy

**Clarity over complexity.** A single readable strike beats five blurred ones. Plan each beat.

**Action → Reaction.** Every strike needs a reaction shot. Without reaction, impact is invisible.

**Three-beat rule.** Each exchange should be readable in a three-beat rhythm: setup → strike → reaction. Stack three of these for a 6–9s sequence.

**Geometry on the ground.** Where are the combatants relative to each other and to camera? Sketch the floor plan before writing the prompt.

**Lens choice = aggression level.** Wide lenses (24mm) read as documentary/realism. Long lenses (85mm+) read as cinematic intimacy. 35mm is the sweet spot for most fight cinematography.

---

## 4. Fight Style Encyclopedia (15 disciplines)

**Unarmed:**

- **Kung Fu (Wushu)** — Spinning kicks, open-palm strikes, low sweeps, flowing evasion. Quick shuffling footwork. *"Flowing kung fu exchanges with spinning crescent kicks and rapid palm strikes."*
- **Karate** — Straight punches, high kicks, knife-hand strikes, deep stances. Linear sharp explosive. *"Sharp karate strikes with deep rooted stances and snapping full-body rotation."*
- **Muay Thai** — Elbows, knees, shin kicks, clinch work, body shots. Bouncing lateral movement. *"Brutal muay thai clinch work with flying elbows and devastating knee strikes."*
- **Capoeira** — Inverted kicks, handstands, ground sweeps, rhythmic circular motion. *"Acrobatic capoeira with inverted kicks and flowing ground-level sweeps."*
- **MMA** — Striking + grappling synthesis, clinch takedowns, ground-and-pound. *"Explosive MMA exchanges mixing striking combos with clinch wrestling."*
- **Taekwondo** — High flying kicks, spinning heel kicks, bouncy vertical extension. *"Soaring taekwondo flying kicks and spinning heel strikes."*
- **Judo / Wrestling** — Hip throws, arm drags, takedowns. Close gripping engagement. *"Explosive judo throws with dramatic arc and momentum-carrying rolls."*
- **Boxing** — Jab, cross, hook, uppercut combinations. Tight footwork. *"Boxing exchange with sharp jab-cross-hook combination and head-snap reactions."*
- **Krav Maga** — Brutal practical strikes, eye gouges, throat hits, no choreography pretense. *"Krav Maga's brutal practical exchange — knees, elbows, control of the centerline."*

**Armed:**

- **Sword / Katana / Longsword** — Overhead slashes, thrusts, parries, ripostes. *"Precise katana exchanges with overhead slashes and counter-thrusts, sparks flying."*
- **Dual Blades** — Alternating slashes, figure-eight patterns, crossing guard. *"Dual-sword combat with alternating slashes and intricate figure-eight patterns."*
- **Staff / Bo / Spear** — Sweeping arcs, thrusts, blocks. Wide spinning patterns. *"Bo staff exchanges with sweeping arcs, vertical blocks, and lunging thrusts."*
- **Nunchaku / Chain Weapons** — Whirling figure-eights, snap strikes, wrapping attacks. *"Nunchaku whirling figure-eights with lightning snap strikes."*
- **Knife / Dagger** — Close-range stabs, slashes, grabs. Tight intimate engagement. *"Knife exchange — close intimate range, slash-stab-grab tempo."*
- **Modern firearms (action choreography)** — Tactical reload, slide-stop techniques, pistol-whip transitions. *"Tactical exchange — reload-mid-roll, transitions to handgun."*

---

## 5. Choreography Keywords Library

**Strikes:** straight punch, hook, uppercut, jab, cross, knife-hand, palm-heel, elbow, knee, front kick, side kick, roundhouse kick, axe kick, spinning back kick, scissor kick, flying kick.

**Defensive moves:** parry, slip, weave, duck, sidestep, pivot, retreat, deflect, block, counter, sprawl, framing.

**Grappling / Throws:** clinch, hip throw, shoulder throw, leg sweep, takedown, ground escape, mount, guard, scramble, submission.

**Acrobatic:** backflip, cartwheel, handspring, wall-run, parkour vault, aerial twist, ground roll.

**Weapon-specific:** overhead slash, lateral cut, thrust, riposte, parry, bind, disarm, draw-cut.

---

## 6. Camera Techniques for Action

**Whip pan with strike** — Camera whips with the trajectory of a fast strike, motion-blur fills the cut.

**Lateral tracking** — Camera moves laterally with the combat. Maintains both fighters in frame.

**Push-in on reaction** — After a strike lands, push in on the receiving fighter's reaction.

**Overhead / God's-eye** — Top-down on a takedown or ground-scramble for spatial clarity.

**Handheld with energy** — Tight handheld micro-shake during exchanges, NOT during slow-mo impacts.

**Slow-mo on impact** — High-fps capture (120fps+) for impact frames, dropping back to 24fps for the rest. This is where Base §3.2 vocab earns its keep.

**Dutch tilt during chaos** — 10–20° tilt during loss-of-control moments (knockdowns, scrambles).

**Static wide for establishing** — Lock-off wide that shows full geometry. Use sparingly — usually at fight start.

---

## 7. Impact Effects

**Sparks** — Weapon clashes, metal-on-stone scrapes.
**Dust clouds** — Ground impacts, hard landings, sweeping sweeps.
**Blood mist** — Strikes to face (use restraint, depends on rating).
**Shockwave** — Cartoonish exaggeration acceptable in stylized fights; real fights use camera shake instead.
**Sweat spray** — High-impact strikes throwing sweat off the receiving fighter's face/hair.
**Cloth tear / armor deform** — Long-form impact indicator, visible damage.
**Environment debris** — Wall chips, table breaks, glass shatter on impact-with-environment.

---

## 8. Fight master-template additions

Layer onto Base §7:

```
[QUALITY VOCAB FROM BASE §3 — FIGHT STACK]
"4K crisp detail, shot on ARRI Alexa with 35mm anamorphic, mixed 24fps base
with 120fps slow-mo cut-ins, gimbal-stabilized with handheld for tight
exchanges, 35mm grain, teal-and-orange action grade."

[FIGHT STYLE FROM §4]
Pick one (or specify hybrid). Sets footwork, range, signature moves.

[GEOMETRY]
Combatants' positions relative to each other and to camera. Front-on,
side-on, opposing diagonals.

[CHOREOGRAPHY BEATS]
3–5 beats with timestamps. Each beat: setup → strike → reaction.

[IMPACT EFFECTS FROM §7]
Pick effects per beat (sparks, dust, sweat spray, etc.).

[CAMERA WORK FROM §6]
Lens, movement type, speed/handheld register, slow-mo cut-ins.
```

---

## 9. Example prompts (3)

### Example 1 — Katana Duel (16:9, 8s)

```
[GENRE / STYLE]
Genre: action. Photoreal cinematic combat register, samurai film lineage.
QUALITY VOCAB: 4K, shot on ARRI Alexa, 35mm anamorphic, 24fps base with
120fps slow-mo cut-in on the clash, gimbal-stabilized, 35mm grain, teal-
and-orange grade.
Palette: cool blue twilight, single warm torch accent, steel and black silhouettes.

[OPENING HOOK — 0 to 2s]
Hook: Blade Unsheathing with Metallic Flash. Static on the dark courtyard.
At 0.5s a katana draws from its sheath at the right of frame; the blade
catches the torch light with a brilliant flash at 1.2s. Audio: implied
metallic ring.

[MAIN ACTION — 2 to 7s]
Two swordsmen face off at 6 feet apart. At 2.5s they close in, two steps.
At 3.0s — overhead slash from the right-fighter; left-fighter parries
diagonally. At 3.5s SLOW-MO CUT (drop to 120fps for 0.8s): blades touch,
sparks burst radially from contact point. At 4.5s back to 24fps: left-
fighter pivots 90°, counter-thrusts forward; right-fighter sidesteps.
At 5.8s right-fighter executes a horizontal cut at waist-height; left-
fighter ducks under, draws their own blade for a counter at 6.5s.

[CHOREOGRAPHY BEATS]
Beat 1 (3.0–3.5s): overhead slash + diagonal parry. Reaction: blade vibration.
Beat 2 (4.5–5.8s): counter-thrust + sidestep. Reaction: pivot stance reset.
Beat 3 (5.8–7.0s): horizontal cut + duck + counter-draw. Reaction: tension hold.

[CAMERA]
35mm equivalent on the master. Slow lateral track during opening close-in.
Whip-pan with the overhead slash. Push-in to extreme close on the spark
moment during slow-mo. Pull back to wide for the sidestep. Handheld micro-
shake during fast exchanges; locked-off during slow-mo.

[LIGHTING]
3000K torch from camera-left as motivated practical, casting warm rim on
combatants' shoulders. Cool 4200K moonlight from camera-right at 30° as
ambient fill. Hard chiaroscuro overall.

[IMPACT EFFECTS]
Beat 1: sparks (5–8 individual) from blade contact, brief metallic flash.
Beat 2: dust kicked up from sidestep pivot.
Beat 3: blade trail (motion blur cyan tint) from counter-draw.

[COLOR & GRADE]
Teal in shadows, warm in highlights. Crushed blacks. Light grain.

[CLOSING BEAT — 7 to 8s]
Both combatants in mid-stance, blades raised, faces lit by torch. Held
breath. Cut to black at 8s.

[TECHNICAL]
resolution: 1080p; mode: std; genre: action; aspect_ratio: 16:9; duration: 8;
medias: [combatant reference photos as role=image]
```

### Example 2 — Muay Thai Bout (9:16, 7s)

```
[GENRE / STYLE]
Genre: action. Photoreal sports combat register.
QUALITY VOCAB: 4K crisp detail, shot on Sony Venice, 50mm prime, 24fps base
with 240fps phantom-slow-mo cut on the impact, gimbal-stabilized with
handheld bursts, 35mm grain, sweaty contrast.
Palette: ring-yellow practical light, deep red corner lights, sweat-shine.

[OPENING HOOK — 0 to 2s]
Hook: Slow-Motion Punch Impact. Pre-loaded: cut directly into an elbow
landing on the side of a fighter's head at 240fps slow-motion. Skin
deforms, head whips left, sweat sprays outward. 1.5s of slow-mo before
returning to real-time at 2.0s.

[MAIN ACTION — 2 to 6s]
Both fighters in muay thai clinch at 2.0s. Fighter A drives a knee to the
liver. Fighter B clinches harder, lateral movement to break grip. At 3.5s
they separate with a forearm shove. At 4.0s Fighter A throws a high
roundhouse — shin connects to Fighter B's shoulder (block). At 4.8s
Fighter B counters with low calf-kick. At 5.5s both reset to high guard
stance, breathing hard.

[CHOREOGRAPHY BEATS]
Beat 1 (2.0–3.5s): knee + clinch + lateral break. Footwork close.
Beat 2 (4.0–4.8s): roundhouse + block + counter calf-kick.
Beat 3 (5.5–6.0s): reset, breath, eye contact.

[CAMERA]
50mm tight on the action. Handheld with energy. Push-in on the elbow impact
during the slow-mo hook. Lateral with the lateral break. Static on the reset.

[LIGHTING]
Bright 5500K overhead ring lights with hard shadows. Red corner lights cast
red wash on each fighter when in their corner direction. Practical motivated
throughout.

[IMPACT EFFECTS]
Beat 1 hook: sweat spray on slow-mo impact, blood-mist micro-droplets.
Beat 2: dust off the canvas on the calf-kick. Breath visible as vapor in
the bright lights.

[COLOR & GRADE]
High contrast, slightly desaturated, warm midtones, deep red corner
accents preserved.

[CLOSING BEAT — 6 to 7s]
Both fighters reset, holding stance, eyes locked. Audio: deep breath
audible. Held final frame.

[TECHNICAL]
resolution: 1080p; mode: std; genre: action; aspect_ratio: 9:16; duration: 7;
medias: [fighter reference photos as role=image]
```

### Example 3 — Modern Tactical Hallway (21:9, 10s)

```
[GENRE / STYLE]
Genre: action. Photoreal tactical thriller register, John Wick lineage.
QUALITY VOCAB: 4K, shot on RED Komodo, 35mm anamorphic 2.39:1, 24fps with
selective 60fps slow-mo, gimbal-stabilized, slight teal-and-orange,
feature-film polish.
Palette: neon green emergency lights, hard fluorescent, dark steel.

[OPENING HOOK — 0 to 2s]
Hook: Character Charging Directly at Camera. Dark hallway, single neon-
green emergency light at the far end. At 0.5s a tactical operator sprints
toward the camera with handgun raised. Camera shakes slightly. Stop just
before impact at 2.0s.

[MAIN ACTION — 2 to 8s]
Cut to side-on at 2.0s — operator engages a second armed figure who emerges
from a doorway. Operator strikes the gun-arm down with their off-hand at
2.5s, pistol-whips the figure across the temple at 3.0s. Figure stumbles
back; operator follows with two close-quarter strikes (elbow, then knee)
at 3.8s. At 4.5s, second hostile appears from behind operator — they pivot,
shoulder-check, and snap-fire one round at 5.0s (60fps SLOW-MO 5.0–5.5s
for the shot). At 6.0s back to 24fps, operator clears the hallway with a
tactical reload at 6.5s.

[CHOREOGRAPHY BEATS]
Beat 1 (2.5–3.8s): strike-down + pistol-whip + elbow + knee. Tight CQB rhythm.
Beat 2 (4.5–5.5s): pivot + shoulder-check + snap-fire slow-mo.
Beat 3 (6.0–7.0s): tactical reload, slide-stop, scan corners.

[CAMERA]
35mm anamorphic. Steadicam tracking. Whip-pan from the charge to the side
master. Push-in on the pistol-whip moment. Pull-back during reload.

[LIGHTING]
Single neon-green emergency light from the hallway end. Cool 5000K
fluorescent overheads, half flickering. Anamorphic flares on every direct
light source.

[IMPACT EFFECTS]
Beat 1: blood mist on the pistol-whip (restraint), sweat spray on the elbow.
Beat 2: muzzle flash + ejected shell in slow-mo, brass falls to floor.
Beat 3: tactical efficiency — no extra effects.

[COLOR & GRADE]
Teal-and-orange. Green emergency light preserved. Crushed blacks.

[CLOSING BEAT — 8 to 10s]
Operator advances forward into the hallway, weapon raised, scanning. Final
frame: silhouetted against the green emergency light.

[TECHNICAL]
resolution: 1080p; mode: std; genre: action; aspect_ratio: 21:9; duration: 10;
medias: [operator reference photos as role=image]
```

---

## 10. Fight-specific mistakes (in addition to Base §5)

- **Choreography described as "they fight."** Useless. Specify each beat: who strikes, with what, where it lands, how the other reacts.
- **No reaction shots.** Impact without reaction is invisible. Plan reaction beats explicitly.
- **Slow-mo everywhere.** Slow-mo loses impact when overused. Reserve for 1–2 specific impact moments, return to 24fps for the rest.
- **Camera moves too fast.** Whip pans on every strike makes the action unreadable. Pick 1–2 moments for whips; static or slow-track for the rest.
- **Multiple combatants without geometry.** "Three guys attack one" without spatial layout produces visual chaos. Sketch positions.
- **Vague weapon descriptions.** "A sword" misses the style — katana, longsword, scimitar, rapier all fight differently. Name the weapon and its school.
- **No environmental engagement.** Fights that ignore the environment feel staged. Specify wall use, furniture, footing changes.

---

## 11. Final pre-publish checklist

- [ ] Fight style from §4 named
- [ ] Geometry of combatants explicitly stated
- [ ] 3–5 choreography beats with timestamps
- [ ] Each beat has setup → strike → reaction
- [ ] Slow-mo moments designated and dropped back to 24fps
- [ ] Camera movement type per beat
- [ ] Quality vocabulary stack (4–6 from Base §3, emphasis on §3.2 + §3.4 + §3.7)
- [ ] Impact effects from §7 keyed to beats
- [ ] Reference photos for combatants attached via `medias`
