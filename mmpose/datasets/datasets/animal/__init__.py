# Copyright (c) OpenMMLab. All rights reserved.
from .animalkingdom_dataset import AnimalKingdomDataset
from .animalpose_dataset import AnimalPoseDataset
from .ap10k_dataset import AP10KDataset
from .atrw_dataset import ATRWDataset
from .fly_dataset import FlyDataset
from .horse10_dataset import Horse10Dataset
from .locust_dataset import LocustDataset
from .macaque_dataset import MacaqueDataset
from .zebra_dataset import ZebraDataset
from .ratpose_dataset import RatPoseDataset
from .topviewrodents_dataset import TopViewRodentsDataset


__all__ = [
    'AnimalPoseDataset', 'AP10KDataset', 'Horse10Dataset', 'MacaqueDataset',
    'FlyDataset', 'LocustDataset', 'ZebraDataset', 'ATRWDataset',
    'AnimalKingdomDataset', 'RatPoseDataset', 'TopViewRodentsDataset'
]
