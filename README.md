# 🤖 Image Classification Model

This is a **Streamlit web app** that integrates **MobileNetV2** and a **CIFAR-10** model for image classification. Users can upload images and receive predictions with confidence scores from either model. It features a sleek navigation bar for easy switching and real-time results, which is ideal for learning and practical use.

**🌐 Live App:** [Streamlit Cloud Deployment](https://share.streamlit.io) (See deployment section)
<img width="1908" height="751" alt="image" src="https://github.com/user-attachments/assets/a5c63348-345e-4757-ae46-119b5fdd024a" />


## 🎯 Key Features

- **Dual Model Support**:
  - **MobileNetV2 (ImageNet)**: Recognizes **1,000+ different classes** - animals, vehicles, objects, etc.
  - **Custom CIFAR-10 Model**: Classifies into **10 specific categories** - airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck.

- **Intuitive Interface**:
  - **Navigation Bar**: Seamlessly switch between models using sidebar menu
  - **Real-Time Classification**: Upload images and get instant predictions with confidence scores
  - **Beautiful UI**: Progress bars, formatted results, responsive design

- **Educational & Practical**:
  - Learn about deep learning models and their performance
  - Practical image classification for real-world applications
  - Fully open-source and customizable

## 📋 Prerequisites

- **Python 3.10+** (Recommended: 3.11 for best compatibility)
- **Git** (for version control)
- **Web Browser** (Chrome, Firefox, Safari, Edge)
- **~2GB disk space** (for dependencies and models)

## 🚀 Installation & Setup

### Quick Start (Local Development)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vivek-kumar-P/Image-Classification-model
   cd Image-Classification-model
   ```

2. **Create virtual environment** (Python 3.11 recommended):
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Run the app**:
   ```bash
   streamlit run app.py
   ```

5. **Access the app**:
   Opens automatically at `http://localhost:8501`

### Windows Installation (Step-by-Step)

```powershell
# Navigate to project
cd "e:\code better\Image-Classification-model"

# Activate venv
.\venv\Scripts\Activate.ps1

# Install requirements
pip install -r requirements.txt

# Run app
streamlit run app.py
```


### Usage

1. **Select a Model**:
   - Use the sidebar to choose between **MobileNetV2** or **CIFAR-10**

2. **Upload an Image**:
   - Click "Choose an image..." and select JPG/PNG file
   - Supported formats: JPEG, PNG, JPG
   - Max file size: 200MB

3. **View Predictions**:
   - Real-time classification results
   - Top predictions with confidence scores
   - Progress bars showing confidence levels

---

## 🐛 Known Issues & Solutions

### Issue 1: TensorFlow Installation Error
**Error:** `ERROR: Could not find a version that satisfies the requirement tensorflow`

**Cause:** TensorFlow 2.15+ requires Python 3.10-3.13. Python 3.14+ not yet supported.

**Solution:**
```bash
# Check Python version
python --version

# If Python 3.14+, use Python 3.11 instead
# Create new venv with Python 3.11
python3.11 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Issue 2: Missing Visual C++ Redistributable
**Error:** `OSError: [WinError 126] The specified module could not be found`

**Cause:** TensorFlow needs Microsoft Visual C++ runtime libraries.

**Solution:**
```
1. Download: https://aka.ms/vs/17/release/vc_redist.x64.exe
2. Run the installer (admin mode)
3. Restart your terminal/IDE
4. Reinstall TensorFlow: pip install tensorflow
```

### Issue 3: Port Already in Use
**Error:** `Port 8501 is already in use`

**Cause:** Another Streamlit app is running on the same port.

**Solution:**
```bash
# Use a different port
streamlit run app.py --server.port 8502

# Or kill existing process (Windows):
netstat -ano | findstr :8501
taskkill /PID <PID> /F
```

### Issue 4: Dependencies Conflict
**Error:** `error: subprocess-exited-with-error` with numpy version conflict

**Cause:** Incompatible version pinning in requirements.txt

**Solution:**
```bash
# Clear pip cache
pip cache purge

# Upgrade pip
pip install --upgrade pip

# Reinstall with fresh environment
pip install -r requirements.txt --no-cache-dir
```

### Issue 5: Streamlit Cloud Deployment Error
**Error:** TensorFlow installation fails on Streamlit Cloud

**Cause:** Streamlit Cloud trying to install with wrong Python version

**Solution:**
```
1. Delete the app from Streamlit Cloud
2. Redeploy and select Python 3.11 in Advanced Settings
3. Click Deploy
```

---

## 🌐 Streamlit Cloud Deployment

### Deploy Your App (Live on Web)

1. **Push code to GitHub**:
   ```bash
   git add .
   git commit -m "Your message"
   git push origin main
   ```

2. **Go to Streamlit Cloud**:
   - Visit [https://share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub

3. **Deploy New App**:
   - Click "New app"
   - Select repository: `vivek-kumar-P/Image-Classification-model`
   - Branch: `main`
   - Main file: `app.py`

4. **Configure Python Version** (IMPORTANT):
   - Click "Advanced settings"
   - Select **Python 3.11** from dropdown
   - Click "Deploy"

5. **Wait for deployment** (2-3 minutes):
   - App will be live at: `https://your-username-image-classification.streamlit.app`

### Troubleshooting Deployment

**Build fails with TensorFlow error?**
- Delete app → Redeploy with Python 3.11 selected

**Port/Process errors?**
- Streamlit Cloud handles this automatically, just redeploy

**Dependencies not installing?**
- Update requirements.txt with compatible versions
- Commit → Push → Redeploy

---

## 📊 System Architecture

### Local Development:
```
Your Computer
├─ Python 3.11
├─ Virtual Environment
├─ Dependencies (from requirements.txt)
├─ App code (app.py)
├─ Models (cifar10_model.h5)
└─ Runs on localhost:8501
```

### Streamlit Cloud:
```
Streamlit's Servers
├─ Python 3.11 (selected during deploy)
├─ Virtual Environment (auto-created)
├─ Dependencies (installed from requirements.txt)
├─ Your code (cloned from GitHub)
└─ Runs 24/7 at streamlit.app URL
```

**Key Point:** Cloud app is independent from local setup! Deleting local files won't affect the live app.

---

## 📦 Project Structure

```
Image-Classification-model/
├── app.py                      # Main Streamlit application
├── train.py                    # Model training script
├── cifar10_model.h5           # Pre-trained CIFAR-10 model
├── requirements.txt           # Python dependencies
├── README.md                  # Documentation (this file)
├── .streamlit/
│   └── config.toml            # Streamlit Cloud config
└── Testing Images/
    ├── CIFAR-10/              # Test images
    └── MobileNetV2/           # Test images
```

---

## 📝 Recent Updates (January 28, 2026)

### Changes Made:
✅ Fixed dependency conflicts in `requirements.txt`
✅ Added flexible version constraints instead of strict pinning
✅ Added `.streamlit/config.toml` for Cloud deployment
✅ Updated app.py with better error handling
✅ Tested on Python 3.11 with TensorFlow 2.15.0
✅ Verified Streamlit Cloud deployment

### Problems Tackled:
1. **TensorFlow not available for Python 3.14** → Switched to Python 3.11
2. **Dependency version conflicts** → Updated requirements.txt with compatible versions
3. **Missing Visual C++ libraries** → Provided download and install instructions
4. **Port conflicts on local** → Added port configuration examples
5. **Streamlit Cloud deployment failures** → Added Python version selection guide

---

## 🔧 Troubleshooting Checklist

| Problem | Command | Status |
|---------|---------|--------|
| Wrong Python version | `python --version` | Check output |
| venv not activating | `venv\Scripts\activate.ps1` | PowerShell |
| Dependencies failing | `pip install --upgrade pip` | Then reinstall |
| App not starting | `streamlit run app.py --logger.level=error` | Debug mode |
| Port in use | `streamlit run app.py --server.port 8502` | Alt port |
| TensorFlow error | Use Python 3.11 | Fallback version |

---

## 📚 Model Information

### MobileNetV2 (ImageNet)
- **Classes:** 1,000+
- **Input:** 224×224 RGB images
- **Performance:** Fast, mobile-friendly
- **Use case:** General object detection

### CIFAR-10
- **Classes:** 10 (airplane, car, bird, cat, deer, dog, frog, horse, ship, truck)
- **Input:** 32×32 RGB images
- **Performance:** Specialized classification
- **Use case:** Specific object detection in 10 categories

---

## 🚀 Future Enhancements

- [ ] Add image download with predictions
- [ ] Add batch image processing
- [ ] Deploy custom model training interface
- [ ] Add prediction history
- [ ] Mobile app version
- [ ] Real-time webcam classification

---

## 📄 License

This project is open-source and available for educational and commercial use.

---

## 👥 Contributing

Feel free to:
- Fork the repository
- Create issues for bugs/features
- Submit pull requests
- Share feedback and improvements

---

## 🙏 Acknowledgments

- **Streamlit** - Web app framework
- **TensorFlow** - Deep learning library
- **Keras** - Neural network API
- **MobileNetV2** - Pre-trained model
- **CIFAR-10 Dataset** - Training data

---

## 📞 Support & Contact

For issues or questions:
1. Check the **Troubleshooting** section above
2. Review **Known Issues & Solutions**
3. Open an issue on GitHub
4. Contact the maintainer

---

**Last Updated:** January 28, 2026
**Status:** ✅ Production Ready for Streamlit Cloud
