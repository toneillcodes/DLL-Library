# Binary Specification: eapputil.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\eapputil.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0a13d775371774c59723a73f5cb69503cffebf1a3a1200b1d17a7be0c8c76884`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x7880` | 159 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x7930` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `EapConvertHostToWireFormat16` | `0x79E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `EapConvertHostToWireFormat24` | `0x7A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `EapConvertHostToWireFormat32` | `0x7A20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `EapConvertWireToHostFormat16` | `0x7A50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `EapConvertWireToHostFormat24` | `0x7A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `EapConvertWireToHostFormat32` | `0x7A90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `EapUseLegacyTlsStack` | `0x7AC0` | 173,007 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
