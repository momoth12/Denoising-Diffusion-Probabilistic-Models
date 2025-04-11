import os
from PIL import Image

def create_gif_from_samples(samples_dir, output_path, duration=2):
    """
    Creates a GIF from all sample images (x0_*.png) in the given directory.

    Args:
        samples_dir (str): Directory containing sample images.
        output_path (str): Path to save the output GIF.
        duration (int): Duration between frames in milliseconds.
    """
    # Sort images by timestep
    image_files = sorted([f for f in os.listdir(samples_dir) if f.startswith("x0_") and f.endswith(".png")],
                         key=lambda x: int(x.split("_")[1].split(".")[0]))
    
    # Load images
    images = [Image.open(os.path.join(samples_dir, f)) for f in image_files]

    # Save as GIF
    if images:
        images[0].save(output_path,
                       save_all=True,
                       append_images=images[1:],
                       duration=duration,
                       loop=0)
        print(f"GIF saved to {output_path}")
    else:
        print("No sample images found.")

if __name__ == "__main__":
    create_gif_from_samples("default/samples", "default/ddpm_samples.gif", duration=200)
