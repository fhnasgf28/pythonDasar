import re
from collections import Counter
from textblob import TextBlob

class LieDetector:
    """Deteksi kemungkinan kebohongan berdasarkan analisis teks"""
    
    def __init__(self):
        # Kata-kata yang sering muncul pada pernyataan tidak jujur
        self.doubt_words = [
            'mungkin', 'sepertinya', 'entah', 'agaknya', 'barangkali',
            'rasanya', 'kayaknya', 'kira-kira', 'saya pikir', 'menurut saya'
        ]
        
        self.deception_indicators = {
            'excessive_modifiers': ['sangat', 'benar-benar', 'sungguh-sungguh'],
            'negative_words': ['tidak', 'bukan', 'tidak pernah', 'tidak akan'],
            'distancing_words': ['itu', 'dia', 'orang itu'],
        }
    
    def check_pronoun_usage(self, text):
        """
        Mendeteksi penggunaan pronoun (aku, saya, kami, dll)
        Pembohong cenderung mengurangi penggunaan 'saya'
        """
        text_lower = text.lower()
        pronouns = {
            'saya': len(re.findall(r'\bsaya\b', text_lower)),
            'aku': len(re.findall(r'\baku\b', text_lower)),
            'kami': len(re.findall(r'\bkami\b', text_lower)),
            'kita': len(re.findall(r'\bkita\b', text_lower)),
        }
        return pronouns
    
    def check_doubt_words(self, text):
        """Mendeteksi kata-kata yang menunjukkan keraguan"""
        text_lower = text.lower()
        found_doubt_words = []
        
        for word in self.doubt_words:
            if word in text_lower:
                found_doubt_words.append(word)
        
        return found_doubt_words
    
    def check_negative_words(self, text):
        """Mendeteksi penggunaan kata negatif yang berlebihan"""
        text_lower = text.lower()
        negative_count = 0
        
        for word in self.deception_indicators['negative_words']:
            negative_count += len(re.findall(rf'\b{word}\b', text_lower))
        
        return negative_count
    
    def check_detail_level(self, text):
        """
        Semakin sedikit detail, semakin mungkin berbohong
        Hitung jumlah kata dan tingkat deskripsi
        """
        words = text.split()
        word_count = len(words)
        
        # Hitung kata sifat dan kata keterangan (deskriptif)
        blob = TextBlob(text)
        descriptive_count = sum(1 for word, pos in blob.tags if pos in ['JJ', 'RB'])
        
        detail_ratio = descriptive_count / max(word_count, 1)
        
        return {
            'word_count': word_count,
            'descriptive_words': descriptive_count,
            'detail_ratio': detail_ratio
        }
    
    def analyze_consistency(self, statements):
        """
        Memeriksa konsistensi antara multiple pernyataan
        Pembohong biasanya tidak konsisten
        """
        if len(statements) < 2:
            return None
        
        # Sederhana: hitung kemiripan kata-kata
        all_words = []
        for statement in statements:
            words = set(statement.lower().split())
            all_words.append(words)
        
        # Hitung intersection (kata yang sama di semua pernyataan)
        common_words = set.intersection(*all_words) if all_words else set()
        
        consistency_score = len(common_words) / max(len(all_words[0]), 1) if all_words else 0
        
        return {
            'common_words': list(common_words),
            'consistency_score': consistency_score
        }
    
    def detect(self, text):
        """
        Analisis utama untuk mendeteksi kemungkinan kebohongan
        Returns: skor dan penjelasan (0-100, 0=pasti jujur, 100=pasti bohong)
        """
        score = 0
        indicators = {}
        
        # 1. Pronoun usage (20 poin)
        pronouns = self.check_pronoun_usage(text)
        first_person_count = pronouns['saya'] + pronouns['aku']
        indicators['pronoun_usage'] = {
            'count': first_person_count,
            'assessment': 'Rendah' if first_person_count < 3 else 'Normal'
        }
        if first_person_count < 3:
            score += 15
        
        # 2. Doubt words (25 poin)
        doubt_words = self.check_doubt_words(text)
        indicators['doubt_words'] = doubt_words
        if len(doubt_words) > 3:
            score += 20
        elif len(doubt_words) > 0:
            score += 10
        
        # 3. Negative words (15 poin)
        negative_count = self.check_negative_words(text)
        indicators['negative_words'] = negative_count
        if negative_count > 5:
            score += 15
        
        # 4. Detail level (20 poin)
        details = self.check_detail_level(text)
        indicators['detail_level'] = details
        if details['detail_ratio'] < 0.1:
            score += 15
        
        # 5. Text length (10 poin)
        if len(text.split()) < 20:
            score += 10
        
        # Batasi score ke 0-100
        score = min(score, 100)
        
        # Tentukan kategori
        if score < 25:
            category = "Sangat Mungkin Jujur"
        elif score < 50:
            category = "Mungkin Jujur"
        elif score < 75:
            category = "Mungkin Berbohong"
        else:
            category = "Sangat Mungkin Berbohong"
        
        return {
            'score': score,
            'category': category,
            'indicators': indicators,
            'recommendation': f"Skor kebohongan: {score}/100 - {category}"
        }


# ===== CONTOH PENGGUNAAN =====
if __name__ == "__main__":
    detector = LieDetector()
    
    # Test case 1: Pernyataan yang jujur (detail, menggunakan 'saya')
    honest_statement = """
    Saya pergi ke toko kemarin pada pukul 3 sore. Saya membeli beberapa barang 
    untuk keperluan rumah. Saya mencari buku favorit saya yang berwarna biru dengan 
    sampul yang indah. Toko itu ramai dengan pengunjung yang lain.
    """
    
    # Test case 2: Pernyataan yang mencurigakan (sedikit detail, kata keraguan)
    suspicious_statement = """
    Saya mungkin kemarin. Entahlah, rasanya sudah lama. Barangkali ada yang beli.
    """
    
    print("=" * 60)
    print("TEST CASE 1: Pernyataan Jujur")
    print("=" * 60)
    result1 = detector.detect(honest_statement)
    print(f"Pernyataan: {honest_statement.strip()}")
    print(f"\nHasil Analisis:")
    print(f"Skor: {result1['score']}/100")
    print(f"Kategori: {result1['category']}")
    print(f"Detail yang ditemukan: {result1['indicators']}")
    
    print("\n" + "=" * 60)
    print("TEST CASE 2: Pernyataan Mencurigakan")
    print("=" * 60)
    result2 = detector.detect(suspicious_statement)
    print(f"Pernyataan: {suspicious_statement.strip()}")
    print(f"\nHasil Analisis:")
    print(f"Skor: {result2['score']}/100")
    print(f"Kategori: {result2['category']}")
    print(f"Detail yang ditemukan: {result2['indicators']}")
    
    # Test case 3: Cek konsistensi
    print("\n" + "=" * 60)
    print("TEST CASE 3: Konsistensi Pernyataan")
    print("=" * 60)
    statements = [
        "Saya pergi ke toko buku kemarin",
        "Saya membeli buku di toko kemarin"
    ]
    consistency = detector.analyze_consistency(statements)
    print(f"Pernyataan 1: {statements[0]}")
    print(f"Pernyataan 2: {statements[1]}")
    print(f"Skor Konsistensi: {consistency['consistency_score']:.2%}")
