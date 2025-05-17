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
	h2_wrist_x = scriptOp.inputs[0][0].eval()
	h2_wrist_y = scriptOp.inputs[0][1].eval()
	h1_wrist_y = scriptOp.inputs[0][3].eval()

	hand_size = scriptOp.inputs[1][0].eval()
	
	octave_scale = scriptOp.inputs[2][0].eval()

	octave_height = octave_scale * hand_size
	delta_y = h2_wrist_y - h1_wrist_y
	octaves = math.ceil(math.floor(math.fabs(delta_y) / (octave_height * 0.5)) / 2)
	if delta_y < 0: octaves = -octaves

	octave_top = (octaves + 0.5) * octave_height + h1_wrist_y
	octave_bottom = (octaves - 0.5) * octave_height + h1_wrist_y

	radio = (h2_wrist_y - octave_bottom) / (octave_top - octave_bottom)

	chan_wrist_x = scriptOp.appendChan('h2:wrist:x')
	chan_wrist_y = scriptOp.appendChan('h2:wrist:y')
	chan_octaves = scriptOp.appendChan('octaves')
	chan_radio = scriptOp.appendChan('radio')
	chan_octave_top_y = scriptOp.appendChan('octave_top:y')
	chan_octave_bottom_y = scriptOp.appendChan('octave_bottom:y')

	chan_wrist_x[0] = h2_wrist_x
	chan_wrist_y[0] = h2_wrist_y
	chan_octaves[0] = octaves
	chan_radio[0] = radio
	chan_octave_top_y[0] = octave_top
	chan_octave_bottom_y[0] = octave_bottom
	return
