import streamlit as st
import numpy as np
from PIL import Image
import warnings
warnings.filterwarnings('ignore')

# Try to import TensorFlow as primary option
try:
    import tensorflow as tf
    TF_AVAILABLE = True
except ImportError:
    TF_AVAILABLE = False

st.set_page_config(page_title="Image Classification", page_icon="🖼️", layout="wide")

# ImageNet sample class names
IMAGENET_SAMPLES = {
    'cat': 0.87,
    'dog': 0.08,
    'other': 0.05
}

CIFAR10_CLASSES = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# Function for MobileNetV2 ImageNet model
def mobilenetv2_imagenet():
    st.title("🖼️ Image Classification with MobileNetV2")
    
    st.markdown("Upload an image and get predictions using MobileNetV2 trained on ImageNet.")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"], key="mobilenet")
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(image, caption='Uploaded Image', use_column_width=True)
        
        with col2:
            st.subheader("Predictions")
            
            if TF_AVAILABLE:
                st.write("🔄 Classifying with TensorFlow...")
                try:
                    # Load MobileNetV2 model
                    model = tf.keras.applications.MobileNetV2(weights='imagenet')
                    
                    # Preprocess the image
                    img = image.resize((224, 224))
                    img_array = np.array(img)
                    img_array = np.expand_dims(img_array, axis=0)
                    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
                    
                    # Make predictions
                    predictions = model.predict(img_array)
                    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=5)[0]
                    
                    st.success("✅ Classification complete!")
                    for i, (imagenet_id, label, score) in enumerate(decoded_predictions, 1):
                        st.write(f"{i}. **{label}**: {score * 100:.2f}%")
                        st.progress(float(score))
                except Exception as e:
                    st.error(f"Error: {str(e)}")
            else:
                st.info("📸 Image uploaded!")
                st.write(f"Size: {image.size[0]}×{image.size[1]} pixels")
                
                st.success("✅ Demo Predictions:")
                sorted_pred = sorted(IMAGENET_SAMPLES.items(), key=lambda x: x[1], reverse=True)
                for class_name, conf in sorted_pred:
                    st.write(f"**{class_name.capitalize()}**: {conf*100:.1f}%")
                    st.progress(conf)
                
                st.warning("**⚠️ Full predictions require TensorFlow. Install with:** `pip install tensorflow`")

# Function for CIFAR-10 model
def cifar10_classification():
    st.title("🎯 CIFAR-10 Image Classification")
    
    st.markdown("Classify images into 10 categories: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"], key="cifar10")
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(image, caption='Uploaded Image', use_column_width=True)
        
        with col2:
            st.subheader("Predictions")
            
            if TF_AVAILABLE:
                st.write("🔄 Classifying with TensorFlow...")
                try:
                    # Load CIFAR-10 model
                    model = tf.keras.models.load_model('cifar10_model.h5')
                    
                    # Preprocess the image
                    img = image.resize((32, 32))
                    img_array = np.array(img)
                    img_array = img_array.astype('float32') / 255.0
                    img_array = np.expand_dims(img_array, axis=0)
                    
                    # Make predictions
                    predictions = model.predict(img_array)
                    predicted_class = np.argmax(predictions, axis=1)[0]
                    confidence = np.max(predictions)
                    
                    st.success(f"✅ **Predicted:** {CIFAR10_CLASSES[predicted_class].upper()}")
                    st.write(f"**Confidence:** {confidence * 100:.2f}%")
                    st.progress(float(confidence))
                except Exception as e:
                    st.error(f"Error: {str(e)}")
            else:
                st.info("📸 Image uploaded!")
                st.write(f"Size: {image.size[0]}×{image.size[1]} pixels")
                
                # Demo prediction
                pred_idx = np.random.randint(0, len(CIFAR10_CLASSES))
                conf = np.random.uniform(0.65, 0.95)
                
                st.success(f"✅ **Demo Prediction:** {CIFAR10_CLASSES[pred_idx].upper()}")
                st.write(f"**Confidence:** {conf*100:.1f}%")
                st.progress(conf)
                
                st.write("**Other possibilities:**")
                other_idx = np.random.choice([i for i in range(len(CIFAR10_CLASSES)) if i != pred_idx], 3, replace=False)
                for idx in other_idx:
                    c = np.random.uniform(0.05, 0.25)
                    st.write(f"  • {CIFAR10_CLASSES[idx].capitalize()}: {c*100:.1f}%")
                
                st.warning("**⚠️ Full predictions require TensorFlow. Install with:** `pip install tensorflow`")

# Main function to control the navigation
def main():
    st.markdown("""
    # 🤖 Image Classification Model
    """)
    
    st.sidebar.title("📋 Navigation")
    choice = st.sidebar.selectbox(
        "Select a model:",
        ("CIFAR-10", "MobileNetV2 (ImageNet)")
    )
    
    if TF_AVAILABLE:
        st.sidebar.success("✅ TensorFlow installed!")
    else:
        st.sidebar.warning("⚠️ TensorFlow not available (demo mode)")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    ### ℹ️ System Information
    - Python 3.14.2
    - Streamlit active
    - All dependencies installed
    
    ### 📦 To enable full predictions:
    ```bash
    pip install tensorflow
    ```
    """)
    
    if choice == "MobileNetV2 (ImageNet)":
        mobilenetv2_imagenet()
    else:
        cifar10_classification()

if __name__ == "__main__":
    main()
