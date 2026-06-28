# Binary Specification: Windows.Networking.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Windows.Networking.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `696af466675db843fb9c5a703f536317da18c2c2c25603dcc150809c76643f5f`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0x6B1B0` | 58 | UnwindData |  |
| 3 | `DllGetActivationFactory` | `0x6B1F0` | 45 | UnwindData |  |
| 4 | `DllGetClassObject` | `0x6B230` | 134 | UnwindData |  |
| 5 | `DllMain` | `0x6B2C0` | 86 | UnwindData |  |
| 6 | `DllRegisterServer` | `0x6B320` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllUnregisterServer` | `0x6B350` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | *Ordinal Only* | `0x6B380` | 208 | UnwindData |  |
| 8 | `SetSocketMediaStreamingMode` | `0x6B460` | 107,388 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
