# Data Science Seminar

Hi guy this is the repository for the Data Science in Finance Seminar.

This guide will help you quickly set up your Python environment and install all required packages.

I would strongly recommend using Visual Studio Code (VSCode)

---
# Recommended VSCode Extensions

Install the following extensions:

## Python Development

- Python

- Jupyter

## LaTeX Development

- LaTeX Workshop

Extension marketplace:

https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop

---

# Recommended Workflow

[A Step for step guide for point 1 and 2 can be found below](README.md#how-to-setup-the-python-environment)

1. Open the repository in VSCode

2. Activate the Python virtual environment

3. Work on:

   - notebooks in `notebooks/`

   - source code in `src/`

   - the paper in `paper/paper.tex`

4. Compile the paper directly inside VSCode using LaTeX Workshop

---

# Using LaTeX Workshop

After installing the extension:

1. Open `paper/paper.tex`

2. Press:

```text

CTRL + ALT + B

```

to build the PDF.

The compiled PDF preview should automatically appear inside VSCode.

---

# Automatic Builds

LaTeX Workshop automatically recompiles the document whenever you save the `.tex` file.

This makes collaborative writing significantly easier.

---

# How to setup the Python Environment
---

# 1. Clone the Repository

Open a terminal and clone the repository:

```bash
git clone <https://github.com/angeloiann-cpu/Data-Science.git>
cd <Data-Science>
```

# 2. Check Python Version

As mentioned in class, for this project it is recommended to use Python 3.13 

Check your installed Python version:

```bash
python --version
```
or on some machines 

```bash
python3 --version
```

# Step 3 — Create a Virtual Environment

A virtual environment keeps project dependencies isolated from your global Python installation.

## macOS / Linux

Create the environment:
```bash
python3 -m venv venv
```

Activate it:
```bash
source venv/bin/activate
```

## Windows (PowerShell)

Create the environment:
```powershell
python -m venv venv
```

Activate it: 
```powershell
venv\Scripts\Activate.ps1
```

## Successful Activation

After activation, your terminal should look similar to:

(venv) username@computer:project-folder$

# Step 4 - Upgrade pip

Before installing packages, upgrade pip:

```bash
pip install --upgrade pip
```

# Step 5 - Install all required packages

Install all dependencies from the requirements.txt file:
```bash
pip install -r requirements.txt
```
This may take a few minutes.


# Step 6 - Verify the installation

```bash 
python -c "import numpy, pandas, scipy, matplotlib, sklearn, statsmodels, yfinance"
```
If no errors appear, the environment was installed successfully.

---
# LaTeX Paper Setup
---


The repository also includes a LaTeX environment for collaboratively writing the seminar paper. 

The paper files are located in: 

```text 
paper/              
paper.tex           -> Main paper document
references.bib      -> Bibliography
figures/            -> Figures and plots
output/             -> Compiled PDF output