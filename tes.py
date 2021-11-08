repple = [800,900]
repple.append(950)
repple.append(970)
repple.append(980)

print(repple)

repple_dit = {}

repple_dit["2/21"] = repple[0]  
repple_dit["2/22"] = repple[1]
repple_dit["2/23"] = repple[2]
repple_dit["2/24"] = repple[3]
repple_dit["2/25"] = repple[4]

avr  = sum(list(repple_dit.values())) / len(list(repple_dit.values()))

print(avr)