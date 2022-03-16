

# WikiDiverse: A Multimodal Entity Linking Dataset with Diversified Contextual Topics and Entity Types




This is the main page of the ACL-IJCNLP 2022 paper:  [**WikiDiverse: A Multimodal Entity Linking Dataset with Diversified Contextual Topics and Entity Types**]().



\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* **Updates** \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

- 16/03/2022: We add a new version of dataset (V2). 
    * An annotator re-annoted the entire dataset based on the annotations in V1.
    * The Train and Valid are resampled to make the distributions more similar. 



## Contents

- [Overview](#overview)
- [Getting Started](#requirements)
  - [Dataset](#Dataset)
    - [Get the Data](#get-the-data)
    - [Data Format](Data-format)
- [Benchmark](#benchmark)
- [Citation](#Citation)

## Overview

WikiDiverse is a high-quality human-annotated MEL dataset with diversified contextual topics and entity types from Wikinews. It has 8K image-caption pairs and uses Wikipedia as the corresponding knowledge base.


## Dataset 

### Get the Data

- Train: [Google Drive for Train Data](https://drive.google.com/file/d/1VNGM8Wa-7E0qUnAM0wdh2S9ICHP62rKd/view?usp=sharing)
- Valid: [Google Drive for Valid Data](https://drive.google.com/file/d/1nEqGMPhpEBSTYqroE99mMwharzuHN5A2/view?usp=sharing)
- Test: [Google Drive for Test Data](https://drive.google.com/file/d/1ovRStLZ8CIWcpK3BnSFdpXO7OPzgyFC7/view?usp=sharing)

### Data Format

```json
[
    "The Lions versus the Packers (2007).",
    "https://upload.wikimedia.org/wikipedia/commons/0/06/DetroitLionsRunningPlay-2007.jpg",
    "sports",
    [
        [
            "Lions",
            "Organization",
            4,
            9,
            "https://en.wikipedia.org/wiki/Detroit_Lions"
        ],
        [
            "Packers",
            "Organization",
            21,
            28,
            "https://en.wikipedia.org/wiki/Green_Bay_Packers"
        ]
    ]
]
```

## Benchmark

To be added


## Citation

If you use WikiDiverse in your work, please cite our paper:

```bibtex
@inproceedings{wang2022wikidiverse,
title={WikiDiverse: A Multimodal Entity Linking Dataset with Diversified Contextual Topics and Entity Types},
author={Wang, Xuwu and Tian, Junfeng and Gui, Min and Li, Zhixu and Wang, Rui and Yan, Ming and Chen, Lihan and Xiao, Yanghua},
booktitle={ACL-IJCNLP},
year={2022}
}
```

## License

WikiDiverse dataset is distributed under the CC BY-SA 4.0 license.