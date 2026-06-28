# Binary Specification: MitigationClient.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\MitigationClient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `14851a1595ff7a34dcdef590c3e370e58c09545df0975a8e97f0c8e6d635cf9b`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllGetActivationFactory` | `0x14820` | 45 | UnwindData |  |
| 4 | `DllCanUnloadNow` | `0x15000` | 59 | UnwindData |  |
| 5 | `DllGetClassObject` | `0x15050` | 367 | UnwindData |  |
| 2 | `ServiceMain` | `0x159A0` | 153 | UnwindData |  |
| 3 | `SvchostPushServiceGlobals` | `0x16250` | 282,476 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
