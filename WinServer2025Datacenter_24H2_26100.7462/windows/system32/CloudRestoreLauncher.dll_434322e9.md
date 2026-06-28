# Binary Specification: CloudRestoreLauncher.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\CloudRestoreLauncher.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `434322e9274eb22424999b6c81ca7f9f001994512e3cdafac8b04bd15beb945a`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllCanUnloadNow` | `0x26D40` | 86 | UnwindData |  |
| 5 | `DllGetClassObject` | `0x26DA0` | 199 | UnwindData |  |
| 4 | `DllGetActivationFactory` | `0x272B0` | 195 | UnwindData |  |
| 1 | `ServiceMain` | `0x281D0` | 64 | UnwindData |  |
| 2 | `SvchostPushServiceGlobals` | `0x28220` | 1,028,493 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
