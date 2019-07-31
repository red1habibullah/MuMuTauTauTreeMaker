# MuMuTauTauTreelizerThis tool is used to treelize MiniAOD (or reMiniAOD) samples. The output files contain vectors of different objects (eg. muons, electrons, taus) and flat branches of object counters (eg. number of vertices, event weights etc.).# Introduction for setting up the environment:$ export SCRAM_ARCH=slc6_amd64_gcc630$ cmsrel CMSSW_9_4_13$ cd CMSSW_9_4_13/src/$ git cms-init$ git cms-merge-topic cms-egamma:EgammaPostRecoTools # Recipe for implanting latest Egamma ID dependence$ git clone https://github.com/Fengwangdong/MuMuTauTauTreeMaker.git$ scram b -j8NOTE: Before executing the scripts below, one needs to customize the "isMC" item accordingly. ("True" for MC while "False" for data). # Run the diMuon treelizer:$ cd MuMuTauTauTreeMaker/MuTauTreelizer/test$ cmsRun runDiMuon_cfg.pyThis script will load the EDM filters and analyzers defined in "MuTauTreelizer/python/DiMuSelector*_cfi.py", in which one may need to modify the input parameter settings for the C++ modules defined in "MuTauTreelizer/plugins".# Run the diMuon + ditau (tau_mu + tau_h) treelizer:$ cd MuMuTauTauTreeMaker/MuTauTreelizer/test$ cmsRun runDiMuTauMuTauHad_cfg.pyThis script will load the EDM filters and analyzers defined in "MuTauTreelizer/python/DiMuTauMuTauHadSelector*_cfi.py", in which one may need to modify the input parameter settings for the C++ modules defined in "MuTauTreelizer/plugins".# Run the diMuon + ditau (tau_e + tau_h) treelizer:$ cd MuMuTauTauTreeMaker/MuTauTreelizer/test$ cmsRun runDiMuTauETauHad_cfg.pyThis script will load the EDM filters and analyzers defined in "MuTauTreelizer/python/DiMuTauETauHadSelector*_cfi.py", in which one may need to modify the input parameter settings for the C++ modules defined in "MuTauTreelizer/plugins".# Run the diMuon + ditau (tau_mu + tau_e) treelizer:$ cd MuMuTauTauTreeMaker/MuTauTreelizer/test$ cmsRun runDiMuTauMuTauE_cfg.pyThis script will load the EDM filters and analyzers defined in "MuTauTreelizer/python/DiMuTauMuTauESelector*_cfi.py", in which one may need to modify the input parameter settings for the C++ modules defined in "MuTauTreelizer/plugins".