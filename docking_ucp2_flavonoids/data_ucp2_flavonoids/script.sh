#!/bin/bash
#SBATCH -J ETHANOLAMINE_MCR-1
#SBATCH -p CPU                 # Particion o cola
#SBATCH --nodes=1              # Numero de nodos
#SBATCH --ntasks-per-node=40   # Numero de cores
#SBATCH --mem-per-cpu=50G      # Bloque de memoria para todos los nodos
#SBATCH --time=24:00:00        # Duracion (D-HH:MM)

for f in *.pdbqt; do
    b=$(basename "$f" .pdbqt)
    echo "Procesando ligando $b"
    mkdir -p "$b"
    ./vina --config conf_vs.txt --ligand "$f" --out "${b}/out.pdbqt" --log "${b}/log.txt"
done
