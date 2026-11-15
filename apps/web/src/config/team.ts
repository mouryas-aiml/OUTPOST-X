/**
 * OUTPOST-X Team Configuration
 * Update this file to change team member names, roles, and links displayed in the footer.
 */

export interface TeamMember {
  name: string;
  role?: string;
}

export const TEAM_CONFIG = {
  teamName: "Team XYZ",
  members: [
    { name: "Team Member 1", role: "Lead Developer" },
    { name: "Team Member 2", role: "UI/UX Designer" },
    { name: "Team Member 3", role: "Simulation Engineer" },
    { name: "Team Member 4", role: "Data & Science" },
    { name: "Team Member 5", role: "Full-Stack Developer" },
  ] as TeamMember[],
  year: 2026,
  projectName: "OUTPOST-X",
  tagline: "Take Command. Build Beyond Earth. Shape Humanity's Next Frontier.",
  nasaAttribution: "Every number in this simulation comes from published NASA research and mission data. OUTPOST-X is not affiliated with or endorsed by NASA.",
  nasaDataUrl: "/about.html",
} as const;
