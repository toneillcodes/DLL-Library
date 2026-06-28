# Binary Specification: netfxperf.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\netfxperf.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3dcf2e34d16da35d7873393c6dd05476dc13faa9a12df31bfc8b1c4e179ca3b3`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ClosePerformanceData` | `0x10860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CollectPerformanceData` | `0x10880` | 35 | UnwindData |  |
| 3 | `OpenPerformanceData` | `0x10B40` | 40 | UnwindData |  |
| 4 | `TraceServiceStart` | `0x10C20` | 16,722 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
