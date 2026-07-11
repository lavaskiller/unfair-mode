# UNFAIR MODE - Devpost Final Copy

## Project name

UNFAIR MODE

## Elevator pitch

Bad interfaces disable people. Experience a hospital kiosk’s barriers, then use DigitalOcean AI to diagnose and rebuild the interface for better access.

## About the project

## Inspiration

A service can technically be available and still be impossible to use.

I arrived in the United States from Korea only a week before this hackathon. Navigating unfamiliar systems made me notice how much every interface assumes: that you understand its language, can read low-contrast text, can accurately hit small controls, and can process dense instructions under pressure. That experience was only the starting point. The larger issue affects disabled people, older adults, and people with temporary impairments every day.

Hospital check-in kiosks make the stakes especially clear. They are often the front door to care, but a few poor design decisions can turn a routine task into a barrier. Accessibility problems are also difficult to communicate when teammates cannot see or feel their effect. We built UNFAIR MODE to make those barriers impossible to ignore.

## What it does

UNFAIR MODE is an interactive accessibility stress test for a hospital check-in kiosk.

A user can activate three observable interface barriers:

- **Low contrast**, which makes essential content and state changes harder to perceive
- **Small targets**, which make controls difficult to operate accurately
- **Cognitive load**, which replaces plain instructions with unnecessarily dense language

The user then attempts the same check-in flow while UNFAIR MODE measures completion time and errors. The app sends a structured description of the active interface and barriers to DigitalOcean AI, which returns a prioritized accessibility report with actionable repairs.

After reviewing the report, the user can rebuild the kiosk with stronger contrast, larger targets, plain language, clearer progress, and visible keyboard focus. They repeat the same task and compare the before-and-after result.

UNFAIR MODE does not claim to simulate disability. It demonstrates specific interface failures. It also does not certify WCAG or ADA compliance or replace testing with disabled people and accessibility professionals.

## How we built it

We built the prototype as a lightweight web application using semantic HTML, responsive CSS, vanilla JavaScript, and a Python standard-library server.

The application has four main parts:

1. **Barrier controls** apply specific UI failures to a realistic hospital check-in flow.
2. **Task instrumentation** records elapsed time and validation errors.
3. **DigitalOcean AI analysis** receives structured screen context and returns constrained JSON containing issue titles, severity, and recommended repairs.
4. **A controlled rebuild layer** applies approved accessibility patterns rather than executing arbitrary model-generated code.

The AI credentials remain server-side. The browser calls a local `/api/analyze` endpoint, and the Python adapter calls the configured DigitalOcean AI endpoint. If the AI service is unavailable, the prototype explicitly displays **Demo fallback** and uses a saved analysis. It never presents fallback output as a live AI response.

We intentionally avoided asking the model to generate and execute arbitrary interface code. Instead, the model produces a structured diagnosis that can be validated and mapped to known accessible components. This makes the system safer, more predictable, and more reliable during a live demonstration.

## Challenges we ran into

The hardest challenge was ethical rather than technical. An early version risked presenting the experience as a “disability simulator.” That framing would overstate what software can reproduce and could reduce real lived experiences to a visual effect. We changed the product to focus on measurable interface barriers, renamed the modes, removed sensational concepts, and added clear limitations.

A second challenge was connecting AI to the core product rather than adding it as decoration. The model needed to make a real decision in the repair loop. We solved this by sending structured UI context and constraining the response to prioritized, actionable issue JSON.

Finally, hackathon connectivity and credentials can be unreliable. We built a transparent fallback path so the demo remains functional without falsely claiming that a saved response came from a live model.

## Accomplishments that we’re proud of

- A judge can understand and try the core idea within seconds.
- The demo completes a full loop from barrier to AI diagnosis, repair, and measured outcome.
- DigitalOcean AI contributes directly to the interface-repair decision.
- The product avoids arbitrary model-generated code.
- The app remains functional without a package installation.
- Offline fallback output is clearly labeled.
- The framing respects the difference between illustrating a UI barrier and reproducing someone’s lived experience.

## What we learned

Accessibility failures are rarely isolated styling mistakes. Contrast, target size, language, sequencing, focus, and feedback combine into a system. A small failure in each area can create a major barrier when someone is trying to access healthcare.

We also learned that responsible AI design requires boundaries. AI can accelerate an initial accessibility review, but it should produce inspectable recommendations, operate within a constrained schema, and support rather than replace disabled users and accessibility professionals.

## What’s next for UNFAIR MODE

Next, we would let teams submit real screenshots or DOM snapshots from public-service interfaces. UNFAIR MODE could then generate a developer-ready issue report, map recommendations to a controlled design system, and export tasks to engineering tools.

We would validate the recommendations with disabled testers, compare model results against expert-labeled accessibility audits, support more public-service flows, and measure whether each repair improves real task outcomes. The goal is not another automated compliance score. The goal is to help product teams see barriers early enough to fix them.

## Built with

Use these tags:

- HTML5
- CSS3
- JavaScript
- Python
- DigitalOcean
- DigitalOcean AI
- REST API
- JSON
- Accessibility
- WCAG
- UX Design

## Tell us more about your actual experience building with DigitalOcean

We designed DigitalOcean AI as part of the product’s core repair loop rather than as a chatbot added at the end. The application sends structured information about the current kiosk screen and active barriers to a server-side adapter, then expects a constrained JSON response containing prioritized issues and actionable repairs. Keeping the model call behind the server made it possible to protect credentials and keep the browser implementation simple.

What we liked most was the opportunity to treat AI as infrastructure for a focused social-impact workflow. A model is most useful here when its output is inspectable and connected to a concrete product action. The main challenge was integration under hackathon time constraints, especially verifying the correct endpoint, model configuration, and credentials while preserving a reliable live demo. To handle service or connectivity failures honestly, we added a clearly labeled saved fallback rather than presenting cached output as a live response.

The experience would be even better with one concise, event-specific quickstart that includes a verified request example, the exact endpoint and model identifier, structured-output guidance, environment-variable names, and a minimal deployment path. A ready-to-fork sample showing browser, server, and DigitalOcean AI together would reduce setup time and leave teams more time to evaluate and improve the social-impact use case.

> Submission honesty check: if a live DigitalOcean AI call has not been successfully verified before submission, do not claim that it was. Keep the wording above, demonstrate the clearly labeled fallback, and explain the intended adapter. If the live call is verified, add one sentence stating which DigitalOcean model or agent was used.

## What was the most interesting thing you learned at the Hack with MLH & DigitalOcean event?

The most interesting lesson was that “AI for social good” is not defined by adding a model to an app. The model needs to participate in a real decision, while the team sets clear limits so its output remains safe, inspectable, and useful to the people affected.

## How likely are you to use DigitalOcean after attending this event?

**Very Likely**

## What was your favorite part about the Hack with MLH & DigitalOcean event?

My favorite part was the build-for-good focus and the freedom to turn a social problem into a working demonstration. The conversations with other participants and mentors helped pressure-test not only whether the prototype worked, but whether we were framing accessibility responsibly.

## Links to complete before submission

- Public GitHub: https://github.com/lavaskiller/unfair-mode
- Live demo: TODO
- Demo video: TODO
