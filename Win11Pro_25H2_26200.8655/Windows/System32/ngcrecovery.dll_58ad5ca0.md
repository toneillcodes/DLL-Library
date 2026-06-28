# Binary Specification: ngcrecovery.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ngcrecovery.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `58ad5ca0c084afd6230cb7c3f735c1a47e4df4d0c080ba29c9e84e0dafc72250`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `NgcGetPinRecoveryParams` | `0x1A800` | 93 | UnwindData |  |
| 2 | `NgcIsPinRecoveryEnabled` | `0x1A870` | 405 | UnwindData |  |
| 3 | `NgcProtectPinRecoverySecret` | `0x1AA10` | 682 | UnwindData |  |
| 4 | `NgcRecoverPin` | `0x1ACC0` | 857 | UnwindData |  |
| 5 | `NgcRecoverPinSilent` | `0x1B020` | 869 | UnwindData |  |
| 6 | `NgcRecoverPinSilentWithToken` | `0x1B390` | 882 | UnwindData |  |
| 7 | `NgcVerifyPinRecoverySecret` | `0x1B710` | 57 | UnwindData |  |
