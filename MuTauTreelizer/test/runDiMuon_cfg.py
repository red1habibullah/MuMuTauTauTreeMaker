import FWCore.ParameterSet.Config as cms

process = cms.Process("DiMuonTreelizer")

process.load("FWCore.MessageService.MessageLogger_cfi")

########## Please specify if you are running on data or MC: ##############
isMC = True
##########################################################################

if isMC == True:
    print " ****** we will run on sample of: MC ******"
    process.load("MuMuTauTauTreeMaker.MuTauTreelizer.DiMuSelectorMC_cfi")

else:
    print " ****** we will run on sample of: data ******"
    process.load("MuMuTauTauTreeMaker.MuTauTreelizer.DiMuSelector_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1000)

# --- please specify the sample that you need to run for local test ---
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/group/phys_higgs/HiggsExo/fengwang/SUSYGluGluToHToAA_AToMuMu_AToTauTau_M-125_M-5_TuneCUETP8M1_13TeV_madgraph_pythia8/MiniAOD_H125AA5_DiMuDiTau_Fall17DRPremix_v1/190520_131735/0000/mumutautau_1.root',
        '/store/group/phys_higgs/HiggsExo/fengwang/SUSYGluGluToHToAA_AToMuMu_AToTauTau_M-125_M-5_TuneCUETP8M1_13TeV_madgraph_pythia8/MiniAOD_H125AA5_DiMuDiTau_Fall17DRPremix_v1/190520_131735/0000/mumutautau_10.root',
        '/store/group/phys_higgs/HiggsExo/fengwang/SUSYGluGluToHToAA_AToMuMu_AToTauTau_M-125_M-5_TuneCUETP8M1_13TeV_madgraph_pythia8/MiniAOD_H125AA5_DiMuDiTau_Fall17DRPremix_v1/190520_131735/0000/mumutautau_11.root',
        '/store/group/phys_higgs/HiggsExo/fengwang/SUSYGluGluToHToAA_AToMuMu_AToTauTau_M-125_M-5_TuneCUETP8M1_13TeV_madgraph_pythia8/MiniAOD_H125AA5_DiMuDiTau_Fall17DRPremix_v1/190520_131735/0000/mumutautau_12.root',
        '/store/group/phys_higgs/HiggsExo/fengwang/SUSYGluGluToHToAA_AToMuMu_AToTauTau_M-125_M-5_TuneCUETP8M1_13TeV_madgraph_pythia8/MiniAOD_H125AA5_DiMuDiTau_Fall17DRPremix_v1/190520_131735/0000/mumutautau_2.root',
        '/store/group/phys_higgs/HiggsExo/fengwang/SUSYGluGluToHToAA_AToMuMu_AToTauTau_M-125_M-5_TuneCUETP8M1_13TeV_madgraph_pythia8/MiniAOD_H125AA5_DiMuDiTau_Fall17DRPremix_v1/190520_131735/0000/mumutautau_3.root',
        '/store/group/phys_higgs/HiggsExo/fengwang/SUSYGluGluToHToAA_AToMuMu_AToTauTau_M-125_M-5_TuneCUETP8M1_13TeV_madgraph_pythia8/MiniAOD_H125AA5_DiMuDiTau_Fall17DRPremix_v1/190520_131735/0000/mumutautau_4.root',
        '/store/group/phys_higgs/HiggsExo/fengwang/SUSYGluGluToHToAA_AToMuMu_AToTauTau_M-125_M-5_TuneCUETP8M1_13TeV_madgraph_pythia8/MiniAOD_H125AA5_DiMuDiTau_Fall17DRPremix_v1/190520_131735/0000/mumutautau_5.root',
        '/store/group/phys_higgs/HiggsExo/fengwang/SUSYGluGluToHToAA_AToMuMu_AToTauTau_M-125_M-5_TuneCUETP8M1_13TeV_madgraph_pythia8/MiniAOD_H125AA5_DiMuDiTau_Fall17DRPremix_v1/190520_131735/0000/mumutautau_6.root',
        '/store/group/phys_higgs/HiggsExo/fengwang/SUSYGluGluToHToAA_AToMuMu_AToTauTau_M-125_M-5_TuneCUETP8M1_13TeV_madgraph_pythia8/MiniAOD_H125AA5_DiMuDiTau_Fall17DRPremix_v1/190520_131735/0000/mumutautau_7.root',
        '/store/group/phys_higgs/HiggsExo/fengwang/SUSYGluGluToHToAA_AToMuMu_AToTauTau_M-125_M-5_TuneCUETP8M1_13TeV_madgraph_pythia8/MiniAOD_H125AA5_DiMuDiTau_Fall17DRPremix_v1/190520_131735/0000/mumutautau_8.root',
        '/store/group/phys_higgs/HiggsExo/fengwang/SUSYGluGluToHToAA_AToMuMu_AToTauTau_M-125_M-5_TuneCUETP8M1_13TeV_madgraph_pythia8/MiniAOD_H125AA5_DiMuDiTau_Fall17DRPremix_v1/190520_131735/0000/mumutautau_9.root',
        #'/store/group/phys_higgs/HiggsExo/fengwang/SingleMuon/MiniAOD_SMu_DataF_17Nov2017_v1/190327_151854/0006/mumutautau_zskim_6131.root',
        #'/store/group/phys_higgs/HiggsExo/fengwang/SingleMuon/MiniAOD_SMu_DataF_17Nov2017_v1/190327_151854/0006/mumutautau_zskim_6130.root',
        #'/store/group/phys_higgs/HiggsExo/fengwang/SingleMuon/MiniAOD_SMu_DataF_17Nov2017_v1/190327_151854/0006/mumutautau_zskim_6132.root',
        #'/store/group/phys_higgs/HiggsExo/fengwang/SingleMuon/MiniAOD_SMu_DataF_17Nov2017_v1/190327_151854/0006/mumutautau_zskim_6133.root',
    )
)

############################################################

process.treelizer = cms.Sequence(
        process.lumiTree*
        process.HLTEle*
        process.TrigMuMatcher*
        process.MuonPtEtaCut*
        process.MuonID*
        process.LeadingMuonIso*
        process.SecondMuonIso*
        process.DiMuonMassSelector*
        process.ThirdMuonIso*
        process.JetSelector*
        process.DiMuonAnalyzer
)

process.options = cms.untracked.PSet(
        wantSummary = cms.untracked.bool(True),
)

process.TFileService = cms.Service("TFileService",
        fileName =  cms.string('MuMuTreelization.root')
)

process.p = cms.Path(process.treelizer)
