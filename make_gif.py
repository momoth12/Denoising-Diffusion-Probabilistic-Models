import os
from PIL import Image

def make_gif_5s(samples_dir, output_gif_path, total_duration_sec=5):
    """
    Creates a GIF from sample images in the directory that plays over 5 seconds.

    Args:
        samples_dir (str): Directory with sample images (x0_*.png).
        output_gif_path (str): File path to save the output GIF.
        total_duration_sec (int): Total duration for the entire GIF in seconds.
    """
    # Collect and sort image filenames by timestep index
    image_files = sorted(
        [f for f in os.listdir(samples_dir) if f.startswith("x0_") and f.endswith(".png")],
        key=lambda x: int(x.split("_")[1].split(".")[0])
    )

    if not image_files:
        raise ValueError("No sample images found in the specified directory.")

    # Load images
    images = [Image.open(os.path.join(samples_dir, f)) for f in image_files]

    # Calculate duration per frame (in milliseconds)
    duration_per_frame = int((total_duration_sec * 1000) / len(images))

    # Save GIF
    images[0].save(
        output_gif_path,
        save_all=True,
        append_images=images[1:],
        duration=duration_per_frame,
        loop=0,
        optimize=True
    )

    print(f"GIF saved to {output_gif_path}")

if __name__ == "__main__":
    make_gif_5s("default/samples", "default/ddpm_samples_5s.gif")
