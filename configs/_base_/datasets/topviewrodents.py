dataset_info = dict(
    dataset_name='topviewrodents',
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
        dict(
            name='right_ear',
            id=1,
            color=[255, 102, 255],
            type='upper',
            swap='left_ear'),
        2:
        dict(
            name='left_ear', id=2, color=[255, 102, 255], type='upper',
            swap='right_ear'),
        3:
        dict(
            name='neck',
            id=3,
            color=[255, 102, 255],
            type='upper',
            swap=''),
        4:
        dict(
            name='center',
            id=4,
            color=[255, 102, 255],
            type='upper',
            swap=''),
        5:
        dict(
            name='right_side_body', id=5, color=[255, 153, 255], type='upper', swap='left_side_body'),
        6:
        dict(
            name='left_side_body', id=6, color=[255, 153, 255], type='upper',
            swap='right_side_body'),
        7:
        dict(
            name='tail_base', id=7, color=[255, 153, 255], type='upper', swap=''),
    },
    skeleton_info={
        0:
        dict(link=('nose', 'left_ear'), id=0, color=[255, 153, 255]),
        1:
        dict(link=('nose', 'right_ear'), id=1, color=[255, 153, 255]),
        2:
        dict(link=('right_ear', 'neck'), id=2, color=[255, 153, 255]),
        3:
        dict(link=('nose', 'neck'), id=3, color=[255, 153, 255]),
        4:
        dict(link=('center', 'tail_base'), id=4, color=[255, 153, 255]),
        5:
        dict(link=('tail_base', 'left_side_body'), id=5, color=[255, 153, 255]),
        6:
        dict(link=('tail_base', 'right_side_body'), id=6, color=[255, 153, 255]),
        7:
        dict(
            link=('left_side_body', 'neck'),
            id=7,
            color=[255, 102, 255]),
        8:
        dict(
            link=('right_side_body', 'neck'),
            id=8,
            color=[255, 102, 255]),
        9:
        dict(
            link=('left_ear', 'neck'),
            id=9,
            color=[255, 102, 255]),
        10:
        dict(
            link=('center', 'neck'),
            id=10,
            color=[255, 102, 255])
    },
    joint_weights=[1.] * 8,
    sigmas=[1.] * 8)
