#!/usr/bin/env bash
set -euo pipefail #-e → il programma si ferma se un comando restituisce errore
#-u → errore se usi una variabile non definita; -o pipefail → se una pipeline (|) fallisce in una parte, fallisce tutto
set -x #Fa stampare ogni comando prima di eseguirlo (modalità debug).

# Compile and run the reaction_ADI example, capturing stdout+stderr to a log.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)" # This sets SCRIPT_DIR to the directory where this script is located, regardless of where it's called from.
REAC_DIR="$(cd "$SCRIPT_DIR/.." && pwd)" # This sets REAC_DIR to the parent directory of SCRIPT_DIR, which is the root of the REACT repository. It assumes this script is located in reactions/examples/ and that the REACT repo structure is intact.

# Allow overriding SUNDIALS install prefix via env var
SUNDIALS_PREFIX="${SUNDIALS_PREFIX:-/mnt/c/Users/annal/REACT/sundials-install}" # This sets SUNDIALS_PREFIX to the value of the environment variable SUNDIALS_PREFIX if it's set, or to a default path if it's not. Adjust the default path as needed for your system.

cd "$SCRIPT_DIR" #Si sposta nella directory corretta prima di compilare.

SRC="reaction_ADI"   # source file in this directory (no .cpp suffix in this tree)
BIN="reaction_ADI_exec" # nome del file eseguibile

echo "Removing old binary to force recompile..." # echo serve per stampare un messaggio informativo
rm -f "$BIN" # rimuove il file eseguibile precedente se esiste, in modo da forzare la ricompilazione. L'opzione -f evita errori se il file non esiste già.

echo "Compiling $SRC -> $BIN"
g++ -x c++ "$SRC" -std=c++11 -o "$BIN" \ 
  -I"$REAC_DIR/include" \
  -I"${SUNDIALS_PREFIX}/include" \
  -L"$REAC_DIR/lib" -L"${SUNDIALS_PREFIX}/lib" \
  -lcopter -lsundials_cvode -lsundials_nvecserial -lsundials_sunmatrixdense -lsundials_sunlinsoldense \
  -lgsl -lgslcblas -lstdc++ -fopenmp

#g++ → compilatore C++; -x c++ → forza linguaggio C++; -std=c++11; -o "$BIN"; -I = directory dove cercare file .h; -L = directory dove cercare librerie .so o .a; il resto sono le librerie da linkare (copter, sundials, gsl, etc.) e le opzioni di compilazione (fopenmp per abilitare il supporto OpenMP).
export LD_LIBRARY_PATH="${SUNDIALS_PREFIX}/lib:${REAC_DIR}/lib:${LD_LIBRARY_PATH:-}"
#Dice al sistema dove cercare le librerie dinamiche a runtime.

echo "Running $BIN (LD_LIBRARY_PATH=$LD_LIBRARY_PATH) — logging to reaction_ADI.log"
"./$BIN" 2>&1 | tee reaction_ADI.log # se sostituisci questa riga con "./$BIN" senza il reindirizzamento, vedresti l'output solo in console e non verrebbe salvato in reaction_ADI.log. Se invece usi "./$BIN > reaction_ADI.log 2>&1", vedresti solo l'output in reaction_ADI.log e non in console. L'uso di tee permette di avere entrambi: output in console e salvataggio su file.
#./$BIN → esegue il programma; 2>&1 | tee reaction_ADI.log → reindirizza sia stdout che stderr al comando tee, che a sua volta scrive l'output sia su console che su reaction_ADI.log.
echo "Run finished; output saved to reaction_ADI.log"
