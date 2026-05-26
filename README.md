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

## Install LaTeX Workshop

- LaTeX Workshop

Extension marketplace:

https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop

---

# Install TinyTeX

TinyTeX installation guide:

https://yihui.org/tinytex/

---

## macOS / Linux

Run:

```bash
curl -sL "https://yihui.org/tinytex/install-bin-unix.sh" | sh
```

Restart the terminal afterwards.

---

## Windows

Install TinyTeX from:

https://yihui.org/tinytex/

Then restart VSCode.

---
# Verify Installation
Open a terminal and run: 

```bash
pdflatex --version
```

If version information appears, the installation succeeded.

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
```

# Build the Paper

Open:

```text
paper/paper.tex
```

Then:
- Save the file
- Press:

```text
CTRL + ALT + B
```

to compile the PDF.

To open the preview:

```text
CTRL + ALT + V
```

---

# Automatic Package Installation

TinyTeX automatically installs missing LaTeX packages when compiling.
This keeps the installation lightweight while remaining fully functional.

# Bibliography and References

The project uses a BibTeX bibliography file:

```text
paper/references.bib
```

This file stores all academic references used in the paper.

---

# Why Use a `.bib` File?

Using BibTeX allows us to:

- centrally manage references
- automatically generate citations
- avoid manually formatting bibliographies
- collaborate more easily on academic writing

---

# Example Workflow

## 1. Add a Reference to `references.bib`

Example:

```bibtex
@article{fama1970,
  title={Efficient Capital Markets: A Review of Theory and Empirical Work},
  author={Fama, Eugene F.},
  journal={The Journal of Finance},
  volume={25},
  number={2},
  pages={383--417},
  year={1970}
}
```

---

## 2. Cite the Reference in `paper.tex`

Inside the LaTeX document:

```latex
\cite{fama1970}
```

---

## 3. Generate the Bibliography

At the end of `paper.tex`:

```latex
\bibliographystyle{plainnat}
\bibliography{references}
```

---

# Useful Reference Sources

References can often be exported directly as BibTeX from:
- Google Scholar
- Semantic Scholar
- arXiv
- JSTOR
- publisher websites

Usually there is a:

```text
Cite -> BibTeX
```

button.

---

# Recommended Practice

- Keep all references in `references.bib`
- Use meaningful citation keys:

  

```text
authorYear
```

Example:

```text
fama1970
blackscholes1973
```

This keeps citations readable and consistent.