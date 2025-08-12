# Academic Research Platform

A comprehensive computational platform for advanced pharmaceutical research, molecular modeling, and meta-analysis. Built with Streamlit and enhanced with JupyterLab integration, featuring enterprise-grade deployment capabilities.

## Features

### Core Research Tools
- **Statistical Analysis**: Advanced meta-analysis and statistical modeling
- **Molecular Modeling**: 3D protein-drug interaction visualization
- **Pharmacology Analysis**: Population-specific drug response modeling
- **Data Import**: Intelligent document processing and validation
- **Academic Writing**: AI-enhanced research paper generation
- **Validation Results**: Comprehensive research validation dashboard

### Advanced Capabilities
- **Population Analysis**: Genetic diversity and drug response modeling
- **Advanced Analytics**: Enhanced computational methods and algorithms
- **Research Methods**: Systematic research methodologies and frameworks
- **JupyterLab Integration**: Dual computational environments (ports 8888 and 8889)

### Platform Capabilities
- Comprehensive tools for systematic reviews and meta-analysis
- 3D molecular visualization and protein docking simulations
- Population-specific drug response modeling for personalized medicine
- Advanced statistical analysis with demographic considerations
- Cloud deployment ready with multiple deployment options
- Systematic methodology framework ensuring research quality

## Quick Start

### Prerequisites
- Python 3.11+
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/academic-research-platform.git
cd academic-research-platform
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py --server.port 5000
```

4. **Access the platform**
Open your browser to `http://localhost:5000`

## Deployment Options

### 1. Streamlit Community Cloud (Free)
1. Fork this repository to your GitHub account
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select this repository
5. Set main file path to `app.py`
6. Click "Deploy"

### 2. Docker Deployment
```bash
docker build -t academic-research-platform .
docker run -p 5000:5000 academic-research-platform
```

### 3. Kubernetes Deployment
```bash
kubectl apply -f kubernetes/
```

## Project Structure

```
academic-research-platform/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── pages/                 # Streamlit pages
│   ├── 1_Statistical_Analysis.py
│   ├── 2_Molecular_Modeling.py
│   ├── 3_Pharmacology_Analysis.py
│   ├── 4_Data_Import.py
│   ├── 5_Academic_Writing.py
│   ├── 6_Validation_Results.py
│   ├── 7_Population_Analysis.py
│   ├── 8_Quantum_Analysis.py
│   ├── 9_Ubuntu_Philosophy.py
│   └── 10_Jupyter_Integration.py
├── utils/                 # Backend utilities
│   ├── statistical_tools.py
│   ├── pdf_processor.py
│   ├── citation_validator.py
│   ├── r_integration.py
│   ├── nlp_processor.py
│   ├── auto_validator.py
│   └── robust_afrofuturistic.py
├── .streamlit/           # Streamlit configuration
│   └── config.toml
├── notebooks/            # Jupyter notebooks
├── tests/               # Test files
├── kubernetes/          # Kubernetes deployment files
└── docs/               # Documentation
```

## Configuration

### Streamlit Configuration
The platform uses optimized Streamlit settings in `.streamlit/config.toml`:

```toml
[server]
headless = true
address = "0.0.0.0"
port = 5000

[theme]
base = "light"
primaryColor = "#3b82f6"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f8fafc"
textColor = "#1e293b"
```

### Environment Variables (Optional)
Create a `.env` file for enhanced functionality:

```bash
# API Keys for enhanced features (optional)
PERPLEXITY_API_KEY=your_perplexity_api_key_here
PUBMED_API_KEY=your_pubmed_api_key_here

# Application Configuration
ENABLE_GPU_COMPUTE=false
MAX_UPLOAD_SIZE=200MB
```

## Usage

### Statistical Analysis
1. Navigate to "Statistical Analysis" page
2. Upload your data or use sample datasets
3. Configure analysis parameters
4. Run meta-analysis and view results
5. Export results in multiple formats

### Molecular Modeling
1. Go to "Molecular Modeling" page
2. Input protein and ligand data
3. Run docking simulations
4. Visualize 3D molecular interactions
5. Analyze binding affinities

### Academic Writing
1. Access "Academic Writing" page
2. Upload research papers for analysis
3. Generate enhanced academic content
4. Validate citations and references
5. Export formatted documents

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Run tests: `python -m pytest tests/`
5. Commit changes: `git commit -am 'Add feature'`
6. Push to branch: `git push origin feature-name`
7. Submit a Pull Request

## Technical Requirements

### Minimum System Requirements
- RAM: 4GB minimum, 8GB recommended
- Storage: 2GB free space
- Network: Internet connection for API integrations

### Supported Platforms
- Windows 10/11
- macOS 10.15+
- Linux (Ubuntu 20.04+, CentOS 8+)
- Docker containers
- Cloud platforms (AWS, GCP, Azure)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- **Documentation**: Check the `/docs` folder for detailed guides
- **Issues**: Report bugs via GitHub Issues
- **Discussions**: Use GitHub Discussions for questions

## Citation

If you use this platform in your research, please cite:

```bibtex
@software{academic_research_platform,
  author = {Ferguson, David Joshua},
  title = {Academic Research Platform: Comprehensive Computational Tools for Pharmaceutical Research},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/your-username/academic-research-platform}
}
```

## Acknowledgments

Built by David Joshua Ferguson, BS, MS, PharmD Candidate, RSci MRSB MRSC

Advanced computational tools for pharmaceutical research and meta-analysis supporting evidence-based research for global health improvement.