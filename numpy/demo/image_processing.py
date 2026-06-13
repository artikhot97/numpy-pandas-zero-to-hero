import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------
# STEP 1: Generate a Sample Image Natively with NumPy
# ----------------------------------------------------------------
# Create a 300x300 pixel RGB canvas (initialized to dark blue)
canvas = np.zeros((300, 300, 3), dtype=np.uint8)
canvas[:, :] = [20, 40, 80] 

# Draw a solid red square using array slicing
canvas[40:120, 40:120] = [255, 0, 0]

# Draw a gradient green square using linear spacing and broadcasting
gradient = np.linspace(0, 255, 100, dtype=np.uint8).reshape(100, 1)
canvas[160:260, 40:140, 1] = gradient  # Broadcast gradient to Green channel

# Draw a bright yellow circle using a mathematical distance mask
Y, X = np.ogrid[:300, :300]
center_y, center_x, radius = 150, 220, 50
circle_mask = (X - center_x)**2 + (Y - center_y)**2 <= radius**2
canvas[circle_mask] = [255, 255, 0]

original_img = canvas.copy()

# ----------------------------------------------------------------
# STEP 2: Apply Image Processing Operations Using Pure NumPy
# ----------------------------------------------------------------

# 1. Cropping (Slicing the array)
cropped = original_img[30:270, 30:270]

# 2. Geometric Flip (Reversing array columns)
flipped = original_img[:, ::-1]

# 3. Brightness Adjustment (Broadcasting addition + clipping)
# We cast to int16 to avoid uint8 overflow issues before clipping
brightened = np.clip(original_img.astype(np.int16) + 80, 0, 255).astype(np.uint8)

# 4. Color Channel Isolate (Zero out Red and Blue, leaving only Green)
green_channel_only = original_img.copy()
green_channel_only[:, :, [0, 2]] = 0

# 5. Grayscale Conversion (Dot product multiplier for human eye luminance)
gray = np.dot(original_img[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)

# 6. Thresholding / Binarization (Boolean masking)
binary = (gray > 100).astype(np.uint8) * 255

# ----------------------------------------------------------------
# STEP 3: Display Results Side-by-Side (Presentation Layout)
# ----------------------------------------------------------------
fig, axes = plt.subplots(2, 4, figsize=(16, 8))
axes = axes.ravel()

# List of items to display
displays = [
    (original_img, "1. Original Shape\n" + str(original_img.shape)),
    (cropped, "2. Cropped (Sliced)\n" + str(cropped.shape)),
    (flipped, "3. Flipped Horizontally\nimg[:, ::-1]"),
    (brightened, "4. Brightness Boost\nnp.clip(img + 80)"),
    (green_channel_only, "5. Isolate Channels\nGreen Only"),
    (gray, "6. Grayscale (2D)\n" + str(gray.shape)),
    (binary, "7. Binary Threshold\n(gray > 100)"),
]

# Plot each array
for i, (img_data, title) in enumerate(displays):
    if len(img_data.shape) == 2:  # Handle 2D arrays (gray/binary)
        axes[i].imshow(img_data, cmap='gray', vmin=0, vmax=255)
    else:
        axes[i].imshow(img_data)
    axes[i].set_title(title, fontsize=12, fontweight='bold')
    axes[i].axis('off')

# Hide the last unused subplot frame
axes[-1].axis('off')

plt.tight_layout()
plt.show()
