from pathlib import Path

p = Path("..\\disasm\\data\\graphics\\portraits\\portrait52.bin")
p.rename(p.with_name("portrait53.bin"))
p = Path("..\\disasm\\data\\graphics\\portraits\\portrait29.bin")
p.rename(p.with_name("portrait52.bin"))
p = Path("..\\disasm\\data\\graphics\\portraits\\new_claude.bin")
p.rename(p.with_name("portrait29.bin"))