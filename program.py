import hr
import karyawan
import performansi

salary_employee = hr.GajiPegawai(1, "Segeng", 15000000 )
hourly_employee = hr.PegawaiJam(2, 'Bejo', 40, 15)
commission_employee = hr.KomisiPegawai(3, 'Parjo', 100000, 200000)
payroll_sistem = hr.SistemPenggajian()
payroll_sistem.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee
])

manager = karyawan.manager(1, 'Masageng', 300000)
secretary = karyawan.secretary(2, 'Masheru', 150000)
sales_guy = karyawan.salesperson(3, 'badroen', 100000)
factory_worker = karyawan.factoryworker(2, 'rendi', 40, 15)
employee = [manager,secretary,sales_guy,factory_worker]
productivity_system = performansi.Performansi()
productivity_system.track(employee,40)
payroll_sistem = hr.SistemPenggajian()
payroll_sistem.calculate_payroll(employees)
