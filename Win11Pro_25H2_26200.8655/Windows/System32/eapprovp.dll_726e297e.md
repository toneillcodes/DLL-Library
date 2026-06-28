# Binary Specification: eapprovp.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\eapprovp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `726e297ea44e724de9430798dd15ca2e0b71f0eae4dff300b1f551ebb2f1548d`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `EapProvPlugGetInfo` | `0x2670` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `EapProvPluginDeinitialize` | `0x26D0` | 274 | UnwindData |  |
| 3 | `EapProvPluginInitialize` | `0x2AC0` | 402 | UnwindData |  |
| 4 | `EapProvPluginTestForAuthenticatingWlanInterfaces` | `0x2C60` | 426 | UnwindData |  |
| 5 | `EapProvPluginWlanCloseHandle` | `0x2E10` | 164 | UnwindData |  |
| 6 | `EapProvPluginWlanOpenHandle` | `0x2EC0` | 202 | UnwindData |  |
| 7 | `EapProvPluginWlanRegisterNotification` | `0x2F90` | 242 | UnwindData |  |
