# Deployment Guide

## Streamlit Community Cloud (Recommended - Free)

### Quick Setup
1. **Fork repository** to your GitHub account
2. **Visit** [share.streamlit.io](https://share.streamlit.io)
3. **Connect** your GitHub account
4. **Select** your forked repository
5. **Configure**:
   - Branch: `main`
   - Main file: `app.py`
   - Python version: 3.11
6. **Deploy!**

### Your app will be available at:
```
https://your-app-name.streamlit.app
```

## Local Development

### Using Python
```bash
# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py --server.port 5000
```

### Using Docker
```bash
# Build image
docker build -t academic-research-platform .

# Run container
docker run -p 5000:5000 academic-research-platform
```

## Advanced Deployment

### Kubernetes
```bash
kubectl apply -f kubernetes/
```

### Cloud Platforms
- **AWS**: Use ECS or Lambda
- **Google Cloud**: Use Cloud Run
- **Azure**: Use Container Instances

## Configuration

### Environment Variables
```bash
# Optional API keys
PERPLEXITY_API_KEY=your_key_here
PUBMED_API_KEY=your_key_here

# App settings
MAX_UPLOAD_SIZE=200MB
ENABLE_GPU_COMPUTE=false
```

### Secrets (Streamlit Cloud)
Add secrets in your app dashboard:
```toml
PERPLEXITY_API_KEY = "your_key_here"
PUBMED_API_KEY = "your_key_here"
```

## Troubleshooting

### Common Issues
1. **Import errors**: Check requirements.txt
2. **Port conflicts**: Change port in config.toml
3. **Memory issues**: Reduce dataset sizes
4. **API failures**: Verify API keys in secrets

### Performance Tips
- Use caching for expensive computations
- Optimize large dataset handling
- Configure memory limits appropriately
- Enable compression for large files