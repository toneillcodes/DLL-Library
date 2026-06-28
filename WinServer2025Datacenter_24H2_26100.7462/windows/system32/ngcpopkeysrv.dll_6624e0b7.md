# Binary Specification: ngcpopkeysrv.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ngcpopkeysrv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6624e0b7d0782898afb1d1ee44b6c909d3cd7e9363f052c7b275a4385c8016b5`
* **Total Exported Functions:** 20

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `s_NgcCreateTokenBindingAik` | `0x120F0` | 352 | UnwindData |  |
| 5 | `s_NgcDecryptWithSymmetricGcmPopKey` | `0x12260` | 507 | UnwindData |  |
| 6 | `s_NgcDecryptWithSymmetricPopKey` | `0x12470` | 421 | UnwindData |  |
| 7 | `s_NgcDeleteSymmetricPopKeyTransportKey` | `0x12620` | 269 | UnwindData |  |
| 8 | `s_NgcDeleteTokenBindingAik` | `0x12740` | 271 | UnwindData |  |
| 9 | `s_NgcEncryptWithSymmetricGcmPopKey` | `0x12860` | 507 | UnwindData |  |
| 10 | `s_NgcEncryptWithSymmetricPopKey` | `0x12A70` | 421 | UnwindData |  |
| 11 | `s_NgcGetKeyAttestationForContainerService` | `0x12C20` | 343 | UnwindData |  |
| 14 | `s_NgcGetSymmetricPopKeyTransportKey` | `0x12D80` | 186 | UnwindData |  |
| 15 | `s_NgcGetSymmetricPopKeyTransportKeyName` | `0x12E40` | 114 | UnwindData |  |
| 16 | `s_NgcGetTokenBindingAikName` | `0x13420` | 301 | UnwindData |  |
| 17 | `s_NgcImportSymmetricPopKey` | `0x13560` | 328 | UnwindData |  |
| 18 | `s_NgcRenewKeyAttestation` | `0x136B0` | 272 | UnwindData |  |
| 19 | `s_NgcSignWithSymmetricPopKey` | `0x137D0` | 387 | UnwindData |  |
| 20 | `s_NgcVerifyWithSymmetricPopKey` | `0x13960` | 379 | UnwindData |  |
| 1 | `NgcGetPregenKey` | `0x205B0` | 270 | UnwindData |  |
| 2 | `NgcPregenKey` | `0x206D0` | 257 | UnwindData |  |
| 3 | `NgcTriggerTask` | `0x207E0` | 253 | UnwindData |  |
| 12 | `s_NgcGetPregenKeyState` | `0x208F0` | 270 | UnwindData |  |
| 13 | `s_NgcGetPregenUserKey` | `0x20A10` | 390 | UnwindData |  |
