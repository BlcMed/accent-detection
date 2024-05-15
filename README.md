# English Accent Recognition Model

## Introduction

This project aims to develop a Deep Learning model for recognizing English accents. Accurate accent recognition is essential in various applications, such as speech analysis, language learning, and speaker identification. By leveraging data from the Speech Accent Archive, we seek to build a robust model capable of identifying accents with high precision.

## Data source

Weinberger, Steven. (2015). Speech Accent Archive. George Mason University. Retrieved from http://accent.gmu.edu 

## Data Cleaning

As a crucial preprocessing step, we performed data cleaning to enhance the quality of our dataset. One significant aspect of this process involved trimming silence segments from the audio recordings. Silence segments often constitute a substantial portion of audio data, which can introduce biases and redundancies into the model [1]. By removing silence segments with an energy level below 1.0% and lasting more than 1 second, we aimed to eliminate irrelevant information while reducing the risk of overfitting.


## Accent Selection

To streamline our analysis and ensure balanced representation, we focused on two primary accents: Arabic and English. These accents were chosen due to their prevalence in the dataset and their equivalence in terms of the number of recordings. While other accents, such as Hindi, were underrepresented, we opted for simplicity and practicality in our analysis.

## Feature Engineering

For feature engineering, we employed Mel-frequency cepstral coefficients (MFCCs), a widely used spectral feature representation in automatic speech recognition (ASR) and accent recognition systems. MFCC features offer excellent performance in shallow models and are well-suited for accent recognition tasks[2] [3].

Speech signal recognition differs fundamentally from static image recognition due to its dynamic nature. In speech recognition, the analysis revolves around dynamic processes rather than fixed patterns, with recognizable speech represented by feature vectors rather than singular ones. Accents, influenced by numerous factors, can result in hybridizations, making it challenging to pinpoint a single accent type accurately. To address this complexity, recognizing accents at specific intervals, rather than across the entire audio signal, is favored. Each segment undergoes feature extraction, yielding 13 Mel-frequency cepstral coefficients (MFCCs). These coefficients form a two-dimensional vector input. Employing time intervals of 25 ms, corresponding to the duration of a phoneme [4][5], aids in spectrogram characterization and feature extraction accuracy.

## Standard Scaling

Standard scaling, also known as z-score normalization, was applied to the feature vectors extracted from the audio data. This preprocessing technique ensures that each feature (mfcc) has a mean of 0 and a standard deviation of 1, allowing for improved convergence and performance of machine learning algorithms.

## Label Encoding

Since our target variable consists of two labels, we employed label encoding to convert categorical labels into numerical format: 1 for english accent and 0 for arabic accent. 

## Model Building

Our model building phase, implemented using TensorFlow and Keras, is currently underway. We plan to employ state-of-the-art Deep Learning architectures to train and evaluate the performance of our accent recognition model. Details on model architecture, training procedures, and evaluation metrics will be provided in subsequent updates.


## Technologies Utilized

- **Librosa**: Leveraged for audio data processing, including loading audio files, calculating energy, and extracting features.
  
- **Scikit-learn**: Employed for developing custom transformers and integrating them into a pipeline for streamlined data preprocessing.
  
- **TensorFlow and Keras**: Utilized for building and training neural networks.

## References

1. Patel, K. H. (2018). Accent recognition using machine learning methods (Master's thesis). California State Polytechnic University, Pomona.

2. Ganchev, Todor & Fakotakis, Nikos & George, Kokkinakis. (2005). Comparative evaluation of various MFCC implementations on the speaker verification task. Proceedings of the SPECOM. 1. 

3. Y. Singh, A. Pillay and E. Jembere, "Features of Speech Audio for Accent Recognition," 2020 International Conference on Artificial Intelligence, Big Data, Computing and Data Communication Systems (icABCD), Durban, South Africa, 2020, pp. 1-6, doi: 10.1109/icABCD49160.2020.9183893. 

4. Pajot, C., & Harrison, S. (Year). Speech Recognition for Accented English: Stanford CS224N Custom Project Milestone. Unpublished manuscript, Stanford University.

5. Goranka Zoric, “Automatic Lip Synchronization by Speech Signal Analysis,” Master Thesis, Faculty of Electrical Engineering and Computing, University of Zagreb, Zagreb, Oct-2005.


For inquiries or collaborations, please contact us boulaich.mohamed970@gmail.com .
