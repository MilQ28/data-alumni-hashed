# py -m pip install faker

from faker import Faker
import random

fake = Faker('id_ID')

jurusan_list = [
    'Rekayasa Perangkat Lunak',
    'Teknik Komputer dan Jaringan',
    'Teknik Jaringan Akses dan Telekomunikasi',
    'Animasi',
]

pekerjaan_list = [
    "Software Engineer",
    "Frontend Developer",
    "Backend Developer",
    "Full Stack Developer",
    "Mobile Developer",
    "Game Developer",
    "Web Developer",
    "UI/UX Designer",
    "Graphic Designer",
    "Animator",
    "3D Artist",
    "Video Editor",
    "Content Creator",
    "YouTuber",
    "Streamer",
    "Digital Marketer",
    "SEO Specialist",
    "Data Analyst",
    "Data Scientist",
    "AI Engineer",
    "Machine Learning Engineer",
    "Cyber Security Analyst",
    "Network Engineer",
    "Cloud Engineer",
    "DevOps Engineer",
    "System Administrator",
    "Database Administrator",
    "IT Support",
    "Helpdesk",
    "QA Engineer",
    "Software Tester",
    "Product Manager",
    "Project Manager",
    "Business Analyst",
    "Entrepreneur",
    "Freelancer",
    "Photographer",
    "Videographer",
    "Illustrator",
    "Teacher",
    "Lecturer",
    "Private Tutor",
    "Accountant",
    "Financial Analyst",
    "Bank Employee",
    "HR Staff",
    "Recruiter",
    "Sales Executive",
    "Marketing Staff",
    "Customer Service",
    "Call Center Agent",
    "Office Administrator",
    "Secretary",
    "Architect",
    "Civil Engineer",
    "Mechanical Engineer",
    "Electrical Engineer",
    "Interior Designer",
    "Doctor",
    "Nurse",
    "Pharmacist",
    "Psychologist",
    "Chef",
    "Barista",
    "Waiter",
    "Hotel Staff",
    "Receptionist",
    "Tour Guide",
    "Pilot",
    "Flight Attendant",
    "Driver",
    "Logistics Staff",
    "Warehouse Staff",
    "Factory Operator",
    "Technician",
    "Electrician",
    "Mechanic",
    "Tailor",
    "Fashion Designer",
    "Makeup Artist",
    "Beauty Therapist",
    "Fitness Trainer",
    "Athlete",
    "Musician",
    "Singer",
    "Actor",
    "Police Officer",
    "Soldier",
    "Government Employee",
    "Lawyer",
    "Notary",
    "Journalist",
    "Writer",
    "Translator",
    "Researcher",
    "Farmer",
    "Fisherman",
    "Peternak",
    "Online Shop Owner",
    "Dropshipper",
    "E-Commerce Specialist",
]

perusahaan_list = [
    "Google",
    "Microsoft",
    "Apple",
    "Meta",
    "Amazon",
    "Netflix",
    "OpenAI",
    "NVIDIA",
    "Tesla",
    "SpaceX",
    "IBM",
    "Oracle",
    "Intel",
    "AMD",
    "Samsung",
    "Sony",
    "Huawei",
    "Xiaomi",
    "Tokopedia",
    "Shopee",
    "Bukalapak",
    "Blibli",
    "Lazada",
    "Gojek",
    "Grab",
    "Traveloka",
    "Tiket.com",
    "Ruangguru",
    "Zenius",
    "Telkom Indonesia",
    "Indosat",
    "XL Axiata",
    "Smartfren",
    "Biznet",
    "BCA",
    "BRI",
    "BNI",
    "Mandiri",
    "CIMB Niaga",
    "Danamon",
    "OVO",
    "DANA",
    "LinkAja",
    "J&T Express",
    "JNE",
    "SiCepat",
    "Pos Indonesia",
    "Pertamina",
    "PLN",
    "KAI",
    "Garuda Indonesia",
    "Lion Air",
    "Astra International",
    "Gudang Garam",
    "Djarum",
    "Indofood",
    "Mayora",
    "Unilever Indonesia",
    "Nestle Indonesia",
    "Honda",
    "Toyota",
    "Suzuki",
    "Yamaha",
    "Mitsubishi",
    "Hyundai",
    "Wuling",
    "Kompas Gramedia",
    "MNC Group",
    "Trans Media",
    "Metro TV",
    "CNN Indonesia",
    "Kompas TV",
    "Detik",
    "IDN Media",
    "Kumparan",
    "Freelance",
    "Startup Lokal",
    "Studio Animasi Nusantara",
    "Creative Digital Agency",
    "SMK Negeri 1",
    "Universitas Indonesia",
    "Universitas Gadjah Mada",
    "Institut Teknologi Bandung",
    "Rumah Sakit Umum Daerah",
    "Klinik Sehat Sentosa",
    "Cafe Kopi Kita",
    "PT Teknologi Masa Depan",
    "PT Maju Jaya Abadi",
    "CV Sumber Rezeki",
    "PT Digital Nusantara",
    "PT Cyber Security Indonesia",
    "PT Solusi AI Indonesia",
    "PT Kreatif Media Visual",
    "PT Infrastruktur Digital",
    "PT Cloud Network Indonesia",
    "PT Game Studio Asia",
    "PT Telekomunikasi Global",
    "PT Industri Otomotif Nasional",
]

def generate_nis():
    return str(random.randint(100000000, 999999999))

sql_values = []

for i in range(100):
    nis = generate_nis()
    nama = fake.name()
    angkatan = random.randint(2018, 2025)
    jurusan = random.choice(jurusan_list)

    username_email = nama.lower().replace(' ', '.')
    email = f"{username_email}{random.randint(1,999)}@gmail.com"

    no_hp = f"08{random.randint(1111111111, 9999999999)}"

    pekerjaan = random.choice(pekerjaan_list)
    perusahaan = random.choice(perusahaan_list)

    alamat = fake.address().replace('\n', ', ')

    sql = f"""(
'{nis}',
'{nama}',
{angkatan},
'{jurusan}',
'{email}',
'{no_hp}',
'{pekerjaan}',
'{perusahaan}',
'{alamat}'
)"""

    sql_values.append(sql)

final_sql = """
INSERT INTO `alumni`
(`nis`, `nama`, `angkatan`, `jurusan`, `email`, `no_hp`, `pekerjaan`, `perusahaan`, `alamat`)
VALUES
"""

final_sql += ",\n".join(sql_values) + ";"

with open("dummy_alumni.sql", "w", encoding="utf-8") as file:
    file.write(final_sql)

print("Berhasil generate 100 data alumni ke dummy_alumni.sql")