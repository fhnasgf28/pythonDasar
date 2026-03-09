import requests
import json
from typing import Optional, Dict, Any
from datetime import datetime
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GoogleChatConnector:
    """
    Kelas untuk menghubungkan OpenClaw atau sistem lainnya dengan Google Chat
    """
    
    def __init__(self, webhook_url: str):
        """
        Inisialisasi connector dengan webhook URL dari Google Chat
        
        Args:
            webhook_url: URL webhook dari Google Chat
                Contoh: https://chat.googleapis.com/v1/spaces/SPACE_ID/messages?key=KEY&token=TOKEN
        """
        self.webhook_url = webhook_url
        self.headers = {'Content-Type': 'application/json; charset=UTF-8'}
    
    def send_simple_message(self, text: str) -> bool:
        """
        Mengirim pesan teks sederhana ke Google Chat
        
        Args:
            text: Teks pesan yang akan dikirim
            
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        message = {"text": text}
        
        try:
            response = requests.post(
                self.webhook_url,
                headers=self.headers,
                data=json.dumps(message),
                timeout=10
            )
            
            if response.status_code == 200:
                logger.info(f"✅ Pesan berhasil dikirim: {text[:50]}...")
                return True
            else:
                logger.error(f"❌ Gagal mengirim pesan: {response.status_code} - {response.text}")
                return False
                
        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Error koneksi: {str(e)}")
            return False
    
    def send_formatted_message(self, title: str, subtitle: str, sections: list) -> bool:
        """
        Mengirim pesan dengan format card/kartu
        
        Args:
            title: Judul kartu
            subtitle: Subtitle kartu
            sections: List berisi detail pesan
            
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        message = {
            "cardsV2": [{
                "cardId": f"card-{datetime.now().timestamp()}",
                "card": {
                    "header": {
                        "title": title,
                        "subtitle": subtitle
                    },
                    "sections": [{
                        "widgets": [
                            {"textParagraph": {"text": section}} 
                            for section in sections
                        ]
                    }]
                }
            }]
        }
        
        try:
            response = requests.post(
                self.webhook_url,
                headers=self.headers,
                data=json.dumps(message),
                timeout=10
            )
            
            if response.status_code == 200:
                logger.info(f"✅ Kartu berhasil dikirim: {title}")
                return True
            else:
                logger.error(f"❌ Gagal mengirim kartu: {response.status_code}")
                return False
                
        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Error koneksi: {str(e)}")
            return False
    
    def send_alert_message(self, alert_type: str, message: str, 
                          severity: str = "MEDIUM") -> bool:
        """
        Mengirim pesan alert/notifikasi dengan styling khusus
        
        Args:
            alert_type: Tipe alert (WARNING, ERROR, INFO, SUCCESS)
            message: Pesan alert
            severity: Level severity (LOW, MEDIUM, HIGH, CRITICAL)
            
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        color_map = {
            "WARNING": "#FFA500",
            "ERROR": "#FF0000",
            "INFO": "#0099FF",
            "SUCCESS": "#00CC00"
        }
        
        severity_emoji = {
            "LOW": "ℹ️",
            "MEDIUM": "⚠️",
            "HIGH": "🔴",
            "CRITICAL": "🚨"
        }
        
        color = color_map.get(alert_type, "#0099FF")
        emoji = severity_emoji.get(severity, "⚠️")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        formatted_message = (
            f"{emoji} **{alert_type} [{severity}]**\n"
            f"Pesan: {message}\n"
            f"Waktu: {timestamp}"
        )
        
        return self.send_simple_message(formatted_message)
    
    def send_disaster_alert(self, disaster_type: str, location: str, 
                           details: Dict[str, Any]) -> bool:
        """
        Mengirim alert bencana dengan detail lengkap
        
        Args:
            disaster_type: Jenis bencana
            location: Lokasi bencana
            details: Dictionary berisi detail bencana
            
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        sections = [
            f"🌍 **Tipe Bencana**: {disaster_type}",
            f"📍 **Lokasi**: {location}",
            f"🕐 **Waktu**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        ]
        
        for key, value in details.items():
            sections.append(f"• **{key}**: {value}")
        
        return self.send_formatted_message(
            title="🚨 ALERT BENCANA",
            subtitle=f"{disaster_type} - {location}",
            sections=sections
        )
    
    def send_system_status(self, status: str, uptime: str, 
                          metrics: Dict[str, Any]) -> bool:
        """
        Mengirim status sistem
        
        Args:
            status: Status sistem (ONLINE, OFFLINE, WARNING)
            uptime: Waktu sistem berjalan
            metrics: Dictionary berisi metrik sistem
            
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        emoji_status = {
            "ONLINE": "✅",
            "OFFLINE": "❌",
            "WARNING": "⚠️"
        }
        
        emoji = emoji_status.get(status, "❓")
        
        sections = [
            f"{emoji} **Status**: {status}",
            f"⏱️ **Uptime**: {uptime}"
        ]
        
        for metric_name, metric_value in metrics.items():
            sections.append(f"• **{metric_name}**: {metric_value}")
        
        return self.send_formatted_message(
            title="📊 Status Sistem",
            subtitle=f"System Check - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            sections=sections
        )
    
    def send_batch_messages(self, messages: list) -> int:
        """
        Mengirim banyak pesan sekaligus
        
        Args:
            messages: List berisi pesan-pesan yang akan dikirim
            
        Returns:
            int: Jumlah pesan yang berhasil dikirim
        """
        success_count = 0
        
        for msg in messages:
            if self.send_simple_message(msg):
                success_count += 1
        
        logger.info(f"📤 Batch send selesai: {success_count}/{len(messages)} berhasil")
        return success_count


# ==================== CONTOH PENGGUNAAN ====================

if __name__ == "__main__":
    # ⚠️ GANTI DENGAN WEBHOOK URL ANDA SENDIRI
    WEBHOOK_URL = "https://chat.googleapis.com/v1/spaces/YOUR_SPACE_ID/messages?key=YOUR_KEY&token=YOUR_TOKEN"
    
    # Inisialisasi connector
    chat = GoogleChatConnector(WEBHOOK_URL)
    
    print("=" * 60)
    print("CONTOH PENGGUNAAN GOOGLE CHAT CONNECTOR")
    print("=" * 60 + "\n")
    
    # 1. Pesan Sederhana
    print("1️⃣ Test: Pesan Sederhana")
    chat.send_simple_message("Hello! Ini pesan dari Python ke Google Chat 🎉")
    print()
    
    # 2. Pesan Berformat dengan Card
    print("2️⃣ Test: Pesan dengan Format Card")
    chat.send_formatted_message(
        title="Laporan Sistem",
        subtitle="Daily Report",
        sections=[
            "Status: Operational ✅",
            "Uptime: 99.8%",
            "Last Check: 2026-03-06 10:30:00"
        ]
    )
    print()
    
    # 3. Alert Message
    print("3️⃣ Test: Alert Message")
    chat.send_alert_message(
        alert_type="WARNING",
        message="CPU usage tinggi mencapai 85%",
        severity="HIGH"
    )
    print()
    
    # 4. Disaster Alert
    print("4️⃣ Test: Alert Bencana")
    chat.send_disaster_alert(
        disaster_type="Gempa Bumi",
        location="Jakarta, Indonesia",
        details={
            "Magnitude": "6.5 SR",
            "Depth": "20 km",
            "Timestamp": datetime.now().isoformat(),
            "Status": "Alert Level 2"
        }
    )
    print()
    
    # 5. System Status
    print("5️⃣ Test: Status Sistem")
    chat.send_system_status(
        status="ONLINE",
        uptime="7 days 3 hours",
        metrics={
            "CPU Usage": "45%",
            "Memory": "62%",
            "Disk": "78%",
            "Active Users": "1250"
        }
    )
    print()
    
    # 6. Batch Messages
    print("6️⃣ Test: Batch Messages")
    messages = [
        "Message 1: First alert",
        "Message 2: Second alert",
        "Message 3: Third alert"
    ]
    chat.send_batch_messages(messages)
    print()
    
    print("=" * 60)
    print("✅ Semua test selesai!")
    print("=" * 60)
