**Overview**  
This project implements a skeleton-based action recognition system using [PySkL](https://github.com/kennymckormick/pyskl) (Python Skeleton-based Action Recognition Library). It leverages deep learning techniques to recognize human actions from skeleton data, with a particular focus on the [NTU RGB+D](https://rose1.ntu.edu.sg/dataset/actionRecognition/) dataset.

---

**Setup Instructions**

**Environment Setup**

Install conda support in Google Colab:

```python
!pip install -q condacolab
import condacolab
condacolab.install()
```

Mount Google Drive:

```python
from google.colab import drive
drive.mount('/content/drive', force_remount=True)
```

Navigate to project directory:

```bash
%cd drive/MyDrive/Path_to_Your_Project/pyskl
```

---

**Dependencies Installation**

Install PySkL requirements:

```bash
!pip install -r requirements.txt
```

Install PySkL in development mode:

```bash
!pip install -e .
```

Install specific YAPF version (required for compatibility):

```bash
!pip install yapf==0.32.0
```

Fix NumPy Inf issue:

```bash
!sed -i 's/np.Inf/np.inf/g' ./pyskl/datasets/pipelines/augmentations.py
```

Set matplotlib backend:

```python
import os
os.environ['MPLBACKEND'] = 'Agg'
```

---

**Dataset Configuration**  
The project uses a customized subset of the NTU RGB+D dataset with 5 action classes.

Create custom config file:

```bash
!cp configs/posec3d/slowonly_r50_ntu120_xsub/joint.py configs/posec3d/slowonly_r50_ntu120_xsub/custom_joint.py
```

Modify config to use custom dataset path:

```bash
!sed -i 's|data/nturgbd/ntu120_hrnet.pkl|./tools/data/ntu5.pkl|g' configs/posec3d/slowonly_r50_ntu120_xsub/custom_joint.py
```

Update number of classes:

```bash
!sed -i 's|num_classes=120|num_classes=5|g' configs/posec3d/slowonly_r50_ntu120_xsub/custom_joint.py
```

---

**Model Architecture**  
The model uses a PoseC3D architecture with the following components:

- **Backbone**: ResNet3dSlowOnly with 3 stages  
- **Input**: 17-channel skeleton data  
- **Head**: I3D classification head with 5 output classes  
- **Data format**: Limb-based heatmaps  

---

**Training**  
To train the model:

```bash
python -m torch.distributed.launch --nproc_per_node=1 --master_port=20374 tools/train.py configs/posec3d/slowonly_r50_ntu120_xsub/custom_joint.py --launcher pytorch
```
**Testing** (needs Python 3.7) 

```bash
python demo/demo_skeleton.py demo/InputVideo.mp4/avi/mov demo/OutputVideo.mp4
```

---

**Training Configuration**

- **Batch size**: 32 videos per GPU  
- **Workers**: 4 per GPU  
- **Optimizer**: SGD with learning rate 0.4, momentum 0.9, weight decay 0.0003  
- **Learning rate schedule**: CosineAnnealing  
- **Total epochs**: 2  
- **Evaluation metrics**: Top-k accuracy (k=1,5), mean class accuracy  

---

**Notes**

- This project is specifically configured for Google Colab with GPU acceleration  
- Training checkpoints will be saved to the \`work_dirs\` directory  
- The project uses distributed training via PyTorch's distributed launch utility  
- A100 GPU is recommended for optimal training performance  

---

**Acknowledgements**  
This project leverages the PySkL framework, which builds upon several open-source projects including MMCV, MMDetection, and MMPose.
