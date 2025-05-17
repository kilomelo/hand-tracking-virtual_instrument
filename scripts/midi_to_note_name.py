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
	scriptOp.clear()

	midi = scriptOp.inputs[0][0].eval()
	note_name = midi_to_pitch(int(midi))
	op('note_name').par.text = note_name
	return

def midi_to_pitch(midi_number: int) -> str:
    """将MIDI编号转换为音高字符串（如C4、A#3）"""
    # 音名数组定义（包含12个半音）
    note_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    
    # 输入验证
    if not (0 <= midi_number <= 127): return ''
    
    # 计算音名索引和八度数[1,6](@ref)
    note_index = midi_number % 12
    octave = (midi_number // 12) - 1  # 八度计算公式
    
    return f"{note_names[note_index]}{octave}"