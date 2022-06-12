

# WikiDiverse: A Multimodal Entity Linking Dataset with Diversified Contextual Topics and Entity Types




This is the main page of the ACL 2022 paper:  [**WikiDiverse: A Multimodal Entity Linking Dataset with Diversified Contextual Topics and Entity Types**]().



\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* **Updates** \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

- 16/03/2022: We add a new version of dataset (V2). 
    * An annotator re-annoted the entire dataset based on the annotations in V1.
    * The Train and Valid are resampled to make the distributions more similar. 
- 12/06/2022: We release more data: 
    * Dataset with 10 cands.
    * The extracted Wikipedia data: entity2desc and entity2imgURLs.
    * The downloaded WikinewsImgs.


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

- The annotated data: [Google Drive](https://drive.google.com/file/d/1jsoa994_8tW9X19pb1cISKrMG8hTwItv/view?usp=sharing)
- The data with retrieved 10 cands: [Google Drive](https://drive.google.com/file/d/1ATTF_AzYAnUlM1N84S_dtFu-y867CELY/view?usp=sharing)
- The Wikipedia data: 
    * Entity2desc (filtered): [Google Drive](https://drive.google.com/file/d/1LKjcWrU6YdFfLX6iKi0cFKtyhf4t2bbe/view?usp=sharing) (split with '@@@@')
    * The original Wikipedia information: to be released.
- The image files:
    * Wikinews: the downloaded and cleaned imgs can be found in [Google Drive](https://drive.google.com/file/d/1Xg7HxKbvhfKWrrHOYi2-59tE634ILTph/view?usp=sharing)
    * Wikipedia: the alignment between entity names and image URLs: [Google Drive](https://drive.google.com/file/d/1ukoThqll410GG3P0I7-29kg299OzYgOT/view?usp=sharing) (split with '@@@@')

### Data Format

- The annotated data (passage level)
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

- The data with cands (mention level)
```json
[
    "Bart writing \"HDTV is worth every cent\" in the \"chalkboard gag.\".", # sentence
    "https://upload.wikimedia.org/wikinews/en/c/ca/Simpsons_new_title_sequence_screenshot.png", # img_url
    "HDTB", # mention
    "Other", # mention type
    ['bart', 'writing'], # list of left context
    [' ', 'be', 'worth', 'every', 'cent', 'in', 'the', 'chalkboard', 'gag'], # list of right context
    "https://en.wikipedia.org/wiki/High-definition_television", # entity url
    [...], # list of candidates
    "entertainment", # topic
    14, # mention start position
    18, # mention end position
]
```

- How to get the wikinews imgs
```python
import hashlib
import re
for item in data:
  m_img = item[1].split('/')[-1]
  prefix = hashlib.md5(m_img.encode()).hexdigest()
  suffix = re.sub(r'(\S+(?=\.(jpg|JPG|png|PNG|svg|SVG)))|(\S+(?=\.(jpeg|JPEG)))', '', m_img)
  m_img = 'path to wikinewsImgs' + prefix + suffix
  m_img = m_img.replace('.svg', '.png').replace('.SVG', '.png')
```

## Benchmark

To be added


## Citation

If you use WikiDiverse in your work, please cite our paper:

```bibtex
@inproceedings{wang2022wikidiverse,
title={WikiDiverse: A Multimodal Entity Linking Dataset with Diversified Contextual Topics and Entity Types},
author={Wang, Xuwu and Tian, Junfeng and Gui, Min and Li, Zhixu and Wang, Rui and Yan, Ming and Chen, Lihan and Xiao, Yanghua},
booktitle={ACL},
year={2022}
}
```

## License

WikiDiverse dataset is distributed under the CC BY-SA 4.0 license.