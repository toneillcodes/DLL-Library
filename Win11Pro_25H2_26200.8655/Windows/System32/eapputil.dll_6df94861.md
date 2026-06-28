# Binary Specification: eapputil.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\eapputil.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6df948619ee2dd7a2d696a6213abb24ab25aa7d56883fa4b28423f85d27ef03c`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x78A0` | 159 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x7950` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `EapConvertHostToWireFormat16` | `0x7A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `EapConvertHostToWireFormat24` | `0x7A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `EapConvertHostToWireFormat32` | `0x7A40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `EapConvertWireToHostFormat16` | `0x7A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `EapConvertWireToHostFormat24` | `0x7A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `EapConvertWireToHostFormat32` | `0x7AB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `EapUseLegacyTlsStack` | `0x7AE0` | 168,959 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
