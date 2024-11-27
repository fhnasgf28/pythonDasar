def remove_model_data(self):
    models_to_remove = [
        'user.spesific',
        'user.fields',
        'ks.user.standard.specific',
        'ks.user.standard.fields',
        'user.mode',
    ]

    if models_to_remove:
        try:
            # Debugging - Tampilkan daftar model yang ingin dihapus
            print(f"Models to remove: {models_to_remove}")

            # Hapus data terkait dari mail_followers
            self.env.cr.execute("""
                DELETE FROM mail_followers WHERE res_model IN %s
            """, (tuple(models_to_remove),))
            print("Berhasil menghapus mail_followers.")

            # Hapus metadata model dari ir_model
            self.env.cr.execute("""
                DELETE FROM ir_model WHERE model IN %s
            """, (tuple(models_to_remove),))
            print("Berhasil menghapus metadata model di ir_model.")

            # Hapus metadata field dari ir_model_fields
            self.env.cr.execute("""
                DELETE FROM ir_model_fields WHERE model IN %s
            """, (tuple(models_to_remove),))
            print("Berhasil menghapus metadata field di ir_model_fields.")
        except Exception as e:
            # Tangani kesalahan
            print(f"Error saat menghapus data: {str(e)}")
    else:
        print("Tidak ada model yang ditemukan untuk dihapus.")
