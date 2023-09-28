### Faster R-CNN algorithm for object detection in neutron images

Nowadays, inspection of baggage for threat objects (such as explosives) using images is of interest as it can contribute towards more effective and advanced security screen- ing systems. As neutron imaging presents certain advantages over traditional X-Ray imaging, Dynaxion is a company located in Eindhoven that designed a screening sys- tem based on neutron generation. Moreover, the checking of baggage is partially based on manual detection. While this can be efficient, it is also costly and leaves window open for human error. Therefore, this study aims at optimizing a Faster R-CNN that can accurately detect and classify illegal objects contained in neutron images that were generated from Dynaxion. For this, six Faster R-CNN models were trained based on different techniques of feature extraction (ResNet50 and MobileNet-v3), optimiz- ers (Adam or SGD), learning rates, batch sizes, number of epochs and weight decays. In conclusion, the best detection was achieved by the combination of the SGD opti- mizer and the ResNet50 feature extractor, achieving an overall F1 score of 0.85. Sample images on a test dataset demonstrate the model’s accurate object detection capabilities.
