/**
 * OUTPOST-X Team Configuration
 * Update this file to change team member names, roles, and links displayed in the footer.
 */

export interface TeamMember {
  name: string;
  role?: string;
  linkedin?: string;
}

export const TEAM_CONFIG = {
  teamName: "TensorMinds",
  members: [
    { name: "Mourya S", role: "Team Lead & Lead Developer", linkedin: "https://www.linkedin.com/in/mouryas" },
    { name: "Chitra Shree K", role: "UI/UX & Aerospace Simulation", linkedin: "https://www.linkedin.com/in/chitra-shree-k" },
    { name: "Monika S", role: "Data Architect & Systems Engineering", linkedin: "https://www.linkedin.com/in/monika-s" },
  ] as TeamMember[],
  year: 2026,
  projectName: "OUTPOST-X",
  tagline: "Take Command. Build Beyond Earth. Shape Humanity's Next Frontier.",
  nasaAttribution: "Every number in this simulation comes from published NASA research and mission data. OUTPOST-X is not affiliated with or endorsed by NASA.",
  nasaDataUrl: "/about.html",
} as const;
