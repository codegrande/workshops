from idautils import *
from idc import *

def find_xor_jz():
	heads = Heads(SegStart(ScreenEA()), SegEnd(ScreenEA()))
	results = []
	found_first = False
	previous = ""
	for i in heads:
		if (found_first and GetMnem(i) == "jz"):
			results.append(previous)
			results.append(i)
			Message("Found possibly anti-disassembly technique at 0x%x, instruction: %s\n" % (previous,GetDisasm(previous)))
			Message("Found possibly anti-disassembly technique at 0x%x, instruction: %s\n" % (i,GetDisasm(i)))
			found_first = False
		elif GetMnem(i) == "xor" and GetOpnd(i,0) == GetOpnd(i,1):
			found_first = True
		else: found_first = False
		previous = i
	return results

def find_jmp_ff():
	results = []
	ea = FindBinary(SegStart(ScreenEA()), SEARCH_DOWN, "EB FF")
	while(ea != BADADDR):
		if GetMnem(ea) == "jmp":
			results.append(ea)
			Message("Found possibly anti-disassembly technique at 0x%x, instruction: %s\n" % (ea,GetDisasm(ea)))
		ea = FindBinary(ea, SEARCH_NEXT, "EB FF")
	return results
		
def find_jz_jnz():
	results = []
	ea = FindBinary(SegStart(ScreenEA()), SEARCH_DOWN, "74 03 75 01")
	while(ea != BADADDR):
		if GetMnem(ea) == "jz":
			results.append(ea)
			results.append(ea+2)
			Message("Found possibly anti-disassembly technique at 0x%x, instruction: %s,%s\n" % (ea,GetDisasm(ea),GetDisasm(ea+2)))
		ea = FindBinary(ea, SEARCH_NEXT, "74 03 75 01")
	return results
		
def main():
	anti_da_locations = []
	anti_da_locations.extend(find_xor_jz())
	anti_da_locations.extend(find_jmp_ff())
	anti_da_locations.extend(find_jz_jnz())
	for i in anti_da_locations:
		SetColor(i, CIC_ITEM, 0x0000ff)
	
if __name__ == "__main__":
    main()