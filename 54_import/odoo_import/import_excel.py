# Import library
import csv
from odoo import models, fields, api

class StudentImport(models.TransientModel):
    _name = 'student.import'
    _description = 'Student Import Wizard'

    excel_file = fields.Binary(string='Excel File', required=True)

    def import_students(self):
        # Decode the binary data from the Excel file
        decoded_data = base64.b64decode(self.excel_file)
        file_path = '/tmp/students.csv'  # Specify the path where the CSV file will be saved

        # Save the decoded data to a CSV file
        with open(file_path, 'wb') as f:
            f.write(decoded_data)

        # Read data from the CSV file
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Create student records in Odoo
                self.env['student.student'].create({
                    'name': row['nama'],
                    'class_id': row['kelas'],
                    'teacher_id': row['nama_guru'],
                    'subject': row['mata_pelajaran'],
                })

        # Optional: Delete the CSV file after import
        os.remove(file_path)

        return {'type': 'ir.actions.act_window_close'}
