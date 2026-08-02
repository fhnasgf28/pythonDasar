"""ai_role.ai_in_coding

Contoh OOP (Python) yang menggambarkan beberapa peran AI di dunia koding:
- CodeAssistant: bantu autocomplete dan saran snippet
- CodeReviewer: berikan komentar review sederhana
- AutoFormatter: format kode dasar
- TestGenerator: buat skeleton test berdasarkan signature fungsi sederhana

File ini dibuat sebagai materi pembelajaran, bukan sebagai pengganti tool nyata.
"""
from __future__ import annotations

import abc
import re
import textwrap
from typing import List


class AIModel(abc.ABC):
    """Base class untuk model AI sederhana."""

    def __init__(self, name: str, version: str = "1.0") -> None:
        self.name = name
        self.version = version

    @abc.abstractmethod
    def assist(self, code: str) -> str:
        """Berikan bantuan berbentuk teks berdasarkan kode yang diberikan."""
        raise NotImplementedError

    def __repr__(self) -> str:  # pragma: no cover - small helper
        return f"<{self.__class__.__name__} name={self.name} v={self.version}>"


class CodeAssistant(AIModel):
    """Menyarankan potongan kode dan autocomplete sederhana."""

    def assist(self, code: str) -> str:
        suggestions = []
        if "for " in code and ":" in code:
            suggestions.append("Pertimbangkan menggunakan enumerate() jika Anda butuh index: for i, v in enumerate(...)" )
        if "print(" in code:
            suggestions.append("Untuk debugging, gunakan logging daripada print untuk aplikasi nyata.")
        if "def " in code and "return" not in code:
            suggestions.append("Fungsi ini belum mengembalikan nilai — apakah Anda lupa return?")
        if not suggestions:
            suggestions.append("Tidak ada saran spesifik. Pertimbangkan menambahkan tipe hint untuk dokumentasi lebih baik.")
        return "\n".join(suggestions)

    def autocomplete(self, prefix: str) -> List[str]:
        # contoh stub autocomplete statis
        completions = [prefix + suffix for suffix in ["_handler", "_manager", "_service"]]
        return completions


class CodeReviewer(AIModel):
    """Memberi review statis sederhana (pattern-based)."""

    def assist(self, code: str) -> str:
        comments = self.review_code(code)
        if not comments:
            return "CodeReview: Tidak ditemukan isu langsung."
        return "CodeReview:\n" + "\n".join(f"- {c}" for c in comments)

    def review_code(self, code: str) -> List[str]:
        issues: List[str] = []
        if "TODO" in code or "FIXME" in code:
            issues.append("Terdapat TODO/FIXME — pastikan tangani sebelum merge.")
        if re.search(r"\bprint\(.*\)", code):
            issues.append("Menggunakan print() di kode produksi — gunakan logging.")
        if len(code.splitlines()) > 200:
            issues.append("File sangat panjang — pertimbangkan memecah modul.")
        if re.search(r"\bexcept:\\n", code):
            issues.append("Menangkap exception umum tanpa menangani tipe spesifik.")
        return issues


class AutoFormatter(AIModel):
    """Formatter sederhana: normalisasi indentasi dan hapus trailing whitespace.

    Catatan: ini bukan pengganti black/autopep8.
    """

    def assist(self, code: str) -> str:
        return self.format_code(code)

    def format_code(self, code: str) -> str:
        # Ganti tab dengan 4 spasi
        out = code.replace("\t", "    ")
        # Hapus trailing whitespace di setiap baris
        lines = [ln.rstrip() for ln in out.splitlines()]
        # Pastikan ada satu newline di akhir
        result = "\n".join(lines).rstrip() + "\n"
        # Dedent berlebih pada contoh
        result = textwrap.dedent(result)
        return result


class TestGenerator(AIModel):
    """Menghasilkan skeleton test sederhana berdasarkan signature fungsi.

    Implementasi sangat dasar: mencari def <name>(...) dan membuat fungsi pytest sederhana.
    """

    def assist(self, code: str) -> str:
        return self.generate_tests(code)

    def generate_tests(self, code: str) -> str:
        functions = re.findall(r"def\s+(\w+)\s*\(([^)]*)\):", code)
        if not functions:
            return "# Tidak ada fungsi yang ditemukan untuk digenerate test-nya."
        tests = ["import pytest", "", "# Generated tests (skeleton)", ""]
        for name, params in functions:
            param_names = [p.strip().split("=")[0].strip() for p in params.split(",") if p.strip()]
            param_setup = []
            for p in param_names:
                # isi nilai default sederhana
                if p:
                    param_setup.append(f"    {p} = None  # TODO: isi input yang sesuai untuk {p}")
            tests.append(f"def test_{name}_basic():")
            if param_setup:
                tests.extend(param_setup)
            tests.append(f"    # TODO: panggil {name} dan assert hasilnya")
            tests.append("")
        return "\n".join(tests)


# Demo: gunakan kelas-kelas di atas untuk menampilkan bagaimana AI dapat membantu alur kerja dev.

DEMO_SNIPPET = """
def greet(name):
	print("Hello, " + name)
"""


def demo() -> None:
    print("=== Demo peran AI di dunia koding (OOP example) ===")

    assistant = CodeAssistant(name="SimpleAssistant", version="0.1")
    reviewer = CodeReviewer(name="SimpleReviewer", version="0.1")
    formatter = AutoFormatter(name="SimpleFormatter", version="0.1")
    tester = TestGenerator(name="SimpleTestGen", version="0.1")

    print("\n-- Original snippet --")
    print(DEMO_SNIPPET)

    print("\n-- Assistant suggestions --")
    print(assistant.assist(DEMO_SNIPPET))
    print("Autocomplete examples:", assistant.autocomplete("process"))

    print("\n-- Code review --")
    print(reviewer.assist(DEMO_SNIPPET))

    print("\n-- Formatted code --")
    formatted = formatter.assist(DEMO_SNIPPET)
    print(formatted)

    print("\n-- Generated tests --")
    print(tester.assist(formatted))


if __name__ == "__main__":
    demo()
