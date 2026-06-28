# Binary Specification: StartTileData.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\StartTileData.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f6793ebca4e3c1a6a2438a1d68005850f8fc720ede32d630558513ac45681c40`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `HasMigratedTDLData` | `0xEA780` | 30 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x100E00` | 402 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x1043D0` | 69 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x151FC0` | 334 | UnwindData |  |
| 4 | `GetSetting` | `0x193210` | 646,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `ProcessStartLayoutPolicy` | `0x231130` | 223 | UnwindData |  |
| 7 | `TryMigrateTDLData` | `0x28B3B0` | 530 | UnwindData |  |
