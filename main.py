from PIL import Image

SCREEN_WIDTH = 2400
SCREEN_HEIGHT = 1080
K = 16  # Pixel per lens
V = 2   # Images per lens
VIEW_WIDTH = K // V

SHIFT_PIXELS = 8  # Maximal horizontal pixel shift for fake 3d

def prepare_image(path):
    img = Image.open(path).convert("RGB").resize((SCREEN_WIDTH, SCREEN_HEIGHT))
    return img

def fake_3d(img):
    out = Image.new("RGB", (SCREEN_WIDTH, SCREEN_HEIGHT))
    px_in = img.load()
    px_out = out.load()

    for x in range(SCREEN_WIDTH):
        stripe = (x // VIEW_WIDTH)
        offset = ((stripe % 2) * 2 - 1) * SHIFT_PIXELS // 2
        for y in range(SCREEN_HEIGHT):
            src_x = x + offset
            if src_x < 0: 
                src_x = 0
            if src_x >= SCREEN_WIDTH:
                src_x = SCREEN_WIDTH - 1
            px_out[x, y] = px_in[src_x, y]
    return out

if __name__ == "__main__":
    img = prepare_image("img.png")
    out = fake_3d(img)
    out.save("out_fake3d.png")
