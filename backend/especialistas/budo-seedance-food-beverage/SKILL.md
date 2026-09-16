---
name: budo-seedance-food-beverage
description: Generate food and beverage video prompts for Seedance 2.0 on Higgsfield. Use whenever the user wants food video, restaurant content, recipe video, cocktail, dessert, drink commercial, culinary content, ASMR food, or any appetite-triggering content. Triggers on: food video, restaurant, recipe, cocktail, dessert, drink, beverage, cooking, plating, food styling, food porn, culinary, food ad, restaurant video, or any food/drink content request. Use even for "make food look delicious" or "appetizing food video." Reads BUDOSKILL_Seedance_Base.md first for platform specs, the 2-Second Hook framework, the visual-quality vocabulary library, prompt principles, common mistakes, platform table, master template, and output workflow.
---

# BUDO — Food & Beverage Videos for Seedance 2.0 on Higgsfield

> **Inherits from `BUDOSKILL_Seedance_Base.md`.** Read that file first for the shared foundation. This file adds only what's **specific to food and beverage cinematography.**

---

## 1. What this vertical optimizes for

Food video has a singular goal: **make the viewer hungry within 2 seconds**. Unlike fashion (which sells aspiration), food sells appetite — a direct physiological response. Everything serves this: hero moment timing, lighting register, motion type, sound implication.

Quality vocabulary from Base §3 is essential — food lives on §3.1 (every-pore/every-fiber clarity), §3.2 (slow-mo for hero pours/splashes), §3.4 (90mm macro), §3.5 (motivated practical lighting), and §3.8 ("Michelin-quality food cinematography").

---

## 2. Food hook library (12 hooks)

1. **Cheese Pull/Stretch** — Melted cheese pulled from pizza/burger/grilled cheese. Slow-motion. The ooze is irresistible.
2. **Slow-Motion Sauce Pour** — Viscous sauce (béarnaise, chocolate, caramel, pesto) cascades over protein or dessert. Golden hour lighting on the pour.
3. **Steam Rising from Hot Dish** — Fresh pasta plated, soup ladle lifting with vapor, just-grilled meat. Steam signals freshness. Backlight it.
4. **Knife Cutting with Satisfying Crunch** — Blade hits fresh vegetable, crust, or chocolate. Sound + visual + macro angle on cut surface.
5. **Chocolate Break/Snap** — Chocolate bar or thick cake broken in half, revealing smooth interior or gooey center.
6. **Ice Cream Scoop with Drip** — Warm spoon creates scoop, ice cream softening and dripping onto waffle cone or bowl.
7. **Sizzling on Hot Surface** — Protein or vegetable hitting a screaming-hot pan. Sizzle + steam + color change.
8. **Bubbles Rising in Drink** — Carbonation in beer, soda, champagne. Backlit for luminosity. Hypnotic.
9. **Ingredient Cascade/Rain** — Seasoning sprinkled, flour dusted, garnish scattered, herbs rained from above. Capture the fall and land.
10. **Flame or Torch Moment** — Crème brûlée torch, flambéed dessert, flame-kissed dish. Orange glow inherently cinematic.
11. **Juice or Oil Drizzle** — Olive oil, balsamic, fresh citrus drizzled. Pooling and shine.
12. **Bread Tear/Crumb Reveal** — Fresh bread, croissant, bagel torn to show interior crumb and steam.

---

## 3. Food Video Philosophy

**Trigger appetite, not admiration.** Beautiful is good; mouth-watering is the goal. Steam, sheen, sizzle, motion are direct appetite cues.

**Macro is your friend.** Food at human eating distance reads as a meal. Food at macro distance (90mm at 0.5m) reads as cinema.

**Backlighting reveals freshness.** Steam, gloss, translucence — all live in backlit highlights. Front-only flat light kills food.

**Sound implication.** Even silent video can imply sound. Specify the implied audio (sizzle, knife thunk, pour gurgle) — Seedance considers it when generating.

**The money shot rules.** Identify the single most appetizing moment of the clip and structure everything around it.

---

## 4. Food Category Playbook

**Fine dining.** Slow, deliberate, elegant pacing. Macro plating. Warm directional light. Genre: drama.
**Casual restaurant / Café.** Warm welcoming pace. Mid-range shots. Daylight + practicals.
**Street food.** Energy, action, environment included. Wider lens. Mixed practicals. Genre: action.
**Fast food / QSR.** Bright high-key lighting. Stack-shot product hero shots. Genre: auto.
**Desserts / Pastry.** Macro, slow-motion, soft lighting. Sweetness signaled by warm tones. Genre: drama.
**Beverage / Coffee.** Pour-focused. Backlit for translucence. Genre: auto or drama.
**Cocktails / Alcohol.** Hard directional light on ice and glass. Garnish detail. Genre: drama.
**Healthy / Wellness.** Bright natural light, vibrant ingredient color, minimal styling.
**Comfort food.** Warm, abundant, generous portions. Cozy practical lighting.
**Ethnic / Cultural.** Authentic environment, traditional plating, specific lighting reference (Japanese washi paper / Italian tavern tungsten / Mexican papel picado).

---

## 5. Money Shot Library

**Hero pour** — Sauce, oil, syrup, broth pouring in slow-motion onto plated dish.
**Cheese pull** — Long stretch of melted cheese from cut slice or pulled-apart sandwich.
**Steam cloud** — Lid lifted to reveal steam billowing in directional backlight.
**Knife cut** — Blade slicing through crust, vegetable, chocolate, with macro of cut surface.
**Bite reveal** — Cut sandwich/burger pulled apart to show layered interior.
**Sizzle on the pan** — Steak, vegetable, or protein hitting hot surface with audible (implied) sizzle and visible steam.
**Drizzle pool** — Final drizzle that pools in a perfect circle next to hero ingredient.
**Sprinkle land** — Seasoning landing on hot surface, visible sparkle.
**Ice clink** — Ice cube dropped into glass, splash and bubble eruption.
**Pour foam** — Beer or coffee pour completing with foam stabilizing.
**Crumb fall** — Bread or pastry torn, crumbs falling with steam from the interior.
**Cream swirl** — Cream stirred into coffee, creating a marbled swirl.
**Torch flame** — Crème brûlée or hand torch applied, sugar caramelizing.
**Splash burst** — Liquid hitting another liquid (milk into coffee, juice splash).
**Plate landing** — Plate placed on table from above, food settling.

---

## 6. Food master-template additions

Layer onto Base §7:

```
[QUALITY VOCAB FROM BASE §3 — FOOD STACK]
"8K, hyper-detailed, every fiber visible, macro 90mm at 0.5m, shot on RED
Komodo with 90mm macro, 60fps slow-mo on the hero moment, motivated
practical lighting, Michelin-quality food cinematography."

[CATEGORY FROM §4]
Sets pace, palette, lighting register.

[HERO DISH / DRINK]
Specific dish/drink with exact components, plating, garnish.

[MONEY SHOT FROM §5]
Pick exactly one. This is the visual climax.

[ACTION SEQUENCE]
2–4 beats leading to the money shot.

[LIGHTING]
Warm/cool/mixed. Direction. Backlit element (almost always required).
```

---

## 7. Example prompts (3)

### Example 1 — Fine Dining Scallop Plating (16:9, 10s)

```
[GENRE / STYLE]
Genre: drama. Photoreal fine-dining cinematography.
QUALITY VOCAB: 8K, hyper-detailed, shot on RED Komodo, 90mm macro, 60fps
slow-mo on the hero pour, motivated practical, Michelin-quality food
cinematography polish.
Palette: warm tungsten kitchen, pristine white plate, golden beurre blanc,
deep amber sear.

[OPENING HOOK — 0 to 2s]
Hook: Slow-Motion Sauce Pour. Camera starts on the spoon of beurre blanc
held overhead. Sauce drizzles in slow-motion onto a minimalist white plate
in a deliberate artistic line. Backlit, glossy silky sauce catches light.
Steam ghosting from warm sauce.

[MAIN ACTION — 2 to 8s]
At 2.5s, chef's hand places first scallop with tweezers (top of triangle
formation). At 4.0s, second and third scallops placed. At 5.5s, microgreens
tweezers-placed with extreme precision. At 6.5s, single edible flower
placed deliberately. At 7.5s, final beurre blanc drizzle in slow-motion —
the money shot.

[HERO DISH]
Three pan-seared scallops, golden crust, arranged in geometric triangle.
Microgreens, edible flowers, sea salt crystals. Beurre blanc sauce in
delicate line across plate.

[MONEY SHOT]
Beurre blanc drizzle completing, sauce pooling next to scallop, gloss
catching backlight, steam ghosting across the plate.

[CAMERA]
Overhead at scallop placement (90mm macro). Slow push-in as garnish added.
Switch to low 45° angle for the beurre blanc pour (backlit). Final tight
macro on sauce-and-scallop intersection.

[LIGHTING]
Warm 3200K key from camera-stage-left at 45°. Backlight from camera-back
at 30% for beurre blanc gloss. Side fill on scallops showing sear crust.
Minimal shadows; pristine white plate stays white.

[COLOR & GRADE]
Warm, low-contrast. Restraint on saturation — let the sear color speak.
Light grain.

[CLOSING BEAT — 8 to 10s]
Hold on the completed plate, steam rising. Held final frame.

[IMPLIED AUDIO]
Soft sizzle of recent sear (low). Tweezers placing greens (quiet ping).
Gentle pour of beurre blanc. Faint plating-room ambience.

[TECHNICAL]
resolution: 1080p; mode: std; genre: drama; aspect_ratio: 16:9; duration: 10;
medias: [scallop dish reference photo as role=image if available]
```

### Example 2 — Latte Art Pour (9:16, 6s)

```
[GENRE / STYLE]
Genre: auto. Photoreal café cinematography.
QUALITY VOCAB: 8K, hyper-detailed macro, shot on Sony Venice with 90mm
macro, 60fps slow-mo on the pour, motivated window light, Apple-keynote-
grade polish.
Palette: warm morning sun, deep espresso brown, pure white microfoam,
ceramic cream cup.

[OPENING HOOK — 0 to 2s]
Hook: Steam Rising. Tight on the espresso cup. Deep brown espresso with
thin crema. Steam rising from surface, backlit by window light. At 1.5s
camera lifts slightly to reveal the milk pitcher entering frame from top.

[MAIN ACTION — 2 to 5s]
Milk pitcher begins pour at 2.2s — white microfoam stream visible. White
microfoam mixes with espresso, color change visible. Barista's hand
steadying cup (wrist control visible). At 3.5s, the pouring arm moves to
create the design. At 4.5s, final pour separation — design completes
(rosetta pattern). Pitcher pulls away at 5.0s.

[HERO DISH]
Espresso cup, ceramic white. Crema visible at edges. Final rosetta latte
art design.

[MONEY SHOT]
Pour foam — final pour separation as rosetta completes, microfoam stabilizing.

[CAMERA]
Tight on cup at 45° angle. Slow tracking as pitcher enters. Stay tight as
pour begins (see milk stream). Subtle push-back as design completes.
Slight zoom on finished art as final reveal.

[LIGHTING]
4500K window light from camera-left, soft. Single warm 3000K practical
behind the bar as backlight catching steam. Highlights on the ceramic
cup edge.

[COLOR & GRADE]
Warm, slight teal in shadows. Skin tones warm. Brown of espresso retains
full saturation.

[CLOSING BEAT — 5 to 6s]
Finished rosetta visible in full. Steam continues to rise. Hold.

[IMPLIED AUDIO]
Pour stream gurgle. Soft barista breath. Café ambience low in background.

[TECHNICAL]
resolution: 1080p; mode: std; genre: auto; aspect_ratio: 9:16; duration: 6
```

### Example 3 — Bourbon Cocktail Pour (1:1, 8s)

```
[GENRE / STYLE]
Genre: drama. Photoreal craft cocktail cinematography.
QUALITY VOCAB: 8K, hyper-detailed, shot on ARRI Alexa with 100mm macro,
60fps slow-mo on the pour, hard directional practical lighting, Vanity
Fair cover polish for spirits.
Palette: amber bourbon, deep wood-bar, single golden practical, dark
background.

[OPENING HOOK — 0 to 2s]
Hook: Ice Clink + Bubbles. Tight macro on a single large ice sphere
sitting in an empty heavy-bottom rocks glass. At 0.8s, second ice sphere
drops in from frame-top — slow-motion impact, glass clink, brief micro-
splash of condensation droplets.

[MAIN ACTION — 2 to 6s]
At 2.5s, bourbon pours from a hand-held bottle into the glass, slow-mo.
Stream catches the warm backlight, throwing amber refractions. At 4.0s
pour completes; bottle exits frame. At 4.5s a single orange-peel garnish
is placed deliberately on the ice. At 5.5s the bartender's hand twists
the peel above the glass — visible mist of orange oil falls into the
bourbon.

[HERO DISH]
Single Old Fashioned: heavy-bottom rocks glass, two large clear ice
spheres, amber bourbon (2.5oz), orange-peel garnish.

[MONEY SHOT]
Hero pour — bourbon stream catching warm backlight, throwing amber
refractions through the ice.

[CAMERA]
100mm macro throughout. Static for the ice drop. Slow lateral micro-
movement during the pour (1 inch over the pour duration). Tight push-in
for the orange-peel twist.

[LIGHTING]
Single hard 3000K practical from camera-back-right at 30° elevation
(backlight). Dark background, no fill. Chiaroscuro. Backlight catches
the bourbon's amber transparency.

[COLOR & GRADE]
Deep warm. Crushed blacks. Amber bourbon as the only major color element.
Vintage warm grade, light film grain.

[CLOSING BEAT — 6 to 8s]
Glass sits alone, ice settling, orange oil sheen on the surface. Hold.

[IMPLIED AUDIO]
Ice-on-ice clink. Pour gurgle. Crack of orange peel. Otherwise silence.

[TECHNICAL]
resolution: 1080p; mode: std; genre: drama; aspect_ratio: 1:1; duration: 8
```

---

## 8. Food-specific mistakes (in addition to Base §5)

- **Front-light only.** Flat front lighting kills food. Almost every food shot wants directional + backlight to show steam, gloss, translucence.
- **Camera too far back.** Food at wide-shot distance reads as "table photo." Macro distance (90mm at 0.5m) reads as cinema.
- **No motion / no money shot.** Static plated food is photograph territory. Video earns its keep with a money shot from §5.
- **Steam absent.** Hot food without steam reads as cold. Almost always add steam (backlit).
- **Plate clutter.** Too many garnishes pull focus from the hero. Restraint sells quality.
- **Wrong color temperature for cuisine.** Cool white-balanced light on warm comfort food kills the appetite. Match K to the cuisine register.
- **Implied audio missing.** Specify implied sizzle, pour, knife thunk. Seedance considers it.
- **Over-saturation.** Boosting reds on tomatoes / yellows on cheese reads as artificial. Restraint.

---

## 9. Final pre-publish checklist

- [ ] Category from §4 chosen, drives lighting and pace
- [ ] Hero dish described with specific components
- [ ] Money shot from §5 identified
- [ ] Backlight specified (almost always)
- [ ] Macro distance / lens specified (90mm or equivalent)
- [ ] Slow-mo applied to the money shot specifically, not everywhere
- [ ] Quality vocabulary layered (4–6 from Base §3)
- [ ] Implied audio called out
- [ ] One hook from §2 in the first 2 seconds
