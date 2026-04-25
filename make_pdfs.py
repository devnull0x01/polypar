from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

ROLES = ["", "", "", "", "", "", ""]
DAYS = ["M", "T", "W", "T", "F", "S", "S"]

def draw_schedule(c, W, H):
    margin = 0.5 * inch
    usable_w = W - 2 * margin

    c.setFont("Helvetica-Bold", 15)
    c.drawString(margin, H - margin, "Study Schedule")

    from_label_x = margin + 3.1 * inch
    c.setFont("Helvetica", 9)
    c.drawString(from_label_x, H - margin, "From")
    c.setLineWidth(0.5)
    c.line(from_label_x + 0.32 * inch, H - margin - 1, from_label_x + 1.1 * inch, H - margin - 1)
    c.drawString(from_label_x + 1.18 * inch, H - margin, "To")
    c.line(from_label_x + 1.45 * inch, H - margin - 1, from_label_x + 2.23 * inch, H - margin - 1)

    c.setFont("Helvetica", 8.5)
    c.drawString(margin, H - margin - 13, "Role-based study log  ·  PolyPAR")

    title_bottom = H - margin - 26
    c.setLineWidth(0.8)
    c.line(margin, title_bottom, W - margin, title_bottom)

    c_role     = 1.45 * inch
    c_day      = 0.22 * inch
    c_days     = c_day * 7
    c_code     = 0.4 * inch
    c_from     = 0.38 * inch
    c_to       = 0.38 * inch
    c_site     = 0.4 * inch
    c_topic    = usable_w - c_role - c_days - c_site - c_code - c_from - c_to

    day_x = [margin + c_role + i * c_day for i in range(7)]

    x0 = margin
    x1 = x0 + c_role
    x2 = x1 + c_days
    x3 = x2 + c_site
    x4 = x3 + c_code
    x5 = x4 + c_from
    x6 = x5 + c_to
    col_x = [x0, x1, x2, x3, x4, x5, x6]

    hdr_h = 0.22 * inch
    hdr_top = title_bottom - 4
    hdr_bottom = hdr_top - hdr_h

    c.setFillGray(0.15)
    c.rect(margin, hdr_bottom, usable_w, hdr_h, fill=1, stroke=0)
    c.setFillGray(1)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(col_x[0] + 4, hdr_bottom + 5, "Role")
    for di, day in enumerate(DAYS):
        dx = day_x[di] + (c_day - c.stringWidth(day, "Helvetica-Bold", 7.5)) / 2
        c.drawString(dx, hdr_bottom + 5, day)
    c.drawString(col_x[2] + 4, hdr_bottom + 5, "Site#")
    c.drawString(col_x[3] + 4, hdr_bottom + 5, "Book#")
    c.drawString(col_x[4] + 4, hdr_bottom + 5, "From")
    c.drawString(col_x[5] + 4, hdr_bottom + 5, "To")
    c.drawString(col_x[6] + 4, hdr_bottom + 5, "Key Topic(s) Learned")
    c.setFillGray(0)

    top_y = hdr_bottom
    available_h = top_y - margin - 0.18 * inch
    row_h = available_h / len(ROLES)

    for i, role in enumerate(ROLES):
        row_top = top_y - i * row_h
        row_bottom = row_top - row_h
        line_spacing = row_h / 7

        if i % 2 == 1:
            c.setFillGray(0.95)
            c.rect(margin, row_bottom, usable_w, row_h, fill=1, stroke=0)
            c.setFillGray(0)

        c.setFont("Helvetica-Bold", 9)
        c.drawString(col_x[0] + 5, row_bottom + row_h / 2 - 3, role)

        c.setLineWidth(0.3)
        c.setStrokeGray(0.55)
        for li in range(1, 7):
            ly = row_top - li * line_spacing
            c.line(col_x[1], ly, W - margin, ly)
        c.setStrokeGray(0)

        c.setLineWidth(0.35)
        c.setStrokeGray(0.5)
        c.rect(margin, row_bottom, usable_w, row_h, fill=0, stroke=1)
        c.setStrokeGray(0)

    c.setLineWidth(0.5)
    c.setStrokeGray(0.4)
    for cx in [col_x[1], col_x[2], col_x[3], col_x[4], col_x[5], col_x[6]]:
        c.line(cx, top_y, cx, margin + 0.18 * inch)
    c.setLineWidth(0.3)
    c.setStrokeGray(0.55)
    for di in range(1, 7):
        c.line(day_x[di], top_y, day_x[di], margin + 0.18 * inch)
    c.setStrokeGray(0)

    c.setFont("Helvetica", 7)
    c.setFillGray(0.4)
    c.drawString(margin, margin - 10, "PolyPAR")
    c.setFillGray(0)


def draw_study_codes(c, W, H):
    margin = 0.5 * inch
    usable_w = W - 2 * margin

    c.setFont("Helvetica-Bold", 15)
    c.drawString(margin, H - margin, "Study Codes")
    c.setFont("Helvetica", 8.5)
    c.drawString(margin, H - margin - 13, "Reference legend  ·  PolyPAR")

    title_bottom = H - margin - 26
    c.setLineWidth(0.8)
    c.line(margin, title_bottom, W - margin, title_bottom)

    c_site  = 0.5 * inch
    c_code  = 0.5 * inch
    col_x   = [margin, margin + c_site, margin + c_site + c_code]

    hdr_h = 0.22 * inch
    hdr_top = title_bottom - 4
    hdr_bottom = hdr_top - hdr_h

    c.setFillGray(0.15)
    c.rect(margin, hdr_bottom, usable_w, hdr_h, fill=1, stroke=0)
    c.setFillGray(1)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(col_x[0] + 4, hdr_bottom + 5, "Site#")
    c.drawString(col_x[1] + 4, hdr_bottom + 5, "Book#")
    c.drawString(col_x[2] + 4, hdr_bottom + 5, "Book or Platform")
    c.setFillGray(0)

    top_y = hdr_bottom
    available_h = top_y - margin - 0.18 * inch
    line_h = 0.3 * inch
    num_lines = int(available_h / line_h)

    for i in range(num_lines):
        ly = top_y - (i + 1) * line_h
        if i % 2 == 1:
            c.setFillGray(0.95)
            c.rect(margin, ly, usable_w, line_h, fill=1, stroke=0)
            c.setFillGray(0)
        c.setLineWidth(0.35)
        c.setStrokeGray(0.5)
        c.rect(margin, ly, usable_w, line_h, fill=0, stroke=1)
        c.setStrokeGray(0)

    c.setLineWidth(0.5)
    c.setStrokeGray(0.4)
    c.line(col_x[1], top_y, col_x[1], top_y - num_lines * line_h)
    c.line(col_x[2], top_y, col_x[2], top_y - num_lines * line_h)
    c.setStrokeGray(0)

    c.setFont("Helvetica", 7)
    c.setFillGray(0.4)
    c.drawString(margin, margin - 10, "PolyPAR")
    c.setFillGray(0)


def draw_page_stops(c, W, H):
    margin = 0.5 * inch
    usable_w = W - 2 * margin

    c.setFont("Helvetica-Bold", 15)
    c.drawString(margin, H - margin, "Page Stops")
    c.setFont("Helvetica", 8.5)
    c.drawString(margin, H - margin - 13, "Bookmark reference  ·  PolyPAR")

    title_bottom = H - margin - 26
    c.setLineWidth(0.8)
    c.line(margin, title_bottom, W - margin, title_bottom)

    c_book  = 0.6 * inch
    c_stops = usable_w - c_book
    col_x   = [margin, margin + c_book]

    hdr_h = 0.22 * inch
    hdr_top = title_bottom - 4
    hdr_bottom = hdr_top - hdr_h

    c.setFillGray(0.15)
    c.rect(margin, hdr_bottom, usable_w, hdr_h, fill=1, stroke=0)
    c.setFillGray(1)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(col_x[0] + 4, hdr_bottom + 5, "Book#")
    c.drawString(col_x[1] + 4, hdr_bottom + 5, "Page Stops")
    c.setFillGray(0)

    top_y = hdr_bottom
    available_h = top_y - margin - 0.18 * inch
    num_books = 30
    row_h = available_h / num_books
    stops_per_row = 16
    stop_w = c_stops / stops_per_row

    for i in range(num_books):
        row_top = top_y - i * row_h
        row_bottom = row_top - row_h

        if i % 2 == 1:
            c.setFillGray(0.95)
            c.rect(margin, row_bottom, usable_w, row_h, fill=1, stroke=0)
            c.setFillGray(0)

        c.setLineWidth(0.35)
        c.setStrokeGray(0.5)
        c.rect(margin, row_bottom, usable_w, row_h, fill=0, stroke=1)
        c.setStrokeGray(0)

        c.setLineWidth(0.3)
        c.setStrokeGray(0.55)
        for si in range(1, stops_per_row):
            sx = col_x[1] + si * stop_w
            c.line(sx, row_top, sx, row_bottom)
        c.setStrokeGray(0)

    c.setLineWidth(0.5)
    c.setStrokeGray(0.4)
    c.line(col_x[1], top_y, col_x[1], top_y - num_books * row_h)
    c.setStrokeGray(0)

    c.setFont("Helvetica", 7)
    c.setFillGray(0.4)
    c.drawString(margin, margin - 10, "PolyPAR")
    c.setFillGray(0)


W, H = letter

c1 = canvas.Canvas("/mnt/user-data/outputs/study_schedule.pdf", pagesize=letter)
draw_schedule(c1, W, H)
c1.save()

c2 = canvas.Canvas("/mnt/user-data/outputs/study_codes.pdf", pagesize=letter)
draw_study_codes(c2, W, H)
c2.save()

c3 = canvas.Canvas("/mnt/user-data/outputs/page_stops.pdf", pagesize=letter)
draw_page_stops(c3, W, H)
c3.save()

print("Done.")
