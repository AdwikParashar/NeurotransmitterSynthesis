from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
import os


def display_and_save_molecule(mol, filename, title):
    if mol is not None:
        img = Draw.MolToImage(mol)
        img.save(filename)
        print(f"{title} molecule created and saved as {filename}.")
    else:
        print(f"Failed to create {title} molecule.")


tryptophan_smiles = "N[C@@H](C(O)=O)Cc1c[nH]c2ccccc12"


tryptophan = Chem.MolFromSmiles(tryptophan_smiles)
display_and_save_molecule(tryptophan, "tryptophan.png", "Tryptophan")


htp_smiles = "N[C@@H](C(O)=O)Cc1c[nH]c2ccc(O)cc12"
htp = Chem.MolFromSmiles(htp_smiles)
display_and_save_molecule(htp, "5-htp.png", "5-HTP")


if htp is not None:

    decarboxylation_reaction = AllChem.ReactionFromSmarts('[C:1](C(=O)O)[C:2]>>[C:1][C:2]')


    products = decarboxylation_reaction.RunReactants((htp,))
    if products:
        serotonin = products[0][0]
        serotonin.UpdatePropertyCache()
        display_and_save_molecule(serotonin, "serotonin.png", "Serotonin")
    else:
        print("Decarboxylation reaction failed.")
else:
    print("Skipping decarboxylation step due to failed hydroxylation.")


print("Current working directory:", os.getcwd())


print("Files in current directory:", os.listdir(os.getcwd()))









