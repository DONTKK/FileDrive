_base_ = 'E:/mmdetection/configs/cascade_rcnn/cascade_mask_rcnn_r50_fpn_1x_coco.py'

# 1. 数据集设定
dataset_type = 'CocoDataset'
classes = ('qipao_1', 'huashang_1', 'yiwu_1', 'heidian', 'heidian_1')
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        # 将类别名字添加至 `classes` 字段中
        classes=classes,
        ann_file='F:/data/coco/annotations/instances_val2017.json',
        img_prefix='F:/data/coco/val2017'),
    val=dict(
        type=dataset_type,
        # 将类别名字添加至 `classes` 字段中
        classes=classes,
        ann_file='F:/data/coco/annotations/instances_val2017.json',
        img_prefix='F:/data/coco/val2017'),
    test=dict(
        type=dataset_type,
        # 将类别名字添加至 `classes` 字段中
        classes=classes,
        ann_file='F:/data/coco/annotations/instances_val2017.json',
        img_prefix='F:/data/coco/val2017',))

# 2. 模型设置

# 将所有的 `num_classes` 默认值修改为5（原来为80）
model = dict(
    roi_head=dict(
        bbox_head=[
            dict(
                type='Shared2FCBBoxHead',
                # 将所有的 `num_classes` 默认值修改为 5（原来为 80）
                num_classes=5),
            dict(
                type='Shared2FCBBoxHead',
                # 将所有的 `num_classes` 默认值修改为 5（原来为 80）
                num_classes=5),
            dict(
                type='Shared2FCBBoxHead',
                # 将所有的 `num_classes` 默认值修改为 5（原来为 80）
                num_classes=5)],
        # 将所有的 `num_classes` 默认值修改为 5（原来为 80）
        mask_head=dict(num_classes=5)))
work_dir = 'E:/mmdetection/my/project/work_dirs/my_custom_config'
