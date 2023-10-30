from __future__ import annotations

from typing import Iterable

from gradio.themes.soft import Soft
from gradio.themes import Color, Size
from gradio.themes.utils import colors, sizes, fonts

h2o_yellow = Color(
    name="yellow",
    c50="#fffef2",
    c100="#fff9e6",
    c200="#ffecb3",
    c300="#ffe28c",
    c400="#ffd659",
    c500="#fec925",
    c600="#e6ac00",
    c700="#bf8f00",
    c800="#a67c00",
    c900="#664d00",
    c950="#403000",
)
h2o_gray = Color(
    name="gray",
    c50="#f8f8f8",
    c100="#e5e5e5",
    c200="#cccccc",
    c300="#b2b2b2",
    c400="#999999",
    c500="#7f7f7f",
    c600="#666666",
    c700="#4c4c4c",
    c800="#333333",
    c900="#191919",
    c950="#0d0d0d",
)

text_xsm = Size(
    name="text_xsm",
    xxs="4px",
    xs="5px",
    sm="6px",
    md="7px",
    lg="8px",
    xl="10px",
    xxl="12px",
)

spacing_xsm = Size(
    name="spacing_xsm",
    xxs="1px",
    xs="1px",
    sm="1px",
    md="2px",
    lg="3px",
    xl="5px",
    xxl="7px",
)

radius_xsm = Size(
    name="radius_xsm",
    xxs="1px",
    xs="1px",
    sm="1px",
    md="2px",
    lg="3px",
    xl="5px",
    xxl="7px",
)


class H2oTheme(Soft):
    def __init__(
            self,
            *,
            primary_hue: colors.Color | str = h2o_yellow,
            secondary_hue: colors.Color | str = h2o_yellow,
            neutral_hue: colors.Color | str = h2o_gray,
            spacing_size: sizes.Size | str = sizes.spacing_md,
            radius_size: sizes.Size | str = sizes.radius_md,
            text_size: sizes.Size | str = sizes.text_lg,
            font: fonts.Font
                  | str
                  | Iterable[fonts.Font | str] = (
                    fonts.GoogleFont("Montserrat"),
                    "ui-sans-serif",
                    "system-ui",
                    "sans-serif",
            ),
            font_mono: fonts.Font
                       | str
                       | Iterable[fonts.Font | str] = (
                    fonts.GoogleFont("IBM Plex Mono"),
                    "ui-monospace",
                    "Consolas",
                    "monospace",
            ),
    ):
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
            font=font,
            font_mono=font_mono,
        )
        super().set(
            background_fill_primary_dark="*block_background_fill",
            block_background_fill_dark="*neutral_950",
            block_border_width='1px',
            block_border_width_dark='1px',
            block_label_background_fill="*primary_300",
            block_label_background_fill_dark="*primary_600",
            block_label_text_color="*neutral_950",
            block_label_text_color_dark="*neutral_950",
            block_radius="0 0 8px 8px",
            block_title_text_color="*neutral_950",
            block_title_text_color_dark="*neutral_950",
            body_background_fill="*neutral_50",
            body_background_fill_dark="*neutral_900",
            border_color_primary="*neutral_100",
            border_color_primary_dark="*neutral_700",
            button_border_width="1px",
            button_border_width_dark="1px",
            button_primary_text_color="*neutral_950",
            button_primary_text_color_dark="*neutral_950",
            button_primary_background_fill="*primary_500",
            button_primary_background_fill_dark="*primary_500",
            button_secondary_background_fill_hover_dark="*primary_700",
            button_secondary_border_color="*primary_500",
            button_secondary_border_color_dark="*primary_500",
            button_secondary_border_color_hover_dark="*primary_700",
            checkbox_label_text_color_selected_dark='#000000',
            # checkbox_label_text_size="*text_xs",  # too small for iPhone etc. but good if full large screen zoomed to fit
            checkbox_label_text_size="*text_sm",
            # radio_circle="""url("data:image/svg+xml,%3csvg viewBox='0 0 32 32' fill='white' xmlns='http://www.w3.org/2000/svg'%3e%3ccircle cx='32' cy='32' r='1'/%3e%3c/svg%3e")""",
            # checkbox_border_width=1,
            # heckbox_border_width_dark=1,
            link_text_color="#3344DD",
            link_text_color_hover="#3344DD",
            link_text_color_visited="#3344DD",
            link_text_color_dark="#74abff",
            link_text_color_hover_dark="#a3c8ff",
            link_text_color_active_dark="#a3c8ff",
            link_text_color_visited_dark="#74abff",
        )


class SoftTheme(Soft):
    def __init__(
            self,
            *,
            primary_hue: colors.Color | str = colors.indigo,
            secondary_hue: colors.Color | str = colors.indigo,
            neutral_hue: colors.Color | str = colors.gray,
            spacing_size: sizes.Size | str = sizes.spacing_md,
            radius_size: sizes.Size | str = sizes.radius_md,
            text_size: sizes.Size | str = sizes.text_md,
            font: fonts.Font
                  | str
                  | Iterable[fonts.Font | str] = (
                    fonts.GoogleFont("Montserrat"),
                    "ui-sans-serif",
                    "system-ui",
                    "sans-serif",
            ),
            font_mono: fonts.Font
                       | str
                       | Iterable[fonts.Font | str] = (
                    fonts.GoogleFont("IBM Plex Mono"),
                    "ui-monospace",
                    "Consolas",
                    "monospace",
            ),
    ):
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
            font=font,
            font_mono=font_mono,
        )
        super().set(
            checkbox_label_text_size="*text_sm",
        )


h2o_logo = '<svg id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"' \
           ' viewBox="0 0 600.28 600.28"><defs><style>.cls-1{fill:#fec925;}.cls-2{fill:#161616;}.cls-3{fill:' \
           '#54585a;}</style></defs><g id="Fill-1"><rect class="cls-1" width="600.28" height="600.28" ' \
           'rx="23.24"/></g><path class="cls-2" d="M174.33,246.06v92.78H152.86v-38H110.71v38H89.24V246.06h21.' \
           '47v36.58h42.15V246.06Z"/><path class="cls-2" d="M259.81,321.34v17.5H189.7V324.92l35.78-33.8c8.22-7.' \
           '82,9.68-12.59,9.68-17.09,0-7.29-5-11.53-14.85-11.53-7.95,0-14.71,3-19.21,9.27L185.46,261.7c7.15-10' \
           '.47,20.14-17.23,36.84-17.23,20.68,0,34.46,10.6,34.46,27.44,0,9-2.52,17.22-15.51,29.29l-21.33,20.14Z"' \
           '/><path class="cls-2" d="M268.69,292.45c0-27.57,21.47-48,50.76-48s50.76,20.28,50.76,48-21.6,48-50.' \
           '76,48S268.69,320,268.69,292.45Zm79.78,0c0-17.63-12.46-29.69-29-29.69s-29,12.06-29,29.69,12.46,29.69' \
           ',29,29.69S348.47,310.08,348.47,292.45Z"/><path class="cls-3" d="M377.23,326.91c0-7.69,5.7-12.73,12.' \
           '85-12.73s12.86,5,12.86,12.73a12.86,12.86,0,1,1-25.71,0Z"/><path class="cls-3" d="M481.4,298.15v40.' \
           '69H462.05V330c-3.84,6.49-11.27,9.94-21.74,9.94-16.7,0-26.64-9.28-26.64-21.61,0-12.59,8.88-21.34,30.' \
           '62-21.34h16.43c0-8.87-5.3-14-16.43-14-7.55,0-15.37,2.51-20.54,6.62l-7.43-14.44c7.82-5.57,19.35-8.' \
           '62,30.75-8.62C468.81,266.47,481.4,276.54,481.4,298.15Zm-20.68,18.16V309H446.54c-9.67,0-12.72,3.57-' \
           '12.72,8.35,0,5.16,4.37,8.61,11.66,8.61C452.37,326,458.34,322.8,460.72,316.31Z"/><path class="cls-3"' \
           ' d="M497.56,246.06c0-6.49,5.17-11.53,12.86-11.53s12.86,4.77,12.86,11.13c0,6.89-5.17,11.93-12.86,' \
           '11.93S497.56,252.55,497.56,246.06Zm2.52,21.47h20.68v71.31H500.08Z"/></svg>'

stratgy_logo = '<svg version="1.0" xmlns="http://www.w3.org/2000/svg"'\
    'width="240" height="120" viewBox="0 0 264.000000 113.000000"'\
    'preserveAspectRatio="xMidYMid meet">'\
    '<g transform="translate(0.000000,113.000000) scale(0.100000,-0.100000)"'\
    'fill="#000000" stroke="none">'\
    '<path d="M2239 891 c-31 -32 -35 -59 -16 -105 12 -28 11 -32 -17 -57 -26 -23'\
    '-31 -34 -30 -70 3 -80 87 -124 163 -84 26 13 30 13 41 0 7 -9 29 -15 52 -15'\
    'l40 0 -27 36 -28 37 22 16 c18 14 22 25 19 56 l-3 39 -36 -32 -37 -32 -26 31'\
    '-26 31 30 30 c17 17 30 40 30 54 0 86 -91 125 -151 65z m79 -44 c9 -10 7 -19'\
    '-4 -35 -18 -26 -34 -20 -34 12 0 36 18 47 38 23z m-1 -212 c-6 -18 -50 -18'\
    '-64 1 -17 24 -16 39 3 59 15 15 18 13 40 -17 13 -18 23 -37 21 -43z"/>'\
    '<path d="M559 848 c-6 -13 -23 -33 -37 -46 -25 -21 -26 -24 -9 -36 13 -10 17'\
    '-28 17 -87 0 -91 15 -119 65 -119 45 0 85 16 85 35 0 10 -10 15 -30 15 l-30 0'\
    '0 75 0 75 30 0 c23 0 30 4 30 20 0 16 -7 20 -36 20 -32 0 -36 3 -31 21 13 48'\
    '-32 70 -54 27z"/>'\
    '<path d="M1251 841 c-7 -15 -23 -33 -37 -39 -29 -14 -31 -28 -4 -37 18 -6 20'\
    '-15 20 -94 0 -54 4 -91 12 -99 26 -26 138 -8 138 22 0 9 -6 13 -14 10 -8 -3'\
    '-24 -1 -35 6 -18 9 -21 20 -21 80 l0 70 35 0 c28 0 35 4 35 20 0 16 -7 20 -35'\
    '20 -33 0 -35 2 -35 35 0 30 -3 35 -24 35 -17 0 -27 -8 -35 -29z"/>'\
    '<path d="M360 810 c-51 -9 -77 -26 -84 -55 -9 -37 5 -56 71 -91 60 -32 70 -49'\
    '41 -68 -25 -15 -72 4 -76 32 -2 14 -10 22 -23 22 -15 0 -19 -7 -19 -39 0 -45'\
    '11 -51 97 -51 62 0 96 14 113 45 23 44 5 74 -60 103 -60 27 -79 55 -45 68 27'\
    '11 65 -5 65 -26 0 -13 7 -20 20 -20 16 0 20 7 20 35 0 30 -4 35 -27 40 -50 11'\
    '-58 11 -93 5z"/>'\
    '<path d="M748 802 c-45 -15 -66 -42 -33 -42 12 0 15 -16 15 -85 0 -69 -3 -85'\
    '-15 -85 -8 0 -15 -7 -15 -15 0 -12 16 -15 80 -15 64 0 80 3 80 15 0 8 -9 15'\
    '-20 15 -18 0 -20 7 -20 75 0 81 10 93 45 55 32 -35 53 -15 54 53 1 33 -2 37'\
    '-23 37 -14 0 -39 -12 -56 -26 l-31 -27 3 28 c4 35 -5 37 -64 17z"/>'\
    '<path d="M982 795 c-60 -26 -52 -65 16 -65 28 0 32 3 32 25 0 27 26 35 48 13'\
    '27 -27 14 -46 -42 -58 -72 -15 -106 -42 -106 -84 0 -60 52 -82 125 -52 29 12'\
    '34 12 39 0 8 -20 116 -20 116 0 0 7 -9 16 -20 19 -18 5 -20 14 -20 90 0 80 -2'\
    '87 -26 106 -32 25 -111 28 -162 6z m108 -146 c0 -39 -1 -40 -32 -37 -27 2 -34'\
    '8 -36 29 -3 22 2 29 25 37 42 16 43 15 43 -29z"/>'\
    '<path d="M1442 797 c-68 -38 -78 -150 -17 -207 48 -45 196 -33 203 18 3 20 1'\
    '21 -23 12 -69 -26 -135 -3 -135 48 0 21 3 22 76 18 59 -3 76 -1 81 10 8 23 -6'\
    '64 -32 90 -20 19 -34 24 -77 24 -29 -1 -63 -6 -76 -13z m98 -36 c17 -32 12'\
    '-39 -30 -43 -42 -4 -49 7 -34 46 9 22 51 20 64 -3z"/>'\
    '<path d="M1679 781 c-38 -39 -38 -75 1 -111 26 -25 28 -29 14 -41 -9 -7 -13'\
    '-21 -10 -35 4 -16 1 -23 -14 -27 -46 -12 -37 -77 12 -98 102 -42 247 20 219'\
    '94 -10 26 -42 40 -119 52 -56 9 -50 28 12 35 60 8 90 36 89 85 -1 28 3 35 18'\
    '35 15 0 31 -25 69 -106 55 -117 57 -126 35 -144 -13 -11 -18 -10 -29 6 -12 15'\
    '-16 16 -30 5 -23 -19 -21 -68 4 -76 47 -15 88 36 160 198 30 67 58 117 66 117'\
    '8 0 14 7 14 15 0 11 -12 15 -50 15 -49 0 -64 -11 -36 -27 12 -7 11 -16 -8 -60'\
    '-12 -29 -24 -55 -28 -58 -3 -3 -16 20 -28 51 -23 55 -23 57 -5 70 10 8 17 15'\
    '14 18 -2 2 -80 6 -172 10 l-169 6 -29 -29z m119 -13 c24 -24 7 -98 -23 -98'\
    '-18 0 -35 31 -35 62 0 25 17 48 35 48 6 0 16 -5 23 -12z m25 -230 c25 -38 -52'\
    '-67 -87 -32 -15 15 -21 45 -11 56 11 10 89 -8 98 -24z"/>'\
    '<path d="M730 386 c-6 -8 -14 -34 -16 -58 -3 -24 -7 -49 -9 -56 -3 -7 -1 -11'\
    '4 -8 5 3 11 23 15 45 3 22 12 42 18 44 10 4 10 6 1 6 -21 2 -15 21 10 31 15 6'\
    '17 9 6 9 -9 1 -22 -6 -29 -13z"/>'\
    '<path d="M855 373 c0 -16 -4 -43 -7 -60 -5 -20 -4 -33 2 -33 6 0 10 10 10 23'\
    '0 24 17 47 33 47 5 0 7 -16 4 -35 -4 -24 -2 -35 6 -35 9 0 11 13 9 41 -4 35'\
    '-7 40 -24 36 -17 -5 -19 -2 -14 19 4 16 2 24 -6 24 -7 0 -13 -12 -13 -27z"/>'\
    '<path d="M1060 372 c0 -15 -4 -42 -9 -60 -8 -25 -7 -32 5 -32 8 0 13 3 13 8'\
    '-4 21 3 30 25 36 26 6 44 42 29 56 -4 5 -20 11 -35 14 -25 4 -28 2 -28 -22z'\
    'm50 -12 c0 -11 -7 -23 -15 -27 -21 -7 -25 -2 -18 25 7 28 33 29 33 2z"/>'\
    '<path d="M1300 387 c-49 -25 -52 -98 -4 -105 18 -3 18 -2 2 8 -27 17 -23 66 7'\
    '86 20 13 28 14 40 4 9 -7 15 -8 15 -2 0 5 -7 13 -16 16 -19 7 -14 8 -44 -7z"/>'\
    '<path d="M1901 350 c-14 -66 -13 -81 3 -51 l14 24 11 -21 c6 -12 18 -22 26'\
    '-22 11 0 10 5 -5 20 -24 24 -25 36 -4 44 9 4 14 9 10 13 -3 3 -15 -2 -27 -13'\
    'l-21 -19 7 38 c11 56 -2 45 -14 -13z"/>'\
    '<path d="M295 348 c-4 -24 -12 -49 -17 -55 -8 -10 -5 -13 10 -13 15 0 19 5 15'\
    '20 -4 15 0 20 14 20 26 0 57 35 50 55 -4 9 -19 15 -36 15 -27 0 -30 -4 -36'\
    '-42z m55 19 c0 -14 -20 -37 -32 -37 -10 0 -11 34 -1 43 11 12 33 8 33 -6z"/>'\
    '<path d="M545 366 c-6 -6 -11 -28 -13 -48 -3 -34 0 -38 20 -37 13 0 17 3 11 6'\
    '-18 7 -16 61 1 65 11 2 11 6 2 14 -8 8 -14 8 -21 0z"/>'\
    '<path d="M805 358 c-13 -55 -10 -72 10 -75 11 -1 14 0 8 3 -17 8 -16 51 1 61'\
    '12 7 12 10 0 21 -11 10 -14 8 -19 -10z"/>'\
    '<path d="M1576 362 c-2 -4 -6 -23 -8 -42 -2 -29 1 -35 17 -37 11 -2 14 0 8 3'\
    '-18 8 -16 39 2 57 13 13 13 16 0 21 -8 3 -16 2 -19 -2z"/>'\
    '<path d="M382 348 c-7 -7 -12 -24 -12 -39 0 -26 3 -28 43 -27 23 0 36 3 29 5'\
    '-9 3 -11 15 -6 39 6 31 4 34 -18 34 -13 0 -29 -5 -36 -12z m38 -23 c0 -14 -7'\
    '-28 -15 -32 -22 -8 -28 2 -21 32 8 33 36 33 36 0z"/>'\
    '<path d="M464 319 c-1 -21 2 -36 7 -33 5 3 9 13 9 23 0 21 23 44 33 34 4 -3 7'\
    '-2 7 4 0 5 -12 10 -27 11 -26 0 -28 -3 -29 -39z"/>'\
    '<path d="M632 348 c-15 -15 -16 -55 0 -64 8 -5 9 -2 4 11 -9 24 2 55 19 55 21'\
    '0 26 -16 15 -47 -10 -26 -9 -27 5 -8 9 11 14 29 13 40 -3 23 -37 32 -56 13z"/>'\
    '<path d="M952 348 c-7 -7 -12 -25 -12 -40 0 -23 4 -28 23 -27 16 1 18 2 5 6'\
    '-20 5 -25 48 -7 58 17 11 25 -5 9 -16 -13 -9 -13 -10 0 -6 19 5 26 37 8 37 -8'\
    '0 -19 -5 -26 -12z"/>'\
    '<path d="M1148 320 c4 -39 16 -53 25 -27 5 14 -12 67 -22 67 -3 0 -5 -18 -3'\
    '-40z"/>'\
    '<path d="M1192 341 c-8 -13 -9 -21 -4 -17 6 4 12 -5 14 -21 3 -25 4 -25 18 -8'\
    '8 10 10 16 3 12 -8 -5 -13 3 -15 25 l-3 33 -13 -24z"/>'\
    '<path d="M1240 345 c0 -8 2 -15 4 -15 2 0 6 7 10 15 3 8 1 15 -4 15 -6 0 -10'\
    '-7 -10 -15z"/>'\
    '<path d="M1403 319 c-1 -46 11 -41 20 9 5 22 3 32 -6 32 -7 0 -13 -16 -14 -41z"/>'\
    '<path d="M1448 353 c9 -3 11 -16 6 -39 -5 -29 -3 -34 12 -33 11 0 14 3 6 6 -9'\
    '3 -11 16 -6 39 5 29 3 34 -12 33 -11 0 -14 -3 -6 -6z"/>'\
    '<path d="M1500 346 c-27 -33 12 -88 42 -58 6 6 0 8 -18 4 -23 -4 -26 -2 -21'\
    '12 4 10 7 24 7 32 0 8 7 14 16 14 14 0 15 -2 3 -17 -12 -14 -12 -16 1 -11 8 2'\
    '16 12 18 21 4 21 -31 23 -48 3z"/>'\
    '<path d="M1632 323 c13 -48 14 -49 28 -23 8 15 8 20 1 16 -7 -5 -11 2 -11 18'\
    '0 16 -6 26 -14 26 -12 0 -12 -7 -4 -37z"/>'\
    '<path d="M1678 349 c-6 -18 3 -69 13 -69 4 0 5 17 2 38 -7 43 -9 48 -15 31z"/>'\
    '<path d="M1720 344 c0 -8 5 -12 10 -9 6 3 10 10 10 16 0 5 -4 9 -10 9 -5 0'\
    '-10 -7 -10 -16z"/>'\
    '<path d="M1752 348 c-14 -14 -16 -54 -2 -63 5 -3 9 2 8 12 -3 37 2 53 17 53'\
    '22 0 29 -24 15 -52 -11 -22 -11 -22 5 -3 9 11 14 29 13 40 -3 23 -37 32 -56'\
    '13z"/>'\
    '<path d="M1825 319 c-1 -21 3 -39 7 -39 4 0 8 11 8 24 0 25 22 51 33 39 4 -3'\
    '7 -2 7 4 0 5 -12 10 -27 11 -26 0 -28 -3 -28 -39z"/>'\
    '<path d="M1325 290 c-3 -5 -1 -10 4 -10 6 0 11 5 11 10 0 6 -2 10 -4 10 -3 0'\
    '-8 -4 -11 -10z"/>'\
    '</g>'\
    '</svg>'

def get_h2o_title(title, description):
    # NOTE: Check full width desktop, smallest width browser desktop, iPhone browsers to ensure no overlap etc.
    return f"""<div style="float:left; justify-content:left; height: 80px; width: 195px; margin-top:0px">
                    {description}
                </div>
                <div style="display:flex; justify-content:center; margin-bottom:30px; margin-right:330px;">
                    <div style="height: 60px; width: 60px; margin-right:20px;">{h2o_logo}</div>
                    <h1 style="line-height:60px">{title}</h1>
                </div>
                <div style="float:right; height: 80px; width: 80px; margin-top:-100px">
                    <img src="https://raw.githubusercontent.com/h2oai/h2ogpt/main/docs/h2o-qr.png">
                </div>
                """

def get_stategy_title(title, description):
    # NOTE: Check full width desktop, smallest width browser desktop, iPhone browsers to ensure no overlap etc.
    return f"""<div style="display:flex; justify-content:center; margin-top:25px; margin-bottom:30px; margin-right:90px;">
                    <h1 style="line-height:80px">{title}</h1>
                </div>
                """


def get_simple_title(title, description):
    return f"""{description}<h1 align="center"> {title}</h1>"""


def get_dark_js() -> str:
    return """
        if (document.querySelectorAll('.dark').length) {
            document.querySelectorAll('.dark').forEach(el => el.classList.remove('dark'));
        } else {
            document.querySelector('body').classList.add('dark');
        }
    """


def get_heap_js(heapAppId: str) -> str:
    return (
        """globalThis.window.heap=window.heap||[],heap.load=function(e,t){window.heap.appid=e,window.heap.config=t=t||{};var r=document.createElement("script");r.type="text/javascript",r.async=!0,r.src="https://cdn.heapanalytics.com/js/heap-"+e+".js";var a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(r,a);for(var n=function(e){return function(){heap.push([e].concat(Array.prototype.slice.call(arguments,0)))}},p=["addEventProperties","addUserProperties","clearEventProperties","identify","resetIdentity","removeEventProperty","setEventProperties","track","unsetEventProperty"],o=0;o<p.length;o++)heap[p[o]]=n(p[o])};"""
        f"""heap.load("{heapAppId}");""")


def wrap_js_to_lambda(num_params: int, *args: str) -> str:
    """
    Generates a JS code representing JS lambda that wraps all given '*args' code strings.
    The lambda function has number of parameters based on 'num_params' and returns them
    without modification in an array. Lambda with zero parameters returns an empty array.
    """
    params = ", ".join([f"p{i}" for i in range(num_params)])
    newline = "\n"
    return f"""
        ({params}) => {{
            {newline.join([a for a in args if a is not None])}
            return [{params}];
        }}
    """
