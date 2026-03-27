# 物体相对于 base 系的位置偏移
object_offect_xyz_dict = {
    "cracker_box_small": {"x": -0.25, "y": -0.01, "z": 0.0},
    "custom_box": {"x": -0.10, "y": 0.0, "z": -0.01},
}

# 物体相对于初始坐标系的旋转
object_rotation_dict = {
    "cracker_box_small": (0.5, 0.5, -0.5, 0.5),
    "custom_box": (1.0, 0.0, 0.0, 0.0),
}
  
object_init_position = {
    "packing_table":{"cracker_box_small": (0.7, 0.2, 0.15),},
    "office_204":{"custom_box": (0.2, 0.03, 0.7),},}

object_destination_position = {
    "packing_table":(0.35,-0.35,0.30),
    "office_204":(0.18,-0.20,0.70),
}

#
object_position_random_range = {
    "office_204":{"custom_box" : {"x":(0.2, 0.3), "y":(0.0, 0.05), "z":0.70 },},
    "packing_table":{"cracker_box_small" : {"x":(0.6, 0.8), "y":(0.15, 0.25), "z":0.15},},
}


scene_cam_prim_path = {
    "office_204" : "office_204/camera/Camera/base_link/camera_bottom_screw_frame/camera_link/camera_color_frame/SceneCam",
    "packing_table" : "SceneCam"
}

scene_cam_position = {
    "office_204" : (0.1, 0.0, 0.02),
    "packing_table" :(0.2, -0.09245, 1.4)
}

scene_cam_focal_length = {
    "office_204" : 15,
    "packing_table" :8
}

scene_cam_rotation = {
    "office_204" : (0.5, 0.5, -0.5, -0.5),
    "packing_table" :(0.70711, 0.0, 0.0, -0.70711)
}


embodiment_init_position = {
    "packing_table":{"big_custom" : (-0.25, 0.0, 0.0),},
    "office_204":{"custom" : (-0.25, 0.0, 0.65),}
}
embodiment_init_rotation = {
    "packing_table":{"big_custom" : (1.0, 0.0, 0.0, 0.0),},
    "office_204":{"custom" : (1.0, 0.0, 0.0, 0.0),}
}