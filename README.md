# PolyPAR — Poly Plays A Role

> *These tools are built for people who refuse to learn in a straight line.*
> *Role-based, not schedule-based. Learn like a polymath, not like a calendar.*

---

## The Problem With Traditional Study Schedules

Most study advice sounds like this: *study X minutes per day, stick to a schedule, pick one thing and focus.*

That advice works great if you are one thing. If you are a polymath — a person who pursues mastery across multiple disciplines simultaneously — it falls apart fast. A rigid schedule creates guilt when you follow your curiosity. A single focus ignores the fact that your brain makes connections *across* disciplines, not just within them.

PolyPAR is a different approach.

---

## The Idea: Study By Role, Not By Clock

Instead of asking *"what should I study today?"*, PolyPAR asks *"who am I today?"*

You are not a student who studies networking for 45 minutes on Wednesdays. You are a **Network Technician** — and when that role calls to you, you answer it. Maybe that's Monday. Maybe it's four days in a row. The log captures what actually happened, not what was supposed to happen.

This shift — from time-based to identity-based learning — changes how you absorb and retain material. Putting on a role is a mental mode. It focuses you in a way that a timer never can.

---

## The Forms

PolyPAR ships as three printable PDF forms, designed for a standard laser printer.

---

### Study Schedule (`study_schedule.pdf`)

A weekly log with seven blank role rows. Fill in your own disciplines — the form makes no assumptions about who you are or what you are learning.

| Column | Purpose |
|---|---|
| **Role** | The discipline or identity you are studying as |
| **M T W T F S S** | Tick the days you studied this role |
| **Site#** | Code for the platform or website used (see Study Codes) |
| **Book#** | Code for the book used (see Study Codes) |
| **From** | Starting page or section |
| **To** | Ending page or section |
| **Key Topic(s) Learned** | What actually stuck |

The date range at the top (`Week of`) marks the week the sheet covers.

Print a fresh Study Schedule each week.

---

### Experience Log (`experience_log.pdf`)

Formal study — books, courses, tutorials — is only part of learning. Real-world hands-on activity teaches things no book can. Building a PC, sourcing components, configuring a network, debugging a live system, writing a script that solves an actual problem — these are legitimate learning events that deserve to be logged.

The Experience Log captures that. Same seven roles as the Study Schedule, same seven lines per role. The columns are deliberately simpler — no site codes, no book codes, no page numbers. Just what you did and what it taught you.

| Column | Purpose |
|---|---|
| **Role** | The discipline or identity the experience belongs to |
| **M T W T F S S** | Mark the day the experience occurred |
| **Key Topic(s) Learned** | What you did and what it taught you (e.g. "sourced DDR4-3600 RAM for new build — learned NH-D15 clearance constraints, SPD vs XMP profiles, dual vs single channel") |

**Why experience belongs in the log:**

A polymath's education does not stop at the desk. Assembling hardware, configuring servers, debugging real systems, and solving actual problems all develop genuine competence. Logging experience alongside formal study gives an honest picture of how learning actually happens — and builds a record of practical skills that a book log alone would miss.

Print a fresh Experience Log each week alongside the Study Schedule.

---

### Study Codes (`study_codes.pdf`)

A companion reference page. Write each book or platform once, assign it a number, and use that number on the Study Schedule all week. No rewriting *The Linux Command Line* seven times.

| Column | Purpose |
|---|---|
| **Site#** | A number representing a platform (e.g. 1 = TryHackMe, 2 = HackTheBox) |
| **Book#** | A number representing a book (e.g. 1 = The Linux Command Line) |
| **Book or Platform** | The full title or URL |

Print one Study Codes page and reuse it across many weeks.

---

## Design Decisions

**Why only seven lines per role?**

Seven lines is intentional. Once a role's rows are full for the week, the form is telling you to move on. It prevents over-indexing on one discipline at the expense of the others. The form itself becomes the accountability system — a mechanical enforcer of the polymath philosophy.

If you filled all seven lines for Hacker & Sys Admin, go be a Mathematician for a day.

This applies equally to the Experience Log. Seven hands-on activities in one role in one week is already a full week of that role. Move on.

---

## Default Roles

The forms ship with these seven roles:

- PC Technician
- Software Developer
- Hacker & Sys Admin
- Network Technician
- Mathematician
- Artist
- Linguist

These reflect one polymath's learning path. The source is open — modify the roles in `make_pdfs.py` to fit your own disciplines.

---

## Generating the PDFs

The PDFs are included in the repository and ready to print. If you want to modify the roles or layout, regenerate them with:

Requirements: Python 3, ReportLab

```bash
pip install reportlab
python make_pdfs.py
```

Output: `study_schedule.pdf`, `experience_log.pdf`, and `study_codes.pdf`

---

## Part of the Poly Suite

PolyPAR is part of a growing set of tools built around polymath learning:

- **[PolyWAB](https://github.com/devnull0x01/polywab)** — Poly Wants A Book. A terminal-based reading tracker.
- **PolyPAR** — Poly Plays A Role. A printable role-based study log.
