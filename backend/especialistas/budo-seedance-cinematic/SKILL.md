---
name: budo-seedance-cinematic
description: Generate cinematic film-style video prompts for Seedance 2.0 on Higgsfield. Use whenever the user wants cinematic, film-like, movie-quality, Hollywood-style, dramatic, or professional film-quality AI video. Triggers on: cinematic, film look, movie scene, dramatic lighting, depth of field, lens flare, anamorphic, letterbox, noir, epic, Steadicam, dolly, crane shot, or any cinematic video generation request. Always use this skill even if the user doesn't explicitly say "cinematic" but describes a film-like aesthetic. Reads BUDOSKILL_Seedance_Base.md first for platform specs, the 2-Second Hook framework, the visual-quality vocabulary library, prompt principles, common mistakes, platform table, master template, and output workflow.
---

# BUDO — Cinematic Film-Style Videos for Seedance 2.0 on Higgsfield

> **Inherits from `BUDOSKILL_Seedance_Base.md`.** Read that file first for the shared foundation. This file adds only what's **specific to cinematic / feature-film aesthetics.** Use the photoreal quality vocabulary from Base §3 heavily — cinematic is where it shines.

---

## 1. What this vertical optimizes for

Cinematic register transforms generative video into **production-grade film moments**. The difference between "a video" and "a cinematic video" is *intentionality*: every frame answers questions about lens, light, color, motion, and meaning.

Reference points for visual register: *Blade Runner 2049* (neon city glow), *Dunkirk* (immediate chaos), *1917* (tracking-shot tension), *The Revenant* (natural-light cinematography), *Joker* (gritty grain + isolated frame), *No Country for Old Men* (composed stillness).

Quality vocabulary from Base §3 is essential here. Layer aggressively: resolution + camera body + lens + grade + film texture + production-value tag.

---

## 2. Cinematic hook library (12 hooks)

1. **Extreme Close-Up Snap to Wide Reveal** — Open with macro of a detail (water droplet, fabric weave). At 0.5s, whip-cut to extreme wide shot. Disorientation → context clarity.
2. **Black Screen to Dramatic Light Burst** — Pure black, complete silence. At 0.8s, explosive light burst from a corner; lens flare blooms.
3. **Reverse Motion** — Action moves backward in the first 2 seconds — water droplets float upward, smoke swirls counter-clockwise. Unnatural = immediately interesting.
4. **Unexpected Scale — Macro of Familiar Object** — Extreme macro of fabric, concrete, leaf veins. Treat as a vast landscape. Viewer doesn't recognize scale for 2 seconds.
5. **Silent Beat Then Explosive Sound** — Complete silence 1.2s, then sudden violent sound (gunshot, slam, music drop) synchronized with video freeze/cut/blur.
6. **Extreme Color Shift** — Cool desaturated blue-grey → at 0.6s, sudden warm amber-gold or saturated neon. 50% color shift in 0.4s.
7. **Fast Movement Entering Frame** — Speeding car, sprinting figure, falling object enters from edge (not center). Creates leading lines.
8. **Extreme Rack Focus** — Two planes both sharp initially. At 1s, focus racks dramatically. Shallow depth (f/1.4 cinema).
9. **Stark Geometric Contrast** — Extreme geometric contrast — sharp horizontals vs verticals, circles vs straight edges. High-contrast lighting emphasizes geometry.
10. **Protagonist's Eyes Open/Look** — Close shot of eyes in low-light. At 0.8s, eyes snap open or lock on-camera. Dilating pupil. Primal attention grab.
11. **Disorienting Camera Rotation** — 45°–180° rotation, tilted horizon, slight vertigo. Stabilizes to level at 2s.
12. **Scale Impossibility** — Tiny human in impossibly vast landscape, or giant object in confined space. 5 seconds to realize the trick.

**Hook stacking:** layer 2–3 hooks in the opening for maximum impact (e.g., black screen + color burst + extreme close-up).

---

## 3. Camera Language (15 foundational techniques)

**1. Establishing Shot.** Wide frame, 2–3 planes of depth. *"24–35mm equivalent, pan slowly across landscape revealing foreground / mid-ground / background context."*

**2. Push-In / Dolly Forward.** Increases intimacy and tension. *"Slow dolly forward at 1.5 ft/s, 50mm equivalent, maintain f/2.0."*

**3. Pull-Out / Dolly Back.** Reveals context, scale, isolation. *"Camera retreats at 2 ft/s revealing the protagonist becomes smaller as the world opens around them."*

**4. Tracking Shot.** Follows subject laterally. *"Steadicam tracking left-to-right alongside the subject's walking pace."*

**5. Orbit / Arc.** Circles subject. *"Slow 180° arc around stationary subject, maintains center framing, reveals different facets of context."*

**6. Crane / Jib.** Vertical movement of camera. *"Crane rises from eye-level to 30 feet over 4 seconds, revealing surrounding architecture."*

**7. Whip Pan.** Fast horizontal rotation; for transitions or chaos. *"Whip pan 180° in 0.3s; motion blur fills the cut."*

**8. Static Hold.** Camera doesn't move. *"Locked-off static frame; let the subject move within composition."*

**9. Handheld.** Subtle organic instability. *"Handheld with micro-shake; documentary feel."*

**10. POV.** First-person viewpoint. *"POV from the protagonist's eyes; what they see, including limbs in lower frame."*

**11. Dutch Angle.** Tilted horizon for tension. *"Camera tilted 15° off-axis; suggests psychological imbalance."*

**12. Low Angle.** Looking up at subject. *"Camera at floor level, looking up at 30°; makes subject heroic or imposing."*

**13. High Angle.** Looking down at subject. *"Camera 20 feet above, looking down at 60°; makes subject vulnerable or small."*

**14. Rack Focus Pull.** Shift focus between planes. *"Focus racks from foreground to background over 0.8s; both planes maintained as visible reference."*

**15. Tableau / Composed Frame.** Static painterly composition. *"Symmetrical frame, centered subject, classical golden-ratio composition; held still for 3 seconds."*

---

## 4. Lighting & Atmosphere Library

**Chiaroscuro** — Hard high-contrast light vs deep shadow. Single key, no fill.
**Rembrandt lighting** — Key light 45° to subject creates triangle of light on shadow-side cheek.
**Butterfly / Paramount lighting** — Key directly above subject creates butterfly-shaped shadow under nose.
**Clamshell** — Two soft sources, above and below; flattering, beauty-standard.
**Backlight / Rim** — Strong light from behind subject, creating outline glow.
**Practical** — Visible light source in frame (lamp, neon sign, window).
**Motivated** — Lighting that has a visible justification in the scene.
**Hard noir** — Single hard key, deep blacks, hard-edged shadows, fill at 10%.
**High-key** — Bright, low-contrast, minimal shadow; commercial / sitcom register.
**Low-key** — Predominantly shadow with selective illumination; thriller / drama.
**Volumetric / Atmospheric** — Visible light rays through dust, fog, smoke (god rays).
**Golden hour** — Low warm sun, long shadows, soft horizontal light.
**Blue hour** — Cool ambient pre-dawn or post-sunset; deep blue sky, no sun.
**Magic hour** — The brief window when sky is twilight blue and tungsten interiors glow warm.

---

## 5. Color Grading Presets

**Teal-and-orange** — Modern Hollywood standard. Cool shadows, warm midtones/highlights. Most blockbusters.
**Bleach bypass** — Crushed blacks elevated to dark grey, greys elevated, compressed contrast, heavy grain, 0–20% saturation. *Saving Private Ryan, Minority Report.*
**Cross-process** — Color channels shifted off-balance. Greens push toward yellow, blues push toward teal. *Wes Anderson tilted.*
**Day-for-night** — Footage shot in daylight graded to look like night. Blue-heavy, crushed shadows, isolated highlights.
**Sepia / monochrome** — Period, memory, dream sequences.
**Kodak Vision3 / Portra emulation** — Warm, organic, slight grain, milky highlights.
**Fujifilm Eterna emulation** — Cooler, restrained saturation, professional/documentary feel.
**Cinematic LogC** — Flat capture grade; allows maximum grading flexibility downstream.
**Dolby Vision HDR** — Extreme dynamic range; highlights retain detail at full brightness.

---

## 6. Cinematic master-template additions

Layer onto Base §7. This is where the Base §3 vocabulary library shines:

```
[QUALITY VOCAB — STACK AGGRESSIVELY FROM BASE §3]
Example: "8K, ultra-HD, shot on ARRI Alexa LF, Cooke S4 anamorphic 2.39:1,
f/1.4 shallow depth, 24fps theatrical cadence, teal-and-orange grade,
Kodak Vision3 emulation, 35mm film grain, halation on highlights,
feature-film production value."

[CAMERA TECHNIQUE FROM §3]
Pick 1–2 techniques and specify speed in physical units (ft/s).

[LIGHTING FROM §4]
Pick one named setup. Specify direction, color temperature in K, key-to-fill ratio.

[GRADE FROM §5]
Pick one named grade.

[REFERENCE FILM (optional)]
Name 1 visual reference: "in the register of Roger Deakins' Blade Runner 2049"
or "Emmanuel Lubezki's The Revenant natural-light grammar".
```

---

## 7. Example prompts (3)

### Example 1 — Film Noir Detective Moment (16:9, 10s)

```
[GENRE / STYLE]
Genre: noir. Feature-film noir register.
QUALITY VOCAB: 8K, shot on ARRI Alexa LF, 35mm cinema lens, f/2.0 shallow,
24fps theatrical, bleach bypass grade, 150% 35mm film grain, Roger Deakins
visual reference.
Palette: cool blue-grey shadows, single warm tungsten accent, no saturation
outside skin tone.

[OPENING HOOK — 0 to 2s]
Hook: Black Screen to Dramatic Light Burst + silent beat. Pure black,
complete silence. At 0.8s, sudden explosion of cool blue 5000K light from
upper-left corner — single harsh fluorescent. Hard-edged shadow stripes
across the center of frame.

[ESTABLISHING CONTEXT — 2 to 4s]
Location: 1940s noir warehouse interior. Cool grey concrete, visible metal
beams overhead. Camera 40 feet back, low angle 15° looking up.

[PRIMARY ACTION — 4 to 8s]
Slow dolly forward at 1.5 ft/s. Silhouette of detective figure materializes
in shadow-pool center-frame, motionless. At 5.5s, his face catches the edge
of overhead light — eye glint visible in shadow. Subtle head turn. At 6s,
he pulls a cigarette from pocket (silhouette action).

[CAMERA]
35mm cinema lens, f/2.0 shallow. Focus locked on detective face through dolly,
no focus breathing. Constant 1.5 ft/s velocity, no acceleration.

[LIGHTING — Hard Noir]
Single hard 3000K key from upper-left at 60°, creating extreme shadow pattern
across floor. Minimal fill at 15%. Chiaroscuro setup, deep blacks lifted to
dark grey by bleach bypass.

[COLOR & GRADE]
Bleach bypass noir grading: crushed blacks elevated (dark grey, not pure 0),
greys elevated, compressed contrast range. 0% color saturation. Grain visible
at 150% opacity. Only white light sources and skin tone retain slight warm
cast (2500K). Cold blue shadows.

[CLIMAX MOMENT — 8 to 10s]
At 8s, detective lights cigarette — small flame visible near face. Light
reveals weathered grim expression. At 8.3s, second light source (desk lamp,
practical) flicks on frame-right. Two-source conflicting shadows. He turns
toward camera-left. At 9.5s, fade to black; single remaining light keeps
silhouette profile.

[AUDIO]
0–1s: silence. 1–4s: subtle jazz trumpet enters, low (-6dB). 4–7s: foley
(footsteps on concrete, clothing rustle). 8–8.3s: match-scratch lighter
sound. 8.5–10s: music swells.

[TECHNICAL]
resolution: 1080p; mode: std; genre: noir; aspect_ratio: 16:9; duration: 10
```

### Example 2 — Epic Landscape Establishing Shot (21:9, 12s)

```
[GENRE / STYLE]
Genre: epic. Feature-film widescreen register.
QUALITY VOCAB: 8K, ultra-HD, shot on RED Komodo, anamorphic 2.39:1, golden
hour cinematography, teal-and-orange grade, Kodak Vision3 emulation,
Emmanuel Lubezki natural-light reference, theatrical-quality polish.
Palette: warm gold dominant, deep teal sky, long blue shadows.

[OPENING HOOK — 0 to 2s]
Hook: Scale Impossibility. Extreme wide aerial — a tiny figure of a single
person walking across a vast salt flat. Sky fills upper 70% of frame.

[MAIN ACTION — 2 to 10s]
Crane descent from 200 feet to 30 feet over 8 seconds, slowly approaching the
walking figure. Person's pace is unhurried, methodical. At 6s, they stop;
turn to face the rising sun (off-camera left). At 8s, slight smile catches
the light. Their breath visible in cool air.

[CAMERA]
24mm equivalent on the wide aerial; 50mm on the descent close. Anamorphic
flare on every direct light source. f/4 for landscape depth, racks to f/2.0
on the close approach.

[LIGHTING — Golden Hour]
3000K sun low at 10° above horizon, camera-left. Hard directional. Long
shadows extending right across the salt. Practicals: none — natural only.

[COLOR & GRADE]
Teal-and-orange. Sky teal at the zenith, gold at the horizon. Shadow side
of figure desaturated blue; lit side warm gold. Kodak Vision3 organic milky
highlights. Light 35mm grain.

[CLOSING BEAT — 10 to 12s]
Camera comes to rest at eye level, figure framed against the sun. Anamorphic
horizontal lens flare cuts across the frame. Held still.

[TECHNICAL]
resolution: 1080p; mode: std; genre: epic; aspect_ratio: 21:9; duration: 12
```

### Example 3 — Intimate Drama Moment (16:9, 8s)

```
[GENRE / STYLE]
Genre: drama. Feature-film intimate register.
QUALITY VOCAB: 8K, shot on Sony Venice, Cooke S4 50mm, f/1.4 cinematic depth,
24fps theatrical, motivated lighting, Portra 400 look, KyoAni-like emotional
restraint (cinematic version, photoreal), feature-film production value.
Palette: warm tungsten interior, cool blue twilight outside, low saturation.

[OPENING HOOK — 0 to 1.5s]
Hook: Protagonist's Eyes. Extreme close-up of a woman's eyes in low light.
At 0.8s, she blinks once slowly. Pupils dilate slightly as we hold.

[MAIN ACTION — 1.5 to 6s]
Slow pull-out at 0.8 ft/s reveals she's at a kitchen table, evening light
through window behind. A phone sits on the table; she's not looking at it.
At 3.5s she lifts a hand to her mouth, fingers touching her lower lip — held
gesture. At 5s, she finally looks at the phone.

[CAMERA]
50mm equivalent, f/1.4 (background falls to soft bokeh). Steadicam, almost-
imperceptible breathing micro-movement. Pull-out velocity constant.

[LIGHTING — Motivated]
Single 3000K tungsten practical at upper-right (kitchen pendant), warm bounce
on her face. Cool 4500K blue window light from left, soft. Two-source split
register. No fill.

[COLOR & GRADE]
Portra 400 look. Warm tungsten right side of face, cool blue left. Light
grain. Saturation 70%.

[CLOSING BEAT — 6 to 8s]
She reaches toward the phone. Camera stops just as her hand enters the bokeh
of focus near the phone. Hold on the gesture, undecided. Cut to black at 8s.

[TECHNICAL]
resolution: 1080p; mode: std; genre: drama; aspect_ratio: 16:9; duration: 8
```

---

## 8. Cinematic-specific mistakes (in addition to Base §5)

- **"Cinematic" as adjective only.** Without specifying camera, lens, light, and grade, "cinematic" is a wish, not a direction. Spell out at least lens + lighting + grade.
- **Photoreal vocab missing entirely.** Cinematic is where Base §3 layers earn their keep. Don't be shy with it: stack 4–6 terms across subsections.
- **Hook is fade-from-black.** Cinematic does NOT mean slow fades. Open with impact (see §2).
- **Music described instead of audio direction.** "Cinematic music" is meaningless; describe what the audio DOES (silence, then impact; building strings to crescendo at 6.5s).
- **Lighting unmotivated.** Hard side-key with no source visible in frame reads as "studio." Specify what the light source IS in the world.
- **Mixing genres without intent.** "Noir, but also epic and romantic" produces sludge. Pick one Base §1 `genre` parameter and let it lead.

---

## 9. Final pre-publish checklist

- [ ] Genre parameter set (not just described in prose)
- [ ] Quality vocabulary layered (4–6 terms from Base §3)
- [ ] One hook from §2 in the first 2 seconds (or stacked)
- [ ] Camera technique from §3 named, with speed in ft/s
- [ ] Lighting setup from §4 named, with K temperature and direction
- [ ] Grade from §5 named
- [ ] Audio direction specified (silence vs. score timing)
- [ ] Aspect ratio matches destination (16:9 standard, 21:9 epic, 9:16 social cut)
