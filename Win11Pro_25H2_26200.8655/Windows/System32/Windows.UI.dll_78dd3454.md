# Binary Specification: Windows.UI.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Windows.UI.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `78dd3454d0738569dcf70593af4b5082e72680f8dc985a5e8b22b9ac8dd1867e`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1502 | `DllGetActivationFactory` | `0x19210` | 852 | UnwindData |  |
| 1500 | *Ordinal Only* | `0x2ADF0` | 1,084 | UnwindData |  |
| 1600 | *Ordinal Only* | `0x2D090` | 42 | UnwindData |  |
| 1603 | `CreateControlInputEx` | `0x2D0C0` | 57 | UnwindData |  |
| 1503 | `DllGetClassObject` | `0x33240` | 408 | UnwindData |  |
| 1501 | `DllCanUnloadNow` | `0x55930` | 104 | UnwindData |  |
| 1504 | `DllRegisterServer` | `0x6B1E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1505 | `DllUnregisterServer` | `0x6B210` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1506 | `GetWindowFromWindowId` | `0x6B240` | 14,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1507 | `GetWindowIdFromWindow` | `0x6B240` | 14,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1800 | *Ordinal Only* | `0x6EB80` | 527 | UnwindData |  |
| 1602 | *Ordinal Only* | `0x6EDA0` | 56 | UnwindData |  |
| 1604 | *Ordinal Only* | `0x6EDE0` | 56 | UnwindData |  |
| 1601 | `CreateControlInput` | `0x713D0` | 52 | UnwindData |  |
| 1700 | *Ordinal Only* | `0x86E40` | 204 | UnwindData |  |
