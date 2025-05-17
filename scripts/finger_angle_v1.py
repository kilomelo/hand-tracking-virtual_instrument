# me - this DAT
# scriptOp - the OP which is cooking

# press 'Setup Parameters' in the OP to call this function to re-create the parameters.
def onSetupParameters(scriptOp):
	page = scriptOp.appendCustomPage('Custom')
	p = page.appendFloat('Valuea', label='Value A')
	p = page.appendFloat('Valueb', label='Value B')
	return

# called whenever custom pulse parameter is pushed
def onPulse(par):
	return

def onCook(scriptOp):
	import math
	scriptOp.clear()

	input_ops = scriptOp.inputs
	input_names = [input_op.name for input_op in input_ops]

	if len(input_names) < 1: return

	h1_thumb_tip_x = scriptOp.inputs[0][0].eval()
	h1_thumb_tip_y = scriptOp.inputs[0][1].eval()
	h1_thumb_tip_z = scriptOp.inputs[0][2].eval()

	h1_thumb_ip_x = scriptOp.inputs[0][3].eval()
	h1_thumb_ip_y = scriptOp.inputs[0][4].eval()
	h1_thumb_ip_z = scriptOp.inputs[0][5].eval()
	
    h1_thumb_cmc_x = scriptOp.inputs[0][6].eval()
    h1_thumb_cmc_y = scriptOp.inputs[0][7].eval()
    h1_thumb_cmc_z = scriptOp.inputs[0][8].eval()

	h1_wrist_x = scriptOp.inputs[0][9].eval()
	h1_wrist_y = scriptOp.inputs[0][10].eval()
	h1_wrist_z = scriptOp.inputs[0][11].eval()

	vect_wrist_cmc_x = h1_wrist_x - h1_thumb_cmc_x
	vect_wrist_cmc_y = h1_wrist_y - h1_thumb_cmc_y
	vect_wrist_cmc_z = h1_wrist_z - h1_thumb_cmc_z

	vect_ip_tip_x = h1_thumb_ip_x - h1_thumb_tip_x
	vect_ip_tip_y = h1_thumb_ip_y - h1_thumb_tip_y
	vect_ip_tip_z = h1_thumb_ip_z - h1_thumb_tip_z

	angle_between_2_vectors = math.acos(
		(vect_wrist_cmc_x * vect_ip_tip_x + vect_wrist_cmc_y * vect_ip_tip_y + vect_wrist_cmc_z * vect_ip_tip_z) /
		(math.sqrt(vect_wrist_cmc_x * vect_wrist_cmc_x + vect_wrist_cmc_y * vect_wrist_cmc_y + vect_wrist_cmc_z * vect_wrist_cmc_z)
    * math.sqrt(vect_ip_tip_x * vect_ip_tip_x + vect_ip_tip_y * vect_ip_tip_y + vect_ip_tip_z * vect_ip_tip_z))) / math.pi * 180

	chan_angle = scriptOp.appendChan(input_names[0])

	chan_angle[0] = angle_between_2_vectors
	return
