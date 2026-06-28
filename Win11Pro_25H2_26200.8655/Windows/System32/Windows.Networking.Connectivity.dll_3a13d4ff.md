# Binary Specification: Windows.Networking.Connectivity.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Windows.Networking.Connectivity.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3a13d4ffa2ac29b6049a1fb778e25fe668835751efa8c89148a787c921613685`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0x39B0` | 196 | UnwindData |  |
| 3 | `DllGetActivationFactory` | `0x3A80` | 205 | UnwindData |  |
| 4 | `DllGetClassObject` | `0x30140` | 318 | UnwindData |  |
| 9 | `TeredoExtAcquireTeredoConsumerHandle` | `0x38E00` | 172 | UnwindData |  |
| 1 | `SetHostNameMediaStreamingMode` | `0x39D60` | 344 | UnwindData |  |
| 7 | `FixDisabledComponentsForTeredo` | `0x45CD0` | 139 | UnwindData |  |
| 8 | `RefreshTeredoClientState` | `0x45D70` | 141 | UnwindData |  |
| 10 | `TeredoExtReleaseTeredoConsumerHandle` | `0x45E10` | 159 | UnwindData |  |
| 5 | `DllRegisterServer` | `0x45F20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0x45F50` | 150,885 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
