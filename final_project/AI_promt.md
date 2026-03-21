# 📌 FINAL PROMPT: Generate SpoilGuard HTML Prototype (Zero-Setup)

You are an expert front-end developer and UX designer.

Your task is to generate a COMPLETE, SINGLE-FILE HTML prototype that simulates a mobile application called "SpoilGuard".

The output MUST:
- Be ONE standalone HTML file
- Use only HTML, CSS, and minimal JavaScript
- Run by double-clicking (no installation, no dependencies)
- Simulate navigation between screens
- Be clean, readable, and well-structured
- NOT require React, frameworks, or external libraries

-----------------------------------
PROJECT CONTEXT
-----------------------------------
App Name: SpoilGuard

Problem:
Households waste 30–40% of food due to poor tracking of groceries and expiration dates.

Solution:
A mobile app that:
- Scans grocery receipts (OCR simulation)
- Tracks expiration dates
- Sends alerts for expiring items
- Provides analytics on food waste and savings

Target Users:
- Busy parents (fast interaction needed)
- Elderly users (accessibility support needed)

-----------------------------------
FUNCTIONAL REQUIREMENTS
-----------------------------------
FR-01: Manual grocery logging
FR-02: Receipt scanning (OCR simulation)
FR-03: Expiration tracking and alerts
FR-04: Recipe suggestions
FR-05: Inventory updates (consume/discard)
FR-06: Analytics dashboard

-----------------------------------
USE CASES (MUST ALL BE IMPLEMENTED)
-----------------------------------

UC-01: Scan Receipt (OCR Simulation)
Flow:
- User clicks "Scan Receipt"
- Camera placeholder appears
- User clicks "Capture"
- System shows detected items
- User confirms → items added to inventory

UC-02: Manage Inventory (My Fridge)
Flow:
- User views inventory list
- Each item shows expiration
- User can mark item as:
  - Consumed
  - Discarded

UC-03: Expiration Alerts
Flow:
- System highlights items expiring soon
- User clicks alert → sees item details
- Show recommended action ("Use soon")

UC-04: Savings Analytics
Flow:
- User views summary:
  - Items consumed
  - Items discarded
  - Waste cost
- Show simple visual (progress bar)

-----------------------------------
SCREEN REQUIREMENTS
-----------------------------------
You MUST include these screens:

1. Dashboard (Home / Hub)
2. Scan Receipt Screen
3. OCR Results Screen
4. My Fridge Screen
5. Alerts Screen
6. Analytics Screen
7. Settings Screen (Accessibility)

-----------------------------------
UI DESIGN REQUIREMENTS
-----------------------------------

Style:
- Mobile-app layout centered on screen
- Clean, modern UI
- Card-based design

Colors (High Contrast Mode):
- Background: dark (#0f172a)
- Card: #1f2937
- Accent: yellow (#facc15)
- Text: white/light

Components to include:
- Buttons (primary + secondary)
- Cards
- Inventory list items
- Badges (expiration warning)
- Toggle switches (settings)

-----------------------------------
INTERACTIVITY REQUIREMENTS
-----------------------------------

You MUST implement basic JavaScript to simulate:

Navigation:
- Clicking buttons switches screens
- Include back button

State:
- Maintain a simple inventory array
- When "Confirm Items" is clicked → items appear in "My Fridge"

Actions:
- "Consumed" → remove item
- "Discarded" → remove item and increase waste cost

Alerts:
- Highlight items expiring in ≤ 2 days

Settings:
- Toggle:
  - High contrast mode (light/dark)
  - Large font mode
  - Audio alerts (visual indicator only)

-----------------------------------
DATA (USE THIS INITIAL DATA)
-----------------------------------

Inventory:
- Eggs (expires in 1 day)
- Milk (expires in 2 days)
- Spinach (expires in 3 days)
- Yogurt (expires in 6 days)

OCR Detected Items:
- Eggs
- Milk
- Strawberries
- Spinach

-----------------------------------
ACCESSIBILITY REQUIREMENTS
-----------------------------------

- Large readable text
- High contrast UI
- Clearly labeled buttons
- Simple navigation

-----------------------------------
OUTPUT FORMAT (STRICT)
-----------------------------------

Return ONLY the HTML code.

DO NOT:
- Add explanations
- Add comments outside HTML
- Use external libraries
- Use multiple files

The result must be:
- Fully functional when opened directly in a browser
- Visually structured like a mobile app
- Easy to understand for demonstration

-----------------------------------
GOAL
-----------------------------------

Produce a professional, classroom-ready interactive prototype that demonstrates all 4 use cases clearly.
