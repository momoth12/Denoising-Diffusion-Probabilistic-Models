# Denoising Diffusion Probabilistic Models (DDPM) - MNIST Implementation

This repository provides a PyTorch implementation of **Denoising Diffusion Probabilistic Models (DDPM)**, based on the paper:

> **Denoising Diffusion Probabilistic Models**  
> *Ho et al., NeurIPS 2020*  
> [📄 Read the paper](https://arxiv.org/abs/2006.11239)

This implementation trains a DDPM model on the MNIST dataset, converted from CSV format to image format.

---

## 🔧 Quickstart

### 📁 1. Data Preparation

1. Create image folders:
   ```bash
   mkdir -p data/train/images
   mkdir -p data/test/images
   ```

2. Download the MNIST CSV files from [Kaggle - MNIST in CSV](https://www.kaggle.com/datasets/oddrationale/mnist-in-csv) and place them inside the `data/` directory:
   ```
   data/
   ├── mnist_train.csv
   └── mnist_test.csv
   ```

3. Extract images using the script:
   ```bash
   python utils/extract_mnist_images.py
   ```

4. You should now have:
   ```
   data/
   ├── train/
   │   └── images/
   │       ├── 0/
   │       ├── 1/
   │       └── ...
   └── test/
       └── images/
           ├── 0/
           ├── 1/
           └── ...
   ```

---

### 🚀 2. Training the Model

Train the DDPM model using:

```bash
python scripts/train_ddpm.py --config config/default.yaml
```

This will save model checkpoints to `default/ddpm_ckpt.pth`.

---

### 🎨 3. Sampling Images

To generate samples using the trained model:

```bash
python scripts/sample_ddpm.py --config config/default.yaml
```

Generated images will be saved in:
```
default/samples/x0_*.png
```

---

## 📦 Installation

```bash
git clone https://github.com/momoth12/Denoising-Diffusion-Probabilistic-Models.git
cd Denoising-Diffusion-Probabilistic-Models
pip install -r requirements.txt
```

---

## 📁 Project Structure

```
.
├── config/
│   └── default.yaml
├── dataset/
│   └── mnist_dataset.py
├── models/
│   └── unet_base.py
├── scheduler/
│   └── linear_noise_scheduler.py
├── scripts/
│   ├── train_ddpm.py
│   └── sample_ddpm.py
├── utils/
│   └── extract_mnist_images.py
├── data/
```
├── config/
│   └── default.yaml
├── dataset/
│   └── mnist_dataset.py
├── models/
│   └── unet_base.py
├── scheduler/
│   └── linear_noise_scheduler.py
├── utils/
│   └── extract_mnist_images.py
├── data/
├── default/
│   └── ddpm_ckpt.pth (after training)
│   └── samples/
├── train_ddpm.py
├── sample_ddpm.py
├── README.md
└── requirements.txt
```
│   └── ddpm_ckpt.pth (after training)
│   └── samples/
├── README.md
└── requirements.txt
```

---

## 📌 Acknowledgements

This repository is a clean reimplementation of the DDPM framework from the original paper by Ho et al. It is designed for educational and research use on small datasets like MNIST.

---

## 🧠 Future Ideas

- Conditional DDPM on digit labels
- Training on CIFAR-10 or CelebA
- Integration with logging tools like TensorBoard or Weights & Biases
