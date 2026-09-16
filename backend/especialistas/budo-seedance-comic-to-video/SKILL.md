---
name: budo-seedance-comic-to-video
description: Generate comic-page to animated-video prompts for Seedance 2.0 on Higgsfield. Use whenever the user wants to convert a comic page, manga panel, graphic novel, webtoon, or sequential art into animation. Triggers on: comic to video, manga animation, animate this comic, animate this panel, motion comic, webtoon animation, graphic novel video, panel-to-motion, sequential art animation, or any request to animate static comic-style artwork. Use even when the user uploads a comic page and says "make this move." Reads BUDOSKILL_Seedance_Base.md first for platform specs, the 2-Second Hook framework, the visual-quality vocabulary library, prompt principles, common mistakes, platform table, master template, and output workflow.
---

# BUDO — Comic-to-Video Animation for Seedance 2.0 on Higgsfield

> **Inherits from `BUDOSKILL_Seedance_Base.md`.** Read that file first for the shared foundation. This file adds only what's **specific to converting static comic / manga pages into animated video.**

---

## 1. What this vertical optimizes for

Comic-to-video conversion bridges static sequential art and dynamic motion. Seedance 2.0 is uniquely positioned for this because it respects **reference media identity** — the comic art style, character design, and panel composition pass through to the animated result.

The core challenge: a static comic page contains panels (discrete moments) that the artist *implies* connect via the gutter (the white space between panels). Animation has to fill the gutter. Your prompt's job is to describe what happens in the gutter — the motion the artist trusted the reader to imagine.

Quality vocab from Base §3 needs to match the source comic style: Western superhero = bold inked + CMYK halftone; manga = clean lines + screentone; webtoon = digital coloring + vertical flow; graphic novel = painterly. Don't impose photoreal vocab over comic art.

---

## 2. Comic-to-video hook library (10 hooks)

1. **Dramatic Panel Crack/Shatter Reveal** — The panel border literally cracks and shatters, revealing the animated scene within. Best for action climaxes, shocking revelations.
2. **Speech Bubble Pops to Life** — A dialogue bubble explodes into visibility, pulling attention to the speaker. Character mouth and gestures animate in sync. Best for dramatic declarations, comedic punchlines.
3. **Ink Splash Transition** — An ink explosion erupts across the frame, temporarily obscuring the previous panel and revealing a new scene. Best as morphing transitions between sequential panels.
4. **Page Turn Reveal** — The current panel folds or curls like a page turning, revealing the next scene beneath. Tactile book-like sensation. Best for webtoons and manga.
5. **Panel Borders Dissolve** — Rigid grid structure softens and dissolves, allowing character motion to break free. Symbolizes stillness-to-motion transition.
6. **Character Steps Out of Frame** — A foreground character steps or gestures partially out of the original panel border into 3D space.
7. **Speed Lines Become Motion Blur** — Manga-style speed lines animate into full motion blur. Converts 2D motion indicators into 3D camera/character dynamics.
8. **Spotlight or Light Flare Focus** — A light effect moves across the panel, drawing attention and triggering character animation where it lands.
9. **Thought Bubble Unfolds into Background** — A thought/dream/imagination bubble expands to become the full scene. Narrative depth transition.
10. **Background Comes Alive** — Character stays static while environmental elements (fire, water, wind, crowds) animate within the scene.

**Hook selection by scene type:**
- Action/combat → Panel Crack/Shatter or Speed Lines → Motion Blur
- Dialogue/dramatic beats → Speech Bubble Pops or Spotlight Focus
- Emotional transitions → Panel Borders Dissolve or Thought Bubble Unfolds
- Environmental storytelling → Background Comes Alive or Page Turn Reveal
- Comedic timing → Character Steps Out or Speech Bubble Pops
- Webtoon vertical → Page Turn or Spotlight for vertical flow

---

## 3. Reading-order signal (critical)

The reading order of the source comic affects camera direction in animation:

- **Western LTR (left-to-right):** Camera momentum favors left-to-right pans, characters move toward the right edge of frame ("forward").
- **Manga RTL (right-to-left):** Camera momentum reverses — right-to-left pans, characters move toward the left edge of frame ("forward" in the cultural reading sense).
- **Webtoon vertical:** Camera reads top-to-bottom, often with scroll-mimicking motion.

Always declare the reading order in the prompt so Seedance respects it.

---

## 4. Panel-to-Motion Technique Library (15 techniques)

**1. Static-to-Dynamic Stance Transition.** Character shifts from one pose to another (standing → fighting stance). Use natural weight-shift motion, preserve character silhouette throughout. Duration 0.5–2s.

**2. Dialogue Speech Pattern Animation.** Mouth, jaw, head movement, emphasis gestures. Specify the exact dialogue and language phonetics. Duration calculated from word count (~2–4s for 6–10 words).

**3. Impact Sequencing (Setup → Follow-Through).** Panel 1 setup, Panel 2 result. Animate the motion between with secondary motion (reactions, environmental disturbance, weapon trail). Duration 0.3–1s.

**4. Environmental Animation (Background Active).** Character static, environment animates — flames flicker, water flows, leaves blow, crowds shift. Duration 1–3s or continuous loop.

**5. Camera Pan from Panel to Panel.** Treat sequential panels as a continuous space. Camera pans across, revealing each panel's content in sequence.

**6. Push-In on Emotional Beat.** Static panel; camera pushes in slowly toward character's face or significant detail. Best for emotional beats or revelations.

**7. Pull-Back to Reveal Context.** Start tight on detail, pull back to reveal panel's wider context. Best for "wait, where are we?" moments.

**8. Dutch Angle for Tension.** Rotate camera off-axis to convey psychological tension or imbalance.

**9. Speed-Line Conversion.** 2D speed lines become 3D motion blur + camera tracking. Best for action shots originally drawn with stress lines.

**10. Whip Pan Between Panels.** Fast horizontal sweep simulating eye flicking between panels. Best for high-energy action sequences.

**11. Onomatopoeia Animation.** "BOOM", "CRASH", "WHAM" text animates with the impact — appears, pulses, fades. Sync timing precisely.

**12. Spotlight Reveal.** Light effect moves across panel, illuminating elements progressively.

**13. Color Shift on Emotion.** Subtle color grade shift mid-clip to match emotional beat (e.g., warm to cold on betrayal).

**14. Panel Border Animation.** The borders themselves move, distort, or break. Best for surreal or psychological scenes.

**15. Static Camera with Character Motion.** Locked-off camera; let character animation do all the work. Best for dialogue scenes and intimate beats.

---

## 5. Art Style Preservation Keywords

Match the source's visual identity:

**Western superhero comics:** heavy black ink outlines, CMYK halftone shading, high-contrast primary colors, dynamic panel composition, foreshortened anatomy, exaggerated musculature.

**Manga:** clean precise linework, screentone shading (dot patterns), monochrome with selective color, large expressive eyes, dramatic lighting, stylized hair physics.

**Manhwa / webtoon:** digital coloring with smooth gradients, vertical reading composition, soft cel shading, modern character proportions, painterly backgrounds.

**Graphic novel painterly:** visible brush strokes, painted color application, muted realistic palettes, atmospheric backgrounds.

**Indie / underground comics:** sketchy imperfect lines, limited or unconventional palette, hand-lettered text, visible paper texture.

**European bande dessinée:** clean ligne claire (clear line), flat color blocks, detailed backgrounds, restrained motion.

---

## 6. Comic master-template additions

Layer onto Base §7:

```
[READING ORDER]
LTR / RTL / vertical (webtoon) — drives camera direction.

[ART STYLE PRESERVATION]
Source style from §5. Layer specific style keywords.

[PANEL SEQUENCE BREAKDOWN]
List 2–6 panels, each with: character, environment, action, speech/sound.

[GUTTER-FILL MOTION]
What happens between Panel N and Panel N+1? The motion the artist trusted
the reader to imagine.

[TRANSITION TECHNIQUE]
Pick from §4 for each panel-to-panel transition (e.g., crack, smoke wipe,
whip pan, dissolve).

[SPEECH / SFX TIMING]
Map each dialogue line and sound effect to a specific timestamp.
```

---

## 7. Example prompts (3)

### Example 1 — Western Superhero Clash (16:9, 8s)

```
[READING ORDER] Western LTR.
[ART STYLE] Heavy black ink outlines (DC Comics register), CMYK halftone
shading in shadows, high-contrast primary colors (reds, blues, yellows),
comic-book emphasis lines around impacts, manga-influenced speed lines on
high-velocity panels.

[OPENING HOOK — 0 to 2s]
Hook: Dramatic Panel Crack/Shatter Reveal. Panel 1 visible static for 0.5s
showing Superman mid-air, fists clenched, cape billowing. At 1.0s the panel
border CRACKS and SHATTERS outward from the impact point, revealing the
animated collision moment within.

[PANEL SEQUENCE — 2 to 7s]
Panel 1 (Setup, 0-2s — used in hook):
- Superman, mid-air, body angled toward the right, cape billowing
- Metropolis skyline at twilight, buildings slightly blurred
- Action: Superman launching full-force punch toward the right
- Speech: "For Earth!" — delivered with determination at 1.5s

Panel 2 (Clash, 2-4s):
- Darkseid bracing, arms crossed defensively, face surprised/pained
- Same skyline + impact crater/shockwave radiating outward
- Action: Superman's punch connects; Darkseid's form shows the force
- SFX: "KRAAAAASSHHH" onomatopoeia animates at 2.7s, pulsing then fading

Panel 3 (Reaction, 4-7s):
- Superman in follow-through stance, still in forward motion
- Darkseid recoiling backward, buildings shaking, rubble in the air
- Speech: "You can't win, Superman..." defiant but hurt, at 5.5s

[GUTTER-FILL MOTION]
Panel 1→2: full punch travel arc, comic-book impact frame, knockback initiation
Panel 2→3: Darkseid's recoil momentum continues, dust expands outward

[CAMERA]
Pan left-to-right with Superman's movement (LTR convention). Slight push-in
during impact panel 2 for emphasis. Pull-back for panel 3 to show aftermath.

[TRANSITION TECHNIQUE]
Panel 1→2: Panel Crack/Shatter (hook). Panel 2→3: Smoke/Dust Wipe.

[CLOSING BEAT — 7 to 8s]
Dust settles slowly around Darkseid's recoiling form. Hold on final composition.

[TECHNICAL]
resolution: 1080p; mode: std; genre: action; aspect_ratio: 16:9; duration: 8;
medias: [original comic page as role=image]
```

### Example 2 — Manga Emotional Realization Scene (4:3, 6s)

```
[READING ORDER] Manga RTL.
[ART STYLE] Clean precise linework, screentone shading (visible dot patterns
in shadow areas), monochrome with one selective color accent (cherry red
ribbon), large expressive eyes, dramatic chiaroscuro lighting.

[OPENING HOOK — 0 to 2s]
Hook: Spotlight Focus. Static manga panel: two characters in a school
hallway, one foreground, one background. At 0.5s a soft spotlight effect
moves slowly from right to left across the panel (RTL reading direction),
landing on the foreground character's face at 1.7s, triggering animation.

[PANEL SEQUENCE — 2 to 5.5s]
Panel 1 (the wider hallway, 2-3.5s):
- Foreground character: realization on her face, eyes widening slowly
- Background character: turning away, expression hidden
- Subtle hair movement from corridor draft
- No dialogue — pure visual beat

Panel 2 (close-up insert, 3.5-5.5s):
- Extreme close-up of the foreground character's eye
- Single tear forming at the inner corner, swelling but not falling
- Screentone shading pulses subtly with breath
- Internal thought, single line: "...so that's how it was."
  (delivered as whisper, 4.2-5.0s)

[GUTTER-FILL MOTION]
Panel 1→2: Camera pushes from medium shot to extreme close-up over 0.8s,
smooth easing. Background character exits frame to the left (RTL direction)
during the transition.

[CAMERA]
Slow right-to-left pan throughout panel 1, then rapid push-in to extreme
close-up of the eye. RTL convention.

[TRANSITION TECHNIQUE]
Panel 1→2: Push-In on Emotional Beat (no cut — continuous camera move).

[CLOSING BEAT — 5.5 to 6s]
Tear catches the spotlight. Hold on the close-up. Final frame: the tear
about to fall, suspended.

[TECHNICAL]
resolution: 1080p; mode: std; genre: drama; aspect_ratio: 4:3; duration: 6;
medias: [original manga page as role=image]
```

### Example 3 — Webtoon Action Beat (9:16, 8s)

```
[READING ORDER] Webtoon vertical (top-to-bottom).
[ART STYLE] Digital coloring with smooth gradients, vertical composition,
soft cel shading, modern character proportions, painterly backgrounds.

[OPENING HOOK — 0 to 2s]
Hook: Speed Lines Become Motion Blur. Top of vertical frame shows a
character mid-leap, drawn with traditional 2D speed lines. At 0.5s the speed
lines animate forward, transforming into 3D motion blur trailing the
character's body as they descend through the vertical frame.

[PANEL SEQUENCE — 2 to 7s]
The whole clip reads as one continuous vertical scroll. The camera moves
downward at a steady pace.
- 2-3.5s: Character falls through air, mid-frame, scenery (forest treetops)
  scrolls past
- 3.5-5s: Character lands hard at lower-mid-frame in a crouch, dust burst
  on impact
- 5-7s: Character rises slowly, looks up (towards the camera/source of leap),
  determined expression. Background reveals a fantasy temple courtyard.

[GUTTER-FILL MOTION]
Continuous downward scroll. Character motion: falling → impact → rising in
one continuous animation, no cuts.

[CAMERA]
Vertical track downward at 3 ft/s. f/2.8 for the character; background slightly
softer.

[TRANSITION TECHNIQUE]
No panel transitions — single continuous webtoon vertical flow with the
camera moving instead of cutting.

[SFX]
"FWOOSH" onomatopoeia text appears during fall (2.5s, fades 0.5s after).
"WHAM" onomatopoeia on landing (3.7s, pulses 0.3s).

[CLOSING BEAT — 7 to 8s]
Character holds the standing pose. Hold final frame on their determined face.

[TECHNICAL]
resolution: 1080p; mode: std; genre: action; aspect_ratio: 9:16; duration: 8;
medias: [original webtoon page as role=image]
```

---

## 8. Multi-page sequencing (assembled in edit)

A full comic page or sequence typically exceeds Seedance's 15s limit. Strategy:
- Generate **one clip per 2–4 panel cluster** (8–15s each).
- Use the **last frame of clip N as the `start_image` of clip N+1** to maintain visual continuity.
- Plan the master arc on paper before generating: which clip ends on what beat, what audio bridges between.
- Assemble in a video editor with intentional gutters (brief cuts) between clips that mirror the comic's narrative pacing.

---

## 9. Comic-specific mistakes (in addition to Base §5)

- **Ignoring reading order.** Western camera momentum applied to manga (or vice versa) reads as wrong-direction. Always declare the reading order.
- **Generic motion without source style match.** Animating a Western superhero comic with anime impact frames produces dissonance. Match the technique library to the source.
- **Trying to animate the entire page in one clip.** Comic pages have 4–9 panels. One Seedance clip = 1–3 panels. Plan accordingly.
- **No reference image attached.** The source comic page MUST be passed via `medias` as `role=image` (or first panel as `start_image`). Describing the art in words loses identity.
- **Speech bubbles ignored.** Comic dialogue is part of the visual grammar. Either animate the bubbles (Hook 2) or explicitly state they're omitted in motion.
- **Photoreal quality vocab on comic art.** "8K, ray-traced" fights cel inks and screentones. Use art-style preservation keywords from §5 instead.

---

## 10. Final pre-publish checklist

- [ ] Reading order declared (LTR / RTL / vertical)
- [ ] Source comic page attached via `medias` as `role=image` or `start_image`
- [ ] Art style keywords from §5 match the source
- [ ] One hook from §2 in the first 2 seconds
- [ ] Panel sequence broken down with timing
- [ ] Gutter-fill motion explicitly described
- [ ] Transition technique named for each panel-to-panel
- [ ] Speech and SFX timing mapped
- [ ] Multi-clip plan if total page exceeds 15s
