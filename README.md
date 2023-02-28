# Geosciences images classifier
Classify Geosciences Images

## Model Card for petroglyphs-nlp-consulting/GeoImages57kB7

This model classifies Geosciences images among 57 categories, related to Economic Geosciences, in particular for Oil and Gas applications.

## Model Details

This model is based on EfficientNet(B0 and B7).

EfficientNet model trained on ImageNet-1k at resolution 600x600. It was introduced in the paper [EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks
](https://arxiv.org/abs/1905.11946) by Mingxing Tan and Quoc V. Le.

### Model description

EfficientNet is a mobile-friendly pure convolutional model (ConvNet) that proposes a new scaling method that uniformly scales all dimensions of depth/width/resolution using a simple yet highly effective compound coefficient.

![model image](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/efficientnet_architecture.png)


### Model Description

- **Developed by:** Petroglyphs NLP Consulting
- **Model type:** EfficientNetB7
- **Language(s):** en
- **License:** gpl
- **Finetuned from model:** EfficientNetB0 / EfficientNetB7

### Model Sources

- **Repository:** https://keras.io/examples/vision/image_classification_efficientnet_fine_tuning/
- **Paper:** https://arxiv.org/abs/1905.11946

## Uses

### Direct Use

This model can be used for classifying geosciences images into one of the 57 proposed categories.

Labels descrition = {
    'ARE': 'Area Diagram',
    'COR': 'Cores',
    'CUT': 'Cuttings',
    'DIS': 'Distributions as Bars',
    'DST': 'DST Plot',
    'DTB': 'Distribution as Tukey Boxes',
    'FOS': 'Fossil Macroscopic',
    'GE2': 'Geosciences 2D',
    'GE3': 'Geosciences 3D',
    'HBD': 'Horizontal Bar Diagram',
    'HSD': 'Horizontal Bar Symmetrical',
    'IN2': 'Installation Schema 2D',
    'IN3': 'Installation Schema 3D',
    'LCO': 'Logs Correlation',
    'LEB': 'Colorbar Legend',
    'LIM': 'Logs Imagery',
    'LIN': 'Logs Interpreted',
    'LOG': 'Logo',
    'LSE': 'Logs Seismic',
    'M2D': 'Model 2D',
    'M3D': 'Model 3D',
    'MAD': 'Map Administrative',
    'MEQ': 'Equation',
    'MGE': 'Map Geosciences',
    'MIC': 'Optical Microscopy',
    'MMO': 'Map Geomodel',
    'MSE': 'Map Seismic',
    'ORG': 'Organization',
    'OUT': 'Outcrop',
    'PAD': 'Production Area Diagram',
    'PIE': 'Pie Chart',
    'PLN': 'Project Diagram',
    'SAT': 'Satellite Imagery',
    'SCA': 'Scale Legend',
    'SEM': 'Scanning Electronic Microscopy',
    'SIA': 'Seismic with Attributes',
    'SIG': 'Signature',
    'SII': 'Seismic with Interpretations',
    'SIR': 'Seismic Raw',
    'STB': 'Stratigraphic Bar Chart',
    'STL': 'Litho-Stratigraphic Diagram',
    'STT': 'Stratigraphic Diagram',
    'SUR': 'Equipment Surface',
    'TAB': 'Table',
    'TGN': 'Ternary Diagram',
    'TSI': 'Thin-Section Microscopic',
    'TSM': 'Thin-Section Macroscopic',
    'TXT': 'Text Legend',
    'VBD': 'Vertical Bar Diagram',
    'VBU': 'Vertical Bar Uncertainty',
    'VSD': 'Vertical Stacked Bar Diagram',
    'WDS': 'Well Design',
    'XPC': 'Geochemistry Plot',
    'XPM': 'Cross-Plot Points & Curve',
    'XPP': 'Cross-Plot Points',
    'XPR': 'Polar Plot',
    'XPV': 'Cross-Plot Curve'
}

The model returns the 5 most probable categories with associated scores.

### Downstream Use

Images embeddings could be used for other tasks such as automated labeling of additional images.

## Environmental Impact

- **Hardware Type:** 2 x Titan RTX
- **Hours used:** 5
- **Cloud Provider:** Private Infrastructure
- **Carbon Emitted:** 0.6 kgCO2eq of which 0 percent were directly offset.

## Citation

**BibTeX:**

```bibtex
@article{Tan2019EfficientNetRM,
  title={EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks},
  author={Mingxing Tan and Quoc V. Le},
  journal={ArXiv},
  year={2019},
  volume={abs/1905.11946}
}
```
