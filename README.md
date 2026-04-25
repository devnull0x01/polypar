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

PolyPAR ships as four printable PDF forms, designed for a standard laser printer. Download them directly from this repository — no setup required.

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

The date range at the top (`From / To`) marks the week the sheet covers. Print a fresh Study Schedule each week.

---

### Experience Schedule (`experience_schedule.pdf`)

Formal study — books, courses, tutorials — is only part of learning. Real-world hands-on activity teaches things no book can. Building a PC, configuring a network, debugging a live system, writing a script that solves an actual problem — these are legitimate learning events that deserve to be logged.

The Experience Schedule captures that. Same seven roles, same seven lines per role. The columns are deliberately simpler — no site codes, no book codes, no page numbers. Just what you did and what it taught you.

| Column | Purpose |
|---|---|
| **Role** | The discipline or identity the experience belongs to |
| **M T W T F S S** | Tick the day the experience occurred |
| **Experience / Activity** | What you did and what it taught you — written as one natural entry |

Print a fresh Experience Schedule each week alongside the Study Schedule.

---

### Study Codes (`study_codes.pdf`)

A companion reference page. Write each book or platform once, assign it a number, and use that number on the schedule all week. No rewriting a long title seven times.

| Column | Purpose |
|---|---|
| **Site#** | A number representing a platform (e.g. S1 = TryHackMe, S2 = HackTheBox) |
| **Book#** | A number representing a book (e.g. B1 = The Linux Command Line) |
| **Book or Platform** | The full title or URL |

Print one Study Codes page and reuse it across many weeks.

---

### Page Stops (`page_stops.pdf`)

A dedicated bookmark reference. No dog-earing required. Each row holds a Book# on the left and 16 cells for recording page stops as you move through a book over time. If a row fills up, simply start a new entry below.

| Column | Purpose |
|---|---|
| **Book#** | The code assigned to the book in Study Codes |
| **Page Stops** | 16 cells to record your stopping page each session |

Print one Page Stops page and reuse it across many weeks.

---

## Modifying the Forms

Want to change the layout, column widths, or number of rows? The forms are generated with Python and ReportLab.

Requirements: Python 3, ReportLab

```bash
pip install reportlab
python make_pdfs.py
```

---

## FAQ

**What sorts of codes should I use?**

The coding system is entirely up to you. Some examples to get started:

- `B1`, `B2`, `B3` — books
- `S1`, `S2`, `S3` — websites and online platforms
- `YT1`, `YT2` — YouTube channels

**Why only seven lines per role?**

Seven lines is intentional. Once a role's rows are full for the week, the form is telling you to move on. It prevents over-indexing on one discipline at the expense of the others. The form itself becomes the accountability system — a mechanical enforcer of the polymath philosophy.

If you filled all seven lines for Hacker, go be a Mathematician for a day.

---

## Part of the Poly Suite

PolyPAR is part of a growing set of tools built around polymath learning:

- **[PolyWAB](https://github.com/devnull0x01/polywab)** — Poly Wants A Book. A terminal-based reading tracker.
- **PolyPAR** — Poly Plays A Role. A printable role-based study log.

---

*PolyPAR*
