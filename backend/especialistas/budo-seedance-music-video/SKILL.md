---
name: budo-seedance-music-video
description: Generate music video and beat-synced video prompts for Seedance 2.0 on Higgsfield. Use whenever the user wants a music video, performance video, lyric video, visualizer, concert footage, beat-synced video, or any music-driven visual content. Triggers on: music video, music clip, performance video, lyric video, visualizer, MV, concert, performance footage, beat-synced, music visualization, or any video synced to music/audio. Reads BUDOSKILL_Seedance_Base.md first for platform specs, the 2-Second Hook framework, the visual-quality vocabulary library, prompt principles, common mistakes, platform table, master template, and output workflow.
---

# BUDO — Music Video & Beat-Synced Videos for Seedance 2.0 on Higgsfield

> **Inherits from `BUDOSKILL_Seedance_Base.md`.** Read that file first for the shared foundation. This file adds only what's **specific to music videos, performance footage, lyric videos, and visualizers.**

---

## 1. What this vertical optimizes for

Music video lives or dies on **beat sync**. Visuals that ignore the song's structure feel disconnected; visuals tied tightly to drops, builds, and vocal moments feel inevitable. Seedance 2.0 accepts `audio` references via `medias` — use this. Pass the actual track so the model can sync motion to it.

Quality vocab from Base §3 varies by genre — hip-hop wants gritty 35mm grain + hard practical light; ballad wants soft anamorphic + golden hour; electronic wants UE5 ray-traced + neon volumetrics; indie wants 16mm + natural light.

---

## 2. Music-video hook library (12 hooks)

1. **Beat Drop Visual Explosion** — Bass drop → particles explode outward, color saturates, light flashes, geometric shapes burst.
2. **Silent Intro Then Bass Hit** — Opening silence/minimal, then sudden low-end impact. Dark scene illuminates, camera shakes, color floods.
3. **Rapid Flash Cuts on Hi-Hats** — Fast percussion demands quick visual cuts. Jump cuts between 2–4 frames synced to each hat hit.
4. **Slow-Mo to Real-Time on Beat** — Slow-motion footage, then snaps to real-time on impact. Builds tension.
5. **Visual Glitch on Synth Stab** — Sharp electronic sound matched to screen tearing, color shift, frame duplicate/lag.
6. **Dramatic Performer Reveal on Downbeat** — Intro builds, performer enters perfectly on the downbeat. Empty stage → sudden cut to performer.
7. **Orbital Camera on Chorus** — Camera orbits subject, completing rotation per N bars, speed increasing on final bar.
8. **Color Shift on Harmonic Change** — Chord/key modulation triggers color palette shift.
9. **Geometry Morphing to Melody** — Geometric shapes grow/rotate/transform tracking melody contour.
10. **Depth Zoom on Energy Peak** — Highest energy pushes camera deeply into space; tunnel-vision acceleration.
11. **Inverted/Negative Flash on Peak** — Colors invert for 0.5s at climactic beat, then snap back.
12. **Cascading Reveals on Stacked Vocals** — Each vocal harmony layer reveals a new visual element / light source.

---

## 3. Music Video Philosophy

**Audio reference is non-negotiable.** Pass the song via `medias` as `role=audio`. Don't try to describe the beat in words alone.

**Song structure → video structure.** Intro / verse / pre-chorus / chorus / drop / bridge / outro each have visual logic. Plan the video on the song's timeline.

**Performance vs narrative vs visualizer.** Pick one mode (or a controlled blend). Don't try all three in a 15s clip.

**The chorus is the hook of the hook.** Whatever the chorus's signature visual is — that's the moment of the video. Everything builds toward and away from it.

**Restraint in production design.** If everything is at 10, nothing is. Save peak intensity for peak moments.

---

## 4. Genre Visual Language Guide

**Hip-Hop / Rap.** Gritty urban, hard practical lighting (warehouses, alleys, neons), gold/red/black palette, swagger-led performance, slow-mo on movement, lens flares. Genre: drama or action.

**Pop / Pop-rock.** Bright high-key, vibrant colors, clean production, dance choreography, performance-focused.

**R&B / Soul.** Soft warm lighting, intimate close-ups, slow camera movement, deep blacks, single light sources. Genre: drama.

**Electronic / EDM.** Neon-heavy, futuristic environments, geometric effects, fast cuts on drops, laser/light shows. Genre: action or epic.

**Indie / Alt-Rock.** Natural light, 16mm grain, lo-fi aesthetic, real environments (forest, city street, apartment), candid performance.

**Country.** Warm golden hour, rural environments (fields, barns, trucks), wide landscape shots, performance-focused.

**Metal / Hard Rock.** High-contrast, low-key lighting, fog, hard backlight, stage-set environments, fast cuts.

**Latin / Reggaeton.** Saturated tropical palette, dance-focused, daylight party, choreography, urban energy.

**K-Pop.** Hyper-polished, choreographed, multiple set changes per video, candy color palette, group formations.

**Folk / Acoustic.** Single light source, intimate framing, natural environments, slow camera, contemplative pace.

**Trap / Drill.** Dark and moody, neon accents, slow-mo, jewelry detail shots, urban night.

**Synthwave / Retro.** 80s neon palette (magenta, cyan), VHS grain, sun-and-grid horizons, vintage cars.

---

## 5. Beat-Sync Techniques

**Cut on the kick.** Every kick drum = visual cut to new angle. Standard sync.

**Flash on the snare.** Color flash or quick frame transition synced to snares.

**Movement on the bass.** Camera move (push, pull, orbit) initiates on bass note.

**Stutter on hi-hats.** Frame-skipping or strobe effect during fast hi-hat sections.

**Hold on the silence.** When the track has a held breath or silence, the visual goes static.

**Build on the build.** Camera move accelerates as the track builds toward drop.

**Drop = peak intensity.** Maximum visual complexity reserved for the drop.

**Slow-mo on the wind-up.** The bar before the drop in slow motion makes the drop feel earned.

---

## 6. Performance vs Narrative vs Visualizer (pick one)

**Performance.** Artist is the focus. Camera covers the performance from multiple angles. Best for established artists who want screen time.

**Narrative.** A story (with or without the artist appearing) plays out across the song. Best for songs whose lyrics tell a clear story.

**Visualizer.** Abstract or semi-abstract motion responds to the music. No performer required. Best for instrumental work, electronic music, or budget-constrained productions.

---

## 7. Music-video master-template additions

Layer onto Base §7:

```
[GENRE FROM §4]
Sets palette, lighting register, pace.

[MODE FROM §6]
Performance / narrative / visualizer.

[SONG STRUCTURE MAP]
For each clip in the multi-clip plan, identify which song section it covers
(intro / verse 1 / pre-chorus / chorus / drop / bridge / outro).

[BEAT-SYNC EVENTS]
Specific musical moments mapped to visual events:
- Kick at 0:08 → cut to new angle
- Snare at 0:09 → color flash
- Drop at 0:32 → red light floods warehouse

[QUALITY VOCAB FROM BASE §3]
Match to genre — gritty 35mm grain for hip-hop, soft anamorphic for ballad,
UE5 + neon for electronic.

[AUDIO]
ALWAYS pass the track via medias as role=audio.
```

---

## 8. Example prompts (3)

### Example 1 — Hip-Hop Performance Video (clip from a longer assembly, 9:16, 12s)

```
[GENRE / STYLE]
Genre: drama. Photoreal hip-hop performance register.
QUALITY VOCAB: 4K, shot on RED Komodo, 35mm anamorphic 2.39:1 (cropped to
9:16), hard practical lighting, 35mm grain, teal-and-orange grade with
gold accents.
Palette: gold, red, deep black, single neon accent.

[MODE] Performance.
[SONG STRUCTURE COVERED] Intro + Verse 1 + first hit of Chorus (covers
~0:00-0:32 of the track).

[OPENING HOOK — 0 to 2s]
Hook: Dramatic Performer Reveal on Downbeat. Dark warehouse interior,
minimal lighting. Single spotlight illuminates the ground center-frame.
At 0.8s the artist enters from frame-left, steps into the spotlight with
confident stride. At 1.8s (downbeat hit) a harsh spotlight snaps onto the
artist's face directly.

[MAIN ACTION — 2 to 10s]
VERSE 1 (corresponds to song 0:08-0:25):
- 2-4s: Tight close-up on artist's face during opening verse lines.
- 4-6s: Cut to wide shot showing full artist in spotlight with dark warehouse
  background. Slow orbital camera, half rotation.
- 6-8s: Hard shadows across face, rim-lighting creating edge. Gold neon sign
  flickers irregularly in background.

PRE-CHORUS BUILD (corresponds to song 0:25-0:32):
- 8-9.5s: Cut rate increases — alternating wide + tight every 0.6s.
- 9.5-10s: Camera push-in arrives at extreme close-up of face by 10s.

[CHORUS HIT — 10 to 12s]
At 10.0s (bass drop), red light floods the entire warehouse, creating
shadow of artist against back wall. Cut to new angle every kick drum (cuts
at 10.4s, 10.8s, 11.2s, 11.6s). Snare hits trigger gold-to-red color flashes.

[BEAT-SYNC EVENTS]
1.8s = downbeat → spotlight snap
10.0s = bass drop → red flood
10.4s/10.8s/11.2s/11.6s = kicks → cut to new angle
Each snare during 10-12s = gold-red flash

[CAMERA]
35mm anamorphic. Slow orbit in verse, push-in in pre-chorus, rapid-cut
hand-held + gimbal coverage in chorus.

[LIGHTING]
Hard directional spotlights, deep shadows, gold and red neon accents.
No fill — pure chiaroscuro.

[COLOR & GRADE]
Crushed blacks, gold and red highlights preserved. Teal in deepest shadows.
35mm grain at 80% opacity.

[CLOSING BEAT — 12s]
Ultra-wide shot showing the full warehouse lit in gold and red, artist as
silhouette in center.

[TECHNICAL]
resolution: 1080p; mode: std; genre: drama; aspect_ratio: 9:16; duration: 12;
medias: [song audio file as role=audio, artist reference photo as role=image]
```

### Example 2 — Pop Ballad Emotional Performance (16:9, 10s)

```
[GENRE / STYLE]
Genre: drama. Photoreal pop-ballad register, intimate emotional.
QUALITY VOCAB: 8K, shot on ARRI Alexa, Cooke S4 50mm, f/1.4 cinematic
depth, anamorphic 2.39:1 (cropped to 16:9), golden hour cinematography,
Portra 400 emulation.
Palette: warm gold, soft skin tone, deep navy shadows.

[MODE] Performance with narrative undertone.
[SONG STRUCTURE COVERED] Pre-chorus + chorus (corresponds to ~0:45-1:05).

[OPENING HOOK — 0 to 2s]
Hook: Slow-Mo to Real-Time on Beat. Slow-motion (50%) of the singer
standing alone in a sunlit window-lit room, hair moving slightly in a
breeze. At 1.8s the beat hits and the footage snaps to real-time.

[MAIN ACTION — 2 to 8s]
PRE-CHORUS:
- 2-4s: Slow lateral dolly across the singer in profile, golden window light
  on her face. Eyes closed, mouth shaping vocal phrasing.
- 4-5s: Cut to her hand resting on the window frame, light catching the skin.

CHORUS (5-8s):
- 5.0s (bass drop) — eyes open suddenly, looks toward camera. Light
  intensifies as if a cloud has just moved.
- 5.5-7s: Slow orbital camera, half rotation, around the singer; her
  expression shifts through controlled vulnerability.
- 7-8s: Push-in on the singer's face. Held breath at the end of the bar.

[BEAT-SYNC EVENTS]
1.8s = beat hit → slow-mo→real-time snap
5.0s = bass drop → eyes-open snap + light intensification
End of bar at 8s = held silence + held visual

[CAMERA]
50mm equivalent, f/1.4. Slow lateral dolly, then orbital, then push-in.
Movement velocities all under 1 ft/s — restrained.

[LIGHTING]
3000K golden hour from window, camera-right at 30°. No artificial fill.
Light intensifies at 5.0s as if naturally — practical timed effect.

[COLOR & GRADE]
Warm. Portra 400 milky highlights. Skin retains natural warmth. Light grain.

[CLOSING BEAT — 8 to 10s]
Held close-up on her face, eyes still on camera. Light catching tears in her
eyes (not falling yet).

[TECHNICAL]
resolution: 1080p; mode: std; genre: drama; aspect_ratio: 16:9; duration: 10;
medias: [song audio file as role=audio, artist reference photo as role=image]
```

### Example 3 — Electronic / Visualizer Drop (16:9, 8s)

```
[GENRE / STYLE]
Genre: epic. CGI motion design + photoreal volumetric.
QUALITY VOCAB: Unreal Engine 5 cinematic, ray-traced reflections, Lumen GI,
HDRI environment, volumetric fog, neon emissive surfaces, mathematical
motion easing, 4K detail.
Palette: pure black base, cyan + magenta + lime neon accents, white core.

[MODE] Visualizer.
[SONG STRUCTURE COVERED] Build + drop (last 4 bars before drop, then 4 bars
of drop).

[OPENING HOOK — 0 to 2s]
Hook: Silent Intro Then Bass Hit. Frame is pure black with a single small
cyan dot center, pulsing subtly. The track is in its quietest build moment.
At 1.8s the bass hits — white light floods the frame, camera shakes,
geometry begins materializing.

[MAIN ACTION — 2 to 7s]
BUILD CONTINUATION (2-4s):
Multiple geometric shapes (cubes, spheres, line segments) emerge from
particle dust at center frame, rotating and orbiting each other. Each
beat in the build triggers a new shape entering.

DROP (4-7s):
At 4.0s the drop hits — particles EXPLODE outward in cyan, magenta, lime.
Geometry collapses into a tunnel that the camera flies through at high
speed. Walls of the tunnel pulse with each kick (4.4s, 4.8s, 5.2s, 5.6s,
6.0s, 6.4s, 6.8s). Magenta light dominates at 5.6s; lime at 6.4s.

[BEAT-SYNC EVENTS]
1.8s = bass hit → white flood + camera shake
4.0s = drop → particle explosion + tunnel reveal
4.4s, 4.8s, 5.2s, 5.6s, 6.0s, 6.4s, 6.8s = kicks → tunnel wall pulses
5.6s = harmonic shift → magenta dominance
6.4s = harmonic shift → lime dominance

[CAMERA]
Static during the build. At drop, push-in at increasing velocity — starts
at 5 ft/s, accelerates to 30 ft/s by 6s. Slight Dutch tilt during peak.

[LIGHTING]
Pure emissive. Geometry emits its own light; HDRI environment is black void
with light bouncing off particles. Volumetric fog fills the tunnel.

[COLOR & GRADE]
HDR with extreme highlights. Pure RGB neons. No grain — clean digital.

[CLOSING BEAT — 7 to 8s]
Camera exits the tunnel into white light. Brief held white frame, then
fade to black.

[TECHNICAL]
resolution: 1080p; mode: std; genre: epic; aspect_ratio: 16:9; duration: 8;
medias: [song audio file as role=audio]
```

---

## 9. Music-video-specific mistakes (in addition to Base §5)

- **No audio reference attached.** Words can't describe a beat to a model that can listen. Pass the track via `medias` as `role=audio`.
- **Generic "music video" with no genre specified.** Hip-hop and ballad use opposite tools. Genre dictates lighting, pace, palette.
- **Cuts not synced to beats.** Random cut timing reads as amateur. Beat-sync every cut deliberately.
- **Chorus visualized same as verse.** The chorus is the visual peak. If the verse and chorus look the same, the chorus loses its punch.
- **Mode confusion.** Half-performance, half-narrative, half-visualizer produces incoherent video. Pick one mode and commit.
- **Over-effects on drops.** Every effect at once during the drop = visual noise. Pick 2–3 effects max.
- **Performance video with no artist reference.** The artist's identity must be passed via `medias` as `role=image` for consistency across clips.

---

## 10. Final pre-publish checklist

- [ ] Audio track attached via `medias` as `role=audio`
- [ ] Genre from §4 named, drives palette and pace
- [ ] Mode from §6 picked (performance / narrative / visualizer)
- [ ] Song structure section identified for this clip
- [ ] Beat-sync events mapped to timestamps
- [ ] Quality vocabulary matches genre
- [ ] One hook from §2 in the first 2 seconds
- [ ] Multi-clip plan if total video exceeds 15s (almost always for full songs)
- [ ] Artist reference photo attached via `medias` if performance mode
