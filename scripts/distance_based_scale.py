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
	p1x = scriptOp.inputs[0][0].eval()
	p1y = scriptOp.inputs[0][1].eval()
	p1z = scriptOp.inputs[0][2].eval()
	
	p2x = scriptOp.inputs[0][3].eval()
	p2y = scriptOp.inputs[0][4].eval()
	p2z = scriptOp.inputs[0][5].eval()

	hand_size = scriptOp.inputs[1][0].eval()
	
	min = scriptOp.inputs[2][0].eval()
	max = scriptOp.inputs[2][1].eval()

	mid_x = (p1x + p2x) / 2
	mid_y = (p1y + p2y) / 2
	mid_z = (p1z + p2z) / 2

	dir_x = p1x - p2x
	dir_y = p1y - p2y
	dir_z = p1z - p2z
	mag = math.sqrt(dir_x**2 + dir_y**2 + dir_z**2)
	dir_x = dir_x / mag
	dir_y = dir_y / mag
	dir_z = dir_z / mag

	range_min = min * hand_size
	range_max = max * hand_size

	if mag > range_max: mag = range_max
	if mag < range_min: mag = range_min

	scale = (mag - range_min) / (range_max - range_min)
	p1x = mid_x + dir_x * mag * 0.5
	p1y = mid_y + dir_y * mag * 0.5
	p1z = mid_z + dir_z * mag * 0.5
	p2x = mid_x - dir_x * mag * 0.5
	p2y = mid_y - dir_y * mag * 0.5
	p2z = mid_z - dir_z * mag * 0.5

	# debug(f'mid: ({mid_x:.2f}, {mid_y:.2f}, {mid_z:.2f}), dir: ({dir_x:.2f}, {dir_y:.2f}, {dir_z:.2f})\nrange_min: {range_min:.2f}  range_max: {range_max:.2f}')

	max_a_x = mid_x + dir_x * range_max * 0.5
	max_a_y = mid_y + dir_y * range_max * 0.5
	max_a_z = mid_z + dir_z * range_max * 0.5

	max_b_x = mid_x - dir_x * range_max * 0.5
	max_b_y = mid_y - dir_y * range_max * 0.5
	max_b_z = mid_z - dir_z * range_max * 0.5

	min_a_x = mid_x + dir_x * range_min * 0.5
	min_a_y = mid_y + dir_y * range_min * 0.5
	min_a_z = mid_z + dir_z * range_min * 0.5

	min_b_x = mid_x - dir_x * range_min * 0.5
	min_b_y = mid_y - dir_y * range_min * 0.5
	min_b_z = mid_z - dir_z * range_min * 0.5

	chan_p1_x = scriptOp.appendChan('p1:x')
	chan_p1_y = scriptOp.appendChan('p1:y')
	chan_p1_z = scriptOp.appendChan('p1:z')

	chan_p2_x = scriptOp.appendChan('p2:x')
	chan_p2_y = scriptOp.appendChan('p2:y')
	chan_p2_z = scriptOp.appendChan('p2:z')

	chan_max_a_x = scriptOp.appendChan('max_a:x')
	chan_max_a_y = scriptOp.appendChan('max_a:y')
	chan_max_a_z = scriptOp.appendChan('max_a:z')

	chan_max_b_x = scriptOp.appendChan('max_b:x')
	chan_max_b_y = scriptOp.appendChan('max_b:y')
	chan_max_b_z = scriptOp.appendChan('max_b:z')
	
	chan_min_a_x = scriptOp.appendChan('min_a:x')
	chan_min_a_y = scriptOp.appendChan('min_a:y')
	chan_min_a_z = scriptOp.appendChan('min_a:z')

	chan_min_b_x = scriptOp.appendChan('min_b:x')
	chan_min_b_y = scriptOp.appendChan('min_b:y')
	chan_min_b_z = scriptOp.appendChan('min_b:z')

	chan_scale = scriptOp.appendChan('scale')

	chan_p1_x[0] = p1x
	chan_p1_y[0] = p1y
	chan_p1_z[0] = p1z

	chan_p2_x[0] = p2x
	chan_p2_y[0] = p2y
	chan_p2_z[0] = p2z

	chan_max_a_x[0] = max_a_x
	chan_max_a_y[0] = max_a_y
	chan_max_a_z[0] = max_a_z

	chan_max_b_x[0] = max_b_x
	chan_max_b_y[0] = max_b_y
	chan_max_b_z[0] = max_b_z

	chan_min_a_x[0] = min_a_x
	chan_min_a_y[0] = min_a_y
	chan_min_a_z[0] = min_a_z

	chan_min_b_x[0] = min_b_x
	chan_min_b_y[0] = min_b_y
	chan_min_b_z[0] = min_b_z
	
	chan_scale[0] = scale
	return
