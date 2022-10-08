print(70*"*")
gp = float(input("Gaji Pokok: "))
jk = float(input("Total Jam Kerja: "))
print(70*"*")
tjg = gp*20/100
print(f'Gaji Pokok:\t\t\t\t\t\t{gp:,}')
print(f'Tunjangan [20% x Gaji Pokok]:\t\t\t\t{tjg:,}')
lm = 20000 * (jk-200) if jk >200 else 0
print(f'Uang Lembur [Jam Kerja>200 jam x Rp 20,000/jam]:\t{lm:,}')
print(f'Potongan Pajak [10%]:\t\t\t\t\t({(gp+tjg+lm)*0.10:,})')
print(70*"*")
print(f"Gaji [Gaji Pokok + Tunjangan + Uang Lembur - Pajak]:\t{gp+tjg+lm-((gp+tjg+lm)*0.10):,}")
print(70*"*")
