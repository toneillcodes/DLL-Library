# Binary Specification: dinput.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dinput.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4a97b9aacc3e5fd03299159b789fc43228abc31d7fd147362f470ce620943280`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DirectInputCreateA` | `0xD550` | 41 | UnwindData |  |
| 2 | `DirectInputCreateEx` | `0xD580` | 202 | UnwindData |  |
| 3 | `DirectInputCreateW` | `0xD710` | 41 | UnwindData |  |
| 4 | `DllCanUnloadNow` | `0xD740` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllGetClassObject` | `0xD850` | 171 | UnwindData |  |
| 6 | `DllRegisterServer` | `0x1BB30` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllUnregisterServer` | `0x1BDA0` | 21,197 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
