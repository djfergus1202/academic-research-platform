"""
Unit tests for Teratrend Analyzer
"""

import pytest
import pandas as pd
from utils.teratrend_analyzer import TeratrendAnalyzer, TeratrendResult


class TestTeratrendAnalyzer:
    """Test cases for TeratrendAnalyzer class"""
    
    def setup_method(self):
        """Set up test fixtures"""
        self.analyzer = TeratrendAnalyzer()
    
    def test_analyzer_initialization(self):
        """Test that analyzer initializes correctly"""
        assert self.analyzer is not None
        assert hasattr(self.analyzer, 'structural_database')
        assert hasattr(self.analyzer, 'mechanism_database')
        assert hasattr(self.analyzer, 'therapeutic_timeline')
    
    def test_analyze_drug_teratrends_basic(self):
        """Test basic teratrend analysis functionality"""
        result = self.analyzer.analyze_drug_teratrends("Atorvastatin")
        
        assert isinstance(result, TeratrendResult)
        assert result.drug_name == "Atorvastatin"
        assert result.drug_class is not None
        assert isinstance(result.structural_motifs, list)
        assert isinstance(result.mechanism_trends, dict)
        assert isinstance(result.therapeutic_evolution, dict)
        assert 0.0 <= result.prediction_confidence <= 1.0
    
    def test_drug_class_identification(self):
        """Test drug class identification logic"""
        # Test known drug classes
        assert "ACE Inhibitor" in self.analyzer._identify_drug_class("lisinopril")
        assert "Beta-blocker" in self.analyzer._identify_drug_class("propranolol")
        assert "Statin" in self.analyzer._identify_drug_class("atorvastatin")
        assert "Antibiotic" in self.analyzer._identify_drug_class("amoxicillin")
    
    def test_structural_motifs_analysis(self):
        """Test structural motifs analysis"""
        motifs = self.analyzer._analyze_structural_motifs("atorvastatin", "HMG-CoA Reductase Inhibitor")
        
        assert isinstance(motifs, list)
        assert len(motifs) > 0
        
        for motif in motifs:
            assert 'motif_type' in motif
            assert 'frequency' in motif
            assert 'therapeutic_impact' in motif
            assert 'innovation_potential' in motif
            assert 0.0 <= motif['frequency'] <= 1.0
    
    def test_mechanism_trends_analysis(self):
        """Test mechanism trends analysis"""
        trends = self.analyzer._analyze_mechanism_trends("Cardiovascular")
        
        assert isinstance(trends, dict)
        assert 'historical_evolution' in trends
        assert 'mechanism_complexity' in trends
        assert 'innovation_velocity' in trends
    
    def test_combination_potential_analysis(self):
        """Test combination potential analysis"""
        combinations = self.analyzer._analyze_combination_potential("atorvastatin", "Statin")
        
        assert isinstance(combinations, list)
        assert len(combinations) > 0
        
        for combo in combinations:
            assert 'combination_type' in combo
            assert 'mechanism' in combo
            assert 'clinical_potential' in combo
    
    def test_prediction_confidence_calculation(self):
        """Test prediction confidence calculation"""
        # Mock data for testing
        structural_motifs = [{'motif_type': 'test', 'frequency': 0.8}] * 3
        mechanism_trends = {'trend1': 'value1', 'trend2': 'value2'}
        therapeutic_evolution = {'evolution1': 'value1'}
        
        confidence = self.analyzer._calculate_prediction_confidence(
            structural_motifs, mechanism_trends, therapeutic_evolution
        )
        
        assert 0.5 <= confidence <= 0.95
        assert isinstance(confidence, float)
    
    def test_empty_drug_name(self):
        """Test handling of empty drug name"""
        result = self.analyzer.analyze_drug_teratrends("")
        assert result.drug_name == ""
        assert result.drug_class is not None
    
    def test_unknown_drug_class(self):
        """Test handling of unknown drug class"""
        result = self.analyzer.analyze_drug_teratrends("unknown_drug_xyz")
        assert "Unspecified" in result.drug_class
        assert len(result.structural_motifs) > 0  # Should still return generic motifs


# Integration test
def test_end_to_end_analysis():
    """Test complete end-to-end teratrend analysis"""
    analyzer = TeratrendAnalyzer()
    
    # Test with a well-known drug
    result = analyzer.analyze_drug_teratrends("Atorvastatin")
    
    # Verify all components are present
    assert result.drug_name == "Atorvastatin"
    assert len(result.structural_motifs) > 0
    assert len(result.combination_potential) > 0
    assert result.prediction_confidence > 0.5
    
    # Verify data structure integrity
    assert isinstance(result.mechanism_trends, dict)
    assert isinstance(result.therapeutic_evolution, dict)
    assert isinstance(result.market_dynamics, dict)
    assert isinstance(result.innovation_patterns, dict)