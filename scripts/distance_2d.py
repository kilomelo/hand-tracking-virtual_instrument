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
	
	# one line version of the above
	# to get next 2 inputs
	p1x = scriptOp.inputs[0][0].eval()
	p1y = scriptOp.inputs[0][1].eval()
	# p1z = scriptOp.inputs[0][2].eval()
	
	p2x = scriptOp.inputs[0][3].eval()
	p2y = scriptOp.inputs[0][4].eval()
	# p2z = scriptOp.inputs[0][5].eval()

	# Calculate midpoint
	mid_x = (p1x + p2x) / 2
	mid_y = (p1y + p2y) / 2
	# mid_z = (p1z + p2z) / 2

	# Calculate distance between the two points
	# distance = math.sqrt((p2x - p1x)**2 + (p2y - p1y)**2 + (p2z - p1z)**2)
	distance = math.sqrt((p2x - p1x)**2 + (p2y - p1y)**2)
	

	dist = scriptOp.appendChan('distance')

	# Assign out channels
	dist[0] = distance
	return
