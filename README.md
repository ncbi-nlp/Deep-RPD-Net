# Deep-RPD-Net 
This repository provides scripts and OCT scan samples for the paper titled "Deep-RPD-Net: A 3D Deep Network for Detection of Reticular Pseudodrusen on Optical Coherence Tomography Scans".

## Instructions to set up
### Prerequisites
Have python 3.7, tensorflow 2.8, keras 2.8 installed locally.

### Clone the repository
```
git clone https://github.com/aelsawy/Deep-RPD-Net.git
cd Deep-RPD-Net
```

### Create a virtual environment
```
python -m venv deep_rpd_net
source deep_rpd_net/bin/activate 
```

### The trained models

- You can access the trained models, including Deep-RPD-Net, from the "Models" folder.
- We included the models with the best validation accuracy.

- These model were trained on our development AREDS2 OCT dataset and validated on Dark Adpatation Study OCT dataset.


### Sample scans
- We included two sample OCT scans from each OCT dataset in the "Data" folder.


### Run the script

You can run the model on the sample data using

```
python .\classify_data.py
```
Please note that models and images are provided in the repository

You can run the model on new data using
```
python classify_data.py "model_folder" "your_data_folder" "your_output.csv"
```
Please, stucture your data folder simialr to the provided samples. Make sure to have a folder for each scan including 128 B-scans. If your OCT scan has differnt number of B-scans, you many resample to have the exact number of B-scans.


## NCBI's Disclaimer
This tool shows the results of research conducted in the [Computational Biology Branch](https://www.ncbi.nlm.nih.gov/research/), [NCBI](https://www.ncbi.nlm.nih.gov/home/about). 

The information produced on this website is not intended for direct diagnostic use or medical decision-making without review and oversight by a clinical professional. Individuals should not change their health behavior solely on the basis of information produced on this website. NIH does not independently verify the validity or utility of the information produced by this tool. If you have questions about the information produced on this website, please see a health care professional. 

More information about [NCBI's disclaimer policy](https://www.ncbi.nlm.nih.gov/home/about/policies.shtml) is available.

About [text mining group](https://www.ncbi.nlm.nih.gov/research/bionlp/).

## For Research Use Only
The performance characteristics of this product have not been evaluated by the Food and Drug Administration and is not intended for commercial use or purposes beyond research use only. 

## Acknowledgement
This research was supported in part by the Intramural Research Program of the National Eye Institute, National Institutes of Health, Department of Health and Human Services, Bethesda, Maryland, and the National Center for Biotechnology Information, National Library of Medicine, National Institutes of Health. The sponsor and funding organization participated in the design and conduct of the study; data collection, management, analysis, and interpretation; and the preparation, review and approval of the manuscript.
The views expressed herein are those of the authors and do not reflect the official policy or position of Walter Reed National Military Medical Center, Madigan Army Medical Center, Joint Base Andrews, the U.S. Army Medical Department, the U.S. Army Office of the Surgeon General, the Department of the Air Force, the Department of the Army/Navy/Air Force, Department of Defense, the Uniformed Services University of the Health Sciences or any other agency of the U.S. Government. Mention of trade names, commercial products, or organizations does not imply endorsement by the U.S. Government.


## Cite our work
Amr Elsawy, Tiarnan D. L. Keenan, Alisa T Thavikulwat, Amy Lu, Sunil Bellur,  Souvick Mukherjee, Elvira Agron, Qingyu Chen, Emily Y. Chew, and Zhiyong Lu. "Deep-RPD-Net: A 3D Deep Network for Detection of Reticular Pseudodrusen on Optical Coherence Tomography Scans." Ophthalmology Science.