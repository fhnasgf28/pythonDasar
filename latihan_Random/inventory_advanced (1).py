"""
Sistem Inventory Lengkap dengan Fitur Advanced
- Stock Management
- Supplier Management
- Low Stock Alert
- Expiry Date Tracking
- Batch/Lot Management
- Stock Opname
- Analytics & Reporting
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import json

class TransferStatus(Enum):
    PENDING = "pending"
    IN_TRANSIT = "in_transit"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class MovementType(Enum):
    """Tipe pergerakan inventory"""
    MASUK = "masuk"
    KELUAR = "keluar"
    TRANSFER = "transfer"
    ADJUSTMENT = "adjustment"
    RETURN = "return"
    DAMAGED = "damaged"

@dataclass
class Supplier:
    """Model Supplier"""
    supplier_id: str
    supplier_name: str
    contact_person: str
    phone: str
    email: str
    address: str
    city: str
    payment_terms: str  # Misal: "Net 30", "COD"
    active: bool = True

@dataclass
class Batch:
    """Model Batch/Lot untuk tracking item"""
    batch_id: str
    item_id: str
    quantity: int
    received_date: datetime
    expiry_date: Optional[datetime]
    supplier_id: str
    location: str
    notes: str = ""

@dataclass
class InventoryItem:
    """Model Item Inventory dengan tracking detail"""
    item_id: str
    item_name: str
    category: str
    sku: str
    quantity: int
    unit: str
    location: str
    price: float
    min_stock: int
    max_stock: int
    supplier_id: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    batches: List[Batch] = field(default_factory=list)

@dataclass
class StockMovement:
    """Log pergerakan stock"""
    movement_id: str
    item_id: str
    item_name: str
    type: MovementType
    quantity: int
    from_location: Optional[str]
    to_location: Optional[str]
    reference_id: Optional[str]  # Transfer ID, PO ID, etc
    created_at: datetime
    notes: str = ""

@dataclass
class StockOpname:
    """Data Stock Opname"""
    opname_id: str
    location: str
    start_date: datetime
    end_date: Optional[datetime]
    status: str  # draft, completed
    adjustments: Dict[str, Dict] = field(default_factory=dict)  # item_id -> {system_qty, physical_qty, variance}
    created_by: str = ""
    notes: str = ""

class AdvancedInventorySystem:
    """Sistem Inventory Advanced dengan fitur lengkap"""
    
    def __init__(self):
        self.inventory: Dict[str, List[InventoryItem]] = {
            "Gudang A": [],
            "Gudang B": [],
            "Gudang C": [],
        }
        
        self.suppliers: Dict[str, Supplier] = {}
        self.stock_movements: List[StockMovement] = []
        self.stock_opnames: List[StockOpname] = []
        self.alerts: List[str] = []
        
        # Counters
        self.movement_counter = 5000
        self.opname_counter = 1000
        
    # ==================== SUPPLIER MANAGEMENT ====================
    
    def add_supplier(self, supplier: Supplier) -> bool:
        """Tambah supplier baru"""
        if supplier.supplier_id in self.suppliers:
            print(f"❌ Supplier '{supplier.supplier_id}' sudah ada!")
            return False
        
        self.suppliers[supplier.supplier_id] = supplier
        print(f"✅ Supplier '{supplier.supplier_name}' berhasil ditambahkan")
        return True
    
    def get_supplier(self, supplier_id: str) -> Optional[Supplier]:
        """Dapatkan info supplier"""
        return self.suppliers.get(supplier_id)
    
    def list_suppliers(self) -> List[Supplier]:
        """List semua supplier aktif"""
        return [s for s in self.suppliers.values() if s.active]
    
    def print_suppliers(self):
        """Tampilkan daftar supplier"""
        suppliers = self.list_suppliers()
        if not suppliers:
            print("Tidak ada supplier")
            return
        
        print("\n" + "="*120)
        print(f"{'ID':<12} {'Nama':<30} {'Contact':<25} {'Phone':<15} {'Kota':<15} {'Terms':<12}")
        print("="*120)
        
        for supplier in suppliers:
            print(f"{supplier.supplier_id:<12} {supplier.supplier_name:<30} {supplier.contact_person:<25} "
                  f"{supplier.phone:<15} {supplier.city:<15} {supplier.payment_terms:<12}")
        
        print("="*120 + "\n")
    
    # ==================== BATCH MANAGEMENT ====================
    
    def receive_item_with_batch(self, item: InventoryItem, supplier_id: str, 
                               expiry_date: Optional[datetime] = None, notes: str = "") -> bool:
        """Terima item dengan batch tracking"""
        
        supplier = self.get_supplier(supplier_id)
        if not supplier:
            print(f"❌ Supplier tidak ditemukan!")
            return False
        
        if item.location not in self.inventory:
            print(f"❌ Lokasi '{item.location}' tidak ditemukan!")
            return False
        
        # Buat batch baru
        batch_id = f"BATCH-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        batch = Batch(
            batch_id=batch_id,
            item_id=item.item_id,
            quantity=item.quantity,
            received_date=datetime.now(),
            expiry_date=expiry_date,
            supplier_id=supplier_id,
            location=item.location,
            notes=notes
        )
        
        # Cek item sudah ada
        existing_item = self.check_stock(item.location, item.item_id)
        
        if existing_item:
            existing_item.quantity += item.quantity
            existing_item.batches.append(batch)
            print(f"✅ Item '{item.item_name}' diterima dari {supplier.supplier_name}")
            print(f"   Batch ID: {batch_id}")
            print(f"   Jumlah: {item.quantity} {item.unit}")
            if expiry_date:
                print(f"   Expiry: {expiry_date.strftime('%Y-%m-%d')}")
        else:
            item.batches.append(batch)
            self.inventory[item.location].append(item)
            print(f"✅ Item '{item.item_name}' ditambahkan (Batch: {batch_id})")
        
        # Log movement
        self._log_movement(
            item.item_id, item.item_name, MovementType.MASUK,
            item.quantity, None, item.location, batch_id, notes
        )
        
        return True
    
    def get_batch_info(self, batch_id: str) -> Optional[Batch]:
        """Dapatkan info batch"""
        for location_items in self.inventory.values():
            for item in location_items:
                for batch in item.batches:
                    if batch.batch_id == batch_id:
                        return batch
        return None
    
    def check_expiry_items(self) -> List[Batch]:
        """Cek item yang akan kadaluarsa (dalam 7 hari)"""
        expiring_items = []
        now = datetime.now()
        expiry_threshold = now + timedelta(days=7)
        
        for location_items in self.inventory.values():
            for item in location_items:
                for batch in item.batches:
                    if batch.expiry_date and now <= batch.expiry_date <= expiry_threshold:
                        expiring_items.append(batch)
                    elif batch.expiry_date and batch.expiry_date < now:
                        # Item sudah expired
                        alert = f"⚠️  EXPIRED: {item.item_name} (Batch: {batch.batch_id}) - Expired on {batch.expiry_date.strftime('%Y-%m-%d')}"
                        if alert not in self.alerts:
                            self.alerts.append(alert)
        
        return sorted(expiring_items, key=lambda x: x.expiry_date)
    
    def print_expiry_report(self):
        """Laporan item yang akan expired"""
        expiring = self.check_expiry_items()
        
        if not expiring:
            print("✅ Tidak ada item yang akan expired\n")
            return
        
        print("\n" + "="*100)
        print("⚠️  LAPORAN ITEM AKAN EXPIRED (7 HARI KE DEPAN)")
        print("="*100)
        print(f"{'Item ID':<12} {'Nama Item':<30} {'Batch ID':<20} {'Qty':<8} {'Expiry Date':<15} {'Hari Tersisa':<12}")
        print("-"*100)
        
        now = datetime.now()
        for batch in expiring:
            days_left = (batch.expiry_date - now).days
            item = next((it for loc in self.inventory.values() for it in loc 
                        if it.item_id == batch.item_id), None)
            
            if item:
                print(f"{batch.item_id:<12} {item.item_name:<30} {batch.batch_id:<20} "
                      f"{batch.quantity:<8} {batch.expiry_date.strftime('%Y-%m-%d'):<15} {days_left:<12}")
        
        print("="*100 + "\n")
    
    # ==================== LOW STOCK ALERTS ====================
    
    def check_low_stock(self) -> Dict[str, List[InventoryItem]]:
        """Cek item dengan stok rendah"""
        low_stock_items = {}
        
        for location, items in self.inventory.items():
            low_items = [item for item in items if item.quantity <= item.min_stock]
            
            if low_items:
                low_stock_items[location] = low_items
                
                for item in low_items:
                    alert = f"🔴 LOW STOCK: {item.item_name} ({item.item_id}) di {location} - Stok: {item.quantity}, Min: {item.min_stock}"
                    if alert not in self.alerts:
                        self.alerts.append(alert)
        
        return low_stock_items
    
    def check_overstock(self) -> Dict[str, List[InventoryItem]]:
        """Cek item dengan stok berlebih"""
        overstock_items = {}
        
        for location, items in self.inventory.items():
            over_items = [item for item in items if item.quantity > item.max_stock]
            
            if over_items:
                overstock_items[location] = over_items
                
                for item in over_items:
                    alert = f"📦 OVERSTOCK: {item.item_name} ({item.item_id}) di {location} - Stok: {item.quantity}, Max: {item.max_stock}"
                    if alert not in self.alerts:
                        self.alerts.append(alert)
        
        return overstock_items
    
    def print_stock_alerts(self):
        """Tampilkan semua alerts"""
        if not self.alerts:
            print("✅ Tidak ada alerts\n")
            return
        
        print("\n" + "="*80)
        print("🚨 STOCK ALERTS")
        print("="*80)
        
        for alert in self.alerts:
            print(alert)
        
        print("="*80 + "\n")
    
    def print_low_stock_report(self):
        """Laporan item stok rendah"""
        low_stock = self.check_low_stock()
        
        if not low_stock:
            print("✅ Semua item stoknya normal\n")
            return
        
        print("\n" + "="*100)
        print("⚠️  LAPORAN STOK RENDAH")
        print("="*100)
        
        for location, items in low_stock.items():
            print(f"\n📍 {location}:")
            print(f"{'Item ID':<12} {'Nama Item':<30} {'Stok Saat Ini':<15} {'Min':<8} {'Deficit':<10}")
            print("-"*100)
            
            for item in items:
                deficit = item.min_stock - item.quantity
                print(f"{item.item_id:<12} {item.item_name:<30} {item.quantity:<15} "
                      f"{item.min_stock:<8} {deficit:<10}")
        
        print("="*100 + "\n")
    
    # ==================== STOCK MOVEMENT TRACKING ====================
    
    def _log_movement(self, item_id: str, item_name: str, movement_type: MovementType,
                     quantity: int, from_location: Optional[str], to_location: Optional[str],
                     reference_id: Optional[str] = None, notes: str = ""):
        """Catat pergerakan stock"""
        movement_id = f"MOV-{self.movement_counter}"
        self.movement_counter += 1
        
        movement = StockMovement(
            movement_id=movement_id,
            item_id=item_id,
            item_name=item_name,
            type=movement_type,
            quantity=quantity,
            from_location=from_location,
            to_location=to_location,
            reference_id=reference_id,
            created_at=datetime.now(),
            notes=notes
        )
        
        self.stock_movements.append(movement)
    
    def get_movement_history(self, item_id: Optional[str] = None, 
                            location: Optional[str] = None,
                            movement_type: Optional[MovementType] = None) -> List[StockMovement]:
        """Dapatkan history pergerakan stock dengan filter"""
        results = self.stock_movements
        
        if item_id:
            results = [m for m in results if m.item_id == item_id]
        
        if location:
            results = [m for m in results if m.from_location == location or m.to_location == location]
        
        if movement_type:
            results = [m for m in results if m.type == movement_type]
        
        return sorted(results, key=lambda x: x.created_at, reverse=True)
    
    def print_movement_history(self, movements: List[StockMovement]):
        """Tampilkan history pergerakan"""
        if not movements:
            print("Tidak ada history pergerakan\n")
            return
        
        print("\n" + "="*120)
        print(f"{'ID':<12} {'Item':<25} {'Type':<12} {'Qty':<8} {'Dari':<15} {'Ke':<15} {'Tanggal':<20} {'Ref ID':<15}")
        print("="*120)
        
        for mov in movements:
            from_loc = mov.from_location or "-"
            to_loc = mov.to_location or "-"
            ref_id = mov.reference_id or "-"
            
            print(f"{mov.movement_id:<12} {mov.item_name:<25} {mov.type.value:<12} {mov.quantity:<8} "
                  f"{from_loc:<15} {to_loc:<15} {mov.created_at.strftime('%Y-%m-%d %H:%M:%S'):<20} {ref_id:<15}")
        
        print("="*120 + "\n")
    
    # ==================== STOCK OPNAME (FISIK COUNT) ====================
    
    def create_opname(self, location: str, created_by: str = "Admin") -> str:
        """Buat stock opname baru"""
        opname_id = f"OPNAME-{self.opname_counter}"
        self.opname_counter += 1
        
        opname = StockOpname(
            opname_id=opname_id,
            location=location,
            start_date=datetime.now(),
            end_date=None,
            status="draft",
            created_by=created_by
        )
        
        self.stock_opnames.append(opname)
        print(f"✅ Stock Opname '{opname_id}' dibuat untuk {location}")
        
        return opname_id
    
    def add_opname_item(self, opname_id: str, item_id: str, physical_qty: int) -> bool:
        """Tambah data fisik count pada opname"""
        opname = next((o for o in self.stock_opnames if o.opname_id == opname_id), None)
        
        if not opname:
            print(f"❌ Opname '{opname_id}' tidak ditemukan!")
            return False
        
        # Cari item di inventory
        item = None
        for loc_items in self.inventory.values():
            for it in loc_items:
                if it.item_id == item_id:
                    item = it
                    break
        
        if not item:
            print(f"❌ Item '{item_id}' tidak ditemukan!")
            return False
        
        # Hitung variance
        variance = physical_qty - item.quantity
        
        opname.adjustments[item_id] = {
            "item_name": item.item_name,
            "system_qty": item.quantity,
            "physical_qty": physical_qty,
            "variance": variance
        }
        
        return True
    
    def complete_opname(self, opname_id: str, apply_adjustment: bool = True) -> bool:
        """Selesaikan opname dan apply adjustment jika diperlukan"""
        opname = next((o for o in self.stock_opnames if o.opname_id == opname_id), None)
        
        if not opname:
            print(f"❌ Opname tidak ditemukan!")
            return False
        
        if apply_adjustment:
            print(f"\n✅ Applying adjustments untuk {opname_id}...")
            
            for item_id, data in opname.adjustments.items():
                variance = data["variance"]
                
                if variance != 0:
                    # Update item quantity
                    for loc_items in self.inventory.values():
                        for item in loc_items:
                            if item.item_id == item_id:
                                old_qty = item.quantity
                                item.quantity = data["physical_qty"]
                                
                                # Log adjustment
                                self._log_movement(
                                    item_id, item.item_name, MovementType.ADJUSTMENT,
                                    abs(variance), opname.location, opname.location,
                                    opname_id, f"Adjustment: {old_qty} → {data['physical_qty']}"
                                )
                                
                                symbol = "📈" if variance > 0 else "📉"
                                print(f"  {symbol} {item.item_name}: {old_qty} → {data['physical_qty']} (Δ {variance:+d})")
                                break
        
        opname.status = "completed"
        opname.end_date = datetime.now()
        print(f"\n✅ Opname '{opname_id}' completed\n")
        
        return True
    
    def print_opname_report(self, opname_id: str):
        """Laporan detail opname"""
        opname = next((o for o in self.stock_opnames if o.opname_id == opname_id), None)
        
        if not opname:
            print(f"❌ Opname tidak ditemukan!")
            return
        
        print("\n" + "="*100)
        print(f"LAPORAN STOCK OPNAME - {opname_id}")
        print("="*100)
        print(f"Lokasi: {opname.location}")
        print(f"Dibuat: {opname.start_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Status: {opname.status}")
        if opname.end_date:
            print(f"Selesai: {opname.end_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Dibuat oleh: {opname.created_by}\n")
        
        print(f"{'Item ID':<12} {'Nama Item':<30} {'Sistem':<10} {'Fisik':<10} {'Variance':<12}")
        print("-"*100)
        
        total_variance = 0
        for item_id, data in opname.adjustments.items():
            variance = data["variance"]
            total_variance += variance
            symbol = "✓" if variance == 0 else ("📈" if variance > 0 else "📉")
            
            print(f"{item_id:<12} {data['item_name']:<30} {data['system_qty']:<10} "
                  f"{data['physical_qty']:<10} {variance:+d} {symbol:<4}")
        
        print("-"*100)
        print(f"Total Variance: {total_variance:+d}")
        print("="*100 + "\n")
    
    # ==================== ANALYTICS & REPORTING ====================
    
    def get_inventory_value(self, location: Optional[str] = None) -> float:
        """Hitung total nilai inventory"""
        total_value = 0
        
        if location:
            items = self.inventory.get(location, [])
            total_value = sum(item.quantity * item.price for item in items)
        else:
            for items in self.inventory.values():
                total_value += sum(item.quantity * item.price for item in items)
        
        return total_value
    
    def print_inventory_summary(self):
        """Ringkasan inventory di semua lokasi"""
        print("\n" + "="*80)
        print("📊 RINGKASAN INVENTORY")
        print("="*80)
        
        grand_total_qty = 0
        grand_total_value = 0
        
        for location in self.inventory.keys():
            items = self.inventory[location]
            total_items = len(items)
            total_qty = sum(item.quantity for item in items)
            total_value = self.get_inventory_value(location)
            
            grand_total_qty += total_qty
            grand_total_value += total_value
            
            print(f"\n📍 {location}:")
            print(f"   - Jumlah SKU: {total_items}")
            print(f"   - Total Unit: {total_qty}")
            print(f"   - Total Nilai: Rp {total_value:,.0f}")
        
        print(f"\n{'─'*80}")
        print(f"TOTAL KESELURUHAN:")
        print(f"   - Total Unit: {grand_total_qty}")
        print(f"   - Total Nilai: Rp {grand_total_value:,.0f}")
        print("="*80 + "\n")
    
    def get_top_items_by_value(self, limit: int = 10) -> List[Tuple[str, float, int]]:
        """Dapatkan top items berdasarkan nilai (item_name, total_value, qty)"""
        item_values = {}
        
        for location_items in self.inventory.values():
            for item in location_items:
                key = item.item_id
                if key not in item_values:
                    item_values[key] = {
                        "name": item.item_name,
                        "qty": 0,
                        "value": 0
                    }
                
                item_values[key]["qty"] += item.quantity
                item_values[key]["value"] += item.quantity * item.price
        
        sorted_items = sorted(item_values.items(), key=lambda x: x[1]["value"], reverse=True)
        
        return [(item_id, data["value"], data["qty"]) for item_id, data in sorted_items[:limit]]
    
    def print_top_items_report(self, limit: int = 10):
        """Laporan top items"""
        top_items = self.get_top_items_by_value(limit)
        
        if not top_items:
            print("Tidak ada item\n")
            return
        
        print(f"\n" + "="*80)
        print(f"TOP {limit} ITEMS BERDASARKAN NILAI")
        print("="*80)
        print(f"{'Rank':<6} {'Item ID':<12} {'Nama Item':<30} {'Qty':<8} {'Nilai':<15}")
        print("-"*80)
        
        for rank, (item_id, value, qty) in enumerate(top_items, 1):
            item = next((it for loc in self.inventory.values() for it in loc 
                        if it.item_id == item_id), None)
            item_name = item.item_name if item else "Unknown"
            
            print(f"{rank:<6} {item_id:<12} {item_name:<30} {qty:<8} Rp {value:,.0f}")
        
        print("="*80 + "\n")
    
    # ==================== BASIC OPERATIONS ====================
    
    def check_stock(self, location: str, item_id: str) -> Optional[InventoryItem]:
        """Cek stok item di lokasi"""
        if location not in self.inventory:
            return None
        
        for item in self.inventory[location]:
            if item.item_id == item_id:
                return item
        return None
    
    def transfer(self, item_id: str, from_location: str, to_location: str,
                quantity: int, notes: str = "") -> bool:
        """Transfer item antar lokasi"""
        
        if from_location not in self.inventory or to_location not in self.inventory:
            print(f"❌ Lokasi tidak valid!")
            return False
        
        if from_location == to_location:
            print(f"❌ Lokasi asal dan tujuan tidak boleh sama!")
            return False
        
        source_item = self.check_stock(from_location, item_id)
        if not source_item or source_item.quantity < quantity:
            print(f"❌ Stok tidak cukup!")
            return False
        
        # Proses transfer
        source_item.quantity -= quantity
        
        dest_item = self.check_stock(to_location, item_id)
        if dest_item:
            dest_item.quantity += quantity
        else:
            new_item = InventoryItem(
                item_id=source_item.item_id,
                item_name=source_item.item_name,
                category=source_item.category,
                sku=source_item.sku,
                quantity=quantity,
                unit=source_item.unit,
                location=to_location,
                price=source_item.price,
                min_stock=source_item.min_stock,
                max_stock=source_item.max_stock,
                supplier_id=source_item.supplier_id
            )
            self.inventory[to_location].append(new_item)
        
        # Log movement
        transfer_id = f"TRF-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self._log_movement(
            item_id, source_item.item_name, MovementType.TRANSFER,
            quantity, from_location, to_location, transfer_id, notes
        )
        
        print(f"✅ Transfer berhasil: {source_item.item_name} ({quantity} {source_item.unit}) dari {from_location} ke {to_location}")
        
        return True
    
    def adjust_stock(self, location: str, item_id: str, quantity_change: int, notes: str = "") -> bool:
        """Penyesuaian stok (positif/negatif)"""
        
        item = self.check_stock(location, item_id)
        if not item:
            print(f"❌ Item tidak ditemukan!")
            return False
        
        old_qty = item.quantity
        new_qty = old_qty + quantity_change
        
        if new_qty < 0:
            print(f"❌ Stok tidak boleh negatif!")
            return False
        
        item.quantity = new_qty
        
        # Log adjustment
        self._log_movement(
            item_id, item.item_name, MovementType.ADJUSTMENT,
            abs(quantity_change), location, location,
            None, f"Adjustment: {old_qty} → {new_qty}. Notes: {notes}"
        )
        
        print(f"✅ Adjustment: {item.item_name} | {old_qty} → {new_qty}")
        
        return True


# ==================== DEMO ====================

def demo():
    """Demonstrasi fitur-fitur advanced"""
    
    system = AdvancedInventorySystem()
    
    print("="*100)
    print("DEMO SISTEM INVENTORY ADVANCED")
    print("="*100)
    
    # 1. Add Suppliers
    print("\n1️⃣  MENAMBAH SUPPLIER")
    print("-"*100)
    
    suppliers = [
        Supplier("SUP001", "PT. Elektronik Jaya", "Budi", "0812-3456-7890", 
                "budi@elektronik.com", "Jl. Merdeka No. 123", "Jakarta", "Net 30"),
        Supplier("SUP002", "CV. Komputer Nusantara", "Andi", "0821-9876-5432",
                "andi@komputer.com", "Jl. Gatot Subroto No. 45", "Surabaya", "COD"),
        Supplier("SUP003", "Toko Aksesoris Digital", "Siti", "0813-5555-6666",
                "siti@aksesoris.com", "Jl. Sudirman No. 789", "Bandung", "Net 15"),
    ]
    
    for supplier in suppliers:
        system.add_supplier(supplier)
    
    system.print_suppliers()
    
    # 2. Receive Items with Batch
    print("\n2️⃣  MENERIMA ITEM DENGAN BATCH TRACKING")
    print("-"*100)
    
    # Item dengan expiry date
    system.receive_item_with_batch(
        InventoryItem("001", "Laptop Dell Inspiron", "Electronics", "SKU-001", 50, "Unit",
                     "Gudang A", 12000000, 20, 100, "SUP001"),
        "SUP001",
        expiry_date=datetime.now() + timedelta(days=365),
        notes="Received from Jakarta"
    )
    
    system.receive_item_with_batch(
        InventoryItem("002", "Mouse Logitech MX", "Accessories", "SKU-002", 200, "Unit",
                     "Gudang A", 500000, 100, 500, "SUP002"),
        "SUP002",
        expiry_date=datetime.now() + timedelta(days=180),
        notes="Batch A - Stock gudang A"
    )
    
    system.receive_item_with_batch(
        InventoryItem("003", "Keyboard Mechanical", "Accessories", "SKU-003", 75, "Unit",
                     "Gudang B", 1500000, 30, 150, "SUP003"),
        "SUP003",
        expiry_date=datetime.now() + timedelta(days=300),
        notes="Premium batch"
    )
    
    # 3. Stock Movements
    print("\n3️⃣  TRANSFER & PERGERAKAN STOK")
    print("-"*100)
    
    system.transfer("001", "Gudang A", "Gudang B", 20, "Transfer ke cabang Surabaya")
    system.transfer("002", "Gudang A", "Gudang C", 50, "Persiapan penjualan")
    system.adjust_stock("Gudang B", "001", -5, "Barang rusak saat pengiriman")
    
    # 4. Low Stock & Overstock Alerts
    print("\n4️⃣  CEK STOK RENDAH & BERLEBIH")
    print("-"*100)
    
    system.receive_item_with_batch(
        InventoryItem("004", "Monitor LG 24 Inch", "Electronics", "SKU-004", 10, "Unit",
                     "Gudang C", 3000000, 50, 200, "SUP001"),
        "SUP001",
        notes="New item - Low stock"
    )
    
    system.check_low_stock()
    system.check_overstock()
    system.print_stock_alerts()
    
    # 5. Low Stock Report
    print("\n5️⃣  LAPORAN STOK RENDAH")
    print("-"*100)
    system.print_low_stock_report()
    
    # 6. Expiry Report
    print("\n6️⃣  LAPORAN ITEM AKAN EXPIRED")
    print("-"*100)
    system.print_expiry_report()
    
    # 7. Stock Opname
    print("\n7️⃣  STOCK OPNAME (FISIK COUNT)")
    print("-"*100)
    
    opname_id = system.create_opname("Gudang A", "Admin Gudang A")
    system.add_opname_item(opname_id, "001", 45)  # System: 30, Fisik: 45 (surplus 15)
    system.add_opname_item(opname_id, "002", 148) # System: 150, Fisik: 148 (minus 2)
    
    system.print_opname_report(opname_id)
    system.complete_opname(opname_id, apply_adjustment=True)
    
    # 8. Movement History
    print("\n8️⃣  HISTORY PERGERAKAN STOK")
    print("-"*100)
    
    movements = system.get_movement_history()
    system.print_movement_history(movements)
    
    # 9. Inventory Summary
    print("\n9️⃣  RINGKASAN INVENTORY")
    print("-"*100)
    system.print_inventory_summary()
    
    # 10. Top Items Report
    print("\n🔟 TOP ITEMS BERDASARKAN NILAI")
    print("-"*100)
    system.print_top_items_report(limit=5)
    
    print("\n✅ DEMO COMPLETED!\n")


if __name__ == "__main__":
    demo()