# Binary Specification: win32spl.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\win32spl.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `25d57b0063f31d00fddbc149237aade5a729d2f6a169bc34eebe7c1133fe03f8`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 343 | `DllMain` | `0x39060` | 315 | UnwindData |  |
| 345 | `InitializePrintProvidor` | `0x3A7C0` | 763 | UnwindData |  |
| 342 | *Ordinal Only* | `0x79EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `InitializePrintMonitor2` | `0x79F00` | 84 | UnwindData |  |
| 400 | *Ordinal Only* | `0x79F60` | 122 | UnwindData |  |
| 401 | *Ordinal Only* | `0x79FE0` | 106 | UnwindData |  |
| 402 | *Ordinal Only* | `0x7A050` | 106 | UnwindData |  |
| 367 | *Ordinal Only* | `0x7A0C0` | 460,764 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
