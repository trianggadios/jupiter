import matplotlib.pyplot as plt

import random

def kalkukasi_turunan(persamaan, berapa_kali):
    # 2x2 + 2x -> 2x2+2x
    persamaan = persamaan.replace(' ', '')
    
    # 2X2 ... -> 2x2
    persamaan = persamaan.lower()

    # 2x+1 -> ['2x', '1']
    list_persamaan = persamaan.split('+')

    berapa_kali_penurunan = int(berapa_kali)

    # ['2', '', '']
    hasil_turunan = []

    for _ in range(berapa_kali_penurunan):
        hasil_turunan_ke = []
        for bilangan in list_persamaan:
            if 'x' in bilangan and len(bilangan) > 1:
                bilangan_2 = bilangan[-1]
                
                if bilangan_2 == 'x':
                    hasil_turunan_ke.append(bilangan.split('x')[0])
                else:
                    bilangan_1 = bilangan.split('x')[0]
                    bilangan_2 = bilangan.split('x')[1]
                    
                    if bilangan_1 == '':
                        bilangan_1 = '1'
                    
                    hasil_bilangan_1 = int(bilangan_1) * int(bilangan_2)
                    hasil_bilangan_2 = int(bilangan_2) - 1
                    
                    if hasil_bilangan_2 == 1:
                        hasil_turunan_ke.append(f"{hasil_bilangan_1}x")
                    else:
                        hasil_turunan_ke.append(f"{hasil_bilangan_1}x{hasil_bilangan_2}")
            elif 'x' in bilangan and len(bilangan) == 1:
                hasil_turunan_ke.append('1')
            else:
                continue
            
        hasil = ' + '.join(hasil_turunan_ke)
        list_persamaan = hasil_turunan_ke
        hasil_turunan.append(hasil)
        
    msgreply = ""
    for i, turunan in enumerate(hasil_turunan):
        msgreply += f"Hasil Turunan Ke-{i+1}: {turunan}\n"
    buka_plot()
    return msgreply

def buka_plot():
    data = [random.random() for _ in range(100)]
    plt.plot(data)
    plt.ylabel('some numbers')
    plt.show(block=False)