#!/bin/bash

export DEVENV=/home/jairot/Documents/University/Master/E18/devenv

# root 
export ROOTSYS=/usr
export DIR_XROOTD=/usr

# cernlib
export CERN_PATH=$DEVENV/software/cernlib-cernlib-2025.02.25.0-free
export CERN_LEVEL=install
export CERN_ROOT=$CERN_PATH/$CERN_LEVEL
export PATH=$CERN_ROOT/bin:$PATH
export CVSCOSRC=$CERN_PATH
export CERN_INCLUDEDIR=$CERN_ROOT/include
export CERN=$CERN_ROOT

# compass data
export COMPASS_FILES=$DEVENV/compass/detector
export BEAMFILES=$DEVENV/compass/beamfiles

# geant4
source $DEVENV/software/geant/geant4-v11.3.0/install/bin/geant4.sh

# primakoff generator
export PRIMGEN=$DEVENV/software/primakoffgenerator
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$PRIMGEN"

# tgeant
source $DEVENV/software/TGEANT/install/thisgeant.sh >> /dev/null

# Loading CORAL
#export CORAL_LOCATION=$DEVENV/software/coral-git
#source $CORAL_LOCATION/coral.sh
#source $CORAL_LOCATION/setup.sh >> /dev/null

## Putting coral.exe and phast in $PATH
#export PATH="$DEVENV/software/phast:$PATH"
