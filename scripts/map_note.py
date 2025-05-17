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

finger_2_midi = {
	# G调两指半音
	'G': {
		0b0000000001: 55,# G
		0b0000000011: 56,# G#
		0b0000000010: 57,# A
		0b0000000110: 58,# A#
		0b0000000100: 59,# B
		0b0000001000: 60,# C
		0b0000011000: 61,# C#
		0b0000010000: 62,# D
		0b0000110000: 63,# D#
		0b0000100000: 64,# E
		0b0001100000: 65,# F
		0b0001000000: 66,# F#
		0b0010000000: 67,# G
		0b0110000000: 68,# G#
		0b0100000000: 69,# A
		0b1100000000: 70,# A#
		0b1000000000: 71,# B
	},
	# C调两指半音
	'C': {
		0b0000000001: 60,# C
		0b0000000011: 61,# C#
		0b0000000010: 62,# D
		0b0000000110: 63,# D#
		0b0000000100: 64,# E
		0b0000001000: 65,# F
		0b0000011000: 66,# F#
		0b0000010000: 67,# G
		0b0000110000: 68,# G#
		0b0000100000: 69,# A
		0b0001100000: 70,# A#
		0b0001000000: 71,# B
		0b0010000000: 72,# C
		0b0110000000: 73,# C#
		0b0100000000: 74,# D
		0b1100000000: 75,# D#
		0b1000000000: 76,# E
	},
}
def onCook(scriptOp):
	scriptOp.clear()
	finger_sig = 0b0
	for i in range(10):
		input_val = scriptOp.inputs[0][i].eval()
		finger_sig += int(input_val) << i
	octaves = scriptOp.inputs[1]['octaves'].eval()
	midi = finger_2_midi['C'][finger_sig] if finger_sig in finger_2_midi['C'] else -1
	if midi != -1: midi += octaves * 12
	chan_note = scriptOp.appendChan('note')
	chan_note[0] = midi
	return
