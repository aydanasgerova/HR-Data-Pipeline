import pandas as pd
from sqlalchemy import create_engine, text

# 1. Docker-dəki bazaya qoşulma xətti
# admin = istifadəçi adı, 123 = parol
engine = create_engine('postgresql://admin:123@localhost:5432/hr_db')

try:
    # 2. 'hr' adlı xüsusi yer (schema) yaradırıq
    with engine.connect() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS hr;"))
        conn.commit()
        print("--- 'hr' sxemi hazırlandı ---")

    # 3. Sənin o 3 faylın
    fayllar = ['employees', 'departments', 'countries']

    for fayl in fayllar:
        # Faylı oxuyuruq
        df = pd.read_csv(f'{fayl}.csv')
        
        # Məlumatı 'hr' sxeminin içinə göndəririk
        df.to_sql(fayl, engine, schema='hr', if_exists='replace', index=False)
        print(f"Uğurla yükləndi: {fayl}")

    print("\nTEBRİKLER! Bütün məlumatlar artıq bazadadır! 🎉")

except Exception as e:
    print(f"Xəta baş verdi: {e}")
    print("\nİpucu: Docker-in işlədiyindən və kitabxanaların yüklü olduğundan əmin ol.")