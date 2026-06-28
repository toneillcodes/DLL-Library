# Binary Specification: msxml3.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msxml3.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dac32538401196583bcf08eddca8f29ebc030cc507723d9517f142a4b12a30a5`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0x36CF0` | 902 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x3FDD0` | 142 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x44DA0` | 21,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x44DA0` | 21,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllMain` | `0x4A000` | 809,740 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
