import time
import random

def delay_print(text, speed=0.05):
    """Fungsi untuk mencetak teks dengan efek kecepatan"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()
    time.sleep(0.5)  # Jeda 0.5 detik setelah setiap teks untuk efek horror

def show_ascii_sword():
    """Menampilkan ASCII art pedang untuk kemenangan"""
    sword = """
    
         ⚔
        __|__
       / ||| \\
      |  |||  |
      |  |||  |
       \\ ||| /
        ‾¹‾¹‾
        
    """
    print(sword)

def show_ascii_skull():
    """Menampilikan ASCII art tengkorak untuk kekalahan"""
    skull = """
    
      ☠☠☠
     ☠☠☠☠☠
    ☠☠☠☠☠☠☠
    ☠ ☠ ☠ ☠ ☠
    ☠☠☠☠☠☠☠
     ☠☠☠☠☠
      ☠☠☠
      
    """
    print(skull)

def show_health(nyawa):
    """Menampilkan status kesehatan pemain"""
    print("\n" + "-"*70)
    bar_length = 30
    filled = int((nyawa / 100) * bar_length)
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"KESEHATAN: {nyawa}/100 [{bar}]")
    print("-"*70 + "\n")

def intro_game():
    """Pengenalan game dan cerita awal"""
    print("\n" + "="*70)
    print(" "*15 + "SILENT HILL: THE LOST SOUL")
    print("="*70 + "\n")
    
    delay_print("Angin dingin berhembus di sekitarmu...", 0.03)
    time.sleep(1)
    delay_print("Kabut tebal menutupi pandanganmu...", 0.03)
    time.sleep(1)
    delay_print("Kota gelap ini... adalah Silent Hill", 0.03)
    time.sleep(1.5)

def play_game(nama):
    """Main game logic yang dapat di-restart"""
    nyawa = 100  # Variabel nyawa pemain
    
    intro_game()
    
    show_health(nyawa)  # Menampilkan nyawa awal
    
    print(f"\n*Cerita dimulai*\n")
    delay_print(f"Namamu adalah {nama}. Istrimu, Mary, telah hilang selama enam bulan.", 0.04)
    time.sleep(1)
    delay_print("Mary adalah segalanya bagimu... istri tercinta yang pergi untuk berkonsultasi kesehatan.", 0.04)
    time.sleep(1)
    delay_print("Dia datang ke Silent Hill karena harus menjalani perawatan medis di Alchemilla Hospital.", 0.04)
    time.sleep(1)
    delay_print("Namun, sejak saat itu, dia tidak pernah kembali...", 0.04)
    time.sleep(1.5)
    
    delay_print("Investigasi pribadi membawamu ke Silent Hill - sebuah kota yang", 0.04)
    delay_print("sepenuhnya ditakuti oleh orang-orang lokal dan penuh dengan misteri.", 0.04)
    time.sleep(1)
    
    # ===== MEMASUKI SILENT HILL =====
    print("\n" + "-"*70)
    delay_print(">>> Kamu melangkah masuk ke kota Silent Hill <<<", 0.05)
    print("-"*70 + "\n")
    
    time.sleep(1)
    delay_print("Suara-suara aneh mengelilingimu...", 0.04)
    time.sleep(0.5)
    delay_print("Bangunan-bangunan tua yang angker berdiri kokoh.", 0.04)
    time.sleep(0.5)
    delay_print("Jalanan sangat sepi dan gelap.", 0.04)
    time.sleep(1)
    
    delay_print("Tiba-tiba... jarak jauh kamu melihat sosok perempuan!", 0.04)
    time.sleep(0.5)
    delay_print("Itu Mary? Tidak... tapi wajahnya terlihat mirip.", 0.04)
    time.sleep(0.5)
    delay_print("Sosok itu hilang dalam kabut...", 0.04)
    time.sleep(1.5)
    
    delay_print("\n*** HALUSINASI KE-1: Kamu melihat bayangan Mary ***", 0.04)
    delay_print("Tapi kepribadiannya berbeda... lebih gelap, lebih menakutkan.", 0.04)
    time.sleep(1.5)
    
    # ===== MEMASUKI ALCHEMILLA HOSPITAL =====
    print("\n" + "-"*70)
    delay_print(">>> Kamu berjalan ke Alchemilla Hospital <<<", 0.05)
    print("-"*70 + "\n")
    
    time.sleep(1)
    delay_print("Rumah sakit ini sangat besar dan penuh dengan misteri.", 0.04)
    time.sleep(0.5)
    delay_print("Pintu depannya terbuka lebar, seolah mengundangmu masuk.", 0.04)
    time.sleep(0.5)
    delay_print("Kamu memasuki lobby rumah sakit yang gelap dan dingin.", 0.04)
    time.sleep(1)
    
    delay_print("Debu berserakan di mana-mana, terlihat tidak ada yang merawat", 0.04)
    delay_print("tempat ini sejak lama.", 0.04)
    time.sleep(1)
    
    # ===== BERTEMU DR. MICHAEL KAUFMAN =====
    print("\n" + "="*70)
    print(" "*20 + "! TIBA-TIBA !")
    print("="*70 + "\n")
    
    delay_print("Suara langkah kaki terdengar...", 0.04)
    time.sleep(0.5)
    delay_print("Seorang dokter dengan wajah pucat keluar dari kegelapan.", 0.04)
    time.sleep(1)
    delay_print("\"Siapa kau? Mengapa kau ada di sini?\" tanyanya dengan nada", 0.04)
    delay_print("yang mencurigakan.", 0.04)
    time.sleep(1)
    
    delay_print(f"\"Namaku {nama}. Aku mencari istri ku, Mary. Dia datang ke rumah sakit ini enam bulan lalu dan tidak pernah kembali,\"", 0.04)
    delay_print("katamu dengan suara yang tertahan.", 0.04)
    time.sleep(1)
    
    delay_print("Dokter itu menghela napas keras dan memperkenalkan dirinya.", 0.04)
    delay_print("\"Aku Dr. Michael Kaufman. Aku adalah kepala medis di rumah", 0.04)
    delay_print("sakit ini...\"", 0.04)
    time.sleep(1.5)
    
    # Dokter menceritakan sejarah
    print("\n" + "-"*70)
    print(" "*15 + "~~ Dr. Kaufman Menceritakan Sejarah Kota ~~")
    print("-"*70 + "\n")
    
    delay_print("\"Kota Silent Hill memiliki sejarah yang sangat gelap.\"", 0.04)
    time.sleep(0.5)
    delay_print("\"Beberapa tahun yang lalu, ada insiden yang mengubah semua.\"", 0.04)
    time.sleep(1)
    delay_print("\"Seorang anak perempuan bernama Alessa Gillespie...\"", 0.04)
    time.sleep(0.5)
    delay_print("\"...dia dipukul dan dibakar hidup-hidup oleh penduduk kota.\"", 0.04)
    time.sleep(1)
    
    delay_print("\"Sejak saat itu, kota ini dikutuk. Monster-monster aneh", 0.04)
    delay_print("mulai bermunculan. Banyak orang yang hilang...\"", 0.04)
    time.sleep(1.5)
    
    delay_print("\"Mary... istri mu... ada kemungkinan dia menjadi", 0.04)
    delay_print("korban kutukan yang menimpa kota ini.\"", 0.04)
    time.sleep(1)
    
    # ===== BERTEMU SUSTER LISA GARLAND =====
    print("\n" + "="*70)
    print(" "*20 + "! SUSTER MUNCUL !")
    print("="*70 + "\n")
    
    delay_print("Seorang suster dengan rambut panjang muncul dari koridor", 0.04)
    delay_print("samping dengan wajah yang ketakutan.", 0.04)
    time.sleep(1)
    
    delay_print("\"Dr. Kaufman! Ada... ada sesuatu yang bergerak di basement!\"", 0.04)
    time.sleep(1)
    
    delay_print("Dr. Kaufman melihat ke arahmu. \"Ini Suster Lisa Garland.\"", 0.04)
    time.sleep(0.5)
    delay_print("\"Lisa, ceritakan kepada tamu kita tentang yang terjadi di", 0.04)
    delay_print("rumah sakit ini.\"", 0.04)
    time.sleep(1.5)
    
    delay_print("Lisa mulai bercerita dengan suara yang gemetar...", 0.04)
    time.sleep(0.5)
    delay_print("\"Ada banyak pasien yang meninggal di sini secara misterius.\"", 0.04)
    time.sleep(0.5)
    delay_print("\"Kami tidak tahu penyebabnya. Tapi aku yakin...\"", 0.04)
    time.sleep(0.5)
    delay_print("\"...ada sesuatu yang supernatural yang terjadi di sini.\"", 0.04)
    time.sleep(1.5)
    
    # ===== EKSPLORASI RUMAH SAKIT =====
    print("\n" + "="*70)
    print(" "*20 + "! MULAI EKSPLORASI !")
    print("="*70 + "\n")
    
    delay_print("Setelah mendengarkan cerita mereka, kamu memutuskan untuk", 0.04)
    delay_print("menjelajahi lebih dalam rumah sakit ini.", 0.04)
    time.sleep(1)
    
    delay_print("Mungkin ada barang bukti yang bisa membantumu bertemu Mary...", 0.04)
    time.sleep(1.5)
    
    delay_print("\"Hati-hati,\" kata Dr. Kaufman dengan nada serius.", 0.04)
    time.sleep(0.5)
    delay_print("\"Rumah sakit ini penuh dengan jebakan dan monster.\"", 0.04)
    time.sleep(1.5)
    
    # ===== PILIHAN UTAMA =====
    print("\n" + "="*70)
    print(" "*20 + "!!! PILIHAN PENTING !!!")
    print("="*70 + "\n")
    
    delay_print("Saat kamu menjelajahi koridor rumah sakit, kamu menemukan", 0.04)
    delay_print("dua jalan yang mengarah ke arah berbeda:", 0.04)
    time.sleep(1)
    
    print("\n[1] Naik ke LANTAI RAHASIA 4 (Dunia Nightmare penuh monster)")
    print("[2] Turun ke BASEMENT (Ruang rahasia misterius)")
    
    pilihan = input("\nPilihan mu (1 atau 2): ").strip()
    
    # ===== LANTAI RAHASIA 4 (NIGHTMARE WORLD) =====
    if pilihan == "1":
        print("\n" + "="*70)
        print(" "*15 + ">>> LANTAI RAHASIA 4 - NIGHTMARE WORLD <<<")
        print("="*70 + "\n")
        
        time.sleep(1)
        delay_print("Kamu memilih untuk naik ke lantai rahasia 4...", 0.05)
        time.sleep(1)
        
        delay_print("Tangga melengkung di depanmu, cahaya merah terang menerangi", 0.04)
        delay_print("jalan tersebut.", 0.04)
        time.sleep(1)
        
        delay_print("Saat kamu mencapai lantai 4, semuanya berubah...", 0.04)
        time.sleep(0.5)
        delay_print("Realitas terdistorsi, dinding bergerak sendiri.", 0.04)
        time.sleep(1)
        
        delay_print("INI ADALAH DIMENSI LAIN... DUNIA NIGHTMARE!", 0.05)
        time.sleep(1)
        
        delay_print("\n*** HALUSINASI KE-2: Mary muncul lagi ***", 0.04)
        delay_print("Tapi kali ini dia berbicara dengan suara yang menyeramkan:", 0.04)
        delay_print("\"Mengapa kau mencilaka ku? Mengapa tidak biarkan aku tenang?\"", 0.04)
        delay_print("Sosoknya berubah menjadi monster dengan leher panjang dan", 0.04)
        delay_print("mata yang kosong.", 0.04)
        time.sleep(2)
        
        print("\n" + "="*70)
        print(" "*15 + "!!! PERTARUNGAN MELAWAN MONSTER !!!")
        print("="*70 + "\n")
        
        show_health(nyawa)
        
        delay_print("Monster-monster bergemuruh keluar dari dinding!", 0.05)
        time.sleep(1)
        
        delay_print("Kamu melihat berbagai monster mengerikan:", 0.04)
        time.sleep(0.5)
        delay_print("- BORN: Makhluk tanpa daging, hanya tulang dan organ", 0.04)
        time.sleep(0.5)
        delay_print("- PRISONER: Pria yang dikurung dalam rantai", 0.04)
        time.sleep(0.5)
        delay_print("- ABSTRACT DADDY: Bentuk yang tidak jelas dan menakutkan", 0.04)
        time.sleep(1.5)
        
        pertarungan = input("\nApakah kamu akan melawan monster-monster ini? (ya/tidak): ").strip().lower()
        
        if pertarungan == "ya":
            delay_print("\n*** PERTARUNGAN SENGIT ***", 0.05)
            time.sleep(1)
            
            # Round 1 dengan randomness
            delay_print("\n[ROUND 1] Pertarungan dimulai!", 0.04)
            delay_print("Kamu mengambil pistol dari tas ranselmu...", 0.04)
            time.sleep(0.5)
            delay_print("BANG! BANG! BANG!", 0.05)
            time.sleep(0.5)
            
            # Random outcome untuk Round 1
            round1_result = random.choice([1, 2])  # 1 = Hit, 2 = Kena Counterattack
            if round1_result == 1:
                delay_print("Monster BORN mencoba serang tapi kamu berhasil menghindar!", 0.04)
                delay_print("Serangan mu kena mengenai monster itu!", 0.04)
                time.sleep(1)
            else:
                delay_print("Monster BORN menyerang balik dengan ganas!", 0.04)
                delay_print("Cakar tajamnya menggores lenganmu...", 0.04)
                nyawa -= 20
                delay_print(f"Nyawamu berkurang! Sisa nyawa: {nyawa}/100", 0.04)
                show_health(nyawa)
                
                if nyawa <= 0:
                    show_ascii_skull()
                    delay_print("\n*** KAMU TERBUNUH OLEH MONSTER ***", 0.05)
                    time.sleep(1)
                    delay_print("Semuanya menjadi gelap...", 0.04)
                    time.sleep(0.5)
                    delay_print("Kamu terjatuh ke lantai, darah mengalir dari tubuhmu.", 0.04)
                    time.sleep(1)
                    delay_print("Dunia ini tidak akan pernah melepasmu...", 0.04)
                    time.sleep(1.5)
                    delay_print("\n!!! GAME OVER !!!", 0.05)
                    delay_print(f"Kamu telah mati setelah perjalanan yang singkat, {nama}...", 0.04)
                    time.sleep(1.5)
                    return False  # Restart game
            
            # Round 2 dengan randomness
            time.sleep(1)
            delay_print("\n[ROUND 2] Kamu bangkit kembali!", 0.04)
            delay_print("Dengan semangat terakhirmu, kamu terus menembak...", 0.04)
            time.sleep(0.5)
            
            round2_result = random.choice([1, 2])  # 1 = Dodge, 2 = Terkena serangan
            if round2_result == 1:
                delay_print("Kamu berhasil menghindari serangan monster PRISONER!", 0.04)
                delay_print("Rantainya hanya menyeret-seret lantai...", 0.04)
                time.sleep(1)
            else:
                delay_print("Monster PRISONER bergerak cepat dan menyergap!", 0.04)
                delay_print("Rantainya membungkus tubuhmu!", 0.04)
                nyawa -= 20
                delay_print(f"Nyawamu berkurang! Sisa nyawa: {nyawa}/100", 0.04)
                show_health(nyawa)
                
                if nyawa <= 0:
                    show_ascii_skull()
                    delay_print("\n*** KAMU TERBUNUH OLEH MONSTER ***", 0.05)
                    time.sleep(1)
                    delay_print("Rantai mencekik lehermu dengan kuat...", 0.04)
                    time.sleep(0.5)
                    delay_print("Pandanganmu menjadi gelap dan dingin...", 0.04)
                    time.sleep(1)
                    delay_print("\n!!! GAME OVER !!!", 0.05)
                    delay_print(f"Perjalananmu berakhir di sini, {nama}...", 0.04)
                    time.sleep(1.5)
                    return False  # Restart game
            
            # Round 3 dengan randomness
            time.sleep(1)
            delay_print("\n[ROUND 3] Pertarungan final!", 0.04)
            delay_print("Abstract Daddy muncul dengan bentuknya yang menakutkan!", 0.04)
            time.sleep(0.5)
            delay_print("Kamu menembaknya berkali-kali, tetapi dia tetap menyerang!", 0.04)
            time.sleep(1)
            
            round3_result = random.choice([1, 2, 3])  # Hasil random untuk round terakhir
            if round3_result == 1:
                delay_print("Dengan keberuntungan terakhirmu, kamu berhasil!", 0.04)
                delay_print("Abstract Daddy terhempas ke dinding dan tidak bergerak!", 0.04)
                time.sleep(1)
            elif round3_result == 2:
                delay_print("Cakar panjangnya mencakar badanmu!", 0.04)
                nyawa -= 20
                delay_print(f"Nyawamu berkurang! Sisa nyawa: {nyawa}/100", 0.04)
                show_health(nyawa)
                
                if nyawa <= 0:
                    show_ascii_skull()
                    delay_print("\n*** KAMU TERBUNUH OLEH MONSTER ***", 0.05)
                    time.sleep(1)
                    delay_print("Dunia gelap mengelilingimu selamanya...", 0.04)
                    time.sleep(1)
                    delay_print("\n!!! GAME OVER !!!", 0.05)
                    delay_print(f"Perjalananmu mencari Mary berakhir dengan tragis, {nama}...", 0.04)
                    time.sleep(1.5)
                    return False  # Restart game
            else:
                delay_print("Kamu menembak dengan presisi sempurna!", 0.04)
                delay_print("Monster itu jatuh terpukul mundur!", 0.04)
                time.sleep(1)
            
            # Survived
            time.sleep(1)
            show_ascii_sword()
            delay_print("Kamu selamat dari pertarungan yang sengit!", 0.04)
            delay_print("Akhirnya, kamu bisa kabur dari nightmare world.", 0.04)
            time.sleep(0.5)
            delay_print("Tetapi Mary masih belum ditemukan...", 0.04)
            time.sleep(1)
            
            print("\n" + "="*70)
            print(" "*20 + "~~ ENDING: PERTARUNGAN ~~")
            print("="*70 + "\n")
            
            show_health(nyawa)
            
            delay_print("Kamu keluar dari lantai 4 dengan luka-luka yang dalam.", 0.04)
            time.sleep(0.5)
            delay_print("Petunjuk tentang Mary masih belum jelas...", 0.04)
            time.sleep(0.5)
            delay_print("Tapi kau tahu bahwa istrimu masih ada di tempat ini.", 0.04)
            time.sleep(1)
            delay_print("Pencarian mu belum berakhir...", 0.04)
            time.sleep(1)
            return True  # Game continues
            
        else:
            delay_print("\n*** KAMU MELARIKAN DIRI ***", 0.05)
            time.sleep(1)
            
            delay_print("Kamu berlari secepat mungkin turun dari lantai 4!", 0.04)
            time.sleep(0.5)
            delay_print("Monster-monster itu mengejar, tapi tidak bisa menyusulmu.", 0.04)
            time.sleep(1)
            
            print("\n" + "="*70)
            print(" "*20 + "~~ ENDING: PELARIAN ~~")
            print("="*70 + "\n")
            
            show_health(nyawa)
            
            delay_print("Kamu berhasil keluar dengan selamat, tapi hatimu penuh", 0.04)
            delay_print("dengan rasa takut dan kekhawatiran tentang keselamatan istrimu.", 0.04)
            time.sleep(1)
            delay_print("Mary masih hilang, dan misteri semakin dalam.", 0.04)
            time.sleep(1)
            return True  # Game continues
    
    # ===== BASEMENT (RUANG RAHASIA) =====
    elif pilihan == "2":
        print("\n" + "="*70)
        print(" "*15 + ">>> BASEMENT - RUANG RAHASIA <<<")
        print("="*70 + "\n")
        
        show_health(nyawa)
        
        time.sleep(1)
        delay_print("Kamu memilih untuk turun ke basement...", 0.05)
        time.sleep(1)
        
        delay_print("Tangga turun ke kegelapan yang mendalam.", 0.04)
        time.sleep(0.5)
        delay_print("Bau busuk menyebar di udara.", 0.04)
        time.sleep(1)
        
        delay_print("Lampunya berpendar samar, menciptakan bayangan aneh.", 0.04)
        time.sleep(1)
        
        delay_print("Kamu sampai di basement yang luas dan penuh dengan", 0.04)
        delay_print("ruang-ruang misterius.", 0.04)
        time.sleep(1.5)
        
        delay_print("Tiba-tiba, kamu menemukan pintu besi besar yang dikunci", 0.04)
        delay_print("dengan rapi dan penuh dengan simbol-simbol aneh.", 0.04)
        time.sleep(1)
        
        delay_print("Lampu di atas pintu itu bersinar merah membara.", 0.04)
        time.sleep(1)
        
        print("\n" + "="*70)
        print(" "*15 + "!!! RUANG RAHASIA DITEMUKAN !!!")
        print("="*70 + "\n")
        
        delay_print("Dengan kesulitan, kamu membuka pintu itu...", 0.05)
        time.sleep(1)
        
        delay_print("Di dalam ruangan itu, kamu melihat...", 0.04)
        time.sleep(0.5)
        delay_print("ALESSA GILLESPIE!", 0.05)
        time.sleep(1)
        
        delay_print("\n*** HALUSINASI KE-3: Alessa berbicara ***", 0.04)
        delay_print("\"Selamat datang... kami telah menunggu kedatangan mu.\"", 0.04)
        time.sleep(1)
        
        delay_print("Suaranya aneh, seolah ribuan suara berbicara bersamaan.", 0.04)
        time.sleep(1)
        
        print("\n" + "-"*70)
        print(" "*15 + "~~ Alessa Menceritakan Kebenaran ~~")
        print("-"*70 + "\n")
        
        delay_print("\"Mary bukanlah gadis biasa. Dia adalah perpanjangan dari", 0.04)
        delay_print("diriku.\"", 0.04)
        time.sleep(1)
        
        delay_print("\"Kutukan yang menghancurkan kota ini berasal dari", 0.04)
        delay_print("penderitaanku.\"", 0.04)
        time.sleep(1)
        
        delay_print("\"Mary adalah manifestasi dari sisi baik dalam diriku,", 0.04)
        delay_print("sementara sisi jahatku menciptakan monster-monster itu.\"", 0.04)
        time.sleep(1.5)
        
        delay_print("\"Jika kamu ingin menemukan Mary yang sebenarnya...\"", 0.04)
        time.sleep(0.5)
        delay_print("\"...kamu harus memilih untuk melindungi atau mengorbankan", 0.04)
        delay_print("diriku.\"", 0.04)
        time.sleep(1.5)
        
        print("\n" + "="*70)
        print(" "*20 + "!!! PILIHAN AKHIR !!!")
        print("="*70 + "\n")
        
        pilihan_akhir = input("Apakah kamu akan melindungi Alessa? (ya/tidak): ").strip().lower()
        
        if pilihan_akhir == "ya":
            print("\n" + "="*70)
            print(" "*20 + "~~ ENDING: PENEBUSAN ~~")
            print("="*70 + "\n")
            
            show_ascii_sword()
            delay_print("Kamu menetapkan hati untuk melindungi Alessa...", 0.04)
            time.sleep(1)
            
            delay_print("Cahaya berkembang di ruangan itu.", 0.04)
            time.sleep(0.5)
            delay_print("Kutukan perlahan-lahan melepaskan jamáannya atas kota.", 0.04)
            time.sleep(1)
            
            delay_print("Alessa dan Mary menyatu dalam cahaya putih.", 0.04)
            time.sleep(1)
            
            delay_print("Mary akhirnya muncul di depanmu, dengan wajah yang", 0.04)
            delay_print("damai dan tersenyum.", 0.04)
            time.sleep(1)
            
            delay_print("\"Terima kasih telah menyelamatkanku...\"", 0.04)
            delay_print("kata Mary dengan lembut.", 0.04)
            time.sleep(1)
            
            delay_print("\nKalian berdua meninggalkan Silent Hill bersama-sama.", 0.04)
            delay_print("Kota itu perlahan-lahan menyembuh dari kutukannya.", 0.04)
            time.sleep(1)
            
            delay_print("\n*** GOOD ENDING: PENEBUSAN DAN PERSAHABATAN ***", 0.05)
            
        else:
            print("\n" + "="*70)
            print(" "*20 + "~~ ENDING: PENGORBANAN ~~")
            print("="*70 + "\n")
            
            show_ascii_skull()
            delay_print("Kamu memilih untuk mengorbankan Alessa...", 0.04)
            time.sleep(1)
            
            delay_print("Alessa tersenyum keputusan-putusanmu adalah kekal.", 0.04)
            time.sleep(0.5)
            delay_print("Dia bersatu dengan dark version-nya.", 0.04)
            time.sleep(1)
            
            delay_print("Mary tiba di hadapanmu, tapi dengan energi suram.", 0.04)
            time.sleep(0.5)
            delay_print("Dia bukan lagi Mary yang dulu...", 0.04)
            time.sleep(1)
            
            delay_print("\"Terima kasih telah memilih aku...\"", 0.04)
            delay_print("kata Mary dengan nada yang dingin dan menakutkan.", 0.04)
            time.sleep(1)
            
            delay_print("Kamu meninggalkan Silent Hill dengan Mary,", 0.04)
            delay_print("tapi dalam hatimu adalah kegelapan.", 0.04)
            time.sleep(1)
            
            delay_print("\n*** BAD ENDING: HARGA DARI KEABUAN ***", 0.05)
    
    else:
        delay_print("Pilihan tidak valid. Game berakhir.", 0.04)
        return True
    
    # ===== FINAL MESSAGE =====
    print("\n" + "="*70)
    print(" "*15 + "~~ TERIMA KASIH TELAH BERMAIN ~~")
    print("="*70)
    show_health(nyawa)
    delay_print(f"Sampai jumpa lagi, {nama}... semoga kau dapat menemukan Mary...", 0.05)
    print("Mimpi buruk baru menunggu di Silent Hill...\n")
    return True

def game_utama():
    """Fungsi utama game dengan loop untuk "Play Again" feature"""
    nama = "Harry"  # Nama pemain utama adalah Harry
    
    while True:
        print("--- SELAMAT DATANG KE DUNIA HORROR ADVENTURE ---\n")
        
        # Main game loop
        result = play_game(nama)
        
        # Tanya "Play Again?" setelah game selesai
        print("\n" + "="*70)
        delay_print(">>> APAKAH KAMU INGIN BERMAIN LAGI? <<<", 0.04)
        print("="*70)
        
        play_again = input("\nMain lagi? (y/n): ").strip().lower()
        
        if play_again == "y" or play_again == "ya":
            print("\n")
            continue
        else:
            delay_print("\nTerima kasih telah bermain Silent Hill: The Lost Soul...", 0.04)
            time.sleep(0.5)
            delay_print("Sampai jumpa di dunia yang lebih gelap lagi...", 0.04)
            time.sleep(1)
            break

if __name__ == "__main__":
    game_utama()
