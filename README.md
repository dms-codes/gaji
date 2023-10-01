# Calculate Salary

This Python script calculates an employee's salary based on their basic salary (Gaji Pokok), total working hours (Total Jam Kerja), and tax deductions.

## Usage

1. Run the script:

   ```bash
   python script.py
   ```

2. The script will prompt you to enter the following information:
   - `Gaji Pokok`: Enter the basic salary.
   - `Total Jam Kerja`: Enter the total working hours.

3. The script will calculate the following components:
   - `Tunjangan`: 20% of the basic salary.
   - `Uang Lembur`: Overtime pay (Rp 20,000 per hour for hours worked beyond 200 hours).
   - `Potongan Pajak`: 10% tax deduction on the total income (basic salary + tunjangan + uang lembur).
   - `Gaji`: Net salary after tax deductions.

4. The script will display the calculated components and the final net salary.

5. Repeat the process for different employees or salary scenarios.

## Example

```bash
**********************************************************************
Gaji Pokok: 8000000
Total Jam Kerja: 220
**********************************************************************
Gaji Pokok:                        8,000,000.0
Tunjangan [20% x Gaji Pokok]:       1,600,000.0
Uang Lembur [Jam Kerja>200 jam x Rp 20,000/jam]:  4,000,000.0
Potongan Pajak [10%]:               (640,000.0)
**********************************************************************
Gaji [Gaji Pokok + Tunjangan + Uang Lembur - Pajak]:  11,960,000.0
**********************************************************************
```

## Customization

You can customize the tax rate, overtime pay rate, or any other parameters in the script as needed.

## License

This script is provided under the [MIT License](LICENSE).
```

Feel free to modify the script and README.md file to match your specific requirements or use case.
