# Binary Specification: DispBroker.Desktop.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DispBroker.Desktop.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1285314351d0a33d33736a4bdf6ae5219e0738537bcb17cd91675cc23f57300d`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetActivationFactory` | `0x1DB90` | 434 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x35540` | 138 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x355D0` | 242 | UnwindData |  |
| 5 | `ServiceMain` | `0x363C0` | 30 | UnwindData |  |
| 6 | `SvchostPushServiceGlobals` | `0x363F0` | 364,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GetProxyDllInfo` | `0x8F470` | 233,755 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
