// -*- C++ -*-
//
// Package:    testED/MuMuTauMuTauMuAnalyzer
// Class:      MuMuTauMuTauMuAnalyzer
// 
/**\class MuMuTauMuTauMuAnalyzer MuMuTauMuTauMuAnalyzer.cc testED/MuMuTauMuTauMuAnalyzer/plugins/MuMuTauMuTauMuAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Fengwangdong Zhang
//         Created:  Mon, 29 Jul 2019 12:45:22 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "DataFormats/PatCandidates/interface/Vertexing.h"
#include "TTree.h"
#include <math.h>
#include <string>
#include <iostream>

using namespace std;
//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class MuMuTauMuTauMuAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit MuMuTauMuTauMuAnalyzer(const edm::ParameterSet&);
      ~MuMuTauMuTauMuAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      // ----------member data ---------------------------
      edm::EDGetTokenT<edm::View<pat::Muon>> Mu1Mu2Tag;
      edm::EDGetTokenT<edm::View<pat::Muon>> Mu3Tag;
      edm::EDGetTokenT<edm::View<pat::Jet>> JetTag;
      edm::EDGetTokenT<edm::View<pat::MET>> MetTag;
      edm::EDGetTokenT<edm::View<reco::Vertex>> VertexTag;
      bool isMC;
      edm::EDGetTokenT<edm::View<PileupSummaryInfo>> PileupTag;
      edm::EDGetTokenT<GenEventInfoProduct> generator;

      TTree *objectTree;
      // --- below is the vectors of object variables ---
      
      // --- reconstructed muons ---
      vector<float> recoMuonPt;
      vector<float> recoMuonEta;
      vector<float> recoMuonPhi;
      vector<float> recoMuonEnergy;
      vector<int> recoMuonPDGId;
      vector<float> recoMuonIsolation;

      // --- reconstructed jets ---
      vector<float> recoJetPt;
      vector<float> recoJetEta;
      vector<float> recoJetPhi;
      vector<float> recoJetEnergy;
      vector<float> recoJetCSV;
      
      // --- reconstructed MET ---
      vector<float> recoMET;
      vector<float> recoMETPhi;

      // --- pileup and reconstructed vertices ---
      int recoNPrimaryVertex;
      int recoNPU;
      int trueNInteraction;

      // --- event weight for MC ---
      float genEventWeight; 
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
MuMuTauMuTauMuAnalyzer::MuMuTauMuTauMuAnalyzer(const edm::ParameterSet& iConfig):
    Mu1Mu2Tag(consumes<edm::View<pat::Muon>>(iConfig.getParameter<edm::InputTag>("Mu1Mu2Tag"))),
    Mu3Tag(consumes<edm::View<pat::Muon>>(iConfig.getParameter<edm::InputTag>("Mu3Tag"))),
    JetTag(consumes<edm::View<pat::Jet>>(iConfig.getParameter<edm::InputTag>("JetTag"))),
    MetTag(consumes<edm::View<pat::MET>>(iConfig.getParameter<edm::InputTag>("MetTag"))),
    VertexTag(consumes<edm::View<reco::Vertex>>(iConfig.getParameter<edm::InputTag>("VertexTag"))),
    PileupTag(consumes<edm::View<PileupSummaryInfo>>(iConfig.existsAs<edm::InputTag>("PileupTag") ? iConfig.getParameter<edm::InputTag>("PileupTag") : edm::InputTag())),
    generator(consumes<GenEventInfoProduct>(iConfig.existsAs<edm::InputTag>("Generator") ? iConfig.getParameter<edm::InputTag>("Generator") : edm::InputTag()))
{
   //now do what ever initialization is needed
   usesResource("TFileService");
   isMC = iConfig.getParameter<bool>("isMC");
}


MuMuTauMuTauMuAnalyzer::~MuMuTauMuTauMuAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
MuMuTauMuTauMuAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   edm::Handle<edm::View<pat::Muon>> pMu1Mu2;
   iEvent.getByToken(Mu1Mu2Tag, pMu1Mu2);

   edm::Handle<edm::View<pat::Muon>> pMu3;
   iEvent.getByToken(Mu3Tag, pMu3);

   edm::Handle<edm::View<pat::Jet>> pJet;
   iEvent.getByToken(JetTag, pJet);

   edm::Handle<edm::View<pat::MET>> pMet;
   iEvent.getByToken(MetTag, pMet);

   edm::Handle<edm::View<reco::Vertex>> pVertex;
   iEvent.getByToken(VertexTag, pVertex);

   if (isMC)
   {
       edm::Handle<GenEventInfoProduct> gen_ev_info;
       iEvent.getByToken(generator, gen_ev_info);

       edm::Handle<edm::View<PileupSummaryInfo>> pileup_info;
       iEvent.getByToken(PileupTag, pileup_info);

       if (gen_ev_info.isValid())
       {
           genEventWeight = gen_ev_info->weight();
       }

       if (pileup_info.isValid())
       {
           for(edm::View<PileupSummaryInfo>::const_iterator iPileup=pileup_info->begin(); iPileup!=pileup_info->end(); iPileup++)
           {
               if (iPileup->getBunchCrossing() == 0)
               {
                   trueNInteraction = iPileup->getTrueNumInteractions();
                   recoNPU = iPileup->getPU_NumInteractions();
               }
           }
       }
   }

   // --- prepare for offline primary vertices ---
   recoNPrimaryVertex = 0; 
   if (pVertex.isValid())
   {
       for(edm::View<reco::Vertex>::const_iterator iPV=pVertex->begin(); iPV!=pVertex->end(); iPV++)
       {
           recoNPrimaryVertex++;
       }
   }

   // --- prepare muon vector ---
   pat::Muon Mu1 = pMu1Mu2->at(0);
   pat::Muon Mu2 = pMu1Mu2->at(1);

   recoMuonPt.push_back(Mu1.pt());
   recoMuonPt.push_back(Mu2.pt());

   recoMuonEta.push_back(Mu1.eta());
   recoMuonEta.push_back(Mu2.eta());

   recoMuonPhi.push_back(Mu1.phi());
   recoMuonPhi.push_back(Mu2.phi());

   recoMuonEnergy.push_back(Mu1.energy());
   recoMuonEnergy.push_back(Mu2.energy());

   recoMuonPDGId.push_back(Mu1.pdgId());
   recoMuonPDGId.push_back(Mu2.pdgId());
   
   reco::MuonPFIsolation iso = Mu1.pfIsolationR04();
   double reliso = (iso.sumChargedHadronPt + std::max(0.,iso.sumNeutralHadronEt + iso.sumPhotonEt - 0.5*iso.sumPUPt)) / Mu1.pt();
   recoMuonIsolation.push_back(reliso);

   iso = Mu2.pfIsolationR04();
   reliso = (iso.sumChargedHadronPt + std::max(0.,iso.sumNeutralHadronEt + iso.sumPhotonEt - 0.5*iso.sumPUPt)) / Mu2.pt();
   recoMuonIsolation.push_back(reliso);

   for(edm::View<pat::Muon>::const_iterator iMuon=pMu3->begin(); iMuon!=pMu3->end(); iMuon++)
   {
       if ((deltaR(*iMuon, Mu1) < 0.0001) && (fabs(iMuon->pt()-Mu1.pt()) < 0.0001)) // exclude mu1 from the collection
           continue;

       else if ((deltaR(*iMuon, Mu2) < 0.0001) && (fabs(iMuon->pt()-Mu2.pt()) < 0.0001)) // exclude mu2 from the collection
           continue;

       recoMuonPt.push_back(iMuon->pt());
       recoMuonEta.push_back(iMuon->eta());
       recoMuonPhi.push_back(iMuon->phi());
       recoMuonEnergy.push_back(iMuon->energy());
       recoMuonPDGId.push_back(iMuon->pdgId());
       iso = iMuon->pfIsolationR04();
       reliso = (iso.sumChargedHadronPt + std::max(0.,iso.sumNeutralHadronEt + iso.sumPhotonEt - 0.5*iso.sumPUPt)) / iMuon->pt();
       recoMuonIsolation.push_back(reliso);
   }

   // --- prepare jet vector ---
   if(pJet->size()>0)
   {
       for(edm::View<pat::Jet>::const_iterator iJet=pJet->begin(); iJet!=pJet->end(); iJet++)
       {
           recoJetPt.push_back(iJet->pt());
           recoJetEta.push_back(iJet->eta());
           recoJetPhi.push_back(iJet->phi());
           recoJetEnergy.push_back(iJet->energy());
           // --- btag for jet ---
           // reference: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2017#Jets
           recoJetCSV.push_back(iJet->bDiscriminator("pfCombinedSecondaryVertexV2BJetTags"));
       }
   }

   // --- prepare MET vector ---
   if(pMet->size()>0)
   {
       for(edm::View<pat::MET>::const_iterator iMet=pMet->begin(); iMet!=pMet->end(); iMet++)
       {
           recoMET.push_back(iMet->pt());
           recoMETPhi.push_back(iMet->phi());
       }
   }

   // --- fill the object tree ---
   objectTree->Fill();

   // ---- clear all the vectors for next event ----
   // --- reconstructed muons ---
   recoMuonPt.clear();
   recoMuonEta.clear();
   recoMuonPhi.clear();
   recoMuonEnergy.clear();
   recoMuonPDGId.clear();
   recoMuonIsolation.clear();

   // --- reconstructed jets ---
   recoJetPt.clear();
   recoJetEta.clear();
   recoJetPhi.clear();
   recoJetEnergy.clear();
   recoJetCSV.clear();
   
   // --- reconstructed MET ---
   recoMET.clear();
   recoMETPhi.clear();
}


// ------------ method called once each job just before starting event loop  ------------
void 
MuMuTauMuTauMuAnalyzer::beginJob()
{
    // -- initialize the skimmed object vector tree --
    edm::Service<TFileService> fileService;
    objectTree = fileService->make<TTree>("objectTree","objectTree");

    objectTree->Branch("recoMuonPt", &recoMuonPt);
    objectTree->Branch("recoMuonEta", &recoMuonEta);
    objectTree->Branch("recoMuonPhi", &recoMuonPhi);
    objectTree->Branch("recoMuonEnergy", &recoMuonEnergy);
    objectTree->Branch("recoMuonPDGId", &recoMuonPDGId);
    objectTree->Branch("recoMuonIsolation", &recoMuonIsolation);

    objectTree->Branch("recoJetPt", &recoJetPt);
    objectTree->Branch("recoJetEta", &recoJetEta);
    objectTree->Branch("recoJetPhi", &recoJetPhi);
    objectTree->Branch("recoJetEnergy", &recoJetEnergy);
    objectTree->Branch("recoJetCSV", &recoJetCSV);
    
    objectTree->Branch("recoMET", &recoMET);
    objectTree->Branch("recoMETPhi", &recoMETPhi);

    objectTree->Branch("recoNPrimaryVertex", &recoNPrimaryVertex, "recoNPrimaryVertex/I");

    if (isMC)
    {
        objectTree->Branch("recoNPU", &recoNPU, "recoNPU/I");
        objectTree->Branch("trueNInteraction", &trueNInteraction, "trueNInteraction/I");
        objectTree->Branch("genEventWeight", &genEventWeight, "genEventWeight/F");
    }
}

// ------------ method called once each job just after ending the event loop  ------------
void 
MuMuTauMuTauMuAnalyzer::endJob() 
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
MuMuTauMuTauMuAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(MuMuTauMuTauMuAnalyzer);