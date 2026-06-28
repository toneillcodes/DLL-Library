# Binary Specification: webthreatdefsvc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\webthreatdefsvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f40f2f800b6509b3174d8e77a79a5baa557a6d7e198e92ac4b4d6f7d5271efc6`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `ServiceMain` | `0x11AB0` | 214 | UnwindData |  |
| 7 | `SvchostPushServiceGlobals` | `0x11B90` | 18,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x16580` | 65 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x165D0` | 49 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x16610` | 125 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x166A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x166D0` | 16,348 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
