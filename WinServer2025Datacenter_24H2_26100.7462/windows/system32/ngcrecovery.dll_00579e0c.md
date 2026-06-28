# Binary Specification: ngcrecovery.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ngcrecovery.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `00579e0c780c5c97fd02828cba0e1ada3b36f910b4fc735898fcbdaa6d8ecf85`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `NgcGetPinRecoveryParams` | `0x1A680` | 93 | UnwindData |  |
| 2 | `NgcIsPinRecoveryEnabled` | `0x1A6F0` | 405 | UnwindData |  |
| 3 | `NgcProtectPinRecoverySecret` | `0x1A890` | 682 | UnwindData |  |
| 4 | `NgcRecoverPin` | `0x1AB40` | 857 | UnwindData |  |
| 5 | `NgcRecoverPinSilent` | `0x1AEA0` | 869 | UnwindData |  |
| 6 | `NgcRecoverPinSilentWithToken` | `0x1B210` | 882 | UnwindData |  |
| 7 | `NgcVerifyPinRecoverySecret` | `0x1B590` | 57 | UnwindData |  |
