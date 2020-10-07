import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

options = VarParsing.VarParsing('analysis')

# -------- input files. Can be changed on the command line with the option inputFiles=... ---------
options.inputFiles = ['/store/group/phys_higgs/HiggsExo/fengwang/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MiniAOD_DYJetsToLL_M50_Fall17DRPremix_v1/190806_145316/0000/mumutautau_zskim_100.root']
options.register('isMC', 1, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "Sample is MC")
options.register('tauCluster', 2, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "different tau clusters")
options.register('numThreads', 8, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "Set number of CPU cores")
options.parseArguments()

process = cms.Process("ZMuMuInclusiveTreelizer")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration.StandardSequences.GeometryRecoDB_cff') # need for RecoEgamma recipe
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff') # globaltag is also needed for RecoEgamma recipe inclusion
from Configuration.AlCa.GlobalTag import GlobalTag

########## Please specify if you are running on data (0) or MC (1) in the command line: #########################
########### eg: cmsRun runZMuMuInclusive_2018_cfg.py isMC=1 ###############
##########################################################################

if options.isMC == 1:
    print " ****** we will run on sample of: MC ******"
    process.load("MuMuTauTauTreeMaker.MuTauTreelizer.ZMuMuInclusiveSelectorMC_cfi")
    process.GlobalTag.globaltag = '102X_upgrade2018_realistic_v20'

else:
    print " ****** we will run on sample of: data ******"
    process.load("MuMuTauTauTreeMaker.MuTauTreelizer.ZMuMuInclusiveSelector_cfi")
    process.GlobalTag.globaltag = '102X_dataRun2_v12'

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1000)

# --- please specify the sample that you need to run for local test ---
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(options.inputFiles)
)

######### embed 2017v2 tauID into the miniAOD ###############
# reference: https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePFTauID#Rerunning_of_the_tau_ID_on_M_AN1
if options.tauCluster <= 0:
    print " ====== use slimmedTaus cluster ======"
    updatedTauName = "slimmedTausNewID"
    import MuMuTauTauTreeMaker.MuTauTreelizer.TauIdDeep_slimmedTaus as tauIdConfig
    tauIdEmbedder = tauIdConfig.TauIDEmbedder(process, cms,
            debug = True,
            updatedTauName = updatedTauName,
            toKeep = ["deepTau2017v2p1","2017v2"]
            )
    tauIdEmbedder.runTauID()
    process.rerunTauIDSequence = cms.Sequence(process.rerunMvaIsolationSequence * getattr(process,updatedTauName))

elif options.tauCluster == 1:
    print " ====== use slimmedTausMuonCleaned cluster ======"
    updatedTauName = "slimmedTausNewID"
    import MuMuTauTauTreeMaker.MuTauTreelizer.TauIdDeep_slimmedTausMuonCleaned as tauIdConfig
    tauIdEmbedder = tauIdConfig.TauIDEmbedder(process, cms,
            debug = True,
            updatedTauName = updatedTauName,
            toKeep = ["deepTau2017v2p1","2017v2"]
            )
    tauIdEmbedder.runTauID()
    process.rerunTauIDSequence = cms.Sequence(process.rerunMvaIsolationSequence * getattr(process,updatedTauName))

elif options.tauCluster == 2:
    print " ====== use slimmedTausElectronCleaned cluster ======"
    updatedTauName = "slimmedTausNewID"
    import MuMuTauTauTreeMaker.MuTauTreelizer.TauIdDeep_slimmedTausElectronCleaned as tauIdConfig
    tauIdEmbedder = tauIdConfig.TauIDEmbedder(process, cms,
            debug = True,
            updatedTauName = updatedTauName,
            toKeep = ["deepTau2017v2p1","2017v2"]
            )
    tauIdEmbedder.runTauID()
    process.rerunTauIDSequence = cms.Sequence(process.rerunMvaIsolationSequence * getattr(process,updatedTauName))

elif options.tauCluster == 3:
    print " ====== use slimmedTausMuonCleanedMedium cluster ======"
    updatedTauName = "slimmedTausNewID"
    import MuMuTauTauTreeMaker.MuTauTreelizer.TauIdDeep_slimmedTausMuonCleanedMedium as tauIdConfig
    tauIdEmbedder = tauIdConfig.TauIDEmbedder(process, cms,
            debug = True,
            updatedTauName = updatedTauName,
            toKeep = ["deepTau2017v2p1","2017v2"]
            )
    tauIdEmbedder.runTauID()
    process.rerunTauIDSequence = cms.Sequence(process.rerunMvaIsolationSequence * getattr(process,updatedTauName))

elif options.tauCluster == 4:
    print " ====== use slimmedTausElectronCleanedMedium cluster ======"
    updatedTauName = "slimmedTausNewID"
    import MuMuTauTauTreeMaker.MuTauTreelizer.TauIdDeep_slimmedTausElectronCleanedMedium as tauIdConfig
    tauIdEmbedder = tauIdConfig.TauIDEmbedder(process, cms,
            debug = True,
            updatedTauName = updatedTauName,
            toKeep = ["deepTau2017v2p1","2017v2"]
            )
    tauIdEmbedder.runTauID()
    process.rerunTauIDSequence = cms.Sequence(process.rerunMvaIsolationSequence * getattr(process,updatedTauName))

elif options.tauCluster == 5:
    print " ====== use slimmedTausMuonCleanedTight cluster ======"
    updatedTauName = "slimmedTausNewID"
    import MuMuTauTauTreeMaker.MuTauTreelizer.TauIdDeep_slimmedTausMuonCleanedTight as tauIdConfig
    tauIdEmbedder = tauIdConfig.TauIDEmbedder(process, cms,
            debug = True,
            updatedTauName = updatedTauName,
            toKeep = ["deepTau2017v2p1","2017v2"]
            )
    tauIdEmbedder.runTauID()
    process.rerunTauIDSequence = cms.Sequence(process.rerunMvaIsolationSequence * getattr(process,updatedTauName))

else:
    print " ====== use slimmedTausElectronCleanedTight cluster ======"
    updatedTauName = "slimmedTausNewID"
    import MuMuTauTauTreeMaker.MuTauTreelizer.TauIdDeep_slimmedTausElectronCleanedTight as tauIdConfig
    tauIdEmbedder = tauIdConfig.TauIDEmbedder(process, cms,
            debug = True,
            updatedTauName = updatedTauName,
            toKeep = ["deepTau2017v2p1","2017v2"]
            )
    tauIdEmbedder.runTauID()
    process.rerunTauIDSequence = cms.Sequence(process.rerunMvaIsolationSequence * getattr(process,updatedTauName))
############################################################

######## implant the 2017v2 egamma ID into the 2018 miniAOD ############
# reference: https://twiki.cern.ch/twiki/bin/view/CMS/EgammaMiniAODV2#2017_MiniAOD_V2

from RecoEgamma.EgammaTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
setupEgammaPostRecoSeq(process, era='2018-Prompt')
###########################################################

if options.isMC == 1:
    process.treelizer = cms.Sequence(
            process.lumiTree*
            process.HLTEle*
            process.MuonID*
            process.MuonSelector*
            process.TrigMuMatcher*
            process.egammaPostRecoSeq*
            process.ElectronCandSelector*
            process.rerunTauIDSequence*
            process.TauCandSelector*
            process.DeepDiTauProducer*
            process.JetIdEmbedder*
            process.GenMuonCandSelector*
            process.GenElectronCandSelector*
            process.GenTauMuCandSelector*
            process.GenTauEleCandSelector*
            process.GenTauHadCandSelector*
            process.ZMuMuInclusiveAnalyzer
    )

    process.TFileService = cms.Service("TFileService",
            fileName =  cms.string('ZMuMuTreelization_mc.root')
    )

else:
    process.treelizer = cms.Sequence(
            process.lumiTree*
            process.HLTEle*
            process.MuonID*
            process.MuonSelector*
            process.TrigMuMatcher*
            process.egammaPostRecoSeq*
            process.ElectronCandSelector*
            process.rerunTauIDSequence*
            process.TauCandSelector*
            process.DeepDiTauProducer*
            process.JetIdEmbedder*
            process.ZMuMuInclusiveAnalyzer
    )

    process.TFileService = cms.Service("TFileService",
            fileName =  cms.string('ZMuMuTreelization_data.root')
    )

process.options = cms.untracked.PSet(
        wantSummary = cms.untracked.bool(True),
)

process.options.numberOfThreads = cms.untracked.uint32(options.numThreads)
process.p = cms.Path(process.treelizer)
