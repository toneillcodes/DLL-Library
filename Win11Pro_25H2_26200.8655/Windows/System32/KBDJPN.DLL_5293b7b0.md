# Binary Specification: KBDJPN.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\KBDJPN.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5293b7b0453858137b32a8cf5f294fc2ac9e3bb673fa050c47c2d1600176737a`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `KbdLayerRealDllFileNT4` | `0x1288` | 1,036 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `KbdLayerRealDllFile` | `0x1694` | 187 | UnwindData |  |
| 1 | `KbdLayerDescriptor` | `0x199C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `KbdNlsLayerDescriptor` | `0x19AC` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `KbdLayerMultiDescriptor` | `0x19BC` | 304 | UnwindData |  |
