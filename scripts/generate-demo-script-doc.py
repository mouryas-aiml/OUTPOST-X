import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def create_element(name):
    return OxmlElement(name)

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_callout(doc, title, text, bg_color="F0F9FF", border_color="0284C7"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, bg_color)
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
    
    # Left border only
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:top w:val="none"/><w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/><w:bottom w:val="none"/><w:right w:val="none"/></w:tcBorders>')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(3)
    run_title = p.add_run(f"📌 {title}\n")
    run_title.bold = True
    run_title.font.name = "Segoe UI"
    run_title.font.size = Pt(10.5)
    run_title.font.color.rgb = RGBColor(11, 18, 36)
    
    run_text = p.add_run(text)
    run_text.font.name = "Segoe UI"
    run_text.font.size = Pt(9.5)
    run_text.font.color.rgb = RGBColor(51, 65, 85)

def build_document(output_path):
    doc = docx.Document()
    
    # Set standard margins
    for section in doc.sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)
        section.header.paragraphs[0].text = "OUTPOST-X | 3-Minute Demonstration Script — NASA Space Apps Challenge 2026"
        section.header.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
        section.header.paragraphs[0].runs[0].font.name = "Segoe UI"
        section.header.paragraphs[0].runs[0].font.size = Pt(8.5)
        section.header.paragraphs[0].runs[0].font.color.rgb = RGBColor(148, 163, 184)

    # Palette
    C_NAVY = RGBColor(11, 18, 36)      # #0B1224
    C_CYAN = RGBColor(0, 163, 196)     # #00A3C4
    C_BLUE = RGBColor(37, 99, 235)     # #2563EB
    C_DARK = RGBColor(30, 41, 59)      # #1E293B
    C_MUTED = RGBColor(100, 116, 139)  # #64748B
    
    # ---------------------------------------------------------
    # HEADER / TITLE BLOCK
    # ---------------------------------------------------------
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(2)
    r_kicker = p_title.add_run("NASA SPACE APPS CHALLENGE 2026 · OFFICIAL VIDEO DEMONSTRATION SCRIPT\n")
    r_kicker.bold = True
    r_kicker.font.name = "Segoe UI"
    r_kicker.font.size = Pt(9.5)
    r_kicker.font.color.rgb = C_CYAN
    
    r_title = p_title.add_run("OUTPOST-X: Mission Operations Demonstration")
    r_title.bold = True
    r_title.font.name = "Segoe UI"
    r_title.font.size = Pt(24)
    r_title.font.color.rgb = C_NAVY
    
    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(12)
    r_sub = p_sub.add_run("Take Command. Build Beyond Earth. Shape Humanity’s Next Frontier.\n3-Minute (180-Second) High-Fidelity Video Script & Production Guide")
    r_sub.font.name = "Segoe UI"
    r_sub.font.size = Pt(12)
    r_sub.font.color.rgb = C_MUTED
    
    # Metadata Table
    meta_tbl = doc.add_table(rows=5, cols=2)
    meta_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ("Event & Challenge", "2026 NASA Space Apps Challenge — 'Build a Junior Astronaut Mission Trainer'"),
        ("Project & Team", "OUTPOST-X — Developed by Team TensorMinds (Mourya S, Chitra Shree K, Monika S)"),
        ("Video Duration", "Exact 180 Seconds (03:00 Minutes) · 8 Precision Timestamped Scenes"),
        ("Spoken Pace & Word Count", "143 words per minute (~430 words total) · Perfectly balanced for UI actions & pauses"),
        ("Live Verification Links", "Web: https://outpostx.vercel.app/  |  Drive: https://drive.google.com/drive/folders/1wsaJml4QNPZhfF7jVdb0f7KvSvgHjKfd")
    ]
    for i, (k, v) in enumerate(meta_data):
        cell_k = meta_tbl.cell(i, 0)
        cell_v = meta_tbl.cell(i, 1)
        cell_k.width = Inches(2.2)
        cell_v.width = Inches(4.8)
        set_cell_background(cell_k, "F8FAFC")
        set_cell_background(cell_v, "FFFFFF")
        set_cell_margins(cell_k, top=60, bottom=60, left=100, right=100)
        set_cell_margins(cell_v, top=60, bottom=60, left=100, right=100)
        pk = cell_k.paragraphs[0]
        pk.paragraph_format.space_before = Pt(0)
        pk.paragraph_format.space_after = Pt(0)
        rk = pk.add_run(k)
        rk.bold = True
        rk.font.name = "Segoe UI"
        rk.font.size = Pt(9)
        rk.font.color.rgb = C_DARK
        
        pv = cell_v.paragraphs[0]
        pv.paragraph_format.space_before = Pt(0)
        pv.paragraph_format.space_after = Pt(0)
        rv = pv.add_run(v)
        rv.font.name = "Segoe UI"
        rv.font.size = Pt(9)
        rv.font.color.rgb = C_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # ---------------------------------------------------------
    # SECTION 1: PRODUCTION & RECORDING CHECKLIST
    # ---------------------------------------------------------
    h1 = doc.add_heading("1. Pre-Recording Technical Checklist", level=1)
    h1.runs[0].font.name = "Segoe UI"
    h1.runs[0].font.color.rgb = C_NAVY
    
    add_callout(doc, "Screen & Audio Capture Setup", 
        "• Resolution: 1920×1080 (1080p, 60 FPS) in Full Screen mode (press F11 in Chrome to hide browser bookmarks).\n"
        "• Audio Setup: Dedicated USB cardioid microphone, quiet room, normalize audio to -14 LUFS with crisp vocal EQ.\n"
        "• Browser Tab: Open http://localhost:5173/ (or https://outpostx.vercel.app/) with mouse cursor smoothing enabled.\n"
        "• Language Setting: Ensure English is active (verify top-right toggle displays English).\n"
        "• Navigation Rule: Only click the exact buttons and tabs named in this script. Never guess or improvise page paths.",
        bg_color="F1F5F9", border_color="0EA5E9"
    )
    
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # ---------------------------------------------------------
    # SECTION 2: 180-SECOND SCRIPT & TIMELINE TABLE
    # ---------------------------------------------------------
    h2 = doc.add_heading("2. Complete 180-Second Timeline & Narration Script", level=1)
    h2.runs[0].font.name = "Segoe UI"
    h2.runs[0].font.color.rgb = C_NAVY
    
    p_intro = doc.add_paragraph("This timeline divides the 3-minute video into eight tightly synchronized scenes. The spoken narration is presented in quotation marks, matched with exact on-screen cursor movements, clicks, and UI interactions.")
    p_intro.runs[0].font.name = "Segoe UI"
    p_intro.runs[0].font.size = Pt(9.5)
    p_intro.runs[0].font.color.rgb = C_MUTED

    timeline_scenes = [
        {
            "time": "00:00 – 00:25\n(25 sec)",
            "scene": "Scene 1: Introduction, Problem Statement & Team TensorMinds",
            "screen": "1. Start on Home (/) showing the animated 3D starfield canvas, OUTPOST-X logo, and headline: 'Take Command. Build Beyond Earth. Shape Humanity’s Next Frontier.'\n"
                      "2. Scroll down smoothly to show the embedded Artemis II 3D orbital trajectory replay card (azmth.space/embed/artemis2).\n"
                      "3. Highlight the team footer: Team TensorMinds (Mourya S, Chitra Shree K, Monika S).",
            "narration": "“Welcome to OUTPOST-X, built for the 2026 NASA Space Apps Challenge by Team TensorMinds—Mourya S, Chitra Shree K, and Monika S.\n\n"
                         "Our challenge: 'Build a Junior Astronaut Mission Trainer.' Traditional space education often reduces planetary missions to trivia or oversimplified clickers, hiding the real physical trade-offs of human spaceflight.\n\n"
                         "OUTPOST-X solves this translation gap by turning authentic NASA engineering, closed-loop life support, and space weather data into an immersive mission-control simulator.”",
            "ui_actions": "• Page: Home\n• Actions: Smooth scroll past Hero to Artemis II card and Mission Pillars"
        },
        {
            "time": "00:25 – 00:50\n(25 sec)",
            "scene": "Scene 2: Core Innovation: The Reality Dial",
            "screen": "1. Scroll back to top and click 'LAUNCH OUTPOST' (or 'PLAY').\n"
                      "2. The app opens directly to the Jezero Outpost Mission Command deck in Cockpit view.\n"
                      "3. Focus camera on the Reality Dial selector in the top-center header.\n"
                      "4. Click 'Cadet', then 'Specialist', then 'Commander'. Show gauges dynamically transforming.",
            "narration": "“Our core breakthrough is the Reality Dial: ONE deterministic simulation presented at three cognitive depths.\n\n"
                         "In Cadet mode, younger astronauts ages 7 to 12 see visual icons and plain-language status bars at a Grade 3.6 reading level.\n\n"
                         "Flip to Specialist, and the gauges unlock real SI engineering units: kilowatts, kilograms per day, and millimeters of mercury.\n\n"
                         "Flip to Commander, and high-school students analyze differential rate equations and margin limits.\n\n"
                         "The underlying physics never changes—only the cognitive representation does.”",
            "ui_actions": "• Buttons: 'LAUNCH OUTPOST'\n• Header: Click 'Cadet' ➔ 'Specialist' ➔ 'Commander'"
        },
        {
            "time": "00:50 – 01:10\n(20 sec)",
            "scene": "Scene 3: Mission Setup & The 5 Planetary Scenarios",
            "screen": "1. Click 'New Mission' in the top navigation bar.\n"
                      "2. Show the Setup Wizard: browse landing sites across Mars (Jezero Crater) and the Moon (Connecting Ridge, Marius Hills).\n"
                      "3. Showcase the 5 standard training missions: Jezero Outpost, First Light, The Long Night, Green Thumb, and Storm Watch.\n"
                      "4. Configure Power Architecture (Solar vs Fission) and Shielding (Regolith Berm vs Water Wall). Click 'Launch Standard Mission'.",
            "narration": "“In New Mission, commanders configure authentic planetary landing sites and mission parameters.\n\n"
                         "We provide five distinct scenarios: surviving a massive 2018-scale Martian dust storm at Jezero Crater, enduring a 354-hour cryogenic polar night at lunar Connecting Ridge, managing closed-loop hydroponic crops at Marius Hills, and facing an extreme May 2024 solar proton event.\n\n"
                         "Every parameter traces directly to NASA planetary surface data.”",
            "ui_actions": "• Top Bar: Click 'New Mission'\n• Wizard: Select scenario, configure power/shielding ➔ 'Launch Standard Mission'"
        },
        {
            "time": "01:10 – 01:45\n(35 sec)",
            "scene": "Scene 4: Operational Consoles: Power, Life Support & Comms",
            "screen": "1. Click 'Power' in the left sidebar (#tab-power).\n"
                      "   - Drag load-shedding priority list: demonstrate moving Life Support above Science.\n"
                      "   - Click '▶ Run the sol' in TimeControls (set to 4× speed) to watch solar array generation and battery discharge.\n"
                      "2. Click 'Life Support' in the left sidebar (#tab-lifeSupport).\n"
                      "   - Toggle the Brine Processor Assembly (BPA) switch: highlight water recovery rising from 93% to 98% while consuming 1.5 crew-hours.\n"
                      "3. Click 'Comms' in the left sidebar (#tab-comms).\n"
                      "   - Point to the Earth distance and dynamic light-time latency calculated from JPL Horizons.",
            "narration": "“Command is organized into five specialized stations in the left sidebar.\n\n"
                         "On the Power Console, we manage a hybrid microgrid. Notice how reordering load-shedding priorities protects critical life support when dust storms obscure our solar array.\n\n"
                         "On the Life Support Console, we balance closed-loop ECLSS chemistry. Activating the Brine Processor boosts water recycling to 98%, but demands 1.5 crew-hours daily of intense maintenance.\n\n"
                         "On the Comms Console, messages experience real interplanetary light-time delay—calculated live from NASA JPL Horizons ephemerides coordinates.”",
            "ui_actions": "• Left Sidebar: Click 'Power' ➔ adjust priority list ➔ Click '▶ Run the sol'\n• Left Sidebar: Click 'Life Support' ➔ toggle BPA switch\n• Left Sidebar: Click 'Comms' ➔ inspect light-time delay"
        },
        {
            "time": "01:45 – 02:15\n(30 sec)",
            "scene": "Scene 5: Incident Command, Habitat & Historical Crisis Replay",
            "screen": "1. Click 'Incident Command' in sidebar (#tab-incidentCommand).\n"
                      "   - Show incoming space weather alert from NASA DONKI (e.g. Solar Energetic Particle event).\n"
                      "   - Review the causal dependency tree linking radiation to crew sheltering.\n"
                      "2. Click 'Habitat' in sidebar (#tab-habitat).\n"
                      "   - Show the 2D architectural cutaway of the outpost, airlock cycles, and pressurized volumes.\n"
                      "3. Click 'Crisis Replay' in sidebar (#tab-crisis).\n"
                      "   - Showcase the 3 historical missions: Apollo 13 CO₂ Buildup, Solar Particle Event 1972, and Mir Space Station Fire 1997.",
            "narration": "“When space hazards strike, Incident Command ingests real-time solar flare data from NASA’s DONKI database. A causal Directed Acyclic Graph traces every fault—showing how an unshielded radiation burst halts EVA science and triggers emergency shelter protocols.\n\n"
                         "The Habitat tab visualizes our physical outpost modules and environmental barriers.\n\n"
                         "For master commanders, Crisis Replay recreates legendary space emergencies using official NASA mishap investigation data—from Apollo 13's improvised LiOH scrubber to the 1972 extreme solar storm.”",
            "ui_actions": "• Left Sidebar: Click 'Incident Command' ➔ inspect DONKI alert\n• Left Sidebar: Click 'Habitat' ➔ view module cutaway\n• Left Sidebar: Click 'Crisis Replay' ➔ showcase Apollo 13 & 1972 SPE"
        },
        {
            "time": "02:15 – 02:35\n(20 sec)",
            "scene": "Scene 6: Crew Management, Debrief & Black Box Causality",
            "screen": "1. Click 'Mission Command' in sidebar (#tab-missionCommand).\n"
                      "   - Show crew assignments (Ayesha, Diego, Tunde, Chen) and BVAD-2022 work/rest schedules.\n"
                      "2. Advance time to complete sol; click 'Debrief' in sidebar (#tab-debrief).\n"
                      "   - Inspect the mission outcome summary, Black Box causal chain, and Big Idea concept checks.\n"
                      "3. Click 'View Mission Report' to show the printable PDF-ready debrief and shareable class link.",
            "narration": "“On Mission Command, we assign our crew according to NASA BVAD human spaceflight standards, balancing research against physical fatigue.\n\n"
                         "At mission end, the Debrief console provides flight telemetry forensics. The Black Box records every decision's ripple effect, followed by Big Idea formative checks that verify what students learned about deep-space survival.\n\n"
                         "Teachers can generate a shareable class link—replaying the exact mission seed without student logins.”",
            "ui_actions": "• Left Sidebar: Click 'Mission Command' ➔ inspect crew roster\n• Left Sidebar: Click 'Debrief' ➔ inspect Black Box DAG & Big Idea checks\n• Click 'View Mission Report'"
        },
        {
            "time": "02:35 – 02:50\n(15 sec)",
            "scene": "Scene 7: Scientific Foundations, Data Passport & Technical Stack",
            "screen": "1. Click 'Data Passport' in the top navigation bar.\n"
                      "   - Scroll through the 59 authenticated dataset rows (BVAD, OCHMO, DONKI, OSDR, RadLab).\n"
                      "2. Click 'Data Sources' to show primary literature citations.\n"
                      "3. Briefly display terminal/GitHub showing 691 passing automated Vitest tests.",
            "narration": "“Scientifically, OUTPOST-X contains zero fabricated numbers. In our Data Passport, every single constant cites NASA standards, from OCHMO medical briefs to OSDR radiation dosimetry.\n\n"
                         "Technically, the simulation engine is written in pure deterministic TypeScript, verified by 691 automated unit tests and a 4,050-seed Monte Carlo suite, running as a 100% offline Progressive Web App.”",
            "ui_actions": "• Top Bar: Click 'Data Passport' ➔ scroll 59 source rows\n• Top Bar: Click 'Data Sources' ➔ highlight BVAD & OCHMO citations"
        },
        {
            "time": "02:50 – 03:00\n(10 sec)",
            "scene": "Scene 8: Conclusion & Call to Action",
            "screen": "1. Click 'Home' in top bar to return to the landing deck.\n"
                      "2. Center on the OUTPOST-X logo and tagline with the animated 3D starfield canvas.\n"
                      "3. Display final slide with team names, project URL, and NASA Space Apps 2026 insignia.",
            "narration": "“OUTPOST-X bridges authentic aerospace engineering with interactive play—inspiring the next generation of engineers, flight directors, and astronauts.\n\n"
                         "Take command today at outpostx.vercel.app. We are Team TensorMinds. Thank you!”",
            "ui_actions": "• Top Bar: Click 'Home'\n• Fade out on OUTPOST-X logo, live URL, and Team TensorMinds credits"
        }
    ]

    for item in timeline_scenes:
        # Scene heading
        p_sh = doc.add_paragraph()
        p_sh.paragraph_format.space_before = Pt(14)
        p_sh.paragraph_format.space_after = Pt(2)
        r_time = p_sh.add_run(f"⏱ {item['time'].replace(chr(10), ' ')} — {item['scene']}")
        r_time.bold = True
        r_time.font.name = "Segoe UI"
        r_time.font.size = Pt(12)
        r_time.font.color.rgb = C_BLUE

        # Table for Scene Breakdown
        tbl = doc.add_table(rows=3, cols=2)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        
        # Col widths
        rows_content = [
            ("Screen Recording & Visuals", item['screen']),
            ("Spoken Narration (Voiceover)", item['narration']),
            ("UI Targets & Clicks", item['ui_actions'])
        ]
        
        for r_idx, (label, text) in enumerate(rows_content):
            cell_lbl = tbl.cell(r_idx, 0)
            cell_txt = tbl.cell(r_idx, 1)
            cell_lbl.width = Inches(2.0)
            cell_txt.width = Inches(5.0)
            
            if r_idx == 1:
                # Narration row highlighted
                set_cell_background(cell_lbl, "EFF6FF")
                set_cell_background(cell_txt, "FAFAFA")
            else:
                set_cell_background(cell_lbl, "F8FAFC")
                set_cell_background(cell_txt, "FFFFFF")
                
            set_cell_margins(cell_lbl, top=80, bottom=80, left=100, right=100)
            set_cell_margins(cell_txt, top=80, bottom=80, left=120, right=120)
            
            p_l = cell_lbl.paragraphs[0]
            p_l.paragraph_format.space_before = Pt(0)
            p_l.paragraph_format.space_after = Pt(0)
            rl = p_l.add_run(label)
            rl.bold = True
            rl.font.name = "Segoe UI"
            rl.font.size = Pt(9)
            rl.font.color.rgb = C_DARK
            
            p_t = cell_txt.paragraphs[0]
            p_t.paragraph_format.space_before = Pt(0)
            p_t.paragraph_format.space_after = Pt(0)
            rt = p_t.add_run(text)
            rt.font.name = "Segoe UI"
            rt.font.size = Pt(9.5)
            if r_idx == 1:
                rt.font.color.rgb = RGBColor(15, 23, 42)
                rt.italic = True
            else:
                rt.font.color.rgb = C_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # ---------------------------------------------------------
    # SECTION 3: EXACT MENU & PAGE NAVIGATION DIRECTORY
    # ---------------------------------------------------------
    h3 = doc.add_heading("3. Exact Page & Menu Names Directory", level=1)
    h3.runs[0].font.name = "Segoe UI"
    h3.runs[0].font.color.rgb = C_NAVY

    p_nav_note = doc.add_paragraph("CRITICAL RECORDING INSTRUCTION: In accordance with competition evaluation criteria, the narrator and recording operator MUST use ONLY the exact UI labels implemented in the OUTPOST-X production codebase:")
    p_nav_note.runs[0].font.name = "Segoe UI"
    p_nav_note.runs[0].font.size = Pt(9.5)

    nav_table_data = [
        ("UI Location", "Exact Page / Button Label", "Component & Functionality", "Key User Interactions"),
        ("Left Sidebar", "Power", "PowerConsole (#tab-power)", "Dynamic load-shedding priority hierarchy, fission vs solar grid, battery state of charge (kWh)."),
        ("Left Sidebar", "Life Support", "LifeSupportConsole (#tab-lifeSupport)", "Closed-loop ECLSS, ppO2 / ppCO2 partial pressures, Sabatier reactor, Brine Processor water loop."),
        ("Left Sidebar", "Comms", "CommsConsole (#tab-comms)", "Deep Space Network link margins, authentic JPL Horizons light-time latency, radio packets."),
        ("Left Sidebar", "Incident Command", "IncidentCommandConsole (#tab-incidentCommand)", "NASA DONKI space weather alert triage, fault trees, hazard mitigations, causal DAG."),
        ("Left Sidebar", "Mission Command", "MissionCommandConsole (#tab-missionCommand)", "Crew station assignments, NASA BVAD daily schedule, fatigue management, NASA Eyes 3D view."),
        ("Left Sidebar", "Habitat", "HabitatView (#tab-habitat)", "Architectural cutaway of planetary base, module pressure integrity, radiation shelter status."),
        ("Left Sidebar", "Crisis Replay", "CrisisSelectionView (#tab-crisis)", "Replay 3 historical emergencies: Apollo 13 CO2, 1972 Solar Proton Event, 1997 Mir Fire."),
        ("Left Sidebar", "Briefing", "BriefingView (#tab-briefing)", "Mission parameters, landing site environmental overview, initial consumable inventories."),
        ("Left Sidebar", "Debrief", "DebriefView (#tab-debrief)", "Flight outcome forensics, Black Box causal chain, Big Idea formative STEM concept checks."),
        ("Top Bar", "Home", "HomeView (/)", "Command landing deck, Artemis II trajectory replay embed, mission pillars, project credits."),
        ("Top Bar", "New Mission", "SetupWizard", "Custom scenario configuration: landing site, crew size (2-6), power type, shielding type."),
        ("Top Bar", "Data Sources", "DataSourcesView dialog", "Comprehensive academic and agency literature citations for all physical simulation values."),
        ("Top Bar", "Data Passport", "DataPassportView dialog", "59-row verified evidence catalog detailing pedigree (Live, Snapshot, Archived, Derived)."),
        ("Top Bar", "Credits & Licenses", "CreditsView dialog", "Open-source dependency licenses, NASA open-data attribution, Team TensorMinds credits."),
        ("Top Bar", "Cadet | Specialist | Commander", "DialSwitch (Reality Dial)", "3-tier cognitive dial toggling presentation from Grade 3.6 visuals to differential rate equations."),
        ("Top Bar", "Time Controls", "TimeControls component", "▶ Run the sol, Paused, 1x, 4x, 16x speed multipliers, +1 hour, +1 sol, Restart.")
    ]

    nav_tbl = doc.add_table(rows=len(nav_table_data), cols=4)
    nav_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r_idx, row in enumerate(nav_table_data):
        for c_idx, val in enumerate(row):
            cell = nav_tbl.cell(r_idx, c_idx)
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
            if r_idx == 0:
                set_cell_background(cell, "0B1224")
                p = cell.paragraphs[0]
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(0)
                r = p.add_run(val)
                r.bold = True
                r.font.name = "Segoe UI"
                r.font.size = Pt(8.5)
                r.font.color.rgb = RGBColor(255, 255, 255)
            else:
                set_cell_background(cell, "F8FAFC" if r_idx % 2 == 1 else "FFFFFF")
                p = cell.paragraphs[0]
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(0)
                r = p.add_run(val)
                r.font.name = "Segoe UI"
                r.font.size = Pt(8.5)
                r.font.color.rgb = C_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # ---------------------------------------------------------
    # SECTION 4: SCENARIOS & CRISES REFERENCE TABLE
    # ---------------------------------------------------------
    h4 = doc.add_heading("4. Implemented Missions & Historical Emergency Replays", level=1)
    h4.runs[0].font.name = "Segoe UI"
    h4.runs[0].font.color.rgb = C_NAVY

    mission_data = [
        ("Mission Name", "Planetary Body & Site", "Duration", "Primary Operational Challenge & Physical Hazard"),
        ("Jezero Outpost", "Mars · Jezero Crater", "30 Sols", "A 2018-scale global dust storm cutting solar array flux by 85% for 60 consecutive hours."),
        ("First Light", "Moon · Connecting Ridge", "31 Days", "Surviving a 354-hour cryogenic lunar night with early Solar Particle Event (SPE) shelter evacuation."),
        ("The Long Night", "Moon · Artemis Basecamp", "89 Days", "Multi-cycle lunar polar night requiring continuous micro-fission reactor load shedding."),
        ("Green Thumb", "Moon · Marius Hills Lava Tubes", "14 Days", "Closed-loop hydroponic greenhouse: balancing elevated crop CO2 against astronaut respiratory health."),
        ("Storm Watch", "Mars · Jezero Crater", "3 Sols", "NASA DONKI-archived May 10, 2024 extreme solar storm with acute surface radiation bombardment."),
        ("Apollo 13 CO2 Crisis", "Historical · LM Aquarius (1970)", "Emergency Replay", "Improvised square-to-round LiOH canister adapter fabrication before cabin CO2 reaches fatal levels."),
        ("Solar Particle Event 1972", "Historical · Apollo Outpost (1972)", "Emergency Replay", "Catastrophic August 1972 solar proton event (>400 mSv): surface evacuation to regolith shelter."),
        ("Mir Station Fire 1997", "Historical · Mir Kvant-1 (1997)", "Emergency Replay", "Solid-fuel Vika oxygen generator combustion: toxic smoke containment and atmospheric scrubbing.")
    ]

    m_tbl = doc.add_table(rows=len(mission_data), cols=4)
    m_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r_idx, row in enumerate(mission_data):
        for c_idx, val in enumerate(row):
            cell = m_tbl.cell(r_idx, c_idx)
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
            if r_idx == 0:
                set_cell_background(cell, "0B1224")
                p = cell.paragraphs[0]
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(0)
                r = p.add_run(val)
                r.bold = True
                r.font.name = "Segoe UI"
                r.font.size = Pt(8.5)
                r.font.color.rgb = RGBColor(255, 255, 255)
            else:
                set_cell_background(cell, "F8FAFC" if r_idx % 2 == 1 else "FFFFFF")
                p = cell.paragraphs[0]
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(0)
                r = p.add_run(val)
                r.font.name = "Segoe UI"
                r.font.size = Pt(8.5)
                r.font.color.rgb = C_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # ---------------------------------------------------------
    # SECTION 5: NASA SCIENCE PEDIGREE & TECHNICAL STACK
    # ---------------------------------------------------------
    h5 = doc.add_heading("5. NASA Open Data Integrations & Software Architecture", level=1)
    h5.runs[0].font.name = "Segoe UI"
    h5.runs[0].font.color.rgb = C_NAVY

    add_callout(doc, "Scientific Credibility & Zero-Fabrication Guarantee",
        "• NASA BVAD-2022 (NASA/TP-20210024855): Crew metabolic rates (0.84 kg O2/CM-d, 1.00 kg CO2/CM-d, 2.5 L H2O/CM-d, 3000 kcal/CM-d).\n"
        "• NASA OCHMO Technical Briefs (TB-003 & TB-047): Cabin partial pressures (ppO2 >= 19.5 kPa) and survival minimums.\n"
        "• Space Weather Database (DONKI): Live solar flare (FLR), CME, and Solar Energetic Particle (SEP) storm feeds.\n"
        "• NASA OSDR & RadLab: Empirical radiation dosimetry from ISS detectors and deep-space space biology research.\n"
        "• JPL Horizons Ephemerides: Live speed-of-light communications latency calculated dynamically for Earth-Mars and Earth-Moon.\n"
        "• NASA Trek GIS: Viking Orbiter MDIM 2.1 color basemap for Mars and LRO WAC mosaic for the Moon.\n"
        "• Azimuth Artemis II Replay: Authentic 3D circumlunar free-return trajectory telemetry embed.",
        bg_color="F0FDF4", border_color="16A34A"
    )

    p_tech = doc.add_paragraph()
    p_tech.paragraph_format.space_before = Pt(8)
    p_tech.paragraph_format.space_after = Pt(4)
    r_tp = p_tech.add_run("Software Architecture & Engineering Verification:\n")
    r_tp.bold = True
    r_tp.font.name = "Segoe UI"
    r_tp.font.size = Pt(10)
    r_tp.font.color.rgb = C_DARK
    
    r_td = p_tech.add_run(
        "• Pure TypeScript Simulation Engine (@outpost-x/sim): Decoupled from the DOM, zero math randomness or global clocks, 100% deterministic.\n"
        "• Frontend Matrix: React 18, Vite 6, Zustand 5, Tailwind CSS, Leaflet, d3-force, Lucide Icons, HTML5 2D Canvas space starfield.\n"
        "• Offline PWA: vite-plugin-pwa precaches all station assets, sound effects, and NASA snapshot data for spotty school Wi-Fi.\n"
        "• Test Verification: 75 automated Vitest test suites, 691 passing unit tests, and 4,050 Monte Carlo seeds verified for game balance."
    )
    r_td.font.name = "Segoe UI"
    r_td.font.size = Pt(9)
    r_td.font.color.rgb = C_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # ---------------------------------------------------------
    # SECTION 6: TEAM & COPYRIGHT
    # ---------------------------------------------------------
    h6 = doc.add_heading("6. Team Credits & Legal Declarations", level=1)
    h6.runs[0].font.name = "Segoe UI"
    h6.runs[0].font.color.rgb = C_NAVY

    team_data = [
        ("Team Member", "Project Role", "Contact & Professional Profile"),
        ("Mourya S", "Team Lead & Lead Developer\nSoftware Architecture, Deterministic Simulation Engine, UI/UX", "Email: mouryas@outlook.in\nLinkedIn: https://www.linkedin.com/in/mouryas"),
        ("Chitra Shree K", "UI/UX Designer & Aerospace Simulation\nDesign System, Pedagogical Framework, Accessibility", "LinkedIn: https://www.linkedin.com/in/chitra-shree-k"),
        ("Monika S", "Data Architect & Systems Engineering\nNASA Data Ingestion, ECLSS Mass Balances, Quality Assurance", "LinkedIn: https://www.linkedin.com/in/monika-s")
    ]

    t_tbl = doc.add_table(rows=len(team_data), cols=3)
    t_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r_idx, row in enumerate(team_data):
        for c_idx, val in enumerate(row):
            cell = t_tbl.cell(r_idx, c_idx)
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
            if r_idx == 0:
                set_cell_background(cell, "0B1224")
                p = cell.paragraphs[0]
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(0)
                r = p.add_run(val)
                r.bold = True
                r.font.name = "Segoe UI"
                r.font.size = Pt(8.5)
                r.font.color.rgb = RGBColor(255, 255, 255)
            else:
                set_cell_background(cell, "F8FAFC" if r_idx % 2 == 1 else "FFFFFF")
                p = cell.paragraphs[0]
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(0)
                r = p.add_run(val)
                r.font.name = "Segoe UI"
                r.font.size = Pt(8.5)
                r.font.color.rgb = C_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    p_copy = doc.add_paragraph()
    p_copy.paragraph_format.space_before = Pt(6)
    p_copy.paragraph_format.space_after = Pt(0)
    r_cp = p_copy.add_run(
        "Copyright © 2026 OUTPOST-X by Team TensorMinds (Mourya S, Chitra Shree K, Monika S). All Rights Reserved.\n"
        "Developed for the 2026 NASA Space Apps Challenge. OUTPOST-X is not affiliated with or endorsed by NASA. "
        "In compliance with challenge regulations, no NASA logos, meatball emblems, or agency insignias are used. "
        "All telemetry data and planetary imagery are derived from NASA open-access public domain APIs."
    )
    r_cp.font.name = "Segoe UI"
    r_cp.font.size = Pt(8)
    r_cp.font.color.rgb = C_MUTED
    r_cp.italic = True

    doc.save(output_path)
    print(f"Document successfully created at: {output_path}")

if __name__ == "__main__":
    out_dir = r"K:\NASA 2026\OUTPOST-X"
    out_file = os.path.join(out_dir, "OUTPOST-X_3-Minute_Demonstration_Script.docx")
    build_document(out_file)
