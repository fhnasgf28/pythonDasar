"""
Sistem Internal Transfer Inventory
Untuk mengelola transfer barang antar lokasi/gudang
"""

from datetime import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass, field
from enum import Enum

class TransferStatus(Enum):
    """Status transfer inventory"""
    PENDING = "pending"
    IN_TRANSIT = "in_transit"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

@dataclass
class InventoryItem:
    """Model untuk item inventory"""
    item_id: str
    item_name: str
    quantity: int
    unit: str
    location: str
    price: float
    
    def __repr__(self):
        return f"{self.item_name} ({self.item_id}): {self.quantity} {self.unit}"

@dataclass
class TransferLog:
    """Log untuk setiap transfer"""
    transfer_id: str
    item_id: str
    item_name: str
    quantity: int
    from_location: str
    to_location: str
    status: TransferStatus
    created_at: datetime
    updated_at: datetime
    notes: str = ""

class InventoryTransfer:
    """Sistem manajemen internal transfer inventory"""
    
    def __init__(self):
        # Simulasi database inventory di berbagai lokasi
        self.inventory: Dict[str, List[InventoryItem]] = {
            "Gudang A": [],
            "Gudang B": [],
            "Gudang C": [],
        }
        
        # Log transfer
        self.transfer_logs: List[TransferLog] = []
        self.transfer_counter = 1000
    
    def add_inventory(self, location: str, item: InventoryItem) -> bool:
        """Menambah item ke inventory lokasi tertentu"""
        if location not in self.inventory:
            print(f"❌ Lokasi '{location}' tidak ditemukan!")
            return False
        
        # Cek apakah item sudah ada
        for existing_item in self.inventory[location]:
            if existing_item.item_id == item.item_id:
                existing_item.quantity += item.quantity
                print(f"✅ Stok '{item.item_name}' di {location} ditambah menjadi {existing_item.quantity}")
                return True
        
        # Item baru
        self.inventory[location].append(item)
        print(f"✅ Item '{item.item_name}' ditambahkan ke {location} (Qty: {item.quantity})")
        return True
    
    def get_inventory(self, location: str) -> List[InventoryItem]:
        """Mendapatkan semua item di lokasi tertentu"""
        if location not in self.inventory:
            print(f"❌ Lokasi '{location}' tidak ditemukan!")
            return []
        return self.inventory[location]
    
    def check_stock(self, location: str, item_id: str) -> Optional[InventoryItem]:
        """Mengecek stok item di lokasi tertentu"""
        if location not in self.inventory:
            return None
        
        for item in self.inventory[location]:
            if item.item_id == item_id:
                return item
        return None
    
    def transfer(self, item_id: str, from_location: str, to_location: str, 
                quantity: int, notes: str = "") -> bool:
        """
        Melakukan internal transfer inventory
        
        Args:
            item_id: ID item yang ditransfer
            from_location: Lokasi asal
            to_location: Lokasi tujuan
            quantity: Jumlah yang ditransfer
            notes: Catatan transfer
        
        Returns:
            True jika transfer berhasil, False jika gagal
        """
        
        # Validasi lokasi
        if from_location not in self.inventory or to_location not in self.inventory:
            print(f"❌ Lokasi tidak valid!")
            return False
        
        if from_location == to_location:
            print(f"❌ Lokasi asal dan tujuan tidak boleh sama!")
            return False
        
        # Cek item di lokasi asal
        source_item = self.check_stock(from_location, item_id)
        if not source_item:
            print(f"❌ Item '{item_id}' tidak ditemukan di {from_location}")
            return False
        
        # Cek quantity
        if source_item.quantity < quantity:
            print(f"❌ Stok tidak cukup! Available: {source_item.quantity}, Diminta: {quantity}")
            return False
        
        if quantity <= 0:
            print(f"❌ Jumlah transfer harus lebih dari 0!")
            return False
        
        # Proses transfer
        try:
            # Kurangi dari lokasi asal
            source_item.quantity -= quantity
            
            # Tambah ke lokasi tujuan
            destination_item = self.check_stock(to_location, item_id)
            
            if destination_item:
                destination_item.quantity += quantity
            else:
                # Buat item baru di lokasi tujuan
                new_item = InventoryItem(
                    item_id=source_item.item_id,
                    item_name=source_item.item_name,
                    quantity=quantity,
                    unit=source_item.unit,
                    location=to_location,
                    price=source_item.price
                )
                self.inventory[to_location].append(new_item)
            
            # Catat transfer
            transfer_id = f"TRF-{self.transfer_counter}"
            self.transfer_counter += 1
            
            log = TransferLog(
                transfer_id=transfer_id,
                item_id=item_id,
                item_name=source_item.item_name,
                quantity=quantity,
                from_location=from_location,
                to_location=to_location,
                status=TransferStatus.COMPLETED,
                created_at=datetime.now(),
                updated_at=datetime.now(),
                notes=notes
            )
            self.transfer_logs.append(log)
            
            print(f"\n✅ Transfer Berhasil!")
            print(f"   ID Transfer: {transfer_id}")
            print(f"   Item: {source_item.item_name} ({item_id})")
            print(f"   Jumlah: {quantity} {source_item.unit}")
            print(f"   Dari: {from_location} → Ke: {to_location}")
            if notes:
                print(f"   Catatan: {notes}")
            print()
            
            return True
        
        except Exception as e:
            print(f"❌ Error transfer: {str(e)}")
            return False
    
    def get_transfer_history(self, location: Optional[str] = None, 
                            item_id: Optional[str] = None) -> List[TransferLog]:
        """Mendapatkan history transfer dengan filter"""
        results = self.transfer_logs
        
        if location:
            results = [t for t in results if t.from_location == location or t.to_location == location]
        
        if item_id:
            results = [t for t in results if t.item_id == item_id]
        
        return results
    
    def print_transfer_history(self, logs: List[TransferLog]):
        """Menampilkan history transfer dengan format rapi"""
        if not logs:
            print("Tidak ada history transfer")
            return
        
        print("\n" + "="*100)
        print(f"{'ID':<12} {'Item':<25} {'Qty':<8} {'Dari':<15} {'Ke':<15} {'Status':<12} {'Tanggal':<20}")
        print("="*100)
        
        for log in logs:
            print(f"{log.transfer_id:<12} {log.item_name:<25} {log.quantity:<8} "
                  f"{log.from_location:<15} {log.to_location:<15} {log.status.value:<12} "
                  f"{log.created_at.strftime('%Y-%m-%d %H:%M:%S'):<20}")
        
        print("="*100 + "\n")
    
    def print_inventory(self, location: str):
        """Menampilkan inventory di lokasi tertentu"""
        items = self.get_inventory(location)
        
        if not items:
            print(f"Tidak ada item di {location}\n")
            return
        
        print(f"\n{'='*80}")
        print(f"Inventory - {location}")
        print(f"{'='*80}")
        print(f"{'ID':<12} {'Nama Item':<30} {'Qty':<8} {'Unit':<8} {'Harga':<12}")
        print(f"{'-'*80}")
        
        total_value = 0
        for item in items:
            total_value += item.quantity * item.price
            print(f"{item.item_id:<12} {item.item_name:<30} {item.quantity:<8} "
                  f"{item.unit:<8} Rp {item.price:,.0f}")
        
        print(f"{'-'*80}")
        print(f"Total Nilai Inventory: Rp {total_value:,.0f}")
        print(f"{'='*80}\n")


# ==================== DEMO / TESTING ====================
def main():
    """Demonstrasi penggunaan sistem inventory transfer"""
    
    # Inisialisasi sistem
    system = InventoryTransfer()
    
    # Tambah item ke inventory
    print("📦 MENAMBAH ITEM KE INVENTORY\n")
    
    system.add_inventory("Gudang A", InventoryItem("001", "Laptop Dell", 50, "Unit", "Gudang A", 12000000))
    system.add_inventory("Gudang A", InventoryItem("002", "Mouse Logitech", 200, "Unit", "Gudang A", 500000))
    system.add_inventory("Gudang A", InventoryItem("003", "Keyboard Mechanical", 75, "Unit", "Gudang A", 1500000))
    
    system.add_inventory("Gudang B", InventoryItem("001", "Laptop Dell", 30, "Unit", "Gudang B", 12000000))
    system.add_inventory("Gudang B", InventoryItem("004", "Monitor LG 24\"", 40, "Unit", "Gudang B", 3000000))
    
    system.add_inventory("Gudang C", InventoryItem("002", "Mouse Logitech", 100, "Unit", "Gudang C", 500000))
    
    # Tampilkan inventory sebelum transfer
    print("\n📊 INVENTORY SEBELUM TRANSFER")
    system.print_inventory("Gudang A")
    system.print_inventory("Gudang B")
    system.print_inventory("Gudang C")
    
    # Lakukan transfer
    print("\n🚚 MELAKUKAN INTERNAL TRANSFER\n")
    
    system.transfer("001", "Gudang A", "Gudang B", 20, "Transfer stok laptop ke Gudang B")
    system.transfer("002", "Gudang A", "Gudang C", 50, "Perpindahan stok mouse")
    system.transfer("003", "Gudang A", "Gudang B", 25, "")
    system.transfer("004", "Gudang B", "Gudang A", 15, "Transfer monitor ke Gudang A")
    
    # Transfer yang akan gagal
    print("⚠️  TRANSFER YANG GAGAL (TESTING ERROR HANDLING)\n")
    system.transfer("999", "Gudang A", "Gudang B", 10)  # Item tidak ada
    system.transfer("001", "Gudang A", "Gudang A", 5)   # Lokasi sama
    system.transfer("002", "Gudang A", "Gudang B", 999) # Stok tidak cukup
    
    # Tampilkan inventory setelah transfer
    print("\n📊 INVENTORY SETELAH TRANSFER")
    system.print_inventory("Gudang A")
    system.print_inventory("Gudang B")
    system.print_inventory("Gudang C")
    
    # Tampilkan history transfer
    print("\n📋 HISTORY TRANSFER")
    all_transfers = system.get_transfer_history()
    system.print_transfer_history(all_transfers)
    
    # History transfer item tertentu
    print("📋 HISTORY TRANSFER ITEM '001' (Laptop Dell)")
    laptop_transfers = system.get_transfer_history(item_id="001")
    system.print_transfer_history(laptop_transfers)
    
    # History transfer dari lokasi tertentu
    print("📋 HISTORY TRANSFER DARI GUDANG A")
    gudang_a_transfers = system.get_transfer_history(location="Gudang A")
    system.print_transfer_history(gudang_a_transfers)


if __name__ == "__main__":
    main()
