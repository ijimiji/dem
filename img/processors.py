from math import atan2, cos, sin

from PIL import Image, ImageDraw, ImageFont

from static.fonts import arial, times


def time_warp(path: str, factor: int = 15) -> None:
    with Image.open(path) as img:
        width, height = img.size
        new_img: Image.Image = Image.new("RGB", img.size)
        print(f"Loaded {path}:{height}x{width}")

        mid_x: float = 0.5 * width
        mid_y: float = 0.5 * height

        for i in range(width):
            for j in range(height):
                # substract middle for width/height to center effect
                x: float = i - mid_x
                y: float = j - mid_y

                theta: float = atan2(y, x)
                radius: float = ((x**2 + y**2) ** 0.5) ** 0.5 * factor

                u: float = min(max(0, mid_x + radius * cos(theta)), width - 1)
                v: float = min(max(0, mid_y + radius * sin(theta)), height - 1)

                uv: tuple[int, int] = (int(u), int(v))
                xy: tuple[int, int] = (i, j)

                new_img.putpixel(xy, img.getpixel(uv))

        new_img.save(f"new_{path}")


def demotivate(path, title_text="Заглавие", bottom_text="Текст"):
    with Image.open(path) as img:
        width, height = img.size

        title_font_width = int(width * 0.1)
        bottom_font_width = int(title_font_width * 0.5)
        padding_top = int(height * 0.1)
        padding_bottom = int(height * 0.25)
        padding_left = padding_right = int(width * 0.1)
        border_width = 3
        image_padding = border_width * 3
        text_margin = 10

        new_width = width + padding_left + padding_right
        new_height = height + padding_top + padding_bottom

        new_img: Image.Image = Image.new("RGB", (new_width, new_height), color="black")

        draw = ImageDraw.Draw(new_img)

        draw.rectangle(
            (
                (
                    # left
                    padding_left - image_padding,
                    # top
                    padding_top - image_padding,
                ),
                (
                    # right
                    new_width - padding_right + image_padding,
                    # bottom
                    new_height - padding_bottom + image_padding,
                ),
            ),
            fill="black",
            outline="white",
            width=border_width,
        )
        new_img.paste(img, (padding_left, padding_top))

        title_font = ImageFont.truetype(times, title_font_width, encoding="UTF-8")
        bottom_font = ImageFont.truetype(arial, bottom_font_width)

        title_text_width, title_text_height = title_font.getsize(title_text)
        draw.text(
            (
                (new_width - title_text_width) // 2 + border_width,
                new_height - padding_bottom,
            ),
            title_text,
            font=title_font,
        )
        bottom_text_width, _ = bottom_font.getsize(bottom_text)
        draw.text(
            (
                (new_width - bottom_text_width) // 2,
                new_height - padding_bottom + title_text_height + text_margin,
            ),
            bottom_text,
            font=bottom_font,
        )

        new_img.save(f"new_{path}")
