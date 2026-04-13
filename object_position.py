# 机械臂抓取位置相对于物体坐标系的偏移
object_offect_xyz_dict = {
    "cracker_box_small": {"x": -0.25, "y": -0.01, "z": 0.0},
    "custom_box": {"x": -0.10, "y": 0.0, "z": -0.01},
    "custom_package": {"x": -0.18, "y": 0.0, "z": 0.01},
}

# 物体相对于初始坐标系的旋转
object_rotation_dict = {
    "cracker_box_small": (0.5, 0.5, -0.5, 0.5),
    "custom_box": (1.0, 0.0, 0.0, 0.0),
    "custom_package": (1.0, 0.0, 0.0, 0.0),
}
  
#物体在不同background下的初始位置
object_init_position = {
    "packing_table":{"cracker_box_small": (0.7, 0.2, 0.15),},
    "office_204":{"custom_package": (0.2, 0.03, 0.7),"custom_box": (0.2, 0.03, 0.7),},
    "office_204_new":{"custom_package": (0.2, -0.25, 0.7),"custom_box": (0.2, -0.25, 0.7),},
    }


#物体在不同background下的目标位置
object_destination_position = {
    "packing_table":{"cracker_box_small": (0.35,-0.35,0.30),},
    "office_204":{"custom_box": (0.18,-0.20,0.72),"custom_package": (0.08,-0.20,0.75), },
    "office_204_new":{"custom_box": (0.2,0.18,0.80),"custom_package": (0.2,0.18,0.80), }, # custom_box,custom_package need modify
}

# 物体在不同background下的随机位置范围
object_position_random_range = {
    "office_204":{"custom_box" : {"x":(0.2, 0.3), "y":(0.0, 0.05), "z":0.70 },
                  "custom_package" : {"x":(0.2, 0.3), "y":(0.0, 0.05), "z":0.70 },},
    "office_204_new":{"custom_box" : {"x":(0.2, 0.2), "y":(-0.25, -0.25), "z":0.70 },
                  "custom_package" : {"x":(0.2, 0.2), "y":(-0.25, -0.25), "z":0.70 },}, 
    "packing_table":{"cracker_box_small" : {"x":(0.6, 0.8), "y":(0.15, 0.25), "z":0.15},},
}


# 夹爪闭合缩放系数，临时解决夹爪太松的问题
object_gripper_scale = {
    "custom_box": 0.85,
    "custom_package": 0.85,
}

# 场景相机 prim_path
scene_cam_prim_path = {
    "office_204" : "office_204/camera/Camera/base_link/camera_bottom_screw_frame/camera_link/camera_color_frame/SceneCam",
    "office_204_new" : "office_204_new/camera/Camera/base_link/camera_bottom_screw_frame/camera_link/camera_color_frame/SceneCam",
    "packing_table" : "SceneCam"
}

# 场景相机位置
scene_cam_position = {
    "office_204" : (0.1, 0.0, 0.02),
    "office_204_new" : (0.1, 0.0, 0.02),
    "packing_table" :(0.2, -0.09245, 1.4)
}

# 场景相机焦距
scene_cam_focal_length = {
    "office_204" : 18,
    "office_204_new" : 18,
    "packing_table" :8
}

# 场景相机旋转
scene_cam_rotation = {
    "office_204" : (0.5, 0.5, -0.5, -0.5),
    "office_204_new" : (0.5, 0.5, -0.5, -0.5),
    "packing_table" :(0.70711, 0.0, 0.0, -0.70711)
}


# 机械臂在不同background下的初始位置
embodiment_init_position = {
    "packing_table":{"big_custom" : (-0.25, 0.0, 0.0),},
    "office_204":{"custom" : (-0.27, -0.24, 0.65),},
    "office_204_new":{"custom" : (-0.27, -0.24, 0.65),}
}

# 机械臂在不同background下的初始旋转
embodiment_init_rotation = {
    "packing_table":{"big_custom" : (1.0, 0.0, 0.0, 0.0),},
    "office_204":{"custom" : (1.0, 0.0, 0.0, 0.0),},
    "office_204_new":{"custom" : (1.0, 0.0, 0.0, 0.0),}
}

# Isaac Sim 视口相机：eye = 抓取物初始位置 + offset（米）。模长越小一般越“近”（类似滚轮放大）。
# 优先被 CLI --viewer_offset 覆盖；未传 CLI 时用此处按 --background 查表。
viewer_lookat_offset = {
    "office_204": (-1.1, -1.1, 1.1),
    "office_204_new": (-1.1, -1.1, 1.1),
    "packing_table": (-1.5, -1.5, 1.5),
}