
---

# Neurotransmitter Synthesis

This repository contains scripts to simulate the synthesis of neurotransmitters from amino acids using RDKit. It includes the biochemical pathways for creating neurotransmitters such as serotonin from tryptophan.

## Features
- Simulate the conversion of tryptophan to serotonin.
- Generate and save molecular structure images at each step.
- Easily extendable to other neurotransmitter synthesis pathways.

### Setup and Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/AdwikParashar/NeurotransmitterSynthesis.git
   cd NeurotransmitterSynthesis
   ```

2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the script to simulate serotonin synthesis:
   ```sh
   python Serotonin_synthesis.py
   ```

#### Requirements
- RDKit
- Pillow

The script generates images of the molecules at each step and saves them in the current directory.

---

