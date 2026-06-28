# Binary Specification: msimtf.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msimtf.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b95d5d75232c3d136895bd1b71eb77d3e2efda1503eb23c89e39b1013b149e6a`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `MsimtfIsGuidMapEnable` | `0x1800` | 31 | UnwindData |  |
| 6 | `MsimtfIsWindowFiltered` | `0x1930` | 32 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x21D0` | 4,816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x34A0` | 7,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x5180` | 24 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x51A0` | 79 | UnwindData |  |
