#!/usr/bin/env python3
"""Render the 26 November 2026 world-news front page as entry.png (1024x1024).

Fresh code written for the news-image-20261126 bounty. All illustrations are
simple geometric drawings made with Pillow; no photographs or copied artwork.
All story text is paraphrased from the cited news sources (see SOURCES.md).
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 229)
INK = (20, 20, 20)
RED = (164, 31, 31)
BLUE = (31, 58, 95)
GREY = (90, 86, 76)
LIGHT = (232, 225, 208)
GOLD = (176, 132, 40)

FD = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FD, name), size)


F_TITLE = font("DejaVuSerif-Bold.ttf", 58)
F_DATE = font("DejaVuSerif-Bold.ttf", 27)
F_SUB = font("DejaVuSans.ttf", 13)
F_SEC = font("DejaVuSerif-Bold.ttf", 15)
F_BIG_H = font("DejaVuSerif-Bold.ttf", 17)
F_BIG_B = font("DejaVuSans.ttf", 12)
F_MED_H = font("DejaVuSerif-Bold.ttf", 14)
F_MED_B = font("DejaVuSans.ttf", 11)
F_ONE = font("DejaVuSans.ttf", 10)
F_SRC = font("DejaVuSans-Bold.ttf", 9)
F_UTC = font("DejaVuSans-Bold.ttf", 11)
F_BOX = font("DejaVuSans.ttf", 11)
F_FOOT = font("DejaVuSans.ttf", 10)


def wrap(draw, text, fnt, width):
    """Greedy word wrap returning a list of lines fitting width."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, width, leading, color=INK):
    """Draw wrapped paragraph, return y after last line."""
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def rule(draw, x, y, w, color=INK, h=2):
    draw.rectangle([x, y, x + w, y + h], fill=color)


def source_tag(draw, x, y, src):
    draw.text((x, y), "— " + src, font=F_SRC, fill=GREY)


# ---------------------------------------------------------------- illustrations
def draw_tariffs(d, x, y, w, h):
    """Rising bar chart with a tariff arrow."""
    d.rectangle([x, y, x + w, y + h], outline=BLUE, width=2, fill=(226, 232, 240))
    base = y + h - 18
    bars = [0.25, 0.45, 0.35, 0.62, 0.85]
    bw = (w - 24) // len(bars)
    for i, v in enumerate(bars):
        bx = x + 12 + i * bw
        bh = int((h - 34) * v)
        d.rectangle([bx, base - bh, bx + bw - 6, base], fill=RED if i == 4 else BLUE)
    d.line([(x + 10, base - 6), (x + w - 12, y + 16)], fill=GOLD, width=4)
    d.polygon([(x + w - 12, y + 16), (x + w - 26, y + 14), (x + w - 16, y + 30)],
              fill=GOLD)
    d.text((x + 12, y + 4), "% TARIFF", font=F_SRC, fill=BLUE)


def draw_missile(d, x, y, w, h):
    """Missile arc over a globe."""
    d.rectangle([x, y, x + w, y + h], outline=BLUE, width=2, fill=(226, 232, 240))
    d.ellipse([x + 18, y + h - 52, x + 78, y + h + 8], fill=(120, 160, 110),
              outline=BLUE, width=2)
    d.arc([x + 18, y + h - 52, x + 78, y + h + 8], 200, 340, fill=INK, width=2)
    d.polygon([(x + 62, y + 18), (x + 74, y + 44), (x + 58, y + 40)], fill=RED)
    d.rectangle([x + 58, y + 40, x + 66, y + 62], fill=INK)
    d.polygon([(x + 54, y + 62), (x + 70, y + 62), (x + 62, y + 78)], fill=GOLD)
    d.arc([x + 70, y + 8, x + w - 8, y + 66], 300, 90, fill=GREY, width=2)


def draw_dow(d, x, y, w, h):
    """Stock line smashing through the 50,000 line."""
    d.rectangle([x, y, x + w, y + h], outline=BLUE, width=2, fill=(226, 232, 240))
    mid = y + 34
    d.line([(x + 8, mid), (x + w - 8, mid)], fill=RED, width=2)
    d.text((x + 10, y + 6), "50,000", font=F_SRC, fill=RED)
    pts = [(x + 10, y + h - 22), (x + 30, y + h - 34), (x + 52, y + h - 28),
           (x + 74, y + h - 46), (x + 96, y + h - 40), (x + 116, y + 18)]
    d.line(pts, fill=BLUE, width=3, joint="curve")
    d.ellipse([pts[-1][0] - 4, pts[-1][1] - 4, pts[-1][0] + 4, pts[-1][1] + 4],
              fill=GOLD, outline=INK)


def draw_jet(d, x, y, w, h):
    """Jet silhouette with a starburst hit."""
    d.rectangle([x, y, x + w, y + h], outline=BLUE, width=2, fill=(226, 232, 240))
    d.polygon([(x + 14, y + h // 2 + 6), (x + 88, y + h // 2 - 14),
               (x + 108, y + h // 2 - 10), (x + 88, y + h // 2 + 2),
               (x + 96, y + h // 2 + 16), (x + 70, y + h // 2 + 12),
               (x + 30, y + h // 2 + 14)], fill=INK)
    d.polygon([(x + 56, y + h // 2 - 8), (x + 66, y + h // 2 - 30),
               (x + 76, y + h // 2 - 8)], fill=INK)
    cx, cy = x + w - 26, y + 24
    for ang in range(0, 360, 30):
        import math
        r1, r2 = 16, 7
        a = math.radians(ang)
        a2 = math.radians(ang + 15)
        d.polygon([(cx, cy),
                   (cx + r1 * math.cos(a), cy + r1 * math.sin(a)),
                   (cx + r2 * math.cos(a2), cy + r2 * math.sin(a2))], fill=GOLD)
    d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=RED)

# ---------------------------------------------------------------- story data
BIG = [
    ("TARIFF SHOCK", "US unveils tariffs on 14 partners",
     "Washington proposes fresh duties on 14 major trading partners to fight "
     "what it calls excess industrial capacity, with the steepest rates aimed "
     "at China.",
     "BBC / Reuters", draw_tariffs),
    ("NUCLEAR SIGNAL", "Kim orders wider nuclear push",
     "North Korea's leader says the country must deploy tactical nuclear "
     "weapons more widely, state media KCNA reports.",
     "KCNA via Reuters", draw_missile),
    ("MARKET MILESTONE", "Dow tops 50,000 for the first time",
     "The Dow crosses 50,000 for the first time even as Nvidia-led tech "
     "shares slide, with S&P putting the chipmaker's rating on watch after "
     "boardroom turmoil.",
     "Reuters / BBC", draw_dow),
    ("WAR IN UKRAINE", "Ukraine hits air base, five jets hit",
     "Kyiv says its forces struck a major Russian air base and damaged five "
     "military planes, as Russian missiles hit the capital late on Wednesday.",
     "Reuters / BBC", draw_jet),
]

MEDIUM = [
    ("Israeli judges urge dropping top charges against Netanyahu",
     "A panel of judges recommends removing the most serious bribery charges "
     "in the prime minister's long-running corruption trial.", "BBC"),
    ("Israeli strike kills senior Hamas official and family",
     "An airstrike kills a senior Hamas security official and members of his "
     "family, medics and officials say.", "BBC"),
    ("Sudan drone strikes kill 19 civilians in Blue Nile",
     "Drone attacks in Sudan's Blue Nile state kill 19 civilians, in the "
     "latest violence of the country's war.", "Reuters"),
    ("Asia shares bounce as Wall Street steadies",
     "Japan's Nikkei gains 1.6% and South Korea's index rises 1.9% in a "
     "holiday-thinned session, though tariff and AI worries linger.", "Reuters"),
    ("S&P puts Nvidia rating on downgrade watch",
     "The ratings agency cites weak board oversight after the chipmaker's "
     "chief executive left and then returned within days.", "Reuters"),
    ("US approves SpaceX plan for a million satellites",
     "Regulators clear SpaceX to send up to a million data satellites, a "
     "vast expansion of its orbital constellation.", "BBC"),
    ("Australia passes tough online safety law",
     "Internet platforms must proactively remove harmful content or face "
     "fines of up to 5% of their revenue under the new law.", "Reuters"),
    ("Bangladesh lifts garment minimum wage 36%",
     "The government raises pay for garment workers after a wave of strikes "
     "in the world's big clothing-export sector.", "Reuters"),
    ("Duran Duran guitarist Andy Taylor dies at 65",
     "The guitarist and songwriter, a founding member of the 1980s pop "
     "giants, dies aged 65, the band announces.", "BBC"),
    ("31 killed as fuel tanker fire engulfs Cairo highway",
     "A tanker crash sparks a huge fire on a Cairo highway, killing 31 "
     "people, officials say.", "BBC"),
    ("Brent holds above $94 after Houthi refinery claim",
     "Oil stays firm after Yemen's Houthis say they attacked Saudi Arabia's "
     "largest refinery, raising supply fears.", "Reuters"),
    ("US famine monitor to halt reporting as funds run out",
     "More than half the field staff at the US famine monitor will lose "
     "their jobs by year's end, sources tell Reuters.", "Reuters"),
]

ONE_LINERS = [
    ("Lebanon to open a second airport next month", "Reuters"),
    ("States urge Russia to halt alleged riot-agent use", "Reuters"),
    ("Murmansk governor held in graft case", "Reuters"),
    ("Ecuador: US talks focus on reviewing operations", "Reuters"),
    ("Kenyan cult leader convicted of new charges", "Reuters"),
    ("Second judge blocks birthright order", "Reuters"),
    ("US Q3 GDP revised sharply up to 4.3%", "Reuters"),
    ("Fed Beige Book: modest growth, price pressure", "Reuters"),
    ("California warns of flooding at Thanksgiving", "BBC"),
    ("Macy's postpones Thanksgiving parade", "BBC"),
    ("Trump pardons turkeys Freedom and Feathers", "Reuters"),
    ("North Korea expels Swiss diplomat in sanctions row", "BBC"),
    ("Five Mexicans held in Nigeria over $227m meth lab", "BBC"),
    ("Jolie and Pitt settle winery legal battle", "BBC"),
    ("Rodgers released; may have played last game", "BBC"),
    ("NASA: asteroid crater is stadium-sized", "BBC"),
    ("UK to publish new EU treaties; 10-year exit clause", "BBC"),
    ("Poundland collapses; 11,000 jobs at risk", "BBC"),
    ("Norway court voids disputed oil licences", "C54"),
    ("Ghana unveils Heritage Series banknotes", "C54"),
    ("Kenya's last Ebola patient discharged", "C54"),
    ("UCL: Real Madrid 5-1 PSV; Liverpool 3-0", "BBC"),
    ("Sooryavanshi smashes 204 off 53 balls", "Sports"),
    ("Sri Lanka women win Emerging Nations Trophy", "Sports"),
]

UTC_STRIP = [
    ("00:29", "Dow crosses 50,000"),
    ("01:34", "Asia shares bounce"),
    ("02:55", "UK to publish EU treaties"),
    ("05:25", "Reuters world summary"),
]

DATE_CHECK = [
    "Hong Kong tower-block fire, 168 dead (25 Nov) — still burning in reports, not today's news",
    "US midterms: Democrats reclaim Congress (early Nov) — decided weeks ago",
    "Solomon Islands signs Australia security treaty (25 Nov)",
    "Colombia supermarket hostage siege ends (25 Nov)",
    "Six die in plane crash off Mississippi coast (25 Nov)",
]

# ---------------------------------------------------------------- layout
def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 28  # margin
    CW = W - 2 * M

    # ---- masthead
    y = 10
    d.text((M, y), "THE WORLD TODAY", font=F_TITLE, fill=INK)
    tw = d.textlength("THE WORLD TODAY", font=F_TITLE)
    d.text((M + tw + 16, y + 30), "ONE DAY · EVERY TIME ZONE",
           font=F_SRC, fill=RED)
    y += 66
    rule(d, M, y, CW, RED, 4)
    y += 6
    d.text((M, y), "THURSDAY · 26 NOVEMBER 2026", font=F_DATE, fill=INK)
    d.text((M, y + 34), "40 stories first reported today — politics, markets, "
           "war, science, sport and culture, checked against their sources.",
           font=F_SUB, fill=GREY)
    y += 54
    rule(d, M, y, CW, INK, 2)
    y += 8

    # ---- UTC strip
    d.rectangle([M, y, M + CW, y + 30], fill=BLUE)
    d.text((M + 10, y + 8), "THE DAY IN UTC", font=F_UTC, fill=(255, 255, 255))
    x = M + 150
    for t, label in UTC_STRIP:
        d.text((x, y + 8), t + "  " + label, font=F_UTC, fill=(220, 228, 240))
        x += d.textlength(t + "  " + label, font=F_UTC) + 26
    y += 38

    # ---- big four: 2 x 2 grid
    cell_w = (CW - 16) // 2
    cell_h = 104
    for i, (kicker, head, body, src, draw_fn) in enumerate(BIG):
        cx = M + (i % 2) * (cell_w + 16)
        cy = y + (i // 2) * (cell_h + 8)
        draw_fn(d, cx, cy + 12, 128, 88)
        tx = cx + 140
        d.text((tx, cy), kicker, font=F_SRC, fill=RED)
        ny = para(d, tx, cy + 14, head, F_BIG_H, cell_w - 140, 20)
        ny = para(d, tx, ny + 2, body, F_BIG_B, cell_w - 140, 15)
        source_tag(d, tx, cy + cell_h - 16, src)
    y += 2 * cell_h + 8 + 10

    # ---- section header: medium stories
    d.text((M, y), "THE DAY IN BRIEF", font=F_SEC, fill=BLUE)
    rule(d, M, y + 20, CW, BLUE, 2)
    y += 26

    # ---- medium 12: two columns of six
    col_w = (CW - 16) // 2
    row_h = 42
    for i, (head, body, src) in enumerate(MEDIUM):
        col = i // 6
        row = i % 6
        cx = M + col * (col_w + 16)
        cy = y + row * row_h
        d.text((cx, cy), "▸ " + head, font=F_MED_H, fill=INK)
        para(d, cx + 16, cy + 17, body + " — " + src, F_MED_B, col_w - 16, 12)
    y += 6 * row_h + 4

    # ---- one-liners 24: three columns of eight
    d.text((M, y), "ALSO TODAY — IN ONE LINE", font=F_SEC, fill=BLUE)
    rule(d, M, y + 20, CW, BLUE, 2)
    y += 26
    col_w3 = (CW - 32) // 3
    for i, (line, src) in enumerate(ONE_LINERS):
        col = i // 8
        row = i % 8
        cx = M + col * (col_w3 + 16)
        cy = y + row * 23
        sw = d.textlength(" " + src, font=F_SRC)
        avail = col_w3 - sw - 16
        text = "• " + line
        while d.textlength(text, font=F_ONE) > avail and len(text) > 4:
            text = text[:-2] + "…"
        d.text((cx, cy), text, font=F_ONE, fill=INK)
        d.text((cx + col_w3 - sw, cy + 1), src, font=F_SRC, fill=GREY)
    y += 8 * 23 + 6

    # ---- date check box
    d.rectangle([M, y, M + CW, y + 54], outline=RED, width=2, fill=LIGHT)
    d.text((M + 10, y + 6), "DATE CHECK — reported BEFORE 26 November, "
           "deliberately left out:", font=F_SRC, fill=RED)
    items = "  ·  ".join(DATE_CHECK)
    para(d, M + 10, y + 22, items, F_BOX, CW - 20, 13, color=(60, 55, 45))
    y += 62

    # ---- footer
    rule(d, M, y, CW, INK, 2)
    d.text((M, y + 6), "Sources: Reuters, BBC, KCNA, C54, sports wires. "
           "Every story above was first reported on 26 November 2026 in some "
           "time zone; older stories are listed in DATE CHECK, not as today's news.",
           font=F_FOOT, fill=GREY)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG", optimize=True)
    print("saved", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
