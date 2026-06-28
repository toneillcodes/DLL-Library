# Binary Specification: win32spl.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\win32spl.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e0967fbc4533270b4722b54d7a9ca2664f9a86830c6f5aa8fe25ad2a1b649098`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 343 | `DllMain` | `0x38A50` | 420 | UnwindData |  |
| 345 | `InitializePrintProvidor` | `0x39FA0` | 763 | UnwindData |  |
| 342 | *Ordinal Only* | `0x76660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `InitializePrintMonitor2` | `0x76670` | 84 | UnwindData |  |
| 400 | *Ordinal Only* | `0x766D0` | 122 | UnwindData |  |
| 401 | *Ordinal Only* | `0x76750` | 106 | UnwindData |  |
| 402 | *Ordinal Only* | `0x767C0` | 106 | UnwindData |  |
| 367 | *Ordinal Only* | `0x76830` | 473,516 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
