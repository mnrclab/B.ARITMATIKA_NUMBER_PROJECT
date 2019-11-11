rasio_dulu = 1/4
tambahan_rasio_dulu = 1/2
rasio_sekarang = 1/7
tambahan_rasio_skrng = 19

UmurIbu = (rasio_dulu * tambahan_rasio_skrng + tambahan_rasio_dulu) / (rasio_dulu - rasio_sekarang )
print('Usia Ibu Sekarang: ', round(UmurIbu))

UmurAnak = rasio_sekarang * UmurIbu + tambahan_rasio_skrng
print('Usia Anak Sekarang: ', round(UmurAnak))

UmurMelahirkan = UmurIbu - UmurAnak
print('Usia Ibu Melahirkan: ', round(UmurMelahirkan))
