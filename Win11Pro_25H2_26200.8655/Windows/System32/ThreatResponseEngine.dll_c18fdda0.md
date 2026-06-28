# Binary Specification: ThreatResponseEngine.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ThreatResponseEngine.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c18fdda0a1606a749d5461eb96ef93922ad17bbc34669ede00688fecd6204858`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xB220` | 65 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0xB270` | 49 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xB2B0` | 125 | UnwindData |  |
| 4 | `DllRegisterServer` | `0xB3F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0xB420` | 42,556 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
