# Devpost submission copy

## Project title
UNFAIR MODE

## Tagline
Bad interfaces disable people. Feel the barrier, then let AI rebuild the interface.

## Inspiration
A service can technically be available and still be impossible to use. Hospital kiosks are often the front door to care, yet low contrast, tiny targets, and dense language turn an ordinary check-in into a barrier. We wanted to make those invisible design decisions immediately visible—not by claiming to simulate disability, but by stress-testing the interface itself.

## What it does
UNFAIR MODE lets a judge complete a realistic hospital check-in while activating three concrete UI barriers: low contrast, small targets, and cognitive overload. It measures time and errors, sends a structured representation of the interface to DigitalOcean AI, and returns prioritized problems with actionable repairs. The user then activates an accessible rebuild and repeats the same task to compare the outcome.

## How we built it
We built a zero-dependency web prototype with semantic HTML, responsive CSS, and vanilla JavaScript. A small Python server exposes `/api/analyze` and keeps AI credentials off the client. It sends the active interface schema and barrier context to an OpenAI-compatible DigitalOcean AI endpoint, constrains the response to structured issue JSON, and renders the result as a repair plan. If the live service is unavailable, the demo explicitly labels its saved fallback instead of presenting it as live AI.

## Challenges we ran into
The hardest product challenge was drawing an ethical line between demonstrating an interface failure and pretending to reproduce a person's disability. We renamed the controls around observable barriers, removed sensational modes, added explicit limitations, and designed the product as an educational stress test. Technically, we also designed for unreliable hackathon connectivity by separating the live AI adapter from a transparently labeled fallback.

## Accomplishments that we're proud of
- A judge can understand and try the core idea in seconds.
- The demo closes the loop from barrier, to AI diagnosis, to repair, to measured outcome.
- The product does not claim compliance or substitute automated output for disabled users.
- The entire app runs without a package install and remains demoable offline.
- The AI output is structured and tied directly to product changes rather than used as decoration.

## What we learned
Accessibility failures are rarely isolated styling mistakes. Contrast, target size, language, sequencing, and feedback combine into a system. We also learned that responsible framing matters: automated analysis can accelerate a first pass, but meaningful accessibility requires testing with disabled people and accessibility professionals.

## What's next
Next we would accept real product screenshots or DOM snapshots, produce a developer-ready patch and issue export, support additional public-service flows, and validate recommendations with disabled testers. We would also deploy the API on DigitalOcean, add model evaluation against expert-labeled audits, and track which repairs improve task outcomes.

## Built with
HTML, CSS, JavaScript, Python, DigitalOcean AI

## 3-minute demo outline

**0:00–0:20 — Hook**  
“This kiosk works perfectly—if the interface works for you. Bad interfaces disable people.” Introduce UNFAIR MODE as an interface stress test, not a disability simulator.

**0:20–1:05 — Barrier task**  
Activate low contrast, small targets, and cognitive load. Attempt the check-in. Point to live time and error count.

**1:05–1:40 — AI analysis**  
Select Analyze interface. Explain that DigitalOcean AI receives structured UI context and returns prioritized, actionable issue JSON. Point out the live/fallback status label honestly.

**1:40–2:25 — Rebuild and proof**  
Select Rebuild accessibly. Repeat the same task with stronger contrast, larger targets, plain language, progress, and visible focus. Show before/after metrics.

**2:25–3:00 — Impact and close**  
Explain the next step: scan real service interfaces and export developer-ready repairs, then validate with disabled users. Close: “Accessibility should not depend on whether a product team can see the barrier. UNFAIR MODE makes it impossible to ignore.”

## Required links (fill before submission)
- Public GitHub: TODO
- Live demo: TODO
- Demo video: TODO
