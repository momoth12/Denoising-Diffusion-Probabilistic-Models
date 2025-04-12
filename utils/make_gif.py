import os
from PIL import Image

def make_gif_from_subset(samples_dir, output_gif_path, total_frames=10, total_duration_sec=5):
    """
    Creates a GIF using a subset of frames (e.g., 10 out of 1000), spaced evenly and lasting 5 seconds.

    Args:
        samples_dir (str): Directory with sample images (x0_*.png).
        output_gif_path (str): Output file path for the GIF.
        total_frames (int): How many frames to include in the GIF.
        total_duration_sec (int): Total duration of the entire GIF in seconds.
    """
    # Collect and sort images in reverse (denoising order)
    image_files = sorted(
        [f for f in os.listdir(samples_dir) if f.startswith("x0_") and f.endswith(".png")],
        key=lambda x: int(x.split("_")[1].split(".")[0]),
        reverse=True
    )

    if len(image_files) < total_frames:
        raise ValueError(f"Not enough images in {samples_dir} to extract {total_frames} frames.")

    # Sample 10 frames evenly from the list
    step = len(image_files) // total_frames
    selected_images = image_files[::step][:total_frames]

    # Load images
    images = [Image.open(os.path.join(samples_dir, f)) for f in selected_images]

    # Calculate duration per frame
    duration_per_frame = int((total_duration_sec * 1000) / total_frames)

    # Save as GIF
    images[0].save(
        output_gif_path,
        save_all=True,
        append_images=images[1:],
        duration=duration_per_frame,
        loop=0,
        optimize=True
    )

    print(f"GIF saved to {output_gif_path} ({total_frames} frames, {duration_per_frame} ms/frame)")

if __name__ == "__main__":
    make_gif_from_subset("default/samples", "ddpm_samples.gif", total_frames=10, total_duration_sec=5)
