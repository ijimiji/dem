from PIL import Image
from math import atan2, cos, sin


def time_warp(path: str, factor: int = 15) -> None:
    with Image.open(path) as img:
        width, height = img.size
        new_image: Image.Image = Image.new("RGB", img.size)
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

                new_image.putpixel(xy, img.getpixel(uv))

        new_image.save(f"new_{path}")
