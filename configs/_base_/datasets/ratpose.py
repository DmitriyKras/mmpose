dataset_info = dict(
    dataset_name='ratpose',
    paper_info=dict(
        author='',
        title='',
        container='',
        year='',
        homepage='',
    ),
    keypoint_info={
        0:
        dict(name='nose', id=0, color=[255, 153, 255], type='upper', swap=''),
        1:
        dict(name='right_eye', id=1, color=[255, 153, 255], type='upper', swap='left_eye'),
        2:
        dict(
            name='left_eye',
            id=2,
            color=[255, 102, 255],
            type='upper',
            swap='right_eye'),
        3:
        dict(
            name='head',
            id=3,
            color=[255, 102, 255],
            type='upper',
            swap=''),
        4:
        dict(
            name='right_ear',
            id=4,
            color=[255, 102, 255],
            type='upper',
            swap='left_ear'),
        5:
        dict(
            name='left_ear', id=5, color=[255, 102, 255], type='upper',
            swap='right_ear'),
        6:
        dict(
            name='shoulders_center',
            id=6,
            color=[255, 102, 255],
            type='upper',
            swap=''),
        7:
        dict(
            name='body_center',
            id=7,
            color=[255, 102, 255],
            type='upper',
            swap=''),
        8:
        dict(
            name='right_shoulder',
            id=8,
            color=[255, 153, 255],
            type='upper',
            swap='left_shoulder'),
        9:
        dict(
            name='left_shoulder',
            id=9,
            color=[255, 153, 255],
            type='upper',
            swap='right_shoulder'),
        10:
        dict(
            name='tail_base', id=10, color=[255, 153, 255], type='upper', swap=''),
        11:
        dict(
            name='right_hip', id=11, color=[255, 153, 255], type='upper', swap='left_hip'),
        12:
        dict(
            name='left_hip', id=12, color=[255, 153, 255], type='upper',
            swap='right_hip')
    },
    skeleton_info={
        0:
        dict(link=('nose', 'left_eye'), id=0, color=[255, 153, 255]),
        1:
        dict(link=('nose', 'right_eye'), id=1, color=[255, 153, 255]),
        2:
        dict(link=('nose', 'head'), id=2, color=[255, 153, 255]),
        3:
        dict(link=('left_eye', 'left_ear'), id=3, color=[255, 153, 255]),
        4:
        dict(link=('left_ear', 'head'), id=4, color=[255, 153, 255]),
        5:
        dict(link=('right_eye', 'right_ear'), id=5, color=[255, 153, 255]),
        6:
        dict(link=('right_ear', 'head'), id=6, color=[255, 153, 255]),
        7:
        dict(link=('head', 'shoulders_center'), id=7, color=[255, 153, 255]),
        8:
        dict(link=('shoulders_center', 'body_center'), id=8, color=[255, 153, 255]),
        9:
        dict(link=('body_center', 'tail_base'), id=9, color=[255, 153, 255]),
        10:
        dict(
            link=('shoulders_center', 'left_shoulder'),
            id=10,
            color=[255, 102, 255]),
        11:
        dict(
            link=('left_shoulder', 'left_hip'),
            id=11,
            color=[255, 102, 255]),
        12:
        dict(
            link=('left_hip', 'tail_base'), id=12, color=[255, 102, 255]),
        13:
        dict(
            link=('tail_base', 'right_hip'),
            id=13,
            color=[255, 102, 255]),
        14:
        dict(
            link=('right_hip', 'right_shoulder'),
            id=14,
            color=[255, 51, 255]),
        15:
        dict(
            link=('right_shoulder', 'shoulders_center'),
            id=15,
            color=[255, 51, 255])
    },
    joint_weights=[1.] * 13,
    sigmas=[1.] * 13)
