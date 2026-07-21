"""
Text Prediction Model
Modul untuk memprediksi teks selanjutnya menggunakan Markov Chain
"""

import json
from collections import defaultdict, Counter
from typing import List, Dict, Tuple


class TextPredictor:
    """
    Kelas untuk memprediksi teks selanjutnya menggunakan Markov Chain.
    Model ini belajar dari teks pelatihan dan memprediksi kata berikutnya
    berdasarkan urutan kata sebelumnya.
    """
    
    def __init__(self, order: int = 2):
        """
        Inisialisasi TextPredictor.
        
        Args:
            order (int): Jumlah kata sebelumnya yang digunakan untuk prediksi.
                        Default: 2 (bigram)
        """
        self.order = order
        self.transitions = defaultdict(Counter)
        self.is_trained = False
    
    def train(self, text: str) -> None:
        """
        Melatih model dengan teks pelatihan.
        
        Args:
            text (str): Teks untuk melatih model
        """
        # Bersihkan dan tokenisasi teks
        words = text.lower().split()
        
        # Buat transisi dari kata ke kata berikutnya
        for i in range(len(words) - self.order):
            # Ambil urutan kata
            context = tuple(words[i:i + self.order])
            # Ambil kata berikutnya
            next_word = words[i + self.order]
            # Tambahkan ke transitions
            self.transitions[context][next_word] += 1
        
        self.is_trained = True
    
    def predict_next_word(self, context: str, top_n: int = 5) -> List[Tuple[str, float]]:
        """
        Memprediksi kata berikutnya berdasarkan konteks.
        
        Args:
            context (str): Konteks teks untuk prediksi
            top_n (int): Jumlah prediksi teratas yang dikembalikan
        
        Returns:
            List[Tuple[str, float]]: Daftar (kata, probabilitas) terurut
        """
        if not self.is_trained:
            raise ValueError("Model belum dilatih. Jalankan train() terlebih dahulu.")
        
        # Tokenisasi konteks
        words = context.lower().split()
        
        # Pastikan konteks memiliki jumlah kata yang benar
        if len(words) < self.order:
            return []
        
        # Ambil konteks terakhir
        context_tuple = tuple(words[-self.order:])
        
        # Jika konteks tidak ditemukan dalam training data
        if context_tuple not in self.transitions:
            return []
        
        # Dapatkan penghitungan kata berikutnya
        next_words = self.transitions[context_tuple]
        total = sum(next_words.values())
        
        # Hitung probabilitas
        probabilities = [
            (word, count / total) 
            for word, count in next_words.most_common(top_n)
        ]
        
        return probabilities
    
    def generate_text(self, starting_text: str, num_words: int = 10) -> str:
        """
        Generate teks dengan memulai dari starting_text.
        
        Args:
            starting_text (str): Teks awal untuk generasi
            num_words (int): Jumlah kata yang akan dihasilkan
        
        Returns:
            str: Teks yang dihasilkan
        """
        if not self.is_trained:
            raise ValueError("Model belum dilatih. Jalankan train() terlebih dahulu.")
        
        words = starting_text.lower().split()
        
        # Pastikan starting text memiliki cukup kata
        if len(words) < self.order:
            raise ValueError(f"Starting text harus memiliki minimal {self.order} kata")
        
        # Generate kata baru
        for _ in range(num_words):
            context_tuple = tuple(words[-self.order:])
            
            if context_tuple not in self.transitions:
                break
            
            # Dapatkan kata berikutnya yang paling mungkin
            next_words = self.transitions[context_tuple]
            if not next_words:
                break
            
            next_word = next_words.most_common(1)[0][0]
            words.append(next_word)
        
        return ' '.join(words)
    
    def save_model(self, filepath: str) -> None:
        """
        Simpan model ke file JSON.
        
        Args:
            filepath (str): Path file untuk menyimpan model
        """
        model_data = {
            'order': self.order,
            'transitions': {
                str(k): dict(v) 
                for k, v in self.transitions.items()
            }
        }
        
        with open(filepath, 'w') as f:
            json.dump(model_data, f, indent=2)
    
    def load_model(self, filepath: str) -> None:
        """
        Muat model dari file JSON.
        
        Args:
            filepath (str): Path file untuk memuat model
        """
        with open(filepath, 'r') as f:
            model_data = json.load(f)
        
        self.order = model_data['order']
        self.transitions = defaultdict(Counter)
        
        for context_str, words_dict in model_data['transitions'].items():
            # Konversi string kembali ke tuple
            context_tuple = eval(context_str)
            self.transitions[context_tuple] = Counter(words_dict)
        
        self.is_trained = True


# Contoh penggunaan
if __name__ == "__main__":
    # Teks pelatihan contoh
    training_text = """
    Python adalah bahasa pemrograman yang powerful dan mudah dipelajari.
    Python digunakan untuk berbagai keperluan seperti web development, 
    data science, machine learning, dan automation.
    Python memiliki komunitas yang besar dan library yang lengkap.
    Dengan Python Anda dapat membuat aplikasi yang powerful dengan cepat.
    Python adalah bahasa yang sempurna untuk pemula dan profesional.
    """
    
    # Inisialisasi predictor
    predictor = TextPredictor(order=2)
    
    # Latih model
    print("Melatih model...")
    predictor.train(training_text)
    print("Model berhasil dilatih!\n")
    
    # Contoh 1: Prediksi kata berikutnya
    print("=== Prediksi Kata Berikutnya ===")
    context = "python adalah"
    predictions = predictor.predict_next_word(context, top_n=5)
    print(f"Konteks: '{context}'")
    print("Prediksi:")
    for word, prob in predictions:
        print(f"  - {word}: {prob:.2%}")
    print()
    
    # Contoh 2: Generate teks
    print("=== Generate Teks ===")
    starting = "python adalah"
    generated = predictor.generate_text(starting, num_words=15)
    print(f"Awal teks: '{starting}'")
    print(f"Teks yang dihasilkan:\n{generated}\n")
    
    # Contoh 3: Prediksi lain
    print("=== Prediksi Kata Berikutnya (Contoh 2) ===")
    context2 = "dengan python"
    predictions2 = predictor.predict_next_word(context2, top_n=3)
    print(f"Konteks: '{context2}'")
    print("Prediksi:")
    for word, prob in predictions2:
        print(f"  - {word}: {prob:.2%}")
