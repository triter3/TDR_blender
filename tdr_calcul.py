import math
import bge
# entra offset, pos_b, x_a, x_b, x
def calculations(pos_b, x_a, x_b, x, offset, scene):
	armature_name = "Mio_home"

	#Thumb 2
	name = "Thumb2_R"
	q1 = (pos_b[1]/(x_a[1] - x_b[1]))*(x[1] - x_b[1]) - pos_b[1]
	q1 = q1 + offset[1]
	q2 = 0
	q2 = q2 + offset[2]
	scene.objects.get(armature_name).channels[name].rotation_mode = bge.logic.ROT_MODE_YXZ	  
	scene.objects.get(armature_name).channels[name].rotation_euler = (rad(q1), 0, rad(q2))

	#Thumb 3
	name = "Thumb3_R"
	q3 = (pos_b[3]/(x_a[2] - x_b[2]))*(x[2] - x_b[2]) - pos_b[3]
	q3 = q3 + offset[3]
	q4 = 0
	q4 = q4 + offset[4]
	scene.objects.get(armature_name).channels[name].rotation_mode = bge.logic.ROT_MODE_YXZ	  
	scene.objects.get(armature_name).channels[name].rotation_euler = (rad(q3), 0, rad(q4))

	#Thumb 4 
	name = "Thumb4_R"
	q5 = (pos_b[5]/(x_a[3] - x_b[3]))*(x[3] - x_b[3]) - pos_b[5]
	q5 = q5 + offset[5]
	scene.objects.get(armature_name).channels[name].rotation_mode = bge.logic.ROT_MODE_YXZ	  
	scene.objects.get(armature_name).channels[name].rotation_euler = (0, 0, rad(q5))

	# Index 2
	name = "Index2_R"
	q6 = (pos_b[6]/(x_a[9] - x_b[9]))*(x[9] - x_b[9]) - pos_b[6]
	q6 = q6 + offset[6]
	q7 = (pos_b[7]/(x_a[5] - x_b[5]))*(x[5] - x_b[5]) - pos_b[7]
	q7 = q7 + offset[7]
	scene.objects.get(armature_name).channels[name].rotation_mode = bge.logic.ROT_MODE_YXZ	  
	scene.objects.get(armature_name).channels[name].rotation_euler = (rad(q7), 0, rad(q6))

    # Index 3
	name = "Index3_R"
	q8 = (pos_b[8]/(x_a[6] - x_b[6]))*(x[6] - x_b[6]) - pos_b[8]
	# q9 es calcula sense offset q8
	q9 = (2/3) * q8 # calcul previ
	q8 = q8 + offset[8]
	scene.objects.get(armature_name).channels[name].rotation_mode = bge.logic.ROT_MODE_YXZ	  
	scene.objects.get(armature_name).channels[name].rotation_euler = (rad(q8), 0, 0)

	#Index 4
	name = "Index4_R"
	q9 = q9 + offset[9]
	scene.objects.get(armature_name).channels[name].rotation_mode = bge.logic.ROT_MODE_YXZ	  
	scene.objects.get(armature_name).channels[name].rotation_euler = (rad(q9), 0, 0)
	print (name)
	print (x[5],x[6])
	print (q6,q7,q8,q9)

	#Middle 2
	name = "Middle2_R"
	q10 = 0
	q10 = q10 + offset[10]
	q11 = (pos_b[11]/(x_a[7] - x_b[7]))*(x[7] - x_b[7]) - pos_b[11]
	q11 = q11 + offset[11]
	scene.objects.get(armature_name).channels[name].rotation_mode = bge.logic.ROT_MODE_YXZ	  
	scene.objects.get(armature_name).channels[name].rotation_euler = (rad(q11), 0, rad(q10)) 

	#Middle 3
	name = "Middle3_R"
	q12 = (pos_b[12]/(x_a[8] - x_b[8]))*(x[8] - x_b[8]) - pos_b[12]
	q13 = (2/3) * q12 # calcul previ a offset
	q12 = q12 + offset[12]
	scene.objects.get(armature_name).channels[name].rotation_mode = bge.logic.ROT_MODE_YXZ	  
	scene.objects.get(armature_name).channels[name].rotation_euler = (rad(q12), 0, 0) 

	#Middle 4
	name = "Middle4_R"
	q13 = q13 + offset[13]
	scene.objects.get(armature_name).channels[name].rotation_mode = bge.logic.ROT_MODE_YXZ	  
	scene.objects.get(armature_name).channels[name].rotation_euler = (rad(q13), 0, 0) 

	#Ring 3
	name = "Ring3_R"
	q16 = (pos_b[16]/(x_a[12] - x_b[12]))*(x[12] - x_b[12]) - pos_b[16]
	q22 = q16
	q16 = q16 + offset[16]
	q17 = (pos_b[17]/(x_a[10] - x_b[10]))*(x[10] - x_b[10]) - pos_b[17]
	q17 = q17 + offset[17]
	scene.objects.get(armature_name).channels[name].rotation_mode = bge.logic.ROT_MODE_YXZ	  
	scene.objects.get(armature_name).channels[name].rotation_euler = (rad(q17), 0, rad(q16)) 

	#Ring 4
	name = "Ring4_R"
	q18 = (pos_b[18]/(x_a[11] - x_b[11]))*(x[11] - x_b[11]) - pos_b[18]
	q19 = (2/3) * q18 # calcul previ a offset
	q18 = q18 + offset[18]
	scene.objects.get(armature_name).channels[name].rotation_mode = bge.logic.ROT_MODE_YXZ	  
	scene.objects.get(armature_name).channels[name].rotation_euler = (rad(q18), 0, 0) 

	#Ring 5
	name = "Ring5_R"
	q19 = q19 + offset[19]
	scene.objects.get(armature_name).channels[name].rotation_mode = bge.logic.ROT_MODE_YXZ	  
	scene.objects.get(armature_name).channels[name].rotation_euler = (rad(q19), 0, 0) 

	#Pinky 3
	name = "Pinky3_R"
	q22 = q22 + ((pos_b[22]/(x_a[15] - x_b[15]))*(x[15] - x_b[15]) - pos_b[22])
	q22 = q22 + offset[22]
	q23 = (pos_b[23]/(x_a[13] - x_b[13]))*(x[13] - x_b[13]) - pos_b[23]
	q23 = q23 + offset[23]
	scene.objects.get(armature_name).channels[name].rotation_mode = bge.logic.ROT_MODE_YXZ	  
	scene.objects.get(armature_name).channels[name].rotation_euler = (rad(q23), 0, rad(q22))

	#Pinky 4
	name = "Pinky4_R"
	q24 = (pos_b[24]/(x_a[14] - x_b[14]))*(x[14] - x_b[14]) - pos_b[24]
	q25 = (2/3) * q24 # calcul previ a offset
	q24 = q24 + offset[24]
	scene.objects.get(armature_name).channels[name].rotation_mode = bge.logic.ROT_MODE_YXZ	  
	scene.objects.get(armature_name).channels[name].rotation_euler = (rad(q24), 0, 0)

	#Pinky 5
	name = "Pinky5_R"
	q25 = q25 + offset[25]
	scene.objects.get(armature_name).channels[name].rotation_mode = bge.logic.ROT_MODE_YXZ	  
	scene.objects.get(armature_name).channels[name].rotation_euler = (rad(q25), 0, 0)
	print (name)
	print (x[14],x[13])
	print ("p22=",q22," q23=",q23," q24=",q24," q25=",q25)
	# aplica moviments
	scene.objects.get(armature_name).update()

def rad(val):
	val = val * (math.pi/180)
	return val
    
