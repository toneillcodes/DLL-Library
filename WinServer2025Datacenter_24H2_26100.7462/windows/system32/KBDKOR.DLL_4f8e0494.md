# Binary Specification: KBDKOR.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\KBDKOR.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4f8e04942f6067a8f6def16a53e20eb0253c31a011fb677cf99e4a510e1d65c3`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `KbdLayerRealDllFileNT4` | `0x1288` | 1,036 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `KbdLayerRealDllFile` | `0x1694` | 187 | UnwindData |  |
| 1 | `KbdLayerDescriptor` | `0x199C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `KbdNlsLayerDescriptor` | `0x19AC` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `KbdLayerMultiDescriptor` | `0x19BC` | 214 | UnwindData |  |
