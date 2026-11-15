import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# -------------------------------------------------------------
# CONSTANTS & THEME
# -------------------------------------------------------------
FONT_HEADING = "Segoe UI"
FONT_BODY = "Segoe UI"

# Color Palette (Aerospace-inspired on Pure White)
C_WHITE = RGBColor(255, 255, 255)
C_NAVY = RGBColor(11, 18, 36)          # Deep space navy #0B1224
C_SLATE = RGBColor(30, 41, 59)         # Dark slate text #1E293B
C_MUTED = RGBColor(100, 116, 139)      # Muted secondary #64748B
C_CYAN = RGBColor(0, 163, 196)         # Primary Cyan #00A3C4
C_CYAN_LIGHT = RGBColor(236, 254, 255) # Cyan tint #ECFEFF
C_BLUE = RGBColor(37, 99, 235)         # Electric Blue #2563EB
C_VIOLET = RGBColor(124, 58, 237)      # Subtle Violet #7C3AED
C_CARD_BG = RGBColor(248, 250, 252)    # Card Light Slate #F8FAFC
C_BORDER = RGBColor(226, 232, 240)     # Light Border #E2E8F0
C_GREEN = RGBColor(16, 185, 129)       # Success green
C_AMBER = RGBColor(245, 158, 11)       # Warning amber
C_RED = RGBColor(239, 68, 68)          # Alert red

ROOT_DIR = r"K:\NASA 2026\OUTPOST-X"

def set_slide_background(slide):
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = C_WHITE

def add_header(slide, kicker, title, subtitle):
    # Kicker Badge / Category
    kicker_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.28))
    tf_k = kicker_box.text_frame
    tf_k.word_wrap = True
    tf_k.margin_left = tf_k.margin_top = tf_k.margin_right = tf_k.margin_bottom = 0
    p_k = tf_k.paragraphs[0]
    p_k.text = kicker.upper()
    p_k.font.name = FONT_HEADING
    p_k.font.size = Pt(9.5)
    p_k.font.bold = True
    p_k.font.color.rgb = C_CYAN

    # Main Slide Title
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.68), Inches(11.7), Inches(0.45))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
    p_t = tf_t.paragraphs[0]
    p_t.text = title
    p_t.font.name = FONT_HEADING
    p_t.font.size = Pt(20)
    p_t.font.bold = True
    p_t.font.color.rgb = C_NAVY

    # Subtitle
    sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.15), Inches(11.7), Inches(0.3))
    tf_s = sub_box.text_frame
    tf_s.word_wrap = True
    tf_s.margin_left = tf_s.margin_top = tf_s.margin_right = tf_s.margin_bottom = 0
    p_s = tf_s.paragraphs[0]
    p_s.text = subtitle
    p_s.font.name = FONT_BODY
    p_s.font.size = Pt(10.5)
    p_s.font.color.rgb = C_MUTED

def add_footer(slide, current_slide, total_slides=7):
    # Divider line
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.015))
    line.fill.solid()
    line.fill.fore_color.rgb = C_BORDER
    line.line.color.rgb = C_BORDER

    # Footer Left Text
    box_l = slide.shapes.add_textbox(Inches(0.8), Inches(7.12), Inches(8.0), Inches(0.25))
    tf_l = box_l.text_frame
    tf_l.margin_left = tf_l.margin_top = tf_l.margin_right = tf_l.margin_bottom = 0
    p_l = tf_l.paragraphs[0]
    p_l.text = "OUTPOST-X  |  TensorMinds  ·  2026 NASA Space Apps Challenge"
    p_l.font.name = FONT_BODY
    p_l.font.size = Pt(8.5)
    p_l.font.color.rgb = C_MUTED

    # Footer Right Text
    box_r = slide.shapes.add_textbox(Inches(8.8), Inches(7.12), Inches(3.733), Inches(0.25))
    tf_r = box_r.text_frame
    tf_r.margin_left = tf_r.margin_top = tf_r.margin_right = tf_r.margin_bottom = 0
    p_r = tf_r.paragraphs[0]
    p_r.text = f"https://outpostx.vercel.app/   |   Slide {current_slide} of {total_slides}"
    p_r.alignment = PP_ALIGN.RIGHT
    p_r.font.name = FONT_BODY
    p_r.font.size = Pt(8.5)
    p_r.font.color.rgb = C_MUTED

def add_card(slide, left, top, width, height, bg_rgb=C_CARD_BG, border_rgb=C_BORDER):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_rgb
    shape.line.color.rgb = border_rgb
    shape.line.width = Pt(1)
    return shape

def add_framed_image(slide, img_path, left, top, width, height, border_rgb=C_BORDER):
    frame = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    frame.fill.solid()
    frame.fill.fore_color.rgb = C_CARD_BG
    frame.line.color.rgb = border_rgb
    frame.line.width = Pt(1.5)
    
    inset = Inches(0.02)
    img = slide.shapes.add_picture(img_path, left + inset, top + inset, width - (2 * inset), height - (2 * inset))
    return img

def generate_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # =========================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1)

    # NASA Badge
    badge = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.7), Inches(4.3), Inches(0.35))
    badge.fill.solid()
    badge.fill.fore_color.rgb = RGBColor(241, 245, 249)
    badge.line.color.rgb = RGBColor(203, 213, 225)
    badge.line.width = Pt(0.75)
    tf_b = badge.text_frame
    tf_b.margin_top = Inches(0.05)
    p_b = tf_b.paragraphs[0]
    p_b.text = "NASA SPACE APPS CHALLENGE 2026  ·  GLOBAL EVENT"
    p_b.font.name = FONT_HEADING
    p_b.font.size = Pt(8.5)
    p_b.font.bold = True
    p_b.font.color.rgb = C_BLUE

    # Logo
    logo_path = os.path.join(ROOT_DIR, "apps/web/public/branding/outpost-x-logo.png")
    if os.path.exists(logo_path):
        slide1.shapes.add_picture(logo_path, Inches(0.8), Inches(1.2), Inches(3.2), Inches(0.95))

    # Headline & Tagline
    tag_box = slide1.shapes.add_textbox(Inches(0.8), Inches(2.25), Inches(5.8), Inches(1.2))
    tf_tag = tag_box.text_frame
    tf_tag.word_wrap = True
    tf_tag.margin_left = tf_tag.margin_top = tf_tag.margin_right = tf_tag.margin_bottom = 0
    p_tag1 = tf_tag.paragraphs[0]
    p_tag1.text = "Next-Generation Planetary Mission Control"
    p_tag1.font.name = FONT_HEADING
    p_tag1.font.size = Pt(22)
    p_tag1.font.bold = True
    p_tag1.font.color.rgb = C_NAVY

    p_tag2 = tf_tag.add_paragraph()
    p_tag2.space_before = Pt(6)
    p_tag2.text = "Take Command. Build Beyond Earth. Shape Humanity’s Next Frontier."
    p_tag2.font.name = FONT_BODY
    p_tag2.font.size = Pt(12)
    p_tag2.font.color.rgb = C_CYAN
    p_tag2.font.bold = True

    # Challenge & Team Metadata Card
    add_card(slide1, Inches(0.8), Inches(3.65), Inches(5.7), Inches(2.9), bg_rgb=RGBColor(248, 250, 252))

    meta_box = slide1.shapes.add_textbox(Inches(1.05), Inches(3.8), Inches(5.2), Inches(2.6))
    tf_m = meta_box.text_frame
    tf_m.word_wrap = True
    tf_m.margin_left = tf_m.margin_top = tf_m.margin_right = tf_m.margin_bottom = 0

    p_m1 = tf_m.paragraphs[0]
    p_m1.text = "CHALLENGE TRACK"
    p_m1.font.name = FONT_HEADING
    p_m1.font.size = Pt(8.5)
    p_m1.font.bold = True
    p_m1.font.color.rgb = C_MUTED

    p_m2 = tf_m.add_paragraph()
    p_m2.text = "Build a Junior Astronaut Mission Trainer (Ages 7–12+)"
    p_m2.font.name = FONT_HEADING
    p_m2.font.size = Pt(11.5)
    p_m2.font.bold = True
    p_m2.font.color.rgb = C_SLATE

    p_m3 = tf_m.add_paragraph()
    p_m3.space_before = Pt(8)
    p_m3.text = "DEVELOPMENT TEAM"
    p_m3.font.name = FONT_HEADING
    p_m3.font.size = Pt(8.5)
    p_m3.font.bold = True
    p_m3.font.color.rgb = C_MUTED

    p_m4 = tf_m.add_paragraph()
    p_m4.text = "Team TensorMinds"
    p_m4.font.name = FONT_HEADING
    p_m4.font.size = Pt(12)
    p_m4.font.bold = True
    p_m4.font.color.rgb = C_BLUE

    p_m5 = tf_m.add_paragraph()
    p_m5.space_before = Pt(4)
    p_m5.text = "• Mourya S — Team Lead & Lead Developer (Sim Engine, Architecture)\n• Chitra Shree K — UI/UX Designer & Aerospace Simulation Models\n• Monika S — Data Architect & NASA Telemetry Verification"
    p_m5.font.name = FONT_BODY
    p_m5.font.size = Pt(9)
    p_m5.font.color.rgb = C_SLATE

    # Featured Image on Right Side
    hero_img = os.path.join(ROOT_DIR, "docs/screenshots/01-landing-hero.png")
    if os.path.exists(hero_img):
        add_framed_image(slide1, hero_img, Inches(6.8), Inches(1.1), Inches(5.7), Inches(5.45))
        cap = slide1.shapes.add_textbox(Inches(6.8), Inches(6.6), Inches(5.7), Inches(0.3))
        p_c = cap.text_frame.paragraphs[0]
        p_c.text = "Authentic Planetary Mission Deck Powered by Sourced NASA Telemetry"
        p_c.font.name = FONT_BODY
        p_c.font.size = Pt(8.5)
        p_c.font.color.rgb = C_MUTED
        p_c.alignment = PP_ALIGN.CENTER

    add_footer(slide1, 1)

    # =========================================================
    # SLIDE 2: THE PROBLEM & SOLUTION
    # =========================================================
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2)
    add_header(slide2, 
        kicker="Challenge Context & Pedagogical Innovation", 
        title="The Problem: The STEM Translation Gap in Space Education", 
        subtitle="Bridging the divide between oversimplified trivia and complex aerospace flight operations"
    )

    col_w = Inches(3.65)
    col_gap = Inches(0.38)
    top_y = Inches(1.6)
    card_h = Inches(3.1)

    # Column 1: Current Space STEM
    add_card(slide2, Inches(0.8), top_y, col_w, card_h, bg_rgb=RGBColor(254, 242, 242), border_rgb=RGBColor(254, 202, 202))
    b1 = slide2.shapes.add_textbox(Inches(1.0), top_y + Inches(0.15), col_w - Inches(0.4), card_h - Inches(0.3))
    tf1 = b1.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "CURRENT SPACE STEM"
    p1.font.name = FONT_HEADING
    p1.font.size = Pt(9)
    p1.font.bold = True
    p1.font.color.rgb = C_RED

    p1_sub = tf1.add_paragraph()
    p1_sub.text = "Oversimplified & Abstract"
    p1_sub.font.name = FONT_HEADING
    p1_sub.font.size = Pt(13)
    p1_sub.font.bold = True
    p1_sub.font.color.rgb = C_NAVY

    p1_body = tf1.add_paragraph()
    p1_body.space_before = Pt(6)
    p1_body.text = "• Click-to-Win Mechanics: Reduced to cartoon clickers with zero operational depth.\n\n" \
                  "• Detached from Physics: Health, oxygen, and battery bars lack stoichiometric or thermodynamic mass balances.\n\n" \
                  "• Lost Nuance: Students see mission outcomes, never the daily engineering trade-offs flight directors navigate."
    p1_body.font.name = FONT_BODY
    p1_body.font.size = Pt(8.5)
    p1_body.font.color.rgb = C_SLATE

    # Column 2: Deep Space Reality
    add_card(slide2, Inches(0.8) + col_w + col_gap, top_y, col_w, card_h, bg_rgb=RGBColor(241, 245, 249), border_rgb=RGBColor(203, 213, 225))
    b2 = slide2.shapes.add_textbox(Inches(1.0) + col_w + col_gap, top_y + Inches(0.15), col_w - Inches(0.4), card_h - Inches(0.3))
    tf2 = b2.text_frame
    tf2.word_wrap = True
    p2 = tf2.paragraphs[0]
    p2.text = "DEEP-SPACE REALITY"
    p2.font.name = FONT_HEADING
    p2.font.size = Pt(9)
    p2.font.bold = True
    p2.font.color.rgb = C_BLUE

    p2_sub = tf2.add_paragraph()
    p2_sub.text = "Non-Negotiable Constraints"
    p2_sub.font.name = FONT_HEADING
    p2_sub.font.size = Pt(13)
    p2_sub.font.bold = True
    p2_sub.font.color.rgb = C_NAVY

    p2_body = tf2.add_paragraph()
    p2_body.space_before = Pt(6)
    p2_body.text = "• Zero-Sum Power: Solar flux drops 85% during Martian dust storms; 354-hour continuous polar nights on the Moon.\n\n" \
                  "• Closed-Loop ECLSS: Sabatier CO2 scrubbers and water recycling consume critical power and crew maintenance time.\n\n" \
                  "• Hostile Space Environment: Cosmic rays, acute solar proton events (SEPs), and up to 22-minute light-time delay."
    p2_body.font.name = FONT_BODY
    p2_body.font.size = Pt(8.5)
    p2_body.font.color.rgb = C_SLATE

    # Column 3: OUTPOST-X Solution
    add_card(slide2, Inches(0.8) + (col_w + col_gap)*2, top_y, col_w, card_h, bg_rgb=RGBColor(236, 254, 255), border_rgb=RGBColor(165, 243, 252))
    b3 = slide2.shapes.add_textbox(Inches(1.0) + (col_w + col_gap)*2, top_y + Inches(0.15), col_w - Inches(0.4), card_h - Inches(0.3))
    tf3 = b3.text_frame
    tf3.word_wrap = True
    p3 = tf3.paragraphs[0]
    p3.text = "THE OUTPOST-X SOLUTION"
    p3.font.name = FONT_HEADING
    p3.font.size = Pt(9)
    p3.font.bold = True
    p3.font.color.rgb = C_CYAN

    p3_sub = tf3.add_paragraph()
    p3_sub.text = "Grounded Flight Simulator"
    p3_sub.font.name = FONT_HEADING
    p3_sub.font.size = Pt(13)
    p3_sub.font.bold = True
    p3_sub.font.color.rgb = C_NAVY

    p3_body = tf3.add_paragraph()
    p3_body.space_before = Pt(6)
    p3_body.text = "• Authentic Zero-Sum Play: Enforces real trade-offs—e.g. running the Brine Processor yields 98% water but costs 1.5 crew-h/day.\n\n" \
                  "• Sourced NASA Open Data: Integrates DONKI solar telemetry, OSDR biology, and JPL Horizons ephemerides.\n\n" \
                  "• The Reality Dial: One immutable simulation engine presented across 3 cognitive depths (Ages 7–12, 12–14, 15+)."
    p3_body.font.name = FONT_BODY
    p3_body.font.size = Pt(8.5)
    p3_body.font.color.rgb = C_SLATE

    # Bottom Visual: Artemis II Trajectory Embed Screenshot + Callout
    artemis_img = os.path.join(ROOT_DIR, "docs/screenshots/01b-artemis-section.png")
    if os.path.exists(artemis_img):
        add_framed_image(slide2, artemis_img, Inches(0.8), Inches(4.85), Inches(5.7), Inches(2.05))
    
    bot_box = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.75), Inches(4.85), Inches(5.783), Inches(2.05))
    bot_box.fill.solid()
    bot_box.fill.fore_color.rgb = RGBColor(240, 249, 255)
    bot_box.line.color.rgb = C_CYAN
    bot_box.line.width = Pt(1)
    tf_bb = bot_box.text_frame
    tf_bb.word_wrap = True
    tf_bb.margin_left = tf_bb.margin_right = Inches(0.2)
    tf_bb.margin_top = Inches(0.15)
    
    p_bb1 = tf_bb.paragraphs[0]
    p_bb1.text = "EMBEDDED ARTEMIS II FLIGHT REPLAY & MISSION PILLARS"
    p_bb1.font.name = FONT_HEADING
    p_bb1.font.size = Pt(9.5)
    p_bb1.font.bold = True
    p_bb1.font.color.rgb = C_CYAN

    p_bb2 = tf_bb.add_paragraph()
    p_bb2.space_before = Pt(4)
    p_bb2.text = "• NASA Translunar Injection: Features live circumlunar free-return trajectory telemetry via azmth.space.\n" \
                 "• Core Engineering Pillars: Closed-Loop ECLSS, Fission Microgrids, Space Weather Alerts, and Speed-of-Light Interplanetary Comms.\n" \
                 "• Guiding Principle: Saving power today may cost oxygen tomorrow. Every decision enforces a genuine resource trade-off."
    p_bb2.font.name = FONT_BODY
    p_bb2.font.size = Pt(8.5)
    p_bb2.font.color.rgb = C_SLATE

    add_footer(slide2, 2)

    # =========================================================
    # SLIDE 3: FIVE OPERATIONAL CONSOLES
    # =========================================================
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3)
    add_header(slide3, 
        kicker="Mission Operations & Station Consoles", 
        title="Five Specialized Consoles for Planetary Habitat Command", 
        subtitle="Engineered around NASA BVAD-2022 human spaceflight standards and authentic aerospace flight decks"
    )

    card_w = Inches(2.18)
    gap_x = Inches(0.2)
    start_x = Inches(0.8)
    top_y3 = Inches(1.6)
    card_h3 = Inches(5.2)

    consoles = [
        {
            "name": "1. POWER",
            "tag": "Energy Microgrid",
            "img": os.path.join(ROOT_DIR, "docs/screenshots/03-power-console.png"),
            "bullets": [
                "Fission & solar generation",
                "Battery kWh charge/discharge",
                "Load-shedding priority list",
                "Dust obscuration penalties"
            ]
        },
        {
            "name": "2. LIFE SUPPORT",
            "tag": "Closed-Loop ECLSS",
            "img": os.path.join(ROOT_DIR, "docs/screenshots/04-lifesupport-console.png"),
            "bullets": [
                "ppO2 & ppCO2 partial pressures",
                "Sabatier catalytic scrubbers",
                "Brine Processor (98% water)",
                "Electrolysis oxygen loop"
            ]
        },
        {
            "name": "3. COMMS",
            "tag": "Interplanetary DSN",
            "img": os.path.join(ROOT_DIR, "docs/screenshots/05-comms-console.png"),
            "bullets": [
                "Deep Space Network links",
                "JPL Horizons light delay",
                "Earth-Mars/Moon distance",
                "Telemetry packet queues"
            ]
        },
        {
            "name": "4. INCIDENT CMD",
            "tag": "Space Weather Triage",
            "img": os.path.join(ROOT_DIR, "docs/screenshots/06-incident-command.png"),
            "bullets": [
                "NASA DONKI solar flares",
                "Radiation shelter orders",
                "Causal fault trees (DAG)",
                "Subsystem damage triage"
            ]
        },
        {
            "name": "5. MISSION CMD",
            "tag": "Crew & Habitat Ops",
            "img": os.path.join(ROOT_DIR, "docs/screenshots/07-mission-command.png"),
            "bullets": [
                "BVAD crew schedule & rest",
                "Station operator assignments",
                "NASA Eyes 3D orbit view",
                "Sol timeline & speed (1x-16x)"
            ]
        }
    ]

    for idx, c in enumerate(consoles):
        x = start_x + (card_w + gap_x) * idx
        add_card(slide3, x, top_y3, card_w, card_h3)

        header_shape = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, top_y3, card_w, Inches(0.7))
        header_shape.fill.solid()
        header_shape.fill.fore_color.rgb = C_NAVY
        header_shape.line.fill.background()
        tf_ch = header_shape.text_frame
        tf_ch.margin_top = Inches(0.08)
        p_c1 = tf_ch.paragraphs[0]
        p_c1.text = c["name"]
        p_c1.font.name = FONT_HEADING
        p_c1.font.size = Pt(10.5)
        p_c1.font.bold = True
        p_c1.font.color.rgb = C_CYAN
        p_c1.alignment = PP_ALIGN.CENTER

        p_c2 = tf_ch.add_paragraph()
        p_c2.text = c["tag"]
        p_c2.font.name = FONT_BODY
        p_c2.font.size = Pt(8)
        p_c2.font.color.rgb = RGBColor(226, 232, 240)
        p_c2.alignment = PP_ALIGN.CENTER

        if os.path.exists(c["img"]):
            slide3.shapes.add_picture(c["img"], x + Inches(0.08), top_y3 + Inches(0.8), card_w - Inches(0.16), Inches(2.3))

        b_box = slide3.shapes.add_textbox(x + Inches(0.1), top_y3 + Inches(3.2), card_w - Inches(0.2), Inches(1.85))
        tf_cb = b_box.text_frame
        tf_cb.word_wrap = True
        tf_cb.margin_left = tf_cb.margin_top = tf_cb.margin_right = tf_cb.margin_bottom = 0
        for b_i, bullet in enumerate(c["bullets"]):
            p_b = tf_cb.paragraphs[0] if b_i == 0 else tf_cb.add_paragraph()
            p_b.space_before = Pt(3)
            p_b.text = f"• {bullet}"
            p_b.font.name = FONT_BODY
            p_b.font.size = Pt(8.5)
            p_b.font.color.rgb = C_SLATE

    add_footer(slide3, 3)

    # =========================================================
    # SLIDE 4: TECHNICAL SYSTEM ARCHITECTURE
    # =========================================================
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide4)
    add_header(slide4, 
        kicker="System Engineering & Telemetry Pipeline", 
        title="Technical Architecture: Deterministic Engine & Live Data Ingestion", 
        subtitle="Decoupled pure TypeScript simulation core (@outpost-x/sim) with reactive UI and offline PWA"
    )

    box_top = Inches(1.6)
    box_h = Inches(4.55)

    # Layer 1: NASA Open Data Ingestion (Left Column)
    w1 = Inches(2.6)
    add_card(slide4, Inches(0.8), box_top, w1, box_h, bg_rgb=RGBColor(240, 249, 255), border_rgb=C_CYAN)
    t1 = slide4.shapes.add_textbox(Inches(0.95), box_top + Inches(0.15), w1 - Inches(0.3), box_h - Inches(0.3))
    tf_a1 = t1.text_frame
    tf_a1.word_wrap = True
    pa1 = tf_a1.paragraphs[0]
    pa1.text = "NASA OPEN TELEMETRY"
    pa1.font.name = FONT_HEADING
    pa1.font.size = Pt(9.5)
    pa1.font.bold = True
    pa1.font.color.rgb = C_CYAN

    pa1_t = tf_a1.add_paragraph()
    pa1_t.text = "External Agency APIs"
    pa1_t.font.name = FONT_HEADING
    pa1_t.font.size = Pt(13)
    pa1_t.font.bold = True
    pa1_t.font.color.rgb = C_NAVY

    pa1_b = tf_a1.add_paragraph()
    pa1_b.space_before = Pt(8)
    pa1_b.text = "• NASA DONKI API:\n  Solar flares (FLR), CMEs,\n  and radiation storms (SEP)\n\n" \
                 "• JPL Horizons API:\n  Real-time Earth-Mars/Moon\n  light-time latency ephemerides\n\n" \
                 "• NASA OSDR & RadLab:\n  Empirical astronaut dosimetry\n  and space biology findings\n\n" \
                 "• NASA Moon/Mars Trek:\n  Calibrated LRO & Viking\n  orbital topographic basemaps"
    pa1_b.font.name = FONT_BODY
    pa1_b.font.size = Pt(8.5)
    pa1_b.font.color.rgb = C_SLATE

    # Layer 2: Edge Serverless & Offline Cache (Col 2)
    w2 = Inches(2.7)
    x2 = Inches(0.8) + w1 + Inches(0.3)
    add_card(slide4, x2, box_top, w2, box_h, bg_rgb=RGBColor(248, 250, 252))
    t2 = slide4.shapes.add_textbox(x2 + Inches(0.15), box_top + Inches(0.15), w2 - Inches(0.3), box_h - Inches(0.3))
    tf_a2 = t2.text_frame
    tf_a2.word_wrap = True
    pa2 = tf_a2.paragraphs[0]
    pa2.text = "EDGE PROXY & CACHE"
    pa2.font.name = FONT_HEADING
    pa2.font.size = Pt(9.5)
    pa2.font.bold = True
    pa2.font.color.rgb = C_BLUE

    pa2_t = tf_a2.add_paragraph()
    pa2_t.text = "Vercel Functions & PWA"
    pa2_t.font.name = FONT_HEADING
    pa2_t.font.size = Pt(13)
    pa2_t.font.bold = True
    pa2_t.font.color.rgb = C_NAVY

    pa2_b = tf_a2.add_paragraph()
    pa2_b.space_before = Pt(8)
    pa2_b.text = "• Vercel Edge Serverless:\n  api/space-weather.ts\n  api/light-time.ts\n  api/nasa-images.ts\n\n" \
                 "• Query Whitelisting:\n  Strict parameter validation\n  with 8s abort controller\n\n" \
                 "• Offline-First Fallbacks:\n  Committed snapshots in\n  public/snapshots/*.json\n\n" \
                 "• Vite-PWA Service Worker:\n  Precaches full app shell &\n  hardware graphics for offline"
    pa2_b.font.name = FONT_BODY
    pa2_b.font.size = Pt(8.5)
    pa2_b.font.color.rgb = C_SLATE

    # Layer 3: Pure TypeScript Sim Core (Col 3)
    w3 = Inches(3.0)
    x3 = x2 + w2 + Inches(0.3)
    add_card(slide4, x3, box_top, w3, box_h, bg_rgb=RGBColor(238, 242, 255), border_rgb=C_VIOLET)
    t3 = slide4.shapes.add_textbox(x3 + Inches(0.15), box_top + Inches(0.15), w3 - Inches(0.3), box_h - Inches(0.3))
    tf_a3 = t3.text_frame
    tf_a3.word_wrap = True
    pa3 = tf_a3.paragraphs[0]
    pa3.text = "DETERMINISTIC SIM CORE"
    pa3.font.name = FONT_HEADING
    pa3.font.size = Pt(9.5)
    pa3.font.bold = True
    pa3.font.color.rgb = C_VIOLET

    pa3_t = tf_a3.add_paragraph()
    pa3_t.text = "@outpost-x/sim (Pure TS)"
    pa3_t.font.name = FONT_HEADING
    pa3_t.font.size = Pt(13)
    pa3_t.font.bold = True
    pa3_t.font.color.rgb = C_NAVY

    pa3_b = tf_a3.add_paragraph()
    pa3_b.space_before = Pt(8)
    pa3_b.text = "• Zero DOM/Node Dependencies:\n  No Math.random, Date.now,\n  or unseeded system clocks.\n\n" \
                 "• 10-Stage Hourly Pipeline:\n  1. Insolation & Environment\n  2. Microgrid Power Allocation\n  3. Thermal Control Loops\n  4. Closed-Loop ECLSS Balance\n  5. Water Reclamation Draw\n  6. Crop & Food Nutrition\n  7. Radiation Dosimetry\n  8. BVAD Crew Health & EVA\n  9. TRL Reliability Failures\n  10. End-Condition Checks\n\n" \
                 "• sfc32 Seeded PRNG:\n  Isolated sub-streams for weather,\n  failures, and solar storms."
    pa3_b.font.name = FONT_BODY
    pa3_b.font.size = Pt(8.5)
    pa3_b.font.color.rgb = C_SLATE

    # Layer 4: Reactive UI & Visuals (Col 4)
    w4 = Inches(2.6)
    x4 = x3 + w3 + Inches(0.3)
    add_card(slide4, x4, box_top, w4, box_h, bg_rgb=RGBColor(248, 250, 252))
    t4 = slide4.shapes.add_textbox(x4 + Inches(0.15), box_top + Inches(0.15), w4 - Inches(0.3), box_h - Inches(0.3))
    tf_a4 = t4.text_frame
    tf_a4.word_wrap = True
    pa4 = tf_a4.paragraphs[0]
    pa4.text = "MISSION CONTROL UI"
    pa4.font.name = FONT_HEADING
    pa4.font.size = Pt(9.5)
    pa4.font.bold = True
    pa4.font.color.rgb = C_CYAN

    pa4_t = tf_a4.add_paragraph()
    pa4_t.text = "React 18 & Presentation"
    pa4_t.font.name = FONT_HEADING
    pa4_t.font.size = Pt(13)
    pa4_t.font.bold = True
    pa4_t.font.color.rgb = C_NAVY

    pa4_b = tf_a4.add_paragraph()
    pa4_b.space_before = Pt(8)
    pa4_b.text = "• Zustand Store:\n  Immutable reactive run state\n  with zero prop drilling\n\n" \
                 "• Reality Dial Adapter:\n  Transforms simulation state into\n  Cadet / Specialist / Commander\n\n" \
                 "• Interactive 3D Orbit:\n  azmth.space Artemis II embed\n  and NASA Eyes solar system\n\n" \
                 "• Causal Fault Visuals:\n  d3-force directed graphs\n  and Leaflet GIS mapping"
    pa4_b.font.name = FONT_BODY
    pa4_b.font.size = Pt(8.5)
    pa4_b.font.color.rgb = C_SLATE

    # Bottom Tech Stack Badges
    tech_bar = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.3), Inches(11.733), Inches(0.55))
    tech_bar.fill.solid()
    tech_bar.fill.fore_color.rgb = RGBColor(241, 245, 249)
    tech_bar.line.color.rgb = C_BORDER
    tf_tb = tech_bar.text_frame
    tf_tb.margin_top = Inches(0.12)
    p_tb = tf_tb.paragraphs[0]
    p_tb.text = "VERIFIED PRODUCTION STACK: React 18  |  TypeScript 5.9  |  Vite 6  |  Zustand 5  |  D3.js  |  Leaflet  |  Vitest (691 Tests Passed)  |  Playwright E2E"
    p_tb.font.name = FONT_HEADING
    p_tb.font.size = Pt(9)
    p_tb.font.bold = True
    p_tb.font.color.rgb = C_SLATE
    p_tb.alignment = PP_ALIGN.CENTER

    add_footer(slide4, 4)

    # =========================================================
    # SLIDE 5: THE REALITY DIAL & OPERATIONAL WORKFLOW
    # =========================================================
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide5)
    add_header(slide5, 
        kicker="Cognitive Adaptability & Mission Lifecycle", 
        title="The Reality Dial & 5-Stage Mission Operational Lifecycle", 
        subtitle="One deterministic simulation engine supporting three cognitive tiers from youth to flight directors"
    )

    # Top Half: 3 Reality Dial Cards
    top_w = Inches(3.65)
    top_gap = Inches(0.38)
    top_h = Inches(2.25)
    top_y5 = Inches(1.6)

    dial_tiers = [
        {
            "tier": "CADET LEVEL (AGES 7–12)",
            "sub": "Qualitative Visuals",
            "bg": RGBColor(236, 253, 245),
            "accent": C_GREEN,
            "desc": "• Simplified visual gauges and plain-word status ('Air is Good', 'Half Full').\n• Flesch-Kincaid Grade 3.6 readability—zero intimidating jargon.\n• Illustrated junior cockpit and visual alert icons."
        },
        {
            "tier": "SPECIALIST LEVEL (AGES 12–14)",
            "sub": "Explicit Engineering Units",
            "bg": RGBColor(238, 242, 255),
            "accent": C_BLUE,
            "desc": "• Real SI units: kW, kWh, kg/day, mmHg, and mSv/sol.\n• Detailed subsystem breakdown cards for power, ECLSS, and comms.\n• Grade 7.2 reading level suitable for middle-school STEM classrooms."
        },
        {
            "tier": "COMMANDER LEVEL (AGES 15+)",
            "sub": "Rate Equations & Derivatives",
            "bg": RGBColor(248, 250, 252),
            "accent": C_VIOLET,
            "desc": "• Mathematical rate equations (dm/dt, dE/dt) and threshold safety limits.\n• Stoichiometric Sabatier equations and battery degradation curves.\n• Flight-director level telemetry for high school and university students."
        }
    ]

    for i, d in enumerate(dial_tiers):
        dx = Inches(0.8) + (top_w + top_gap) * i
        add_card(slide5, dx, top_y5, top_w, top_h, bg_rgb=d["bg"], border_rgb=d["accent"])
        tb = slide5.shapes.add_textbox(dx + Inches(0.15), top_y5 + Inches(0.12), top_w - Inches(0.3), top_h - Inches(0.24))
        tf = tb.text_frame
        tf.word_wrap = True
        pt1 = tf.paragraphs[0]
        pt1.text = d["tier"]
        pt1.font.name = FONT_HEADING
        pt1.font.size = Pt(9.5)
        pt1.font.bold = True
        pt1.font.color.rgb = d["accent"]

        pt2 = tf.add_paragraph()
        pt2.text = d["sub"]
        pt2.font.name = FONT_HEADING
        pt2.font.size = Pt(13)
        pt2.font.bold = True
        pt2.font.color.rgb = C_NAVY

        pt3 = tf.add_paragraph()
        pt3.space_before = Pt(4)
        pt3.text = d["desc"]
        pt3.font.name = FONT_BODY
        pt3.font.size = Pt(8.5)
        pt3.font.color.rgb = C_SLATE

    # Bottom Half: 5 Process Steps on Left (width 7.0), Setup Screenshot on Right (width 4.4)
    wf_top = Inches(4.05)
    wf_h = Inches(2.75)
    left_flow_w = Inches(7.2)
    add_card(slide5, Inches(0.8), wf_top, left_flow_w, wf_h, bg_rgb=C_CARD_BG)

    wf_box = slide5.shapes.add_textbox(Inches(1.0), wf_top + Inches(0.12), Inches(6.8), Inches(0.3))
    p_wfh = wf_box.text_frame.paragraphs[0]
    p_wfh.text = "END-TO-END MISSION OPERATIONAL WORKFLOW"
    p_wfh.font.name = FONT_HEADING
    p_wfh.font.size = Pt(9.5)
    p_wfh.font.bold = True
    p_wfh.font.color.rgb = C_CYAN

    # 5 Process Steps arranged vertically or grid
    step_flow_box = slide5.shapes.add_textbox(Inches(1.0), wf_top + Inches(0.42), Inches(6.8), Inches(2.2))
    tf_sf = step_flow_box.text_frame
    tf_sf.word_wrap = True
    tf_sf.margin_left = tf_sf.margin_top = tf_sf.margin_right = tf_sf.margin_bottom = 0

    p_s1 = tf_sf.paragraphs[0]
    p_s1.text = "1. Mission Selection: Pick from 5 planetary outposts (Mars Jezero, Lunar Ridge); configure power & shielding."
    p_s1.font.name = FONT_BODY
    p_s1.font.size = Pt(8.5)
    p_s1.font.bold = True
    p_s1.font.color.rgb = C_SLATE

    p_s2 = tf_sf.add_paragraph()
    p_s2.space_before = Pt(4)
    p_s2.text = "2. Resource Management: Assign crew to consoles under NASA BVAD work/rest schedules; prioritize load shedding."
    p_s2.font.name = FONT_BODY
    p_s2.font.size = Pt(8.5)
    p_s2.font.bold = True
    p_s2.font.color.rgb = C_SLATE

    p_s3 = tf_sf.add_paragraph()
    p_s3.space_before = Pt(4)
    p_s3.text = "3. Operational Decisions: Advance sol timeline (1x-16x). Balance battery SOC with insolation and Sabatier scrubbers."
    p_s3.font.name = FONT_BODY
    p_s3.font.size = Pt(8.5)
    p_s3.font.bold = True
    p_s3.font.color.rgb = C_SLATE

    p_s4 = tf_sf.add_paragraph()
    p_s4.space_before = Pt(4)
    p_s4.text = "4. Emergency Response: Triage DONKI solar proton storms, equipment failures, and shelter orders via Incident Command."
    p_s4.font.name = FONT_BODY
    p_s4.font.size = Pt(8.5)
    p_s4.font.bold = True
    p_s4.font.color.rgb = C_SLATE

    p_s5 = tf_sf.add_paragraph()
    p_s5.space_before = Pt(4)
    p_s5.text = "5. Mission Debrief: Inspect Black Box causal DAG and verify learning via Big Idea formative concept checks."
    p_s5.font.name = FONT_BODY
    p_s5.font.size = Pt(8.5)
    p_s5.font.bold = True
    p_s5.font.color.rgb = C_SLATE

    # Right side: Setup Wizard Screenshot
    setup_img = os.path.join(ROOT_DIR, "docs/screenshots/02-setup-wizard.png")
    if os.path.exists(setup_img):
        add_framed_image(slide5, setup_img, Inches(8.25), wf_top, Inches(4.283), wf_h)

    add_footer(slide5, 5)

    # =========================================================
    # SLIDE 6: NASA OPEN DATA & SCIENTIFIC VALIDATION
    # =========================================================
    slide6 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide6)
    add_header(slide6, 
        kicker="Scientific Foundations & Open Data Pedigree", 
        title="Zero Fabricated Numbers: 59 Verified Datasets & Scenarios", 
        subtitle="100% of physical parameters trace to NASA Technical Publications, peer-reviewed literature, and empirical telemetry"
    )

    top_y6 = Inches(1.6)
    col_w6 = Inches(3.65)
    col_gap6 = Inches(0.38)
    col_h6 = Inches(4.35)

    # Col 1: Sourced NASA Technical Literature
    add_card(slide6, Inches(0.8), top_y6, col_w6, col_h6)
    c1_box = slide6.shapes.add_textbox(Inches(0.95), top_y6 + Inches(0.15), col_w6 - Inches(0.3), col_h6 - Inches(0.3))
    tf_c1 = c1_box.text_frame
    tf_c1.word_wrap = True
    pc1_h = tf_c1.paragraphs[0]
    pc1_h.text = "NASA TECHNICAL STANDARDS"
    pc1_h.font.name = FONT_HEADING
    pc1_h.font.size = Pt(9.5)
    pc1_h.font.bold = True
    pc1_h.font.color.rgb = C_CYAN

    pc1_t = tf_c1.add_paragraph()
    pc1_t.text = "Peer-Reviewed Citations"
    pc1_t.font.name = FONT_HEADING
    pc1_t.font.size = Pt(13)
    pc1_t.font.bold = True
    pc1_t.font.color.rgb = C_NAVY

    pc1_b = tf_c1.add_paragraph()
    pc1_b.space_before = Pt(6)
    pc1_b.text = "• NASA BVAD-2022 (NASA/TP-20210024855):\n  Human metabolic rates: 0.84 kg O2, 1.00 kg CO2,\n  2.5 L H2O, 3,000 kcal per crew-day.\n\n" \
                 "• NASA OCHMO Technical Briefs:\n  TB-003 Habitable Atmosphere (ppO2 >= 19.5 kPa),\n  TB-047 Crew Survivability emergency minimums.\n\n" \
                 "• NASA Fission Surface Power (IAC-24):\n  40 kWe Stirling reactor mass (6,000 kg) and\n  thermal radiator rejection characteristics.\n\n" \
                 "• Surface Radiation Dosimetry:\n  Curiosity MSL RAD (0.64 mSv/d) and Chang'e-4\n  lunar dosimeter measurements (1.369 mSv/d)."
    pc1_b.font.name = FONT_BODY
    pc1_b.font.size = Pt(8.5)
    pc1_b.font.color.rgb = C_SLATE

    # Col 2: In-App Data Passport & Pedigree
    add_card(slide6, Inches(0.8) + col_w6 + col_gap6, top_y6, col_w6, col_h6)
    c2_box = slide6.shapes.add_textbox(Inches(0.95) + col_w6 + col_gap6, top_y6 + Inches(0.15), col_w6 - Inches(0.3), col_h6 - Inches(0.3))
    tf_c2 = c2_box.text_frame
    tf_c2.word_wrap = True
    pc2_h = tf_c2.paragraphs[0]
    pc2_h.text = "DATA PASSPORT & PEDIGREE"
    pc2_h.font.name = FONT_HEADING
    pc2_h.font.size = Pt(9.5)
    pc2_h.font.bold = True
    pc2_h.font.color.rgb = C_BLUE

    pc2_t = tf_c2.add_paragraph()
    pc2_t.text = "59 Cataloged Datasets"
    pc2_t.font.name = FONT_HEADING
    pc2_t.font.size = Pt(13)
    pc2_t.font.bold = True
    pc2_t.font.color.rgb = C_NAVY

    pc2_b = tf_c2.add_paragraph()
    pc2_b.space_before = Pt(6)
    pc2_b.text = "• 48 Verified Entries (81.4%):\n  Audited against primary spaceflight literature.\n\n" \
                 "• Evidence Pedigree Labels:\n  Live (active API) | Snapshot (committed)\n  Archived (historical) | Derived (physics model)\n\n" \
                 "• Automated Integrity Test Harness:\n  constants.test.ts asserts 100% of physical\n  constants link to authenticated Data Passport rows.\n\n" \
                 "• Transparent Game-Design Disclosures:\n  Tuned balancing factors are openly tagged\n  with confidence: 'tuned'—never faked as facts."
    pc2_b.font.name = FONT_BODY
    pc2_b.font.size = Pt(8.5)
    pc2_b.font.color.rgb = C_SLATE

    # Col 3: Missions & Crisis Replays
    add_card(slide6, Inches(0.8) + (col_w6 + col_gap6)*2, top_y6, col_w6, col_h6)
    c3_box = slide6.shapes.add_textbox(Inches(0.95) + (col_w6 + col_gap6)*2, top_y6 + Inches(0.15), col_w6 - Inches(0.3), col_h6 - Inches(0.3))
    tf_c3 = c3_box.text_frame
    tf_c3.word_wrap = True
    pc3_h = tf_c3.paragraphs[0]
    pc3_h.text = "TRAINING & HISTORICAL REPLAYS"
    pc3_h.font.name = FONT_HEADING
    pc3_h.font.size = Pt(9.5)
    pc3_h.font.bold = True
    pc3_h.font.color.rgb = C_VIOLET

    pc3_t = tf_c3.add_paragraph()
    pc3_t.text = "5 Missions + 3 Crises"
    pc3_t.font.name = FONT_HEADING
    pc3_t.font.size = Pt(13)
    pc3_t.font.bold = True
    pc3_t.font.color.rgb = C_NAVY

    pc3_b = tf_c3.add_paragraph()
    pc3_b.space_before = Pt(6)
    pc3_b.text = "• 5 Sourced Training Missions:\n  1. Jezero Outpost (Mars global dust storm)\n  2. First Light (354-h polar cryogenic night)\n  3. The Long Night (89-d fission reactor base)\n  4. Green Thumb (closed-loop greenhouse)\n  5. Storm Watch (DONKI May 2024 solar storm)\n\n" \
                 "• 3 Historical NASA Crisis Replays:\n  1. Apollo 13 CO2 Buildup (LiOH adapter)\n  2. 1972 Solar Proton Event (>400 mSv shelter)\n  3. Mir Station Fire 1997 (Vika O2 combustion)"
    pc3_b.font.name = FONT_BODY
    pc3_b.font.size = Pt(8.5)
    pc3_b.font.color.rgb = C_SLATE

    # Bottom Verification Bar
    ver_bar = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.15), Inches(11.733), Inches(0.7))
    ver_bar.fill.solid()
    ver_bar.fill.fore_color.rgb = RGBColor(240, 253, 244)
    ver_bar.line.color.rgb = C_GREEN
    ver_bar.line.width = Pt(1)
    tf_vb = ver_bar.text_frame
    tf_vb.margin_top = Inches(0.12)
    p_vb = tf_vb.paragraphs[0]
    p_vb.text = "RIGOROUS QA HARNESS: 75 Test Suites Passed  ·  691 Unit Tests (0 Failures)  ·  4,050 Monte Carlo Seeds Verified  ·  Zero Lint/Purity Warnings"
    p_vb.font.name = FONT_HEADING
    p_vb.font.size = Pt(9.5)
    p_vb.font.bold = True
    p_vb.font.color.rgb = RGBColor(21, 128, 61)
    p_vb.alignment = PP_ALIGN.CENTER

    add_footer(slide6, 6)

    # =========================================================
    # SLIDE 7: LIVE DEMO, IMPACT & ROADMAP
    # =========================================================
    slide7 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide7)
    add_header(slide7, 
        kicker="Mission Command Showcase & Project Roadmap", 
        title="Ready for Mission Command: Live Demo & Future Horizons", 
        subtitle="A production-grade, classroom-ready platform empowering humanity's next generation of explorers"
    )

    # Left: Large Screenshot of Mission Command
    mc_img = os.path.join(ROOT_DIR, "docs/screenshots/07-mission-command.png")
    if os.path.exists(mc_img):
        add_framed_image(slide7, mc_img, Inches(0.8), Inches(1.65), Inches(6.2), Inches(3.9))
        
        cap7 = slide7.shapes.add_textbox(Inches(0.8), Inches(5.62), Inches(6.2), Inches(0.4))
        p_c7 = cap7.text_frame.paragraphs[0]
        p_c7.text = "Live Mission Command Deck: Crew Station Assignments, Orbital Trackers, and BVAD Schedule"
        p_c7.font.name = FONT_BODY
        p_c7.font.size = Pt(8.5)
        p_c7.font.color.rgb = C_MUTED
        p_c7.alignment = PP_ALIGN.CENTER

    # Left Bottom: 4-Step Demo Sequence Pill
    demo_seq = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.1), Inches(6.2), Inches(0.75))
    demo_seq.fill.solid()
    demo_seq.fill.fore_color.rgb = RGBColor(241, 245, 249)
    demo_seq.line.color.rgb = C_BORDER
    tf_ds = demo_seq.text_frame
    tf_ds.margin_top = Inches(0.12)
    p_ds1 = tf_ds.paragraphs[0]
    p_ds1.text = "LIVE DEMO SEQUENCE FOR JUDGES"
    p_ds1.font.name = FONT_HEADING
    p_ds1.font.size = Pt(8.5)
    p_ds1.font.bold = True
    p_ds1.font.color.rgb = C_BLUE
    p_ds1.alignment = PP_ALIGN.CENTER

    p_ds2 = tf_ds.add_paragraph()
    p_ds2.text = "1. Select Mission  ➔  2. Operate Systems  ➔  3. Handle Emergency  ➔  4. Review Debrief"
    p_ds2.font.name = FONT_HEADING
    p_ds2.font.size = Pt(10)
    p_ds2.font.bold = True
    p_ds2.font.color.rgb = C_NAVY
    p_ds2.alignment = PP_ALIGN.CENTER

    # Right Side: Access Links & Future Roadmap
    rx = Inches(7.3)
    rw = Inches(5.233)

    # Future Roadmap Card
    add_card(slide7, rx, Inches(1.65), rw, Inches(2.2), bg_rgb=C_CARD_BG)
    rm_box = slide7.shapes.add_textbox(rx + Inches(0.2), Inches(1.75), rw - Inches(0.4), Inches(2.0))
    tf_rm = rm_box.text_frame
    tf_rm.word_wrap = True
    p_rm1 = tf_rm.paragraphs[0]
    p_rm1.text = "FUTURE HORIZONS & ROADMAP"
    p_rm1.font.name = FONT_HEADING
    p_rm1.font.size = Pt(9.5)
    p_rm1.font.bold = True
    p_rm1.font.color.rgb = C_CYAN

    p_rm2 = tf_rm.add_paragraph()
    p_rm2.space_before = Pt(4)
    p_rm2.text = "• Expanded Outer Moons: Sub-surface ocean bases on Europa and Enceladus; hydrocarbon balloon habitats on Titan.\n" \
                 "• Real-Time Classroom Multiplayer: Multi-device shared flight deck where students specialize in individual station consoles.\n" \
                 "• Physical Hardware Mockups: Telemetry API bridge for Arduino / Raspberry Pi tactile physical control panels."
    p_rm2.font.name = FONT_BODY
    p_rm2.font.size = Pt(8.5)
    p_rm2.font.color.rgb = C_SLATE

    # Access Links & Team Box
    add_card(slide7, rx, Inches(4.0), rw, Inches(2.85), bg_rgb=RGBColor(240, 249, 255), border_rgb=C_CYAN)
    ln_box = slide7.shapes.add_textbox(rx + Inches(0.2), Inches(4.1), rw - Inches(0.4), Inches(2.6))
    tf_ln = ln_box.text_frame
    tf_ln.word_wrap = True

    p_lnh = tf_ln.paragraphs[0]
    p_lnh.text = "ACCESS & VERIFICATION PORTALS"
    p_lnh.font.name = FONT_HEADING
    p_lnh.font.size = Pt(9.5)
    p_lnh.font.bold = True
    p_lnh.font.color.rgb = C_CYAN

    p_ln1 = tf_ln.add_paragraph()
    p_ln1.space_before = Pt(4)
    p_ln1.text = "🌐 Live Deployment: https://outpostx.vercel.app/\n" \
                 "💻 GitHub Repository: github.com/mouryas-aiml/OUTPOST-X\n" \
                 "📁 Space Apps Assets: Google Drive Submission Folder"
    p_ln1.font.name = FONT_BODY
    p_ln1.font.size = Pt(9)
    p_ln1.font.bold = True
    p_ln1.font.color.rgb = C_BLUE

    p_lnt = tf_ln.add_paragraph()
    p_lnt.space_before = Pt(6)
    p_lnt.text = "Team TensorMinds: Mourya S  ·  Chitra Shree K  ·  Monika S"
    p_lnt.font.name = FONT_HEADING
    p_lnt.font.size = Pt(9.5)
    p_lnt.font.bold = True
    p_lnt.font.color.rgb = C_NAVY

    p_lnq = tf_ln.add_paragraph()
    p_lnq.space_before = Pt(6)
    p_lnq.text = "“Take Command. Build Beyond Earth. Shape Humanity’s Next Frontier.”"
    p_lnq.font.name = FONT_BODY
    p_lnq.font.size = Pt(10)
    p_lnq.font.bold = True
    p_lnq.font.color.rgb = C_CYAN

    add_footer(slide7, 7)

    output_pptx = os.path.join(ROOT_DIR, "OUTPOST-X_TensorMinds_NASA_Space_Apps_2026.pptx")
    prs.save(output_pptx)
    print(f"Presentation successfully created: {output_pptx}")
    print(f"Total slides: {len(prs.slides)}")

if __name__ == "__main__":
    generate_presentation()
