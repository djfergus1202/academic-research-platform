"""
Unit tests for Literature Analyzer
"""

import pytest
import pandas as pd
from utils.literature_analyzer import LiteratureAnalyzer, ComprehensiveReview, LiteratureSearchResult


class TestLiteratureAnalyzer:
    """Test cases for LiteratureAnalyzer class"""
    
    def setup_method(self):
        """Set up test fixtures"""
        self.analyzer = LiteratureAnalyzer()
    
    def test_analyzer_initialization(self):
        """Test that analyzer initializes correctly"""
        assert self.analyzer is not None
        assert hasattr(self.analyzer, 'databases')
        assert hasattr(self.analyzer, 'gray_literature_sources')
        assert hasattr(self.analyzer, 'quality_criteria')
    
    def test_generate_comprehensive_review_basic(self):
        """Test basic comprehensive review generation"""
        review = self.analyzer.generate_comprehensive_review("Atorvastatin", 25)
        
        assert isinstance(review, ComprehensiveReview)
        assert review.drug_name == "Atorvastatin"
        assert review.article_count >= 20  # Should be close to target
        assert isinstance(review.systematic_review_summary, dict)
        assert isinstance(review.meta_analysis_results, dict)
        assert isinstance(review.recommendations, list)
    
    def test_search_terms_generation(self):
        """Test search terms generation"""
        terms = self.analyzer._generate_search_terms("atorvastatin")
        
        assert isinstance(terms, list)
        assert len(terms) > 5  # Should generate multiple search terms
        assert "atorvastatin" in terms
        assert "Atorvastatin" in terms
        
        # Should include therapeutic context terms
        efficacy_terms = [term for term in terms if "efficacy" in term]
        assert len(efficacy_terms) > 0
    
    def test_regular_literature_search(self):
        """Test regular literature search functionality"""
        search_terms = ["atorvastatin", "statin efficacy"]
        articles = self.analyzer._search_regular_literature(search_terms, 10)
        
        assert isinstance(articles, list)
        assert len(articles) <= 10
        
        if articles:
            article = articles[0]
            assert 'pmid' in article
            assert 'title' in article
            assert 'authors' in article
            assert 'journal' in article
            assert 'year' in article
            assert 'study_type' in article
    
    def test_gray_literature_search(self):
        """Test gray literature search functionality"""
        search_terms = ["atorvastatin"]
        gray_lit = self.analyzer._search_gray_literature(search_terms, 5)
        
        assert isinstance(gray_lit, list)
        assert len(gray_lit) <= 5
        
        if gray_lit:
            document = gray_lit[0]
            assert 'document_id' in document
            assert 'title' in document
            assert 'source_type' in document
            assert 'organization' in document
            assert document['source_type'] in self.analyzer.gray_literature_sources
    
    def test_clinical_trials_search(self):
        """Test clinical trials search functionality"""
        search_terms = ["atorvastatin"]
        trials = self.analyzer._search_clinical_trials(search_terms, 5)
        
        assert isinstance(trials, list)
        assert len(trials) <= 5
        
        if trials:
            trial = trials[0]
            assert 'nct_id' in trial
            assert 'title' in trial
            assert 'phase' in trial
            assert 'status' in trial
            assert 'enrollment' in trial
    
    def test_systematic_review_filtering(self):
        """Test systematic review filtering"""
        # Create mock articles
        mock_articles = [
            {'title': 'Systematic review of statins', 'study_type': 'Systematic Review'},
            {'title': 'Meta-analysis of atorvastatin', 'study_type': 'Meta-Analysis'},
            {'title': 'RCT of statin therapy', 'study_type': 'Randomized Controlled Trial'}
        ]
        
        systematic_reviews = self.analyzer._filter_systematic_reviews(mock_articles)
        
        assert isinstance(systematic_reviews, list)
        assert len(systematic_reviews) >= 2  # Should find the systematic review and meta-analysis
        
        for review in systematic_reviews:
            assert 'prisma_compliance' in review
            assert 'studies_included' in review
    
    def test_meta_analysis_filtering(self):
        """Test meta-analysis filtering"""
        mock_articles = [
            {'title': 'Meta-analysis of statin efficacy', 'study_type': 'Meta-Analysis'},
            {'title': 'Systematic review with meta-analysis', 'study_type': 'Systematic Review'},
            {'title': 'Case study', 'study_type': 'Case Study'}
        ]
        
        meta_analyses = self.analyzer._filter_meta_analyses(mock_articles)
        
        assert isinstance(meta_analyses, list)
        assert len(meta_analyses) >= 1
        
        for meta in meta_analyses:
            assert 'effect_size' in meta
            assert 'confidence_interval' in meta
            assert 'heterogeneity_i2' in meta
    
    def test_quality_assessment(self):
        """Test quality assessment functionality"""
        mock_articles = [
            {'quality_score': 0.9, 'study_type': 'RCT'},
            {'quality_score': 0.7, 'study_type': 'Cohort Study'},
            {'quality_score': 0.5, 'study_type': 'Case Series'}
        ]
        
        quality_assessment = self.analyzer._perform_quality_assessment(mock_articles)
        
        assert isinstance(quality_assessment, dict)
        assert 'quality_distribution' in quality_assessment
        assert 'study_type_distribution' in quality_assessment
        assert 'overall_quality_score' in quality_assessment
        
        # Check quality distribution
        quality_dist = quality_assessment['quality_distribution']
        total_articles = sum(quality_dist.values())
        assert total_articles == len(mock_articles)
    
    def test_systematic_review_generation(self):
        """Test systematic review summary generation"""
        # Create mock search results
        mock_search_results = LiteratureSearchResult(
            query_term="atorvastatin",
            total_articles=50,
            systematic_reviews=[],
            meta_analyses=[],
            clinical_trials=[],
            gray_literature=[],
            regular_literature=[{'study_type': 'RCT'} for _ in range(30)],
            search_date="2025-01-01",
            databases_searched=['pubmed', 'cochrane'],
            quality_assessment={'overall_quality_score': 0.8}
        )
        
        systematic_review = self.analyzer._generate_systematic_review(mock_search_results)
        
        assert isinstance(systematic_review, dict)
        assert 'methodology' in systematic_review
        assert 'results' in systematic_review
        assert 'synthesis' in systematic_review
        assert 'limitations' in systematic_review
    
    def test_meta_analysis_generation(self):
        """Test meta-analysis generation"""
        mock_search_results = LiteratureSearchResult(
            query_term="atorvastatin",
            total_articles=30,
            systematic_reviews=[],
            meta_analyses=[{'effect_size': 0.5}, {'effect_size': 0.7}],
            clinical_trials=[],
            gray_literature=[],
            regular_literature=[],
            search_date="2025-01-01",
            databases_searched=['pubmed'],
            quality_assessment={}
        )
        
        meta_analysis = self.analyzer._perform_meta_analysis(mock_search_results)
        
        assert isinstance(meta_analysis, dict)
        assert 'pooled_estimates' in meta_analysis
        assert 'heterogeneity' in meta_analysis
        assert 'publication_bias' in meta_analysis
        
        pooled = meta_analysis['pooled_estimates']
        assert 'effect_size' in pooled
        assert 'confidence_interval' in pooled
    
    def test_recommendations_generation(self):
        """Test clinical recommendations generation"""
        mock_systematic = {'synthesis': {'primary_outcomes': 'positive'}}
        mock_meta = {'pooled_estimates': {'significance': 'Significant'}}
        mock_trials = {'pivotal_trials': [{'trial_name': 'TEST-1'}]}
        
        recommendations = self.analyzer._generate_recommendations(
            mock_systematic, mock_meta, mock_trials
        )
        
        assert isinstance(recommendations, list)
        assert len(recommendations) > 0
        assert all(isinstance(rec, str) for rec in recommendations)
    
    def test_evidence_quality_assessment(self):
        """Test GRADE evidence quality assessment"""
        mock_search_results = LiteratureSearchResult(
            query_term="test",
            total_articles=20,
            systematic_reviews=[],
            meta_analyses=[],
            clinical_trials=[],
            gray_literature=[],
            regular_literature=[],
            search_date="2025-01-01",
            databases_searched=[],
            quality_assessment={'overall_quality_score': 0.8}
        )
        
        evidence_quality = self.analyzer._assess_evidence_quality(mock_search_results)
        
        assert isinstance(evidence_quality, dict)
        assert 'grade_assessment' in evidence_quality
        assert 'strength_of_evidence' in evidence_quality
        assert 'clinical_recommendations' in evidence_quality
    
    def test_target_article_count_handling(self):
        """Test handling of different target article counts"""
        # Test with small count
        review_small = self.analyzer.generate_comprehensive_review("Test Drug", 10)
        assert review_small.article_count >= 8  # Should be close to target
        
        # Test with large count
        review_large = self.analyzer.generate_comprehensive_review("Test Drug", 100)
        assert review_large.article_count >= 80  # Should be close to target


# Integration test
def test_end_to_end_literature_review():
    """Test complete end-to-end literature review generation"""
    analyzer = LiteratureAnalyzer()
    
    # Generate comprehensive review
    review = analyzer.generate_comprehensive_review("Atorvastatin", 50)
    
    # Verify all components are present
    assert review.drug_name == "Atorvastatin"
    assert review.article_count > 0
    assert len(review.recommendations) > 0
    assert len(review.future_research_directions) > 0
    
    # Verify data structure integrity
    assert isinstance(review.systematic_review_summary, dict)
    assert isinstance(review.meta_analysis_results, dict)
    assert isinstance(review.narrative_review, dict)
    assert isinstance(review.scoping_review, dict)
    assert isinstance(review.clinical_trial_summary, dict)
    assert isinstance(review.evidence_quality, dict)