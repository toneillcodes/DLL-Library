# Binary Specification: mfvfw.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mfvfw.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d2923d078ad88af31861cc04fb5984a7833f9c8582ac7cb39d717021b98d8507`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `GetVFWMFTransform` | `0x6EE0` | 889 | UnwindData |  |
| 4 | `IsVFWDecompressorAvailable` | `0x7260` | 114 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x7330` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllMain` | `0x7360` | 489 | UnwindData |  |
